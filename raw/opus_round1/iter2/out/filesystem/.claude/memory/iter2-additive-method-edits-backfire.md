---
name: iter2-additive-method-edits-backfire
description: Iter2 proved (24 rollouts, 3 levers, 12-task breadth) that additive "do-more" method edits break strong tasks via displacement; committed a revert of iter1's net-negative prose back to byte-faithful bare.
metadata:
  type: project
---

**Iter2 outcome: REVERTED to byte-faithful bare.** Inherited harness was iter1 (the "issue census +
cross-reference every doc" prose), which the 30-task REAL-grader trend shows is **net-negative**:
iter0(bare)=0.8423 → iter1=0.8231 (**−0.019**). So the committed change = restore bare
(`system_prompt.md`==iter0 preamble; `agent_loop.py`==bare md5 63def2…; `tools.py` untouched).
Expected +0.019 real vs the inherited state. This is a *validated* net-positive commit, not a guess.

**Why I didn't ship an additive improvement (I built and tested 3 levers, ~$34/24 rollouts):**
- **Diagnosis of iter1 (confirmed on review-gov, cim, compare-leave):** the regression is
  **DISPLACEMENT/crowding-out**, NOT over-coverage. The census frame makes the agent restructure
  around exhaustive issue/doc taxonomies and **silently evict foundational "gimme" facts** bare stated
  plainly (authorized-share counts, aggregate $206.4M, "1x non-participating", EBITDA foot-error,
  matrix dimensions) and soften sharp judgments. Deliverables get longer but bury the graded specifics.
- **PROSE** (bare + anti-displacement method: lead with required outputs/foundational facts, prefer
  grounded specifics over breadth, + numeric discipline). 12-task proxy: 0.826→**0.849 (+0.023)** —
  BUT it **breaks strong tasks**: funds 0.947→0.842 (incl. 2 numeric criteria made WORSE) and
  arbitration 0.974→0.895 (drops specific points bare nailed). Same weak-helps/strong-hurts signature
  as iter1. Per-criterion verdicts proved the breakage is real, not noise.
- **LOOP** (bare + ENFORCED hard-capped finalize self-check, fires once). 5-task proxy 0.861→**0.794
  (−0.067)** — re-created iter1 displacement on the exact victim tasks despite "do not add issues".
  `check_runaway` PASSED (all <3× bare; turns ~2×), so it's not a runaway — it's a quality regression.
- **Numeric lever is DEAD.** Settlement figures stayed 0–1/10, extract 1/6 under bare, prose, AND
  enforced recompute. The error is **interpretation/inputs, not arithmetic** — and "recompute the
  figures" guidance can make a correctly-*transcribed* figure WRONG (funds C-026/C-048). Don't retry it.

**The core generalizing obstacle (the real lesson):** there is an **intrinsic asymmetry** — additive
"do more / develop fully / verify / recompute" guidance HELPS genuinely weak/under-produced tasks
(h1b 0.667→0.872, S-1 +0.078, extract +0.083) but BREAKS near-complete strong tasks via displacement
(drops gimme facts) and numeric-backfire. The train set is **strong-skewed** and the eval rewards
**all-pass**, so a single generic additive method nets **negative-to-coin-flip** on the real grader.
The bare harness sits near a local optimum for *generic method prose*.

**Proxy caveat (critical):** `proxy_eval` (gpt-5-mini) systematically **over-rates additive/elaboration
edits by ~+0.04** — it scored iter1 +0.02 (real −0.019) and PROSE +0.023 (real likely ≤0). On BARE it
tracks the real grader within ~0.03. So: trust proxy for BARE-relative *direction only on weak tasks*;
weight **mechanism evidence** (fact-retention greps, per-criterion deltas, strong-task regressions)
far above the proxy number. The fact-retention discriminator (does the edit KEEP the gimme facts bare
had?) was the most reliable signal.

**Next iteration — do NOT repeat:** another additive method-prose, a coverage push, or a verification/
finalize pass — all THREE now backfire on strong tasks (iter1, PROSE, LOOP). The remaining headroom is
NOT reachable by generic "do more" instructions. Promising-but-unproven directions instead: a mechanism
that fires ONLY for under-produced deliverables (conditional, hard to do safely/generically); or accept
bare as near-optimal for method and look at an orthogonal lever. Supersedes the (now-disproven)
"enforce more coverage" advice in [[iter0-issue-spotting-method]]. See also
[[run-harvey-agent-must-background]].
