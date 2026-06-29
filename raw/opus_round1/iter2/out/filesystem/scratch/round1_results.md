# Round 1 results (5 tasks, single seed, proxy = gpt-5-mini)

Proxy on BARE tracks real iter0 grades well (within ~0.03), so it's a usable triage signal here.

| task | BARE proxy | PROSE proxy | BARE turns | PROSE turns | numeric (bare→prose) |
|---|---|---|---|---|---|
| real-estate/settlement-statement | 0.823 | 0.823 | 33 | 24 | 1/10 → 1/10 |
| trusts/extract-key-exhibits | 0.700 | 0.783 | 15 | 19 | 1/6 → 1/6 |
| corporate-ma/cim-teaser | 0.854 | 0.902 | 26 | 18 | - |
| corporate-ma/review-gov-diligence | 0.963 | 0.981 | 15 | **43** | - |
| corp-gov/compare-paid-leave | 0.967 | 0.950 | 29 | 23 | - |
| **MEAN** | **0.861** | **0.888 (+0.026)** | | | |

## Key findings
- **PROSE numeric discipline FAILED to change behavior**: figures still 1/10, 1/6 (settlement proxy
  identical 0.823). The agent SILENTLY SKIPS the "compute with python / verify footing" prose rule.
  => numeric is a **RELIABILITY gap, not a method gap** -> needs ENFORCEMENT (agent_loop), per manual.
- PROSE's +0.026 gain comes from the "develop fully / required-outputs" framing (extract +0.083,
  cim +0.048), NOT from numeric.
- PROSE blew review-gov to **43 turns (2.9x bare=15)** — near the 3x canary abort line. RISKY.
- Good news: PROSE did NOT re-create the iter1 displacement disaster (compare-leave 0.95 not 0.72,
  review-gov 0.98 not 0.81). So the anti-displacement framing held.

## Next: LOOP arm — does ENFORCED finalize pass force the numeric recompute prose couldn't?
Expect: figures improve (>1/10), turns modest (bare + 1 pass, NOT 43). check_runaway required.

## LOOP arm results (REJECTED)
| task | BARE | PROSE | LOOP | LOOP turns (vs bare iter0) |
|---|---|---|---|---|
| settlement | 0.823 | 0.823 | 0.823 | 63 (2.5x) |
| extract | 0.700 | 0.783 | 0.783 | 33 (1.8x) |
| cim | 0.854 | 0.902 | 0.780 | 38 (1.1x) |
| review-gov | 0.963 | 0.981 | 0.852 | 27 (1.5x) |
| compare-leave | 0.967 | 0.950 | 0.733 | 38 (1.7x) |
| MEAN | 0.861 | **0.888** | 0.794 | check_runaway PASS (all <3x) |

- LOOP **−0.067**: the enforced finalize pass RE-CREATED iter1 displacement (compare-leave 0.733≈iter1's 0.72,
  review-gov 0.852≈iter1's 0.81) despite "don't add issues" — giving the agent another rework turn made it
  reorganize and bury facts. REJECTED.
- Numeric figures: NEITHER prose nor enforced recompute fixed them (settlement 0/10-1/10, extract 1/6 all arms).
  => numeric error is INTERPRETATION/inputs, not arithmetic — NOT method-fixable. Numeric lever DEAD.
- **Fact-retention discriminator (review-gov gimme facts iter1 dropped):** BARE 3/4, PROSE **4/4**, LOOP 2/4.
  PROSE keeps MORE facts than bare AND is more concise (77K vs 96K). => PROSE's +0.026 is real (anti-displacement),
  NOT elaboration inflation. PROSE prose is the OPPOSITE direction from iter1 (prefer specifics over breadth).

## Decision: validate PROSE vs BARE on 7 NEW distinct tasks (breadth), then commit if net up.
