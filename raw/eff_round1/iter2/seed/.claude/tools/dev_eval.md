# Tool — `dev_eval`

> Your **commit gate**: score your current `harness/` on the held-out-from-train **DEV set**, graded
> by the **ensemble** judge — the same grader the canonical verdict uses.

## Purpose

`dev_eval` runs the frozen Harvey agent on each **DEV** task using your **current `harness/`**, then
grades each deliverable with the **ensemble judge** (gpt-5-mini + gpt-5, escalating disagreements to
Sonnet). It returns **all three parts of the gate**: the **accuracy** (`dev_score` = mean ensemble
pass-rate), the **cost** (`cost.mean_input_tokens` / `mean_total_tokens` / `mean_turns`, plus per-task
`input_tokens` / `turns`), and a **per-task THRASH check** — so one call tells you whether accuracy
held, cost dropped, AND no single task blew up under the mean.

This is the signal you should **commit on**. It differs from `proxy_eval` in the two ways that matter:

| | `proxy_eval` | `dev_eval` |
|---|---|---|
| tasks | a TRAIN task you tune on | held-out DEV tasks you never tune on |
| grader | single cheap gpt-5-mini | **ensemble** (same as the real verdict) |
| use | EXPLORE — rank your own attempts | **DECIDE** — gate the commit |

The proxy is a fast, biased hint; the ensemble on held-out dev is measured the way the verdict is.
A high proxy score that does **not** hold up on `dev_eval` is exactly the signal to **not** commit.

## Interface

- **Input:** nothing = the **full** dev set (this is the gate — run it this way). A space-separated
  subset of **dev** ids is allowed (`dev_eval [task_id ...]`) but is only a **noisy, small-sample**
  read: it prints a `PARTIAL DEV … SMALL-SAMPLE` banner and must NOT be the basis for a commit (see
  Guardrails). Every id must be a dev id; any non-dev id (including any val id) refuses the whole call.
  The held-out val set is unreachable here.
- **ASYNC — returns immediately, runs in the background.** A full dev eval is ~30 rollouts
  (~15-25 min), longer than the shell's 10-minute cap, so the command detaches a worker that
  survives the cap and prints a **done-marker path** `scratch/runs/.dev_<id>.done`.
  **Workflow: launch → poll `test -f <marker>` → `cat` it for `dev_score` → commit (or not).**
- **Output** (the marker, read top to bottom):
  - a `PARTIAL DEV … SMALL-SAMPLE` banner **iff** you ran a subset — a heads-up that this read is a
    likely-overfit fluke, not a commit signal;
  - `dev_score=<accuracy>` over `n_graded/n_requested` tasks — the **accuracy gate**;
  - a `cost:` line (`mean_input_tokens` / `mean_total_tokens` / `mean_turns`) — the **cost objective**;
  - a `COMMIT only if ALL THREE hold` line (accuracy ≥ bare−noise AND cost clearly below bare AND no
    per-task THRASH) — the decision rule, restated inline;
  - a `THRASH CHECK:` block — per dev task, flags **≥2× bare turns or tokens = THRASH**, **1.5–2× =
    watch**, vs the per-task bare dev baseline; a task with no bare baseline is reported **cost
    UNKNOWN** (never silently counted clean). turns AND tokens both up = a re-fetch LOOP; tokens up
    with turns ~flat = a one-time re-read.
  - per-task lines (`acc=`, `in_tok=`, `turns=`). The full structured result is also written to
    `scratch/dev_eval_<id>.json`.

## Cost

≈ **~$1.10 per dev task** (one rollout ~$1 + one ensemble grade ~$0.10) × the number of dev tasks.
A full dev gate is ~30 tasks ≈ ~$33. **Metered** — charged per task up to the remaining cap; tasks
beyond the cap come back as `skipped_for_budget`. The gate is your **highest-value spend** (it is the
only held-out generalization signal), so budget for it: score only your **top 1–2** train-picked
candidates (CLAUDE.md §4), but score each on a **large** dev batch — the **full set is best**; a small
subset is a noisy read that overfits. Reserve enough cap to run at least **one full gate** as your
commit decision (and ideally a second, to re-gate after fixing a thrash).

## Guardrails

- **Commit only if ALL THREE hold (CLAUDE.md §4).** (1) **Accuracy** (HARD): candidate `dev_score` ≥
  bare dev_score − noise — never trade accuracy for tokens. (2) **Cost**: candidate `mean_input_tokens`
  clearly below bare's; if cost didn't drop there's nothing to commit. (3) **No per-task THRASH**: a
  flagged **THRASH** (a re-fetch loop, turns+tokens up) is a **reject** — fix it (pin recently re-fetched
  content / cap re-fetches / stop evicting hot content) before committing, even if the mean looks great.
  A **watch** does not block the commit, but record it as a known fragility. Bare's per-task dev baseline
  is in `rollouts/_stats/dev_baseline.json`.
- **Judge on a LARGE sample, not a handful.** A gain on 3–5 dev tasks can look as good as a real
  generalization win by luck, then collapse on the verdict. The thrashers, too, often hide in dev tasks
  a small subset never runs. So decide on the **full** dev set (or a large random batch) — never commit
  on a `PARTIAL DEV` small-sample read.
- **Dev is for deciding, not searching.** This is a *different* failure from small-sample noise: pick
  candidates on **train** (cheap `proxy_eval`); run only your **top 1–2** through `dev_eval`. Running
  *many* variants through `dev_eval` and keeping the max **overfits dev** and destroys the signal — few
  candidates, each on a large sample.
- **Dev measures ranking, not the final number.** Dev is the 30 *hardest* tasks of a fresh sample, so
  dev gains run larger than the held-out verdict will — read dev as "is this edit better?", not as a
  prediction of the reported score.
- **THRASH/watch is always vs that pool's bare baseline** — dev ratios vs the bare *dev* baseline,
  `run_harvey_agent` ratios vs the bare *train* baseline. Clearing train thrash does not clear dev.
- **Require full coverage.** The aggregate is over graded tasks only; if `n_graded < n_requested`
  (some dev rollouts errored), the score is partial — re-run or investigate before trusting it, and
  treat persistent failures as a problem with your edit, not a free pass.
- **DEV-only by construction.** Only dev ids resolve; val is never mounted into the workspace and any
  non-dev id is refused — so the held-out verdict can never be contaminated from here.
