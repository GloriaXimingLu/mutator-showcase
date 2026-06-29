# Tool — `run_harvey_agent`

> The mutator invokes this from its shell to run a BATCH of Harvey rollouts concurrently, for triage.

## Purpose

Run the **frozen Harvey agent** on **one or many task ids** (a **batch**, run **concurrently**),
using your **current `harness/`**: the broker overlays your edited `system_prompt.md` / `tools.py` /
`agent_loop.py` onto the bare harvey-labs checkout and runs that (exactly what the standard eval
would run), producing a deliverable + trajectory **per task** you can inspect and proxy-grade. This
is how you *try* a harness edit before the canonical eval sees it — and how you buy **breadth**:
test one edit across several tasks in a **single call** (they run in parallel) instead of one slow
serial rollout at a time.

The Harvey agent is **frozen** here: this tool does not change the agent, the model, or the
endpoint — it executes the harness as-is. Your edits to `harness/` are what change the output.

## Interface

- **Input:** one or more `task_id`s from your **TRAIN access set** (the matters under `rollouts/` /
  the train manifest), space-separated: `run_harvey_agent <task_id> [task_id2 ...]`. The batch runs
  concurrently (capped at a few at a time). Held-out **val** ids are **not available**; a batch
  containing **any** non-train id is **refused whole**.
- **Output (all under `scratch/`):** one dir per task — `scratch/runs/<task_id>/deliverable.md`
  (printed as `DELIVERABLE_PATH=` for `proxy_eval`) **and `scratch/runs/<task_id>/turns.txt`** (the
  rollout's turn count, also printed as `turns=`) for **`check_runaway`** (the runaway gate). Tasks
  past the remaining budget come back as `skipped_for_budget` (rerun after you free budget); a task
  that errors is reported but doesn't sink the rest of the batch.
- Writes **nothing** outside `scratch/`.

## Cost

≈ **~$1 per task** (one Harvey-agent rollout) × the number of tasks in the batch. **Metered** — see
`budget.md`; a batch is charged per task only up to the remaining cap (the excess is skipped, not
charged). The unit cost is surfaced by the `budget` tool so you can size your batch.

## Guardrails

- **Counts against the budget.** Charged per task, pre-spend. If the **whole** batch is over budget
  the call returns OVER_BUDGET (your "commit now" cue); a partially-over batch runs what fits and
  returns the rest as `skipped_for_budget`. Check `budget` to size your batch. The budget is there to
  be **used**: confirm a candidate across **several distinct train tasks in one batch** (and against
  bare on the same tasks), not a single rollout — breadth across different matters is what shows the
  edit *generalizes* to tasks you can't see, and it's the main thing to spend the budget on
  (CLAUDE.md §3). A near-empty ledger means you under-experimented.
- **Never writes to `rollouts/`.** `rollouts/` is the canonical standard-eval path, owned by the
  outer driver. This tool is private triage; its outputs are ephemeral `scratch/` artifacts and
  **must not feed selection**.
- **Train-only — the val set is unreachable.** Only TRAIN task ids resolve; the held-out val
  tasks are never mounted into the workspace and any non-train id is refused. Running the agent on
  a val task would contaminate the held-out verdict, so it is impossible by construction.
- Frozen agent: do not use this to "grade your own homework" — pair it with `proxy_eval` for a
  cheap private signal only, never as the verdict.
