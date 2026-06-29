# Tool spec — `budget`

> **Spec, not code.** This is the contract Stage 2 implements. The mutator invokes this from its
> shell to self-pace its experiments.

## Purpose

Report the budget meter so you can **self-pace**: how much you have **spent**, how much
**remains**, the **cap**, and the **unit costs** of the paid tools — so you can decide whether
the next experiment fits before you run it.

## Interface

- **Input:** none. Calling `budget` (no args) **prints the ledger**.
- **Output:** the current state —
  - **spent / remaining / cap** (the whole-run budget; `remaining()` is exposed for soft
    self-pacing),
  - a **per-source breakdown** (e.g. mutator reasoning vs. proxy evals; the ledger lands in
    `scratch/`),
  - the **unit costs**, e.g. `run_harvey_agent ≈ $X/task`, `proxy_eval ≈ $Y/deliverable`, so you
    can budget a smoke test instead of a sweep.
- **Free** — reporting the meter is not a paid action.

## Guardrails / the "commit now" signal

- The meter is **synchronous and pre-spend**: it is checked before a rollout starts, after every
  mutator turn, and **before every paid tool call** (the `.claude/tools/` experiment tools; shell
  and file edits are free).
- When the cap is crossed, the **next paid tool call throws**. That exception **is** the "out of
  budget — commit now" signal: stop experimenting and ship your best committed edit.
- A budget-kill is a **learning signal** — write a short `.claude/memory/` lesson (e.g. "that
  proxy config blew the cap") so future runs are cheaper.
