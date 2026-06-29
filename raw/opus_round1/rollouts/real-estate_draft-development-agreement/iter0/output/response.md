# Development Agreement Draft — Summary

## Deliverable
`output/development-agreement-draft.docx` — a negotiation draft of the **Development Agreement** for the Lakemont Station Commons mixed-use transit-oriented development, prepared on behalf of **Granite City Development LLC** (Developer) against the **City of Lakemont, Illinois**.

## Source documents reviewed
1. `negotiated-term-sheet.docx` — principal business terms (non-binding)
2. `rfp-response-narrative.docx` — Developer's winning proposal
3. `city-council-resolution-r2025-017.docx` — conditional approval + 8 conditions
4. `construction-loan-term-sheet.docx` — First Prairie National Bank $210M facility
5. `lakeshore-side-letter.docx` — equity investor consent/anti-dilution rights
6. `phase-ii-esa-summary.docx` — environmental findings & remediation
7. `tif-district-summary-memo.docx` — City counsel's TIF/prevailing-wage analysis

## Approach
- Drafted a 20-article definitive agreement reflecting the **Developer's interests** (broad City environmental indemnity with cost-overrun allocation to City; no reversionary interest; TIF priority reimbursement + good-faith extension covenant; broad permitted-transfer/change-of-control carve-outs with a Key-Person alternative; phased-conveyance option; developer-friendly cure periods and termination rights; living-wage scope limited to controlled entities; local hiring as a good-faith non-default goal; built-in lender protections required to close the loan).
- Embedded **31 bracketed drafting notes** throughout flagging cross-document conflicts and open items, plus an **Appendix Index** organizing 27 open items into three tiers (Critical/High-Priority, Cross-Document Conflicts, Open Items Requiring Negotiation).

## Highest-priority conflicts flagged
1. **Reversionary interest (Resolution #8) vs. Lender's absolute prohibition** — the central conflict. Resolution requires automatic reversion if Phase I isn't complete in 36 months; the construction loan term sheet states this would make the loan "impossible to close" (uninsurable title). Draft substitutes a contractual **Repurchase Option subordinate to the lender's mortgage**, exercisable only after cure periods and lender consent/loan satisfaction.
2. **Force majeure cap** — Term Sheet's 18-month project-wide cap vs. Lender's 180-day Phase I cap (direct Development Agreement vs. Loan Document conflict).
3. **Living wage / permanent-employee requirements** — imposed by Resolution but absent from the Term Sheet; draft limits scope to Developer-controlled entities.
4. **Change-of-control threshold** — three competing thresholds (50% / [50]% / 51%) across Term Sheet, Lender, and Lakeshore Side Letter.

## Other conflicts/open items flagged
RFP number discrepancy (2024-CD-07 vs 2024-CD-018); parcel acquisition history (Parcel 016: tax forfeiture vs. direct purchase); per-parcel acreage; insurance CGL aggregate ($20M vs $25M); equity-demonstration timing/trigger; local-hiring metric (employment vs. labor hours); affordable-unit count ("at least 100" vs 106); NFR letter vs. RAP approval as condition precedent; phased conveyance feasibility; environmental cost-overrun allocation; TIF shortfall risk ($6–10M under abatement scenario); land write-down/infrastructure funding source vs. TIF cap; abatement/TIF interaction; hotel-brand approval; community-center conveyance terms; later-phase performance security; additional later-phase financing consent interplay; rezoning appeal-period risk; lender protections; prevailing-wage scope; mediation administrator; and exhibit preparation.

## Validation
- Generated via Pandoc (`generate_from_md.py`); tables (financing sources, phasing schedule) rendered correctly.
- Passed `validate.py` (ZIP integrity, XML well-formedness, content-type registration, relationship consistency) — exit code 0.
- ~12,700 words; 20 articles + signature page + appendix index.