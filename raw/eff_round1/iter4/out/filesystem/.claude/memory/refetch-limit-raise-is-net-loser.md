# Lesson — raising the eviction REFETCH_LIMIT above 1 is a NET LOSER (train-confirmed, iter3)

**Iteration 3 hypothesis (rejected):** the committed iter2 eviction (`MIN_TURN=28, WINDOW=12,
REFETCH_LIMIT=1`) leaves the cost-dominant **redline giants** (dev-only: subsequent/first-turn-redline,
13-15M input each) near bare, because `limit=1` disables eviction on the redline's FIRST backward
doc-reference. I tried `REFETCH_LIMIT 1→4` (relying on the per-doc `sticky` to bound per-doc loops,
with the global limit as a backstop) to let eviction persist on a redline's **cold tail**.

**Result — REJECTED on the cheap train loop (no dev gate spent).** Batch `ac8b03a7` (5 long train tasks),
iter3(limit=4) vs bare / iter2:
- **markup-of-settlement-agreement: 2.75M (iter2) → 4.37M (limit=4)** = **+33% vs bare** (3.29M). turns 32→39.
- **intercreditor-agreement: 2.48M (iter2) → 4.03M (limit=4)** = **+44% vs bare** (2.80M). turns 21→36.
- motion-to-dismiss ~flat (5.27M→5.37M, 38→45t); the two sub-gate tasks (cim 19t, saas 20t) unchanged.
- Net over the 5: limit=4 **18.47M > iter2 17.55M > bare 18.06M** → worse than the committed harness AND bare.
- THRASH check "clean" (each <1.5× turns), but the **mean hid two real input regressions** — exactly the trap.

## Why (the mechanism, now verified twice)
Negotiation/redline/markup tasks **re-read** their inputs (position letters, settlement docs, the growing
deliverable). Eviction evicts an aged doc → the agent re-reads it → the full doc re-enters context. With
`limit=1` the first such re-read **disables** eviction early, so these re-readers stay ~bare (protected).
Raising the limit lets eviction keep **churning** the re-readers (evict→reread→evict across several docs),
re-inflating context turn after turn. **The dev redline giants ARE re-readers**, so they would balloon the
same way — there is no free redline capture via evict-then-reread. This is the same failure the iter2 memo
saw at `limit=2` ([[eviction-length-gate-and-refetch-killswitch]]); confirmed independently here at `limit=4`.

## Standing conclusion
`REFETCH_LIMIT=1` is a tuned local optimum, not a conservative guess — **do not raise it.** The committed
iter2 config (`MIN_TURN=28, WINDOW=12, MINCHARS=6000, SIZEGATE=250000, REFETCH_LIMIT=1`) is kept. iter3
committed **no change** (banked the validated iter2 −28% / dev_score 0.8171 ≥ bare 0.8079).

## Dead ends ruled out this iter (don't re-explore without a new idea)
- **Dedup of re-read duplicates:** ZERO exact-duplicate large tool results in ANY train transcript — the
  agent reads distinct docs, never re-emits identical bytes. No savings there.
- **System-prompt trim:** the editable `system_prompt.md` is only ~570 tok; the ~4,350-tok bulk is appended
  skill manuals not in the 3 editable files. Negligible per-turn lever.
- **Remaining giant cost is structural:** late-turn context on the giants = evicted-doc stubs (already shed)
  + **accumulated assistant drafts** (never evictable — the work product) + re-reading redlines (churn if
  evicted). Read-eviction is largely tapped out at iter2.
- Watch for the **stale `scratch/test/harness/` copy** — it hijacks `import harness` for scripts run from
  that dir and reports OLD config values; test pure helpers by `exec`-ing the real file's source instead.
