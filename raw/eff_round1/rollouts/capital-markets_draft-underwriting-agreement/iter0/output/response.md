# Response Summary

## Task

Draft an execution-ready firm-commitment underwriting agreement for the IPO of Meridian Pulse Technologies, Inc. and prepare an issues memo flagging cross-document discrepancies and open items.

## Deliverables (in `output/`)

1. **`underwriting-agreement.docx`** — A complete, execution-ready firm-commitment Underwriting Agreement dated March 19, 2025 (Pricing Date), among Meridian Pulse Technologies, Inc., the Selling Stockholders (Cascade Kestridge Ventures, LP; Northlight Growth Partners Fund II, LP; and Dr. Anand Krishnamurthy), and Hargrove Securities LLC and Bellweather Capital Markets, Inc., as Representatives of the several Underwriters.
2. **`issues-memorandum.docx`** — A privileged issues memorandum flagging cross-document discrepancies and open items/conditions precedent to closing.

Both files were generated via Pandoc (markdown → docx) and validated with the docx skill's `validate.py` (ECMA-376 schema-valid, ZIP/XML integrity confirmed).

## Documents reviewed (9)

IPO Term Sheet; Engagement Letter; Amended and Restated Certificate of Incorporation; Credit Agreement Summary; Draft Comfort Letter; Form of Lock-Up Agreement; S-1 Registration Statement excerpts; Power of Attorney and Custody Agreement; Selling Stockholder Questionnaire (Cascade).

## Underwriting Agreement — structure

- Recitals; Article I (Definitions); Article II (Company representations); Article III (Selling Stockholder representations); Article IV (Sale/delivery of Shares, including Over-Allotment Option); Article V (Public offering, discount, delivery/payment); Article VI (Covenants); Article VII (Conditions to the Underwriters' obligations — comfort letter placed at Section 7.4 to match the Comfort Letter's "Section 7(d)" reference); Article VIII (Conditions to Company/Selling Stockholders); Article IX (Over-Allotment Option); Article X (Termination); Article XI (Indemnification & Contribution); Article XII (Expenses); Article XIII (Lock-Up, including Dr. Krishnamurthy springing extension); Article XIV (Miscellaneous).
- Schedules I–V (Underwriters/allocations; Selling Stockholders/shares; Capitalization/lock-up parties; Free Writing Prospectuses; Notices) and Exhibits A–D (form Lock-Up; Springing Extension Annex; Officers' Certificate; Secretary's Certificate; POA reference).
- Drafted to follow the Registration Statement (the operative disclosure) where the Term Sheet, Engagement Letter, or internal summaries conflict; critical open items flagged in brackets.

## Key discrepancies flagged in the Issues Memorandum

**Critical (blocking):**
- A-1: Credit facility lender — "Oakvale National Bank" (S-1, Comfort Letter, Term Sheet) vs. "Ridgemont National Bank" (Credit Agreement Summary).
- A-2: Credit facility terms — agreement date, maturity, interest rate, financial covenants, and change-of-control threshold (50% vs. 35%) differ between the S-1 and the Credit Agreement Summary.
- A-3: Comfort Letter circle-up vs. S-1 Capitalization/Dilution tables — total stockholders' equity ($198.4M vs. $101.4M), cash ($47.3M vs. $38.4M), and net tangible book value ($4.72 vs. $2.17).
- A-4: Mandatory prepayment / Use of Proceeds — ~$10M disclosed (S-1 Use of Proceeds & Capitalization table) vs. ~$15.2M required (S-1 Risk Factors & Credit Agreement).

**Material:**
- B-1: Lock-up springing extension for Dr. Krishnamurthy (in Term Sheet/POA; absent from form Lock-Up and S-1).
- B-2: Dr. Krishnamurthy shares to sell — 500,000 (S-1/POA/Term Sheet) vs. "up to 750,000" (Engagement Letter).
- B-3: Over-Allotment Option source — Company only (S-1/Engagement Letter/Questionnaire) vs. "Company and/or Selling Stockholders" (Term Sheet).
- B-4 / B-5: Cascade and Northlight general partner / control persons / address / entity-name inconsistencies across the S-1, POA, and Questionnaire (e.g., "Cascade Ridge Ventures, LP" in signature blocks vs. "Cascade Kestridge Ventures, LP").
- B-6: Dr. Krishnamurthy shares held — "approximately 8.5 million" (Term Sheet) vs. 8,400,000 (S-1/POA/Engagement Letter).
- B-7: Financial covenants — interest coverage 3.00x (S-1) vs. fixed charge coverage 1.25x (Credit Agreement); omitted minimum revenue covenant.
- B-8 / B-9 / B-10: "Net proceeds" definition; 10b5-1 plan treatment; early-release threshold.

**Open items / conditions precedent (C-1 through C-22):** final/bring-down comfort letters; legal opinions; officers'/secretary's certificates; lock-ups (incl. springing extension); Nasdaq approval; FINRA clearance; outstanding selling-stockholder questionnaires (only Cascade's provided); credit-agreement lender consent and equity-issuance notice; UT Austin license anti-assignment/security-interest; S-1 disclosure of springing extension; Investors' Rights Agreement termination; board observer seat; VitaBand/EEOC litigation monitoring; final public offering price; engagement-letter expense interaction; charter federal-forum provision; transfer agent/DTC; Section 382/NOL analysis; POA execution; and capitalization/dilution reconciliation.

A consolidated discrepancy register (severity, conflict, UA treatment) is included in Section VI of the Issues Memorandum.