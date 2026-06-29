# proxy_archive_arm.sh — A/B harness-variant triage helper (carry-forward)

Usage: `proxy_archive_arm.sh <ARM_LABEL> <task_id ...>`

After a `run_harvey_agent` batch (which writes scratch/runs/<task>/deliverable.md), this proxy_evals
each task and archives deliverable+proxy_score+turns into scratch/arms/<ARM_LABEL>/<task>/, printing a
`proxy=… turns=…` line per task. Use to compare harness variants head-to-head on the same tasks/grader.

**Workflow for testing a harness edit (see memory: run-harvey-agent-must-background,
iter2-additive-method-edits-backfire):**
1. Overlay variant into harness/ (swap system_prompt.md / agent_loop.py / tools.py).
2. `run_harvey_agent <tasks>` in the BACKGROUND (batches exceed the 10-min Bash cap; foreground = pay-and-lose).
3. Wait for the completion notification, then `proxy_archive_arm.sh <LABEL> <tasks>`.
4. Repeat per arm (sequentially); compare means + per-task deltas + per-criterion verdicts.

CAVEAT: proxy (gpt-5-mini) over-rates elaboration ~+0.04 — weight mechanism evidence (fact retention,
per-criterion deltas, strong-task regressions) above the proxy number.
