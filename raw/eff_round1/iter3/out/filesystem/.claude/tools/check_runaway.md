# Tool — `check_runaway`

> The mutator invokes this after a structural edit to catch a turn-count blowup BEFORE committing.

## Purpose

A **hard gate** on the single failure that wastes a whole iteration: a `agent_loop.py` / `tools.py`
edit that makes the agent **run away** (take many more turns than the bare harness) — usually from an
unbounded or stacked enforced step. The eval's **canary aborts the entire iteration** when an edit's
turns exceed **3× the bare baseline**, so check that *yourself* first and reject a runaway edit before
you ship it.

## Interface

- **Input:** the task ids you just tested with `run_harvey_agent` — `check_runaway <task_id> [task_id2 ...]`.
- **What it reads (no cost, local files only):**
  - your edit's turns — `scratch/runs/<task>/turns.txt` (written by `run_harvey_agent`),
  - the bare baseline turns — `rollouts/<task>/iter0/metrics.json` (`turn_count`).
- **Output:** per task, `<edit> turns vs bare <n> = <r>x -> ok | RUNAWAY`. **Exits non-zero (FAIL)
  if ANY task exceeds 3× bare** — that exit code is your automatic "this edit is rejected" signal.

## How to use it (hard rule — see CLAUDE.md §3 "bound every loop change" and §6(e))

After **any** `agent_loop.py` / `tools.py` edit:
1. `run_harvey_agent <a few tasks>` (a batch) to produce deliverables **and** turn counts.
2. `check_runaway <those same tasks>`.
3. **If it FAILS, the edit is REJECTED** — revert it, give the enforced step a hard cap (it fires a
   fixed small number of times, then the agent finishes), or pick a different lever; then re-test.
   **Do not commit a runaway** — the canary will abort the iteration and you'll have spent the budget
   for nothing.

A prose-only `system_prompt.md` edit can't blow up the loop, so it doesn't need this — but a prose
edit that *pushes the agent to do much more work* can still inflate turns, so checking is cheap insurance.
