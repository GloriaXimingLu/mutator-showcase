# Summary of Work

## Deliverable
`output/compromise-ica-terms.docx` — a privileged and confidential attorney memorandum proposing compromise clause language for all four contested provisions of the Meridian Industrial Holdings Intercreditor Agreement (ICA).

## Source Documents Reviewed
All 11 documents in the `documents/` directory were read in full:
- **Position letters:** `cartwright-position-letter.docx` (1L Agent), `ridgeline-position-letter.docx` (2L Agent)
- **Internal flexibility emails:** `buchanan-internal-summary-email.eml` (1L counsel), `oduya-internal-summary-email.eml` (2L counsel)
- **Engagement email:** `tanaka-engagement-email.eml` (Borrower's counsel engagement)
- **Market data:** `ica-market-survey.xlsx` (42-deal survey), `meridian-capital-structure-summary.xlsx`
- **Draft agreement:** `draft-intercreditor-agreement.docx`
- **Supporting documents:** `first-lien-credit-agreement.docx`, `second-lien-credit-agreement.docx`, `lender-appraisal-summary.docx`, `standard-form-ica.docx`

## Memorandum Structure
1. **Privilege legend** — PRIVILEGED & CONFIDENTIAL / Attorney-Client Communication / Attorney Work Product / FRE 408 (marked at top, in legend, and at bottom)
2. **Memorandum header** — To Sandra Koh-Wexler (CEO), From David Tanaka (KTM LLP), dated June 27, 2025
3. **Executive summary table** — all four provisions with 1L/2L opening positions, proposed compromise, and market benchmark
4. **Capital structure context** — leverage, LTV, pricing, covenants, timeline
5. **Four contested provisions** — each with full contractual drafting + negotiation rationale:
   - **§ 3.01(b) Standstill:** 180 days + 3 early termination triggers + Blockage Notice cap
   - **§ 5.01 Purchase Right:** par at non-default rate + optional revolver assumption + LC treatment
   - **§ 2.03(c) Permitted Refinancing:** 10% cap (fees/costs only) + "later of" maturity + narrowed restrictiveness test + MFN
   - **§ 4.02 Proceeds Waterfall:** bifurcated (ordinary-course ≤$20M reinvestment vs. >$20M hard sweep) + anti-evasion + 2L residual + reporting
6. **Interdependence section** — explains why the four provisions form a single indivisible package
7. **Market survey summary** — four data tables with all cited statistics
8. **Recommended next steps** and **reservation of rights**

## Key Features
- **Full contractual drafting** for each provision (insertion-ready language with defined terms, provisos, and cross-references to the credit agreements)
- **Negotiation rationale** for each provision citing both sides' expressed flexibility (from the internal emails) and explaining why the compromise lands within each zone
- **Market data citations** throughout (42-deal survey statistics, Deal-007 comparable transaction)
- **Economic quantification** (e.g., $9.30M accrued interest at non-default rate vs. $11.67M at default rate = $2.37M/90-day savings; $15M principal increase; $20M ordinary-course threshold; $165M equity cushion; 97.66% Total LTV)
- **Single indivisible package** framing with explicit linkage analysis

## Validation
- Generated via `generate_from_md.py` (Pandoc + standard-form-ica.docx reference template)
- Passed `validate.py` (ECMA-376 schema validation, ZIP integrity, content-type registration, relationship consistency)
- 139 paragraphs, 6 tables, ~52KB