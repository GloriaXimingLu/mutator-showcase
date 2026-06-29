---
name: coverage-ledger-method
description: v0 edit — added a generic Coverage Ledger method to initial_skill.md targeting the omissions failure mode
metadata:
  type: feedback
---

v0 edit to `harness/skill/initial_skill.md`: added a generic **Coverage Ledger** method plus compute-the-figure, cite-the-rule/state-the-verdict, and scoping disciplines. Targets failure mode #1 (missing-element/omissions, ~38% of fails) and modes #2–#4 as sub-points.

Diagnosis from all 8 `rollouts/` grade.json files: fails cluster as required sub-points never put on the page — e.g. employment 21 fails are mostly "Flags/Add/Cite X" omissions (workers'-comp carve-out, mutual confidentiality, $25k LD, 409A clause, IP assignment, board-range flag); environmental 0.17 is a scoping error (agent worked the wrong property, discarded the graded Dayton docs); real-estate/trusts fails are compute-the-figure (interest, proration, totals never finished); immigration fails are missing Detail/Recommendation/Severity sub-elements.

**Why it generalizes:** the method encodes the *process* (enumerate required elements → mark present/absent → close all four sub-points per issue → synthesize) with no memorized statutes/numbers, so it transfers to held-out tasks of the same type with different facts. No per-task constants were added (per the overfit lesson).
