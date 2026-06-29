# Key-Terms Extraction Memo — Summary

## Deliverable
`output/key-terms-extraction-memo.docx` — a board-ready key-terms extraction memo with risk flags and negotiation recommendations, prepared from the perspective of Whitmore Analytics Inc.'s outside counsel (Ferndale Hale & Seward LLP) for the June 18, 2025 board meeting.

## Source documents reviewed
- `kbi-whitmore-term-sheet.docx` — non-binding term sheet (May 29, 2025) for the PredictIQ technology license, prepared by KBI's counsel.
- `kbi-mfc-side-letter.docx` — most-favored-customer pricing side letter (May 29, 2025), a condition precedent to the deal.
- `whitmore-internal-emails.eml` — June 3, 2025 email thread among Whitmore's CEO (Rajesh Malhotra), GC (Sarah Yin), and VP Sales (Tom Kendrick) flagging preliminary concerns.

## Memo structure
1. **Executive summary** with a risk-severity summary table.
2. **Transaction overview** and **summary of key commercial terms**.
3. **Key terms extraction** — every section of the Term Sheet (A–N) plus the MFC Side Letter (O).
4. **Risk flags** organized by severity: 3 Critical, 7 High, 6 Medium, and several Lower/favorable items.
5. **Negotiation recommendations** — specific, actionable counter-proposals mapped to each risk (R-C1…R-M6).
6. **Recommended negotiation posture & red lines** — three dealbreaker red lines plus high-priority concessions and items Whitmore can concede.
7. **Process, timeline & next steps** and **items requiring specialist review**.
8. **Appendix A** — five-year fee projection (~$24.5M total); **Appendix B** — document index.

## Key findings (the three critical/dealbreaker issues)
1. **Exclusivity / Non-Compete (TS §12)** — 3-year term with an open-ended "30% revenue" definition that could capture 25–30 additional European manufacturers (incl. 3 active prospects worth $4–5M recurring SaaS) and imposes an unworkable monitoring obligation.
2. **Data Rights (TS §§4.2–4.3)** — blanket prohibition on using KBI data (even anonymized/aggregated) to improve general ML models, plus an Output Data definition claiming KBI ownership of model weights/parameters/training artifacts — threatening PredictIQ's core model-improvement loop.
3. **MFC Side Letter** — no sunset, no carve-outs, retroactive, and extending beyond the term via the perpetual wind-down license.

## Validation
The .docx passed `validate.py` (ZIP integrity, XML well-formedness, content-type registration, relationship consistency) with exit code 0. All tables and formatting rendered correctly via Pandoc.