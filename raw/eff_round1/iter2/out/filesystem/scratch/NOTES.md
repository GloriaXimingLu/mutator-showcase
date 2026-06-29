# Iteration 2 working notes

## Inherited state (iter1 = eviction edit, currently in harness/)
- Free A/B (ab_iters): iter1 vs iter0(bare): **input -6.4% overall**, **mean dAcc -0.0265**, 1 THRASH, 4 watch.
  => inherited eviction is a NET LOSER: barely cuts cost (thrasher cancels wins) AND drops accuracy.
- Model = **glm-5p2** (not Anthropic). cache_read=0 everywhere (no prompt caching; can't reach it from my surface).

## Root causes found
- "THRASH" corporate-ma/review-governance-diligence (18->73 turns, 1.37M->7.05M): NOT a re-fetch loop.
  ZERO doc re-reads; it was a **docx-generation flail** (24x python3 -c, 6x pdftotext, 5x generate_from_md.py).
  => GLM run-to-run variance, largely independent of eviction.
- Real eviction accuracy damage is on SHORT issue-spotting/extraction tasks (<=~20 turns):
  tax(17t) -0.143, cannabis-extract(22t) -0.088, arbitration(13-14t) -0.075/-0.079 — docs evicted before facts fully used.
- Eviction WINS on LONG drafting/redline tasks: motion-to-dismiss(39t) -60%, settlement-stmt(25t) -45%, intercreditor(29t) -33%.

## My edit (agent_loop.py) — conservative + thrash-proof eviction
1. **Task-length gate** `_EVICT_MIN_TURN=20`: no eviction until run passes 20 turns.
   Protects ALL short/medium tasks (they finish <=20t) exactly like bare => zero accuracy risk where cost is tiny.
   Only long drafting/redline runs (where the dollars are) cross the gate.
2. **Re-fetch kill-switch** `_EVICT_REFETCH_LIMIT=2`: re-fetch (re-read OR re-run bash/grep/glob) of an evicted
   output pins it sticky; after 2 re-fetches eviction DISABLES for the rest of the run. Bounds any evict->re-fetch loop.
3. Generalized `_evict_key` to cover bash/grep/glob (not just read). Window 10->12. Size gate 250k kept.
- Unit-tested logic in scratch/test (min-turn gate, window, sticky, kill-switch, evict_key) — ALL PASS. py_compile OK.

## Train validation batch (launched, $5): marker .batch_d6b10478.done
- motion-to-dismiss(39t), JV(32t), cim-teaser(34t)  -> expect eviction fires, cost down, NO thrash
- tax(17t), review-governance(18t)                  -> expect BARE behavior (eviction never fires) => acc protected
- Expected: cost win on long tasks, accuracy held on short tasks, no thrash.

## Train validation RESULTS (batch d6b10478) — my edit vs bare
| task | turns b->me | input b->me | tok% | proxy acc |
|---|---|---|---|---|
| motion-to-dismiss | 39->30 | 5.62M->3.04M | -46% | 0.978 |  (LONG, eviction fired => real win)
| JV agreement | 32->21 | 3.49M->2.79M | -20% | 0.804 |
| cim-teaser | 34->14 | 3.28M->0.85M | -74% | 0.805 |  (14t: variance, eviction didn't fire)
| tax | 17->18 | 1.64M->1.57M | -4% | 0.893 |  (<20t: bare behavior, acc protected)
| review-governance | 18->23 | 1.37M->1.75M | +28% | 0.907 | (NO thrash; iter1 was 73t/7M!)
- check_runaway: ALL within 3x bare (max 1.3x). THRASH CHECK clean. proxy acc all healthy.
- Attributable win = long tasks (motion-to-dismiss -46% acc-intact); short tasks untouched (their swings = GLM variance).
- KEY: kill-switch+min-turn KILLED the iter1 thrash (review-governance 73t->23t).

## Dev GATE 1 (MIN_TURN=20, REFETCH=2) — result:
- dev_score=0.8059 vs bare 0.8079 => -0.002 (PASS, within noise)
- mean_input=3,527,946 vs bare 4,482,674 => **-21.3%** (PASS cost)
- **THRASH: 1** data-privacy/extract-document-requests 17->38 turns, 808K->3.55M (2.2x/4.4x). acc held 0.846.
  => HARD REJECT. Diagnosis: per-turn ctx ~93K vs bare ~47K (2x) => eviction-induced RE-FETCH LOOP
     (agent re-read docs repeatedly, re-inflating ctx). REFETCH=2 let it build up. Small task drifted past turn-20 gate.

## FIX (gate 2): MIN_TURN 20->28, REFETCH_LIMIT 2->1
- REFETCH=1: first re-fetch DISABLES eviction => max 1 extra read => 4.4x loop impossible by construction.
  Also self-targeting: redline tasks (re-read) revert to bare immediately; read-then-draft tasks keep full win.
- MIN_TURN=28: small/medium tasks finish well under 28 even on variance => never disrupted. Huge dev tasks (48-108t) still trigger.
- Re-validated logic tests (boundary turn28 untouched / turn29 evicts / 1 refetch disables). py_compile OK.
- Fixing the thrash also HELPS mean (that task 3.55M->~bare 0.8M).
- Dev GATE 2 launched (.dev_a9a0c38d.done, fresh worker PID1374 @16:31). budget remaining ~$122 before, ~$89 after.

## Decision rule
COMMIT only if dev: acc >= bare(0.8079) - noise AND input clearly < bare(4.48M) AND no THRASH.
dev_baseline: dev_score_bare=0.8079, mean_input=4,482,674, mean_turns=31.

## DEV GATE 2 RESULT — COMMITTED ✓
- dev_score=0.8171 vs bare 0.8079 (+0.009) PASS
- mean_input=3,221,029 vs bare 4,482,674 (-28.1%) PASS
- THRASH=0 (3 watch @1.5-2x, all on <=28-turn tasks => eviction never fired => GLM variance, not the edit) PASS
- Former thrasher data-privacy/extract: 38t/3.55M -> 21t/1.25M, acc 0.846->0.865. FIXED.
- ALL THREE gate conditions hold => COMMIT (leave edited agent_loop.py in harness/).
- Memory written: eviction-length-gate-and-refetch-killswitch.md + glm-variance-and-docx-flail.md
- Broker spend: $71.12 (5 run_harvey + 0.12 proxy + 2 dev gates). Remaining ~$88.88.
