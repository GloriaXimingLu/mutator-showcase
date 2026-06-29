# Key-Terms Extraction Memo — Deliverable Summary

**Deliverable:** `output/key-terms-extraction-memo.docx` (validated, board-ready)

## What was reviewed
- **Term Sheet** (May 29, 2025) — Non-binding Technology License Agreement for Whitmore's PredictIQ platform, prepared by KBI's counsel (Bergström Hecht).
- **MFC Side Letter** (May 29, 2025) — Most-favored-customer pricing provision, conditioned as a prerequisite to the deal.
- **Internal emails** (June 3, 2025) — Whitmore's CEO/GC/VP Sales flagging concerns and requesting outside counsel prepare a board-ready memo for the June 18 board meeting.

## Memo framing
Written from the perspective of Whitmore's outside counsel (Ferndale Hale & Seward LLP) for Whitmore's Board of Directors, ahead of the June 18, 2025 meeting and the June 23 response deadline. Risk flags and recommendations are from Whitmore's (licensor's) perspective.

## Structure
1. **Executive Summary** — deal snapshot, economics (~$9.6M first-year; ~20% of FY24 revenue; ~$24.5M 5-year), and a "proceed but renegotiate" recommendation.
2. **Key-Term Extraction** — section-by-section extraction of all 16 term-sheet sections plus the MFC side letter (7 tables: parties, dates, fees, SLAs, etc.).
3. **Risk Register** — 16-item summary table with severity ratings.
4. **Risk Flags & Negotiation Recommendations** — detailed Issue / Why-it-matters / Recommendation for each item.
5. **Negotiation Posture & Red Lines** — dealbreakers vs. high-priority fixes vs. acceptable terms.
6. **Process, Timeline & Next Steps** — dated action items.
7. **Open Diligence Items** — discrepancies to confirm (e.g., MFC look-back date, perpetual vs. 24-month wind-down license, firm-name inconsistency).
8. **Appendices** — 5-year fee schedule and the Exhibit B competitor list.

## Key risk flags identified
- **Critical (dealbreakers):** (1) Exclusivity/non-compete with open-ended 30% revenue definition; (2) Data-training ban + KBI ownership of model weights/Output Data; (3) Perpetual, no-sunset, no-carve-out MFC.
- **High:** Uncapped IP indemnification; 92% performance warranty with penalties; source-code escrow triggers + perpetual post-release license; perpetual wind-down license on convenience termination; German governing law.
- **Medium/Low:** Derivative-works joint ownership & §3.4/§3.5 contradiction; payment cash-flow mismatch (ASC 606); LoL super-cap; one-way assignment; SLAs; acceptance; currency/tax; binding no-shop.

## Validation
- Generated via Pandoc (docx skill `generate_from_md.py`).
- Passed `validate.py` (ZIP integrity, XML well-formedness, ECMA-376 schema, content-type/relationship consistency).
- Confirmed 7 tables and full heading hierarchy rendered correctly.