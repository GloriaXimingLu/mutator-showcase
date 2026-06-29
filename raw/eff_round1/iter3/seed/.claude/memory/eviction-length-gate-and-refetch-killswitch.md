# Lesson — length-gated, kill-switched eviction is a committed cost win (−28% input, accuracy held)

**Verified on the full DEV gate (30/30 tasks, ensemble).** Iteration 2 committed an improved
carried-context **eviction** in `agent_loop.py`. Result vs bare:
- **dev_score 0.8171 vs bare 0.8079 (+0.009, PASS — accuracy held/above bare)**
- **mean_input_tokens 3.22M vs bare 4.48M (−28.1%, PASS — the cost win)**
- **0 THRASH** (3 "watch" at 1.5-2×, all on ≤28-turn tasks where eviction never fired → pure GLM variance, not the edit).

## What the edit is (generic, not task-specific)
Evict aged large raw `read`/`bash`/`grep`/`glob` outputs to a one-line re-read stub, gated by:
- `_EVICT_MIN_TURN=28` — **never evict until the run passes 28 turns.** Small/medium tasks finish
  under it even on a variance-heavy run, so they behave EXACTLY like bare (zero risk, ~zero cost to
  recover). Only the genuinely HUGE runs (48-120t redlines/drafts — where the dollars are) trigger it.
- `_EVICT_REFETCH_LIMIT=1` — the **FIRST** re-fetch of an evicted output DISABLES eviction for the rest
  of the run (and pins that output). Makes a re-fetch LOOP impossible by construction, and self-targets:
  clause-by-clause redlines (which re-read) revert to bare immediately; read-then-draft runs keep the win.
- `_RECENT_WINDOW=12`, `_MIN_EVICT_CHARS=6000`, `_SIZE_GATE_CHARS=250000`. Wrapped in try/except → bare on error.

## Why it generalizes (method, not memorization)
Keys on run-length and re-fetch behavior, not on any matter. Cuts only the **re-carried** bulk AFTER a
doc has been resident a full window (facts already captured), never what is read — so accuracy holds.

## Hard-won findings (re-check, don't re-derive)
- Model is **glm-5p2** (not Anthropic); `cache_read=0` everywhere — prompt caching is NOT reachable from
  the 3 editable files (adapter is broker-side). Don't chase caching.
- The inherited iter1 eviction (no length gate, sticky-per-read only) was a NET LOSER: −6.4% input,
  −0.0265 train acc, 1 THRASH. Its "thrasher" (review-governance 18→73t) was a **docx-generation flail**
  (0 re-reads, 62 bash) = GLM variance, NOT eviction — see [[glm-variance-and-docx-flail]].
- **REFETCH_LIMIT=2 still thrashed** one dev task (data-privacy/extract: 17→38t, 4.4× tokens — a real
  eviction re-fetch loop; per-turn ctx doubled = repeated re-reads). `=1` fixed it → 21t/1.25M, acc +0.019.
- A small task can drift past a turn-20 gate and get disrupted → set MIN_TURN well clear of the
  medium-task variance band (28, not 20).
- dev_eval marker id is deterministic from the task set: re-gating the full set reuses `.dev_a9a0c38d.done`
  (it IS cleared on relaunch — verify the worker pid/mtime before trusting a poll).

## Next-iteration headroom (chase in cheap train loop, NOT by searching dev)
- 3 watches are variance on sub-gate tasks — not the edit. Could try MIN_TURN 24-26 for more win, but only
  if a full dev re-gate still shows 0 THRASH. Use `.claude/tools/ab_iters` (free iter0-vs-iterN A/B) to localize.
