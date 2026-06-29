# Tool — `dev_eval`

> Your **commit gate**: score your current `harness/` on the held-out-from-train **DEV set**, graded
> by the **ensemble** judge — the same grader the canonical verdict uses.

## Purpose

`dev_eval` runs the frozen Harvey agent on each **DEV** task using your **current `harness/`**, then
grades each deliverable with the **ensemble judge** (gpt-5-mini + gpt-5, escalating disagreements to
Sonnet). It returns **both halves of the gate**: the **accuracy** (`dev_score` = mean ensemble
pass-rate) **and the cost** (`cost.mean_input_tokens` / `mean_total_tokens` / `mean_turns`, plus
per-task `input_tokens` / `turns`) — so one call tells you whether accuracy held AND cost dropped.

This is the signal you should **commit on**. It differs from `proxy_eval` in the two ways that matter:

| | `proxy_eval` | `dev_eval` |
|---|---|---|
| tasks | a TRAIN task you tune on | held-out DEV tasks you never tune on |
| grader | single cheap gpt-5-mini | **ensemble** (same as the real verdict) |
| use | EXPLORE — rank your own attempts | **DECIDE** — gate the commit |

The proxy is a fast, biased hint; the ensemble on held-out dev is measured the way the verdict is.
A high proxy score that does **not** hold up on `dev_eval` is exactly the signal to **not** commit.

## Interface

- **Input:** nothing (the **full** dev set — the gate), or a space-separated subset of **dev** ids
  for a cheaper partial check: `dev_eval [task_id ...]`. Every id must be a dev id; any non-dev id
  (including any val id) refuses the whole call. The held-out val set is unreachable here.
- **ASYNC — returns immediately, runs in the background.** A full dev eval is ~30 rollouts
  (~15-25 min), longer than the shell's 10-minute cap, so the command detaches a worker that
  survives the cap and prints a **done-marker path** `scratch/runs/.dev_<id>.done`.
  **Workflow: launch → poll `test -f <marker>` → `cat` it for `dev_score` → commit (or not).**
- **Output:** the marker holds `dev_score=<accuracy>` AND a `cost:` line
  (`mean_input_tokens` / `mean_total_tokens` / `mean_turns`) + per-task lines (`acc=`, `in_tok=`,
  `turns=`) and the fraction `n_graded/n_requested`. The full structured result is also written to
  `scratch/dev_eval_<id>.json`.

## Cost

≈ **~$1.10 per dev task** (one rollout ~$1 + one ensemble grade ~$0.10) × the number of dev tasks.
A full dev gate is ~30 tasks ≈ ~$33. **Metered** — charged per task up to the remaining cap; tasks
beyond the cap come back as `skipped_for_budget`. Because the gate is expensive, run it on your
**top 1-3 candidates only** (CLAUDE.md §3), not on every experiment.

## Guardrails

- **Dev is for deciding, not searching.** Explore widely on train with `proxy_eval` (cheap), pick
  your best candidate(s), then `dev_eval` them. Running many variants through `dev_eval` and keeping
  the max **overfits dev** and destroys the signal — the same mistake as overfitting train.
- **Dev measures ranking, not the final number.** Dev is the 30 *hardest* tasks of a fresh sample,
  so dev gains run larger than the held-out verdict will — read dev as "is this edit better?", not
  as a prediction of the reported score.
- **Commit only if BOTH hold (the dual gate).** Accuracy: candidate `dev_score` ≥ bare dev_score −
  noise (a HARD gate — never trade accuracy for tokens). Cost: candidate `mean_input_tokens` clearly
  below bare's. If accuracy slips below the gate, reject however big the token saving; if cost didn't
  drop, there's nothing to commit. Bare's dev baseline is in `rollouts/_stats/dev_baseline.json`.
- **Require full coverage.** The aggregate is over graded tasks only; if `n_graded < n_requested`
  (some dev rollouts errored), the score is partial — re-run or investigate before trusting it, and
  treat persistent failures as a problem with your edit, not a free pass.
- **DEV-only by construction.** Only dev ids resolve; val is never mounted into the workspace and any
  non-dev id is refused — so the held-out verdict can never be contaminated from here.
