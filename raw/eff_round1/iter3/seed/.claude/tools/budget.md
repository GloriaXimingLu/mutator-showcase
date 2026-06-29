# Tool spec — `budget`

> The mutator invokes this from its shell to self-pace its experiments **against both limits**.

## Purpose

Report **both budgets** so you can **self-pace**: the **dollar** meter (how much you've **spent** /
**remain** of the broker cap, plus the **unit costs** of the paid tools) **and** the **wall-clock**
meter (how long until your **soft deadline**). Either one running out mid-refinement loses any
uncommitted work, so plan against both. Self-pacing means **spending the cap down on evidence**
(breadth across several tasks per candidate — CLAUDE.md §3) while **reserving enough of each** to run a
FINAL dev gate and commit your best — not tiptoeing, and not blowing the clock on a gate you can't finish.

## Interface

- **Input:** none. Calling `budget` (no args) **prints both meters**.
- **Output:**
  - **wall-clock:** `~Xm remaining to SOFT deadline` (the hard process kill is ~15 min after that),
    with a verdict: **OK** (room for another full gate), **LOW** (not enough for a fresh ~90 min
    gate — finalize + commit your best validated candidate), or **CRITICAL** (commit now or keep bare).
    Read from `MUTATOR_DEADLINE_EPOCH`; if absent, time is unbounded/untracked.
  - **dollars:** **spent / remaining / cap**, a **per-source breakdown** (`run_harvey_agent` vs
    `proxy_eval`), and the **unit costs** (`run_harvey_agent` ≈ $1/task, `proxy_eval` ≈ $0.02/deliverable),
    read straight from the host broker ledger (no in-container copy).
- **Free** — reporting the meters is not a paid action.

## Guardrails / the "commit now" signal

- **Two independent "commit now" triggers — respect whichever fires first:**
  - **Dollars:** the meter is **synchronous and pre-spend** — the broker checks it **before every paid
    tool call**; when the cap is crossed, the **next paid call throws**. That exception **is** "out of
    budget — commit now."
  - **Wall-clock:** the soft deadline is **silent** (nothing throws), so **you** must watch it. A **LOW**
    or **CRITICAL** reading means: stop *starting* new work (let any gate **already running** finish) and
    **commit your best already-validated edit** (or keep bare) — don't commit on a small-sample subset just
    because time is short. Launch a full dev gate **only when `budget` reports wall-clock `OK`** (the `OK`
    verdict already bakes in the full ~90 min gate **plus** the commit margin — trust the verdict, not
    your own arithmetic on the raw minutes). `dev_eval` itself **refuses** to start a full gate that can't
    finish in time, so a doomed gate won't even launch.
- **The hard process timeout is a backstop, not your plan.** It fires ~15 min after the soft deadline
  and **hard-kills** the run; your captured workspace is saved either way (so a committed on-disk edit
  survives), but anything mid-refinement when it hits is lost. Aim to be **done and committed by the
  soft deadline.**
- A budget-kill (dollars OR time) is a **learning signal** — write a short `.claude/memory/` lesson
  (e.g. "a full dev gate is ~85 min; don't start one under ~100 min remaining") so future runs pace better.
