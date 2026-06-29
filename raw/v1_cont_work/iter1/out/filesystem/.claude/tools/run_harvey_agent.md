# Tool — `run_harvey_agent`

> The mutator invokes this from its shell to run a single Harvey rollout for triage.

## Purpose

Run the **frozen Harvey agent** on **ONE task id**, using your **current `harness/`**: the broker
overlays your edited `system_prompt.md` / `tools.py` / `agent_loop.py` onto the bare harvey-labs
checkout and runs that (exactly what the standard eval would run), to produce a deliverable and
trajectory you can inspect and proxy-grade. This is how you *try* a harness edit before the
canonical eval ever sees it.

The Harvey agent is **frozen** here: this tool does not change the agent, the model, or the
endpoint — it executes the harness as-is. Your edits to `harness/` are what change the output.

## Interface

- **Input:** a single `task_id` from your **TRAIN access set** (the matters under `rollouts/` /
  the train manifest). Held-out **val** task ids are **not available and are refused**.
- **Output (all under `scratch/`):** a per-run directory, e.g. `scratch/runs/<task_id>/` holding
  at minimum the **deliverable** (the agent's work product) and the **trajectory** (full agent
  trace). Returns the path to that directory so you can feed the deliverable to `proxy_eval`.
- Writes **nothing** outside `scratch/`.

## Cost

≈ **~$1 per task** (one GLM-5.2 rollout). **Metered** — see `budget.md`. The unit cost is
surfaced by the `budget` tool so you can self-pace.

## Guardrails

- **Counts against the budget.** Checked pre-spend; if the cap is crossed the call **throws**
  (your "commit now" signal). Check `budget` before running; prefer **one smoke task**, not a
  full sweep.
- **Never writes to `rollouts/`.** `rollouts/` is the canonical standard-eval path, owned by the
  outer driver. This tool is private triage; its outputs are ephemeral `scratch/` artifacts and
  **must not feed selection**.
- **Train-only — the val set is unreachable.** Only TRAIN task ids resolve; the held-out val
  tasks are never mounted into the workspace and any non-train id is refused. Running the agent on
  a val task would contaminate the held-out verdict, so it is impossible by construction.
- Frozen agent: do not use this to "grade your own homework" — pair it with `proxy_eval` for a
  cheap private signal only, never as the verdict.
