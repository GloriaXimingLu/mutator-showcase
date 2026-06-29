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
# produced a deliverable. It forces a structured completeness audit against the
# source record so individually-graded issues the agent skipped get surfaced and
# filled before the run ends. Method only — no task-specific answers.
_COMPLETENESS_REVIEW_PROMPT = (
    "Before you finish, run a mandatory COMPLETENESS AUDIT of your deliverable(s) "
    "against the source record. Do not assume your first draft covered everything — "
    "the most common failure on this kind of task is a deliverable that is polished "
    "but omits distinct, individually-graded points the record supports.\n\n"
    "Do this now, as real tool calls (not in your head):\n"
    "1. RE-LIST every distinct issue/requirement the source documents raise. Re-read "
    "the key source files and enumerate each separate problem, gap, discrepancy, "
    "nonconformance, or required element — one per item, not bundled. Include the "
    "ones you already wrote about AND any you have not yet addressed.\n"
    "2. CROSS-CHECK your current deliverable against that list. For each item, is it "
    "actually present and explicitly addressed in the output file? Open the output "
    "file and verify by content, not memory. List every item that is missing, vague, "
    "bundled into another point, or only implied.\n"
    "3. CHECK EACH REQUIRED OUTPUT / DIMENSION: confirm every deliverable the task "
    "asked for exists, and that any required comparison, matrix, or dimension (e.g. "
    "every jurisdiction, every party, every provision, every document in the file) is "
    "covered — do not drop a category because it seemed minor.\n"
    "4. FILL THE GAPS: use edit/write to add every missing item with its own explicit "
    "treatment, drawing the specific facts from the source documents (cite the source). "
    "Do not fabricate issues the record does not support; do add the ones it does that "
    "you skipped.\n"
    "5. Re-validate any binary deliverable per its skill manual, then finish.\n\n"
    "If a thorough re-read finds nothing missing, say so briefly and finish. Otherwise, "
    "make the additions now."
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
    review_injected = False  # one-shot enforced completeness review
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
            # that, run ONE enforced completeness review: if the agent has
            # already produced deliverable output (wrote/edited files) but has
            # not yet been put through the review, inject a review prompt and
            # continue the loop so it can find and fill gaps it skipped. This
            # targets the dominant failure mode — deliverables that omit
            # distinct, individually-graded issues the agent never surfaced.
            if not response.tool_calls:
                produced = (tool_executor.files_written + tool_executor.files_edited) > 0
                if produced and not review_injected and not context_overflow:
                    review_injected = True
                    review_msg = adapter.make_user_message(_COMPLETENESS_REVIEW_PROMPT)
                    messages.append(review_msg)
                    if transcript_file:
                        print(json.dumps({
                            "turn": turn_count,
                            "role": "user",
                            "text": _COMPLETENESS_REVIEW_PROMPT,
                            "injected": "completeness_review",
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
        "completeness_review_injected": review_injected,
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
