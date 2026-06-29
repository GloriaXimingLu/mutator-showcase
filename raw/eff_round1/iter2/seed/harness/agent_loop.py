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
  - **Size gate.** Eviction does NOT run at all until the *resident* raw
    tool-output bytes exceed SIZE_GATE_CHARS. Small / short tasks (whose whole
    document load fits under the gate) therefore behave EXACTLY like bare — they
    are never touched, so they carry zero accuracy risk. The dollar cost is
    dominated by a handful of huge, long-running tasks; those blow past the gate
    and get the full eviction win. We spend the savings exactly where the cost
    is, and nowhere else.
  - Only outputs older than RECENT_WINDOW turns are eligible (the agent has had
    several turns with the doc resident to extract what it needs).
  - Only outputs larger than MIN_EVICT_CHARS are touched (small results stay).
  - **Sticky re-reads (by basename).** A document is evicted at most *once*. If
    the agent re-reads a file it had previously evicted, that file is marked
    sticky and is never evicted again — the agent has demonstrated it needs the
    doc resident throughout (e.g. clause-by-clause redline/markup work). Keying
    on the file's *basename* makes this robust to the agent spelling the same
    file different ways ("x.docx" vs "documents/x.docx" vs an absolute path), so
    a re-read always cancels further churn. This bounds the extra turns eviction
    can ever cause to ≤ (number of distinct documents): each doc is evicted once
    and, if still needed, re-read once and then pinned. That keeps the turn count
    from running away (no >3× blowups) on negotiation/redline matters.
  - The task (system + user messages) and the agent's own reasoning/draft
    output are NEVER evicted — only raw tool results.
  - Eviction adds no model turns directly; it only shrinks the prompt.
  - Wrapped in try/except: any failure degrades to plain bare behavior, never
    crashes the run.

Tunable via env (defaults are conservative):
  HARNESS_EVICT=0             disable eviction entirely (bare behavior)
  HARNESS_EVICT_WINDOW=<n>    keep the last n turns of tool results in full
  HARNESS_EVICT_MINCHARS=<n>  only evict results larger than n chars
  HARNESS_EVICT_SIZEGATE=<n>  only evict once resident raw output exceeds n chars
"""

import os
import time
import json
from pathlib import Path

from harness.adapters.base import ModelAdapter, ModelResponse
from harness.tools import ToolExecutor, get_all_tool_definitions


# ── Eviction configuration ────────────────────────────────────────────────
_EVICT_ENABLED = os.environ.get("HARNESS_EVICT", "1") != "0"
# A generous window is the primary protector of SHORT tasks: a doc is only
# evicted after it has been resident this many turns, so a ≤10-turn issue-
# spotting / extraction run (where the whole document is needed through the
# write-up) is barely touched, while a 50–120-turn drafting run still sheds the
# raw docs across its long tail — which is where the dollars are.
_RECENT_WINDOW = int(os.environ.get("HARNESS_EVICT_WINDOW", "10"))
_MIN_EVICT_CHARS = int(os.environ.get("HARNESS_EVICT_MINCHARS", "6000"))
# A low floor: skip eviction entirely on genuinely tiny tasks (resident raw
# output under this many chars), where there is no cost to recover. The window
# above — not this gate — does the real winner/loser separation.
_SIZE_GATE_CHARS = int(os.environ.get("HARNESS_EVICT_SIZEGATE", "250000"))
# Tools whose raw output is large and safely re-fetchable on demand.
_EVICTABLE_TOOLS = {"read", "bash", "grep", "glob"}


def _read_key(arguments):
    """Identity for sticky/evicted tracking: the file's basename, so different
    spellings of the same path ("x.docx", "documents/x.docx", an absolute path)
    all map together and a re-read reliably cancels further eviction churn."""
    fp = _arg_value(arguments, "file_path")
    if not isinstance(fp, str) or not fp:
        return None
    return fp.rstrip("/").rsplit("/", 1)[-1]


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
                        sticky_reads: set, evicted_reads: set) -> None:
    """Replace large raw tool outputs older than the recent window with a
    re-read handle, in place, in the message objects already in `messages`.

    `tool_log` is a list of records, one per turn that produced tool results:
        {"turn": int, "messages": [<adapter message objects>],
         "items": [{"name","args","full","evicted"}]}
    The message objects in `record["messages"]` are the very objects that live
    in the loop's `messages` list, so mutating them shrinks the next prompt.

    `sticky_reads` / `evicted_reads` are file_paths the agent has, respectively,
    re-read after an eviction (never evict again) and had evicted at least once
    (so a future re-read of the same path becomes sticky).
    """
    if not _EVICT_ENABLED:
        return

    # Size gate: how many chars of raw evictable output are currently resident?
    # If we're under the gate, this is a small/short task — behave exactly like
    # bare (no eviction at all), so there is no accuracy risk where there is no
    # cost to recover.
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
            # Sticky docs (re-read after a prior eviction) stay resident.
            key = _read_key(item["args"]) if item["name"] == "read" else None
            if key is not None and key in sticky_reads:
                item["evicted"] = True  # resolved: leave full, never reconsider
                continue
            stub = _make_stub(item["name"], item["args"], full)
            for msg in rec["messages"]:
                _deep_replace(msg, full, stub)
            item["evicted"] = True
            item["full"] = None  # free memory; we won't need it again
            if key is not None:
                evicted_reads.add(key)  # a future re-read of this file -> sticky


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
    evicted_reads: set[str] = set()  # file_paths evicted at least once
    sticky_reads: set[str] = set()   # file_paths re-read after eviction -> keep

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
                _evict_aged_results(tool_log, turn_count, sticky_reads, evicted_reads)
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

            # A re-read of a previously-evicted document means the agent needs
            # it resident — mark it sticky (by basename) so it is never evicted
            # again. This bounds eviction-induced re-reads to one per document.
            for tc, _result in tool_results:
                if tc.name == "read":
                    key = _read_key(tc.arguments)
                    if key is not None and key in evicted_reads:
                        sticky_reads.add(key)

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
