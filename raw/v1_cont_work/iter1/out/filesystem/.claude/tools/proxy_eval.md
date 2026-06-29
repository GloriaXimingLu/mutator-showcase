# Tool spec — `proxy_eval`

> **Spec, not code.** This is the contract Stage 2 implements. The mutator invokes this from its
> shell to triage a deliverable it produced with `run_harvey_agent`.

## Purpose

Grade **ONE deliverable** with a **cheap proxy grader** — a **single mid-tier judge**, NOT the
full cascaded ensemble — to get a fast, **private triage** signal on whether a harness edit
helped. Use it to rank your own attempts mid-rollout; that is its only job.

## Interface

- **Input:** the **deliverable** (a path under `scratch/`, or the text), plus the **rubric /
  criteria** for that task (the same criteria shape found in each `rollouts/<task>/task.md`).
- **Output (under `scratch/`):** a **score** (e.g. pass-rate + per-criterion verdicts) written
  to `scratch/`, e.g. alongside the run dir. Returns the score so you can compare attempts.

## Cost

**Cheaper than the standard ensemble** — one mid-tier judge call per deliverable, no cascade,
no strong-model escalation. **Metered** — see `budget.md`; the unit cost is surfaced by `budget`.

## The critical wall — triage only, NEVER the verdict

This is the load-bearing guard ("no grading your own homework"):

- **Private triage only.** The proxy never feeds selection. A proxy calibrated on one harness
  mis-ranks the moment the harness changes — and could be gamed — so it can only *hint*.
- **Must NEVER read or run the canonical standard eval**, and must never reproduce it. The
  standard eval is run by the **outer driver**, not by any tool you can call.
- **Writes only under `scratch/`. Never writes to `rollouts/`.** No proxy artifact may reach the
  canonical path.
- **Train deliverables only.** You only ever triage attempts you produced on your TRAIN tasks
  (via `run_harvey_agent`). The held-out val set is invisible to you, so it can never be proxy-graded.
- **NO strong-model APIs** (no GPT-5 / Claude / Opus). A single mid-tier judge, full stop. If a
  proxy config blows the budget, write a `.claude/memory/` lesson so the run gets cheaper.
