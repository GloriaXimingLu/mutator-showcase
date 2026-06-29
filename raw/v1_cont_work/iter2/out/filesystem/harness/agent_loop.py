"""The agent loop — model calls tools until it finishes or hits max turns.

This is the core of the harness. It's deliberately simple: the model does
the thinking, the loop just shuttles messages back and forth.

The agent finishes when it stops making tool calls (no explicit `finish`
tool). The agent loop ends on:
  1. No tool calls returned — the model has nothing more to do
  2. Max turns reached
"""

import time
import json
from pathlib import Path

from harness.adapters.base import ModelAdapter, ModelResponse
from harness.tools import ToolExecutor, get_all_tool_definitions


# Injected once, right after the agent first stops calling tools having already
# produced a deliverable. It forces a source-grounded re-pass against the record:
# each issue tied to a quoted record passage (drop invented ones), every figure
# exact with shown arithmetic (fill/fix computed values), and every
# individually-graded issue surfaced (coverage). Method only — no task-specific
# answers, statutes, or numbers. Replaces the prior coverage-only completeness
# audit, which expanded prose but did not stop fabrication or precision loss and
# regressed quantitative tasks.
_GROUNDING_PROMPT = (
    "Before you finish, run ONE bounded SOURCE-GROUNDED check on your deliverable(s) — "
    "edits to your existing draft, not a rebuild. The most common failures here are (a) "
    "FABRICATION — an issue written from general knowledge rather than THIS record, and "
    "(b) PRECISION LOSS — a figure stated without its inputs, or a required number omitted. "
    "Do this as a few targeted tool calls:\n\n"
    "1. SOURCING: for each issue your draft raises that *claims something is in the record* "
    "(a discrepancy, a nonconformance, a fact about a party/property/provision), confirm you "
    "can point to a passage that states or clearly implies it. REMOVE any such claim you "
    "cannot so ground — it is fabricated. This does NOT apply to required edits or additions "
    "the task asks you to make (a missing provision to draft, a clause to strike, a protective "
    "limitation to add) — keep and complete those. Keep every figure verbatim from the record "
    "(rates, hours, amounts, dates, counts); do not round or paraphrase a number you did not "
    "read.\n"
    "2. ARITHMETIC: where your draft states a derived figure (a reduction, an excess, an "
    "overage %, a total at risk), add the shown inputs (`hours × rate = amount`, `subtotal / "
    "cap − 1 = overage %`). Compute any required figure that is missing. Do not re-derive "
    "values you already showed correctly.\n"
    "3. COVERAGE: skim the key source files for any distinct issue or required dimension you "
    "skipped (every jurisdiction, party, provision, document, listed item). Add only the ones "
    "missing, each tied to its source line — do not re-write sections that are already covered.\n"
    "4. Re-validate any binary deliverable per its skill manual, then finish.\n\n"
    "If the draft is already sourced, arithmetic shown, and coverage complete, say so briefly "
    "and finish. This is a bounded check — make the targeted edits and stop."
)


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

    transcript_file = None
    if transcript_path:
        Path(transcript_path).parent.mkdir(parents=True, exist_ok=True)
        transcript_file = open(transcript_path, "w")
        print(json.dumps({"turn": 0, "role": "system", "text": system_prompt}), file=transcript_file)
        print(json.dumps({"turn": 0, "role": "user", "text": user_prompt}), file=transcript_file)
        transcript_file.flush()

    context_overflow = False
    review_injected = False  # one-shot enforced source-grounding re-pass
    try:
        for turn in range(max_turns):
            turn_count = turn + 1

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

            # If no tool calls, the agent says it is done. Before accepting
            # that, run ONE enforced source-grounding re-pass: if the agent has
            # already produced deliverable output (wrote/edited files) but has
            # not yet been put through the pass, inject the grounding prompt and
            # continue the loop so it (a) removes any issue it cannot tie to a
            # quoted record passage (the fabrication failure), (b) computes and
            # shows the arithmetic for every figure it asserted without inputs
            # (the precision failure), and (c) surfaces any individually-graded
            # issue it skipped (the coverage failure). One shot; hard-capped.
            if not response.tool_calls:
                produced = (tool_executor.files_written + tool_executor.files_edited) > 0
                if produced and not review_injected and not context_overflow:
                    review_injected = True
                    review_msg = adapter.make_user_message(_GROUNDING_PROMPT)
                    messages.append(review_msg)
                    if transcript_file:
                        print(json.dumps({
                            "turn": turn_count,
                            "role": "user",
                            "text": _GROUNDING_PROMPT,
                            "injected": "source_grounding",
                        }), file=transcript_file)
                        transcript_file.flush()
                    continue
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
        "source_grounding_injected": review_injected,
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
