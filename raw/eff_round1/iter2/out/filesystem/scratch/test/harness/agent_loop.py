"""The agent loop — model calls tools until it finishes or hits max turns.

This is the core of the harness. It's deliberately simple: the model does
the thinking, the loop just shuttles messages back and forth.

The agent finishes when it stops making tool calls (no explicit `finish`
tool). The agent loop ends on:
  1. No tool calls returned — the model has nothing more to do
  2. Max turns reached

── Carried-context eviction (cost mechanism) ─────────────────────────────
The agent is input-bound: every tool result it has ever seen rides along on
every later turn's prompt, so the same large raw documents are re-sent turn
after turn. That re-carried bulk dominates cost (a single task can run
millions of input tokens vs. tens of thousands of output).

This loop evicts *aged, large* raw tool outputs (`read`/`bash`) from the
carried message history, replacing each with a compact **re-read handle**: a
one-line stub naming the tool + file/command and telling the agent how to
fetch the bytes back on demand. Accuracy is preserved because the document was
already read **in full** when it was current (facts in late schedules/tables
were seen); we only stop *re-carrying* the raw bytes once they have aged out of
the recent working window. If the agent needs the exact text again it re-reads
— a fresh, full result re-enters context.

Design points that keep this safe and bounded:
  - **Task-length gate (the primary accuracy protector).** Eviction does NOT run
    at all until the run passes EVICT_MIN_TURN turns. The accuracy-fragile tasks
    here are SHORT issue-spotting / extraction runs that read a few docs and need
    every fact for a write-up that lands within ~18-20 turns; they finish under
    the gate and so behave EXACTLY like bare — zero accuracy risk, and there were
    no carried-context dollars to recover there anyway. Only the genuinely LONG
    drafting / redline runs (30-120 turns, millions of carried tokens) cross the
    gate and shed their aged raw docs across the long tail — which is the cost.
  - **Size gate.** Even past the length gate, eviction is skipped until resident
    raw output exceeds SIZE_GATE_CHARS (no cost to recover otherwise).
  - Only outputs older than RECENT_WINDOW turns are eligible (the agent has had
    a full working window with the doc resident to extract what it needs).
  - Only outputs larger than MIN_EVICT_CHARS are touched (small results stay).
  - **Sticky re-fetches + kill-switch (the thrash protector).** An output is
    evicted at most *once*; a re-fetch of an evicted output (re-read of a file,
    re-run of a bash/grep/glob, keyed on a stable identity — see `_evict_key`)
    pins it sticky so it is never evicted again. Beyond that, once the run
    accumulates EVICT_REFETCH_LIMIT re-fetches, eviction is DISABLED for the rest
    of the run: the task has demonstrated it works against resident outputs (the
    clause-by-clause redline pattern), so we stop the evict→re-fetch churn before
    it can run the turn count away (keeps turns < 3× bare).
  - The task (system + user messages) and the agent's own reasoning/draft
    output are NEVER evicted — only raw tool results.
  - Eviction adds no model turns directly; it only shrinks the prompt.
  - Wrapped in try/except: any failure degrades to plain bare behavior, never
    crashes the run.

Tunable via env (defaults are conservative):
  HARNESS_EVICT=0                  disable eviction entirely (bare behavior)
  HARNESS_EVICT_MINTURN=<n>        don't evict until the run passes n turns
  HARNESS_EVICT_WINDOW=<n>         keep the last n turns of tool results in full
  HARNESS_EVICT_MINCHARS=<n>       only evict results larger than n chars
  HARNESS_EVICT_SIZEGATE=<n>       only evict once resident raw output exceeds n
  HARNESS_EVICT_REFETCH_LIMIT=<n>  disable eviction after n re-fetches in a run
"""

import os
import time
import json
from pathlib import Path

from harness.adapters.base import ModelAdapter, ModelResponse
from harness.tools import ToolExecutor, get_all_tool_definitions


# ── Eviction configuration ────────────────────────────────────────────────
_EVICT_ENABLED = os.environ.get("HARNESS_EVICT", "1") != "0"
# **Task-length gate — the primary accuracy & anti-disruption protector.**
# Eviction does NOT run at all until the run has passed this many turns. Eviction
# is mildly DISRUPTIVE to this GLM agent: when a doc it is using turns into a
# stub it may re-read / re-orient, costing extra turns. On a SHORT/medium task
# (issue-spotting, extraction) that disruption dominates any saving AND risks a
# dropped fact — and a dev re-fetch blowup confirmed it (a 17-turn extraction
# task that drifted past a turn-20 gate got disrupted into a 38-turn, 4.4×-token
# run). So the gate is set HIGH (28): small/medium tasks finish well under it even
# on a variance-heavy run, so they never trigger eviction and behave EXACTLY like
# bare (zero risk, ~zero cost to recover anyway). Only the genuinely HUGE runs
# (48-120 turns, millions of carried tokens — the cost-dominant redlines/drafts)
# cross the gate and shed their aged raw docs across the long tail.
_EVICT_MIN_TURN = int(os.environ.get("HARNESS_EVICT_MINTURN", "28"))
# Within a long run, a doc is only evicted after it has been resident this many
# turns — the agent has had a full working window with it current to extract
# what it needs before the raw bytes stop being re-carried.
_RECENT_WINDOW = int(os.environ.get("HARNESS_EVICT_WINDOW", "12"))
_MIN_EVICT_CHARS = int(os.environ.get("HARNESS_EVICT_MINCHARS", "6000"))
# A low floor: skip eviction entirely on genuinely tiny tasks (resident raw
# output under this many chars), where there is no cost to recover.
_SIZE_GATE_CHARS = int(os.environ.get("HARNESS_EVICT_SIZEGATE", "250000"))
# **Re-fetch kill-switch (thrash protector) — disable on the FIRST re-fetch.**
# A re-fetch of a previously-evicted output (a re-read of an evicted file, or a
# re-run of an evicted bash/grep/glob) means this task needs its outputs resident
# — exactly the clause-by-clause redline pattern. Once the run accumulates this
# many re-fetch events, eviction is DISABLED for the remainder of the run (the
# re-fetched output is also pinned sticky). Set to 1 so the VERY FIRST re-fetch
# turns eviction off: this bounds eviction's worst-case overhead to a single
# extra read (one re-orientation), making a re-fetch LOOP impossible by
# construction (a 4.4×-token dev blowup under the old limit=2 motivated this), and
# makes eviction self-targeting — redline tasks that re-read revert to bare almost
# immediately, while read-then-draft tasks that never re-read keep the full win.
_EVICT_REFETCH_LIMIT = int(os.environ.get("HARNESS_EVICT_REFETCH_LIMIT", "1"))
# Tools whose raw output is large and safely re-fetchable on demand.
_EVICTABLE_TOOLS = {"read", "bash", "grep", "glob"}


def _evict_key(name: str, arguments):
    """Stable identity for sticky/evicted tracking across all evictable tools, so
    a re-fetch of the same output reliably cancels further eviction churn.
      - read: the file's basename (so "x.docx", "documents/x.docx", an absolute
        path all map together).
      - bash: the stripped command string.
      - grep/glob: the pattern + path.
    Returns None when no stable key can be derived (such calls are never pinned
    and never counted as re-fetches)."""
    if name == "read":
        fp = _arg_value(arguments, "file_path")
        if not isinstance(fp, str) or not fp:
            return None
        return "read:" + fp.rstrip("/").rsplit("/", 1)[-1]
    if name == "bash":
        cmd = _arg_value(arguments, "command")
        if not isinstance(cmd, str) or not cmd.strip():
            return None
        return "bash:" + cmd.strip()
    if name in ("grep", "glob"):
        pat = _arg_value(arguments, "pattern")
        path = _arg_value(arguments, "path") or ""
        if not isinstance(pat, str) or not pat:
            return None
        return f"{name}:{pat}:{path}"
    return None


def _arg_value(arguments, key):
    """Best-effort extract a named argument from a tool call's arguments,
    which may be a dict or a JSON string."""
    try:
        if isinstance(arguments, str):
            arguments = json.loads(arguments)
        if isinstance(arguments, dict):
            return arguments.get(key)
    except Exception:
        pass
    return None


def _make_stub(name: str, arguments, full: str) -> str:
    """A compact re-read handle that replaces an evicted raw tool output."""
    approx_tok = max(1, len(full) // 4)
    if name == "read":
        fp = _arg_value(arguments, "file_path") or "the same file"
        return (
            f"[context-saver: the full output of read(file_path={fp!r}) "
            f"(~{approx_tok:,} tokens) was already read in full and has been "
            f"elided here to keep the running context small. If you still need "
            f"its exact text, call read on {fp!r} again to bring it back.]"
        )
    if name == "bash":
        cmd = (_arg_value(arguments, "command") or "").strip().replace("\n", " ")
        snippet = (cmd[:120] + "…") if len(cmd) > 120 else cmd
        return (
            f"[context-saver: the full output (~{approx_tok:,} tokens) of bash "
            f"command `{snippet}` has been elided to keep context small. "
            f"Re-run the command if you need its output again.]"
        )
    # grep / glob / anything else
    return (
        f"[context-saver: a large {name} result (~{approx_tok:,} tokens) has "
        f"been elided to keep context small. Re-run the {name} if you need it.]"
    )


def _deep_replace(obj, old: str, new: str):
    """Recursively replace occurrences of `old` with `new` in str leaves of a
    (possibly nested) message object. Dicts/lists are mutated in place; returns
    the (possibly new) value so the caller can reassign str leaves."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            obj[k] = _deep_replace(v, old, new)
        return obj
    if isinstance(obj, list):
        for i, v in enumerate(obj):
            obj[i] = _deep_replace(v, old, new)
        return obj
    if isinstance(obj, str):
        return obj.replace(old, new) if old in obj else obj
    return obj


def _evict_aged_results(tool_log, current_turn: int,
                        sticky_keys: set, evicted_keys: set,
                        evict_state: dict) -> None:
    """Replace large raw tool outputs older than the recent window with a
    re-read handle, in place, in the message objects already in `messages`.

    `tool_log` is a list of records, one per turn that produced tool results:
        {"turn": int, "messages": [<adapter message objects>],
         "items": [{"name","args","full","evicted"}]}
    The message objects in `record["messages"]` are the very objects that live
    in the loop's `messages` list, so mutating them shrinks the next prompt.

    `sticky_keys` / `evicted_keys` are output identities (see `_evict_key`) the
    agent has, respectively, re-fetched after an eviction (never evict again) and
    had evicted at least once (so a future re-fetch becomes sticky and counts
    toward the kill-switch). `evict_state` carries the run-level kill-switch
    (`{"disabled": bool, "refetches": int}`).
    """
    if not _EVICT_ENABLED or evict_state.get("disabled"):
        return

    # Task-length gate: leave SHORT/medium runs exactly like bare. Only genuinely
    # long runs (where the carried-context dollars live) ever shed raw outputs.
    if current_turn <= _EVICT_MIN_TURN:
        return

    # Size gate: how many chars of raw evictable output are currently resident?
    # If we're under the gate, there is no cost to recover — behave like bare.
    resident = 0
    for rec in tool_log:
        for item in rec["items"]:
            if item["evicted"]:
                continue
            full = item["full"]
            if isinstance(full, str) and item["name"] in _EVICTABLE_TOOLS:
                resident += len(full)
    if resident < _SIZE_GATE_CHARS:
        return

    for rec in tool_log:
        if current_turn - rec["turn"] < _RECENT_WINDOW:
            continue  # still in the fresh working window — keep full
        for item in rec["items"]:
            if item["evicted"]:
                continue
            full = item["full"]
            if (not isinstance(full, str) or len(full) < _MIN_EVICT_CHARS
                    or item["name"] not in _EVICTABLE_TOOLS):
                item["evicted"] = True  # never eligible; stop reconsidering
                continue
            # Sticky outputs (re-fetched after a prior eviction) stay resident.
            key = _evict_key(item["name"], item["args"])
            if key is not None and key in sticky_keys:
                item["evicted"] = True  # resolved: leave full, never reconsider
                continue
            stub = _make_stub(item["name"], item["args"], full)
            for msg in rec["messages"]:
                _deep_replace(msg, full, stub)
            item["evicted"] = True
            item["full"] = None  # free memory; we won't need it again
            if key is not None:
                evicted_keys.add(key)  # a future re-fetch of this -> sticky


def run_agent(
    adapter: ModelAdapter,
    system_prompt: str,
    user_prompt: str,
    tool_executor: ToolExecutor,
    tools: list[dict] | None = None,
    max_turns: int = 200,
    transcript_path: str | None = None,
) -> dict:
    """Run the agent loop to completion.

    Args:
        adapter: The model adapter (Anthropic, OpenAI, Google, xAI).
        system_prompt: Capabilities and conventions (preamble + skill manuals).
        user_prompt: The first user message — the task assignment.
        tool_executor: Configured tool executor with documents and output dirs.
        tools: Tool definitions to use. Defaults to standard 6 tools if not provided.
        max_turns: Maximum number of loop iterations.
        transcript_path: Optional path to write transcript JSONL.

    Returns:
        Dict with run results: messages, metrics, timing.
    """
    messages = [
        adapter.make_system_message(system_prompt),
        adapter.make_user_message(user_prompt),
    ]
    if tools is None:
        tools = get_all_tool_definitions()

    total_input_tokens = 0
    total_output_tokens = 0
    total_cache_read = 0
    total_cache_creation = 0
    turn_count = 0
    start_time = time.time()

    # Per-turn records of tool-result messages, used to evict aged raw outputs
    # from the carried context (see module docstring).
    tool_log: list[dict] = []
    evicted_keys: set[str] = set()   # output identities evicted at least once
    sticky_keys: set[str] = set()    # identities re-fetched after eviction -> keep
    # Run-level kill-switch: after _EVICT_REFETCH_LIMIT re-fetches the task has
    # shown it needs its outputs resident, so eviction stops for the rest of the
    # run (bounds any evict→re-fetch loop / turn-count blowup).
    evict_state: dict = {"disabled": False, "refetches": 0}

    transcript_file = None
    if transcript_path:
        Path(transcript_path).parent.mkdir(parents=True, exist_ok=True)
        transcript_file = open(transcript_path, "w")
        print(json.dumps({"turn": 0, "role": "system", "text": system_prompt}), file=transcript_file)
        print(json.dumps({"turn": 0, "role": "user", "text": user_prompt}), file=transcript_file)
        transcript_file.flush()

    context_overflow = False
    try:
        for turn in range(max_turns):
            turn_count = turn + 1

            # Evict aged, large raw tool outputs from the carried context before
            # sending the next prompt. Never let a compaction bug crash the run.
            try:
                _evict_aged_results(tool_log, turn_count, sticky_keys,
                                    evicted_keys, evict_state)
            except Exception as e:
                print(f"[evict] skipped on turn {turn_count}: {type(e).__name__}: {e}")

            # Call the model
            try:
                response = adapter.chat(messages, tools)
            except Exception as e:
                err_msg = str(e)
                if "prompt is too long" in err_msg or "context_length_exceeded" in err_msg:
                    context_overflow = True
                    print(f"Context window exceeded on turn {turn_count}: {err_msg}")
                    break
                raise

            messages.append(response.message)
            total_input_tokens += response.input_tokens
            total_output_tokens += response.output_tokens
            total_cache_read += response.cache_read_input_tokens
            total_cache_creation += response.cache_creation_input_tokens

            # Log to transcript
            if transcript_file:
                _log_turn(transcript_file, turn_count, "assistant", response)

            # If no tool calls, the agent is done
            if not response.tool_calls:
                break

            # Execute each tool call and feed results back
            tool_results = []
            for tc in response.tool_calls:
                result = tool_executor.execute(tc.name, tc.arguments)

                if transcript_file:
                    _log_tool(transcript_file, turn_count, tc.name, tc.arguments, result)

                tool_results.append((tc, result))

            # Add tool results to message history via the adapter
            result_messages = adapter.make_tool_result_messages(
                [(tc.id, result) for tc, result in tool_results]
            )
            messages.extend(result_messages)

            # A re-fetch of a previously-evicted output (re-read of an evicted
            # file, or re-run of an evicted bash/grep/glob) means the agent needs
            # it resident — pin it sticky so it is never evicted again, and count
            # it toward the run-level kill-switch. Once enough re-fetches
            # accumulate, eviction is disabled for the rest of the run so an
            # evict→re-fetch pattern can never run the turn count away.
            for tc, _result in tool_results:
                key = _evict_key(tc.name, tc.arguments)
                if key is not None and key in evicted_keys:
                    sticky_keys.add(key)
                    evict_state["refetches"] += 1
                    if evict_state["refetches"] >= _EVICT_REFETCH_LIMIT:
                        evict_state["disabled"] = True

            # Record these tool-result messages so aged, large raw outputs can
            # be evicted later. The message objects are shared with `messages`,
            # so mutating them in `_evict_aged_results` shrinks the next prompt.
            tool_log.append({
                "turn": turn_count,
                "messages": result_messages,
                "items": [
                    {"name": tc.name, "args": tc.arguments,
                     "full": result, "evicted": False}
                    for tc, result in tool_results
                ],
            })

    finally:
        if transcript_file:
            transcript_file.close()

    elapsed = time.time() - start_time

    return {
        "messages": messages,
        "turn_count": turn_count,
        "input_tokens": total_input_tokens,
        "output_tokens": total_output_tokens,
        "cache_read_input_tokens": total_cache_read,
        "cache_creation_input_tokens": total_cache_creation,
        "wall_clock_seconds": round(elapsed, 2),
        "finished_cleanly": (not context_overflow and
                             (not response.tool_calls if turn_count > 0 else False)),
        "context_overflow": context_overflow,
        "tool_metrics": tool_executor.get_metrics(),
        "finish_summary": None,
    }


def _log_turn(f, turn: int, role: str, response: ModelResponse):
    """Log a turn to the transcript JSONL."""
    entry = {
        "turn": turn,
        "role": role,
        "text": response.text if response.text else None,
        "tool_calls": [
            {"name": tc.name, "arguments": tc.arguments}
            for tc in response.tool_calls
        ] if response.tool_calls else None,
        "input_tokens": response.input_tokens,
        "output_tokens": response.output_tokens,
        "cache_read_input_tokens": response.cache_read_input_tokens,
        "cache_creation_input_tokens": response.cache_creation_input_tokens,
    }
    f.write(json.dumps(entry) + "\n")
    f.flush()


def _log_tool(f, turn: int, name: str, arguments: str, result: str):
    """Log a tool execution to the transcript JSONL."""
    entry = {
        "turn": turn,
        "role": "tool",
        "tool_name": name,
        "arguments": arguments if isinstance(arguments, str) else str(arguments),
        "result_preview": result[:1000],
        "result": result,
    }
    f.write(json.dumps(entry) + "\n")
    f.flush()
