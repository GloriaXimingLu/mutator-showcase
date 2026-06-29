# Iter2 analysis (mutator)

## Ground truth from rollouts/_stats (REAL ensemble grader, 30 train tasks)
- iter0 (bare) train mean = **0.8423**
- iter1 (current committed harness; added "issue census + cross-reference every doc" prose) = **0.8231**
- **iter1 REGRESSED -0.019.** Proxy on 6 tasks had said +0.02 → proxy mis-ranked (biased toward elaboration).
- Current `harness/` carries the net-negative iter1 prose forward.

## CONFIRMED diagnosis of iter1 regression (2 independent clean tasks + matrix task)
Mechanism = **DISPLACEMENT / crowding-out**, NOT over-coverage/fabrication:
- Census/cross-ref frame made agent restructure deliverables around exhaustive issue/doc taxonomies.
- This **silently evicted foundational "gimme" facts** bare stated plainly: authorized shares (C-001/2/3),
  aggregate liquidation pref $206.4M (C-008), "1x non-participating" (C-009), EBITDA foot error $16.8M (C-001),
  top-10 customer % (C-026), FY2024 segment $ (C-033), matrix dimensions (compare-paid-leave C-039..045).
- Also **softened sharp judgments into acceptances** (over-resolved open Qs; accepted figures rubric wanted challenged).
- Deliverables got +33% LONGER but buried specifics. Rubrics score all-pass on precise specifics, not catalog size.
=> The memory's "enforce MORE coverage" suggestion would make it WORSE. Do NOT double down on coverage.

## Bare's OWN dominant generic headroom (from iter0 (fail) criteria across 30 tasks)
**Cluster A — numeric/computational accuracy (the chosen lever; untouched by prior iters; zero displacement risk):**
- real-estate/settlement-statement (0.81): C-004 $2,558.40 interest, C-007 $28,798.40, C-034 $2,012.60 proration,
  C-049/050/054/056 totals — COMPUTED figures, mis-footed/dropped.
- trusts-estates/extract-key-exhibits (0.77): C-015 $123,300 equity, C-029 $193,200, C-052 $619,900, C-053 $241,700.
- capital-markets/S-1 (0.79): C-071 gross proceeds $360M, cap table.
- cim-teaser: C-001 EBITDA bridge foot error.
Fix = compute derived figures PROGRAMMATICALLY (python via bash), verify totals foot, quote figures exactly.

**Cluster B — coverage of specific required issues (employment markup 0.60, h1b, jv).** Harder lever; iter1 proved
generic coverage-push backfires. Lead with required-outputs + grounded specifics instead of breadth.

## Plan
Baseline = BARE (revert iter1 prose). Candidates (one clean variable on top of bare):
- C_prose: bare + "Numbers & finalize discipline" method section (corrected, anti-displacement + numeric).
- C_loop: bare(minimal prose) + ENFORCED hard-capped (fires once) finalize self-check pass in agent_loop.py
  (verify required outputs present; compute/verify every figure; ground claims; do NOT add new issues).
Test 3 arms on focused batch (numeric + 3 iter1 victims), proxy + mechanism reasoning, check_runaway on C_loop.
Commit best validated. Proxy is biased toward elaboration so weight mechanism heavily; vs bare the numeric
gains should still show on proxy.
