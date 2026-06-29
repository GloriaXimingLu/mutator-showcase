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

# ====================== ITERATION 3 (current) ======================
## State at start: harness/ = iter2 committed (eviction MIN_TURN=28, WINDOW=12, REFETCH_LIMIT=1).
##   dev_baseline (BARE): dev_score=0.8079, mean_input=4.48M, mean_turns=31.
##   iter2 (committed, per memory): dev_score=0.8171, mean_input=3.22M (-28%), THRASH=0.
## Backup of iter2 agent_loop.py -> scratch/agent_loop.iter2.bak

## Localization findings (re-verified this iter):
- ZERO exact-duplicate large tool results in ANY train transcript => dedup-of-re-reads is a dead end.
- Cost = N distinct docs read, re-sent every turn. Late-turn context on giants = stubbed reads (evicted) +
  ACCUMULATED ASSISTANT DRAFTS (not evictable). System prompt ~4,922 tok/turn fixed (editable part only ~570 tok).
- Train re-reads are mostly the agent's OWN OUTPUT deliverables on sub-28-turn tasks (eviction never fires).
  Only 2 train tasks cross MIN_TURN=28 (motion-to-dismiss 38t, saas-api 34t) => train cannot exercise the
  redline-giant re-fetch pattern. Redline GIANTS are DEV-ONLY (subsequent/first-turn-redline: 13-15M each).
- HYPOTHESIS: limit=1 kill-switch disables eviction on a redline's FIRST backward doc-reference => the
  cost-dominant redline giants revert to ~bare and capture ~no savings. That ~40M tokens (3 dev tasks) is
  the only sizable money left.

## EDIT under test (iter3 candidate): single change REFETCH_LIMIT 1 -> 4 (MIN_TURN=28, WINDOW=12 unchanged).
- Per-doc sticky (already present) bounds EACH doc to one extra read (no per-doc loop).
- Global backstop @4 bounds the cross-doc "re-read everything" flail to <=4 wasted reads then revert to bare.
- Read-then-draft giants (the proven -28%) UNTOUCHED (they rarely re-fetch -> limit never reached).
- Redlines: eviction now persists on the COLD TAIL through up to 4 backward-refs => intended new savings.
- GATEKEEPER: dev THRASH check. A redline that still loops (turns>=2x AND tokens>=1.5x vs bare) = REJECT -> revert to iter2.
- LANDMINE removed: scratch/test/harness was a stale iter2 copy hijacking `import harness`; deleted.
- Logic unit-tested on the REAL file (exec of helpers): LIMIT=4, backstop@4, sticky bounds loops. py_compile OK.

## Plan: train batch ac8b03a7 (5 long tasks) -> check_runaway + proxy -> ONE full dev gate -> commit iff
##   dev acc>=0.8079-noise AND dev input clearly < iter2's 3.22M (and < bare 4.48M) AND no THRASH. Else revert to iter2.

## ITER3 RESULT — REJECTED limit=4, KEPT iter2 (no dev gate spent)
Train batch ac8b03a7 (limit=4) vs iter2/bare:
  markup-settlement 2.75M->4.37M (+33% vs bare), intercreditor 2.48M->4.03M (+44% vs bare) = re-reader CHURN.
  net 5-task: limit4 18.47M > iter2 17.55M > bare 18.06M. THRASH "clean" but mean HID 2 regressions.
=> raising REFETCH_LIMIT churns re-readers (redline giants ARE re-readers) => net loser, matches iter2 memo (limit=2 thrash).
REVERTED harness/agent_loop.py to iter2 (diff-clean vs scratch/agent_loop.iter2.bak; limit=1, py_compile OK).
Did NOT spend dev gate: no train-validated candidate beats iter2; gating a disproven lever = waste.
Committed state = iter2 (validated -28% input, dev_score 0.8171 >= bare 0.8079). Lesson -> .claude/memory/refetch-limit-raise-is-net-loser.md
Budget used this iter: $5 (1 train batch). ~$154 / ~154min left, but nothing positive-EV to gate.

# ====================== ITERATION 4 (current) ======================
## State at start: harness/ = iter2 committed (eviction MIN_TURN=28,WIN=12,REFETCH_LIMIT=1).
##   dev_baseline(BARE): dev_score=0.8079, mean_input=4.48M. iter2(committed): 0.8171, 3.22M (-28%).
## Backup iter2 -> scratch/agent_loop.iter2_start.bak (== iter2.bak, confirmed).

## NEW FAMILY this iter (result-eviction is tapped out per memory): ASSISTANT TOOL-CALL ARG EVICTION.
## Localization (carry_breakdown.py on bare giants): after iter2 result-eviction, the largest UNTOUCHED
## carried residual is the agent's OWN emitted bytes:
##   - asst_other_tc (bash heredocs building deliverable scripts): motion-to-dismiss 612K (14% of bare,
##     ~28% of post-eviction residual). The agent does `cat >> build_docs.py << PYEOF ...` 7-13K each.
##   - asst_write_edit (write content / edit strings): underwriting 382K(17%), cim 279K(13%), settlement 188K(10%).
## These ride every later turn but result-eviction only mutates tool RESULTS, never tool-CALL args.
## LOSSLESS to shed: command already ran / content already on disk -> recover via `read`.

## EDIT (agent_loop.py): _evict_aged_call_args() mirrors _evict_aged_results() but on assistant msgs.
##   Elides bash.command / write.content / edit.old_string+new_string when aged>WINDOW & run>MIN_TURN(28)
##   & resident bulky args > SIZEGATE(40K) & body>=MINCHARS(6K). Replaces body w/ re-read stub (names file).
##   Handles BOTH adapter reprs (dict str-leaf AND JSON-string-leaf, escaped form, keeps JSON valid).
##   DECOUPLED from result-eviction kill-switch (own argevict_state) -> can still fire on redline
##   re-readers (where result-eviction disables) = potential win on the DEV redline GIANTS.
##   try/except -> degrades to bare on any error. If adapter uses opaque msg objects -> silent no-op (safe).
## Unit tests (exec real file source): both reprs shrink ~99%, JSON stays valid, all gates fire, idempotent. PASS. py_compile OK.

## Train batch .batch_46bdbfc3: motion-to-dismiss(39t save-signal), markup-settlement(40t save),
##   intercreditor(29t re-reader THRASH check), saas-api(20t sub-gate BARE check).
## Decision: confirm input DROPS vs bare/iter2 + no runaway/thrash + proxy acc healthy -> ONE full dev gate.
##   COMMIT iff dev acc>=0.8079-noise AND dev input clearly < iter2 3.22M AND no THRASH. Else keep iter2.
