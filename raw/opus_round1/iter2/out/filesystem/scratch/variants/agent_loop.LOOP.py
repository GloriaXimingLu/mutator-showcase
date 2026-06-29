"""The agent loop — model calls tools until it finishes or hits max turns.

This is the core of the harness. The model does the thinking; the loop shuttles
messages back and forth. One enforced step is layered on top of the bare loop:
a single, hard-capped **finalize verification pass** (see FINALIZE_PROMPT). When
the agent first signals it is done (stops making tool calls), the loop injects
one verification turn that makes the agent check its deliverable for required
outputs, numeric correctness, and grounding, then finish. It fires AT MOST ONCE
(`finalize_fired`), so it cannot run away — after the pass the agent stops
normally on its next no-tool-call turn.

The agent finishes when it stops making tool calls (no explicit `finish` tool).
The agent loop ends on:
  1. No tool calls returned AND the finalize pass has already fired
  2. Max turns reached
"""

import time
import json
from pathlib import Path

from harness.adapters.base import ModelAdapter, ModelResponse
from harness.tools import ToolExecutor, get_all_tool_definitions


# One bounded verification pass, injected once when the agent first stops making
# tool calls. It is deliberately a CORRECTNESS check (required outputs present,
# figures computed and footing, claims grounded) and NOT a "find more issues"
# pass — broadening coverage here displaces required facts and inflates length
# without adding graded credit.
FINALIZE_PROMPT = (
    "Before you finish, run ONE verification pass over the deliverable(s) you have "
    "written. Do not start new analysis or add new issues — only verify and fix. "
    "Check, in order:\n\n"
    "1. REQUIRED OUTPUTS. Re-read each file you wrote in the output directory. "
    "Is every deliverable the task asked for present, in the right format, and does "
    "each contain every section, table, column, or dimension the task named? Add any "
    "required element that is missing.\n\n"
    "2. FIGURES. Is every figure the task needs present and correct? For each DERIVED "
    "figure (a proration, interest accrual, equity = value - debt, a sum, subtotal, "
    "total, per-share or per-unit amount, percentage, or a bridge that must foot), "
    "RECOMPUTE it now with python via `bash` — not mental math — and confirm every "
    "total foots against its components. For each figure STATED in a document, confirm "
    "you quoted it exactly (same number, units, defined term). Fix any number that is "
    "wrong, missing, or does not foot.\n\n"
    "3. GROUNDING. Remove or correct any statement, issue, or figure not supported by a "
    "document; do not invent anything to fill a template.\n\n"
    "If everything is already correct and complete, simply stop without further tool "
    "calls. Otherwise make the fixes with `edit`/`bash`/the skill scripts, then stop."
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

    # The finalize verification pass fires at most once — this guard is the
    # runaway bound (it converts "redo until perfect" into exactly one extra
    # check-and-fix cycle).
    finalize_fired = False

    context_overflow = False
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

            # If no tool calls, the agent thinks it is done.
            if not response.tool_calls:
                # Enforce exactly one finalize verification pass before exiting,
                # provided there is turn headroom to act on it.
                if not finalize_fired and turn_count < max_turns - 1:
                    finalize_fired = True
                    messages.append(adapter.make_user_message(FINALIZE_PROMPT))
                    if transcript_file:
                        print(
                            json.dumps({"turn": turn_count, "role": "user",
                                        "text": FINALIZE_PROMPT, "injected": "finalize"}),
                            file=transcript_file,
                        )
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
