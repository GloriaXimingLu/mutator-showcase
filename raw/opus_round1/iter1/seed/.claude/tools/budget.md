# Tool spec — `budget`

> The mutator invokes this from its shell to self-pace its experiments.

## Purpose

Report the budget meter so you can **self-pace**: how much you have **spent**, how much
**remains**, the **cap**, and the **unit costs** of the paid tools — so you can plan how many
tasks the next *round* of experiments fits. Self-pacing means **spending the cap down on
evidence** (breadth across several tasks per candidate — CLAUDE.md §3), not tiptoeing around it;
a near-empty ledger at the end means you under-experimented.

## Interface

- **Input:** none. Calling `budget` (no args) **prints the ledger**.
- **Output:** the current state —
  - **spent / remaining / cap** (the whole-run budget; `remaining()` is exposed for soft
    self-pacing),
  - a **per-source breakdown** (`run_harvey_agent` vs `proxy_eval` spend), read straight from the
    host-side broker ledger (there is no in-container copy),
  - the **unit costs** (`run_harvey_agent` ≈ $1/task, `proxy_eval` ≈ $0.02/deliverable), so you
    can size a round of experiments across several tasks, not a single smoke run.
- **Free** — reporting the meter is not a paid action.

## Guardrails / the "commit now" signal

- The meter is **synchronous and pre-spend**: the broker checks it **before every paid tool call**
  (the metered `.claude/tools/` experiment tools); shell commands and file edits are free.
- When the cap is crossed, the **next paid tool call throws**. That exception **is** the "out of
  budget — commit now" signal: stop experimenting and ship your best committed edit.
- A budget-kill is a **learning signal** — write a short `.claude/memory/` lesson (e.g. "that
  proxy config blew the cap") so future runs are cheaper.
