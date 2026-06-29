# Task Summary

**Deliverable:** `output/ip-license-renewal-analysis-memo.docx` — a renewal analysis memorandum prepared from the licensee's (Greenfield Biosciences, Inc.) perspective.

## What was reviewed
All seven source documents in `documents/`:
- License A — CRISPR-Ag Suite IP License Agreement (2015) + exhibits
- License B — TraitForge Plant Trait Expression Platform License (2018) + exhibits
- License C — GenoMap Pro Software License Agreement (2020) + exhibits
- NovaTrait consolidated renewal Proposal (Oct 14, 2024 cover; refined Jan 15, 2025 terms)
- Prairielands Seed Cooperative sublicense + NovaTrait consent letter
- Clarendon IP Consulting patent-landscape analysis (Sept 14, 2020)
- Ridgemont/Oakvale financial-impact analysis (Feb 2025) — JSON + XLSX (14 sheets: royalty models, sensitivity, market comparables, switching costs, negotiation priorities, timeline, rate-cap analysis)

## What the memo covers
1. **Executive summary** with bottom-line recommendation (renew all three, on substantially revised terms).
2. **Background & scope** — the three agreements, the Prairielands sublicense, documents reviewed.
3. **Critical deadlines & procedural status** — standstill (Jun 29, 2025), missed renewal-notice deadlines, License A notice deadline (Mar 31, 2025), License C holdover.
4. **Aggregate financial impact** — current ~\$18.6M (4.81% of revenue) vs. proposed ~\$28.0M (7.22%), +49.9%, with caveats (Net Sales redefinition, user-cap overage, Prairielands pass-through, one-time costs).
5. **License-by-license analysis** (A, B, C) — financial terms, the Section 14.3 rate-cap argument, insect-resistance FOV removal, wheat expansion, improvement-ownership reversal, sublicense pass-through, anti-stacking offset, the '117 patent expiry / post-2028 step-down, biological-materials wind-down, audit expansion, source-code elimination, derivative-data ownership, user cap, Version 5.x.
6. **Switching-cost / BATNA analysis** per license.
7. **Patent landscape & IP-value assessment** (Clarendon) and **market comparables** (Ridgemont).
8. **Recommended negotiation strategy** + a 14-item prioritized counter-position matrix with specific numbers.
9. **Diligence & open items** — including a patent-term discrepancy (terminal disclaimers suspected), an MFL-clause reference to a non-existent Section 14.5, renewal-notice delivery confirmation, and a counsel-of-record correction.
10. **Next-steps timeline** and **conclusion**.

## Notable findings flagged for Greenfield
- Proposed rates/fees exceed market comparables in **all three** categories.
- Net Sales redefinition makes the effective License A rate ~6.70% (148.9% of current — barely within the 150% cap) and License B ~5.34%.
- Patent-term discrepancy between the original Exhibit A, the 2020 Clarendon report, and the renewal Proposal Appendix A (suggests terminal disclaimers; concentrates value in the '117 patent expiring Mar 2028 → strengthens the step-down argument).
- NovaTrait references a "Section 14.5 (MFL)" that does not appear in the executed License A.
- New 40% Prairielands pass-through where **no pass-through obligation exists today**.
- Critical data-ownership and source-code concessions in License C.

## How it was produced
Authored as structured markdown, converted to `.docx` via Pandoc (with a Word TOC field, 11 native tables, 106 rows), and validated with `skills/docx/scripts/validate.py` (exit 0 — schema-valid, ZIP/XML integrity confirmed). Dollar signs were escaped to prevent Pandoc math-mode interpretation and verified to render as literal `$`.

The intermediate markdown source is retained at `output/memo-draft.md`.