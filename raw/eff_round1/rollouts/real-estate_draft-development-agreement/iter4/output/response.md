# Development Agreement Draft — Summary

## Deliverable
`output/development-agreement-draft.docx` — a draft Development Agreement for the Lakemont Station Commons mixed-use transit-oriented development, prepared on behalf of Granite City Development LLC (the "Developer"), with bracketed drafting notes flagging cross-document conflicts and open items.

## Source documents reviewed
1. **City Council Resolution No. R-2025-017** (adopted Feb 18, 2025) — conditional approval and conditions
2. **Negotiated Term Sheet** (Jan 22, 2025) — principal business terms between Developer and City
3. **Construction Loan Term Sheet** (First Prairie National Bank, March 2025) — $210M facility, lender requirements
4. **Lakeshore Capital Partners Fund III LP Side Letter** (Feb 10, 2025) — investor consent/anti-dilution rights
5. **Phase II Environmental Site Assessment** (Greenfield Environmental Consultants, Nov 8, 2024)
6. **RFP Response Narrative** (Granite City Development, Dec 16, 2024)
7. **TIF District Summary Memorandum** (Corporation Counsel, Mar 5, 2025)

## Structure of the draft
18 Articles plus Recitals, Signatures, and an Exhibit list:
- Art. 1 Definitions · Art. 2 Property & Land Conveyance · Art. 3 Project & Development Program · Art. 4 Phasing & Schedule · Art. 5 Public Incentives · Art. 6 Environmental Matters · Art. 7 Performance Security · Art. 8 Community Benefits · Art. 9 Construction Standards · Art. 10 Assignment & Change of Control · Art. 11 Completion Assurance (in lieu of reversionary interest) · Art. 12 Default, Cure & Termination · Art. 13 Indemnification · Art. 14 Construction Lender Protections · Art. 15 Representations & Warranties · Art. 16 Conditions Precedent · Art. 17 Dispute Resolution · Art. 18 Miscellaneous

## Developer-favorable positions taken
- **No reversionary interest** — substituted liquidated damages, a City repurchase option exercisable only after the Lender's mortgage is satisfied, and an enhanced completion guaranty (Art. 11), to preserve fee simple absolute title and enable the construction loan to close.
- **City bears environmental cost overruns** above the $3.14M base estimate, with broad surviving indemnity for pre-existing contamination (Art. 6).
- **TIF reimbursement priority** placing remediation and Developer on-site infrastructure first; City good-faith covenant to seek a TIF extension; abatement structured not to reduce TIF increment (Art. 5).
- **Narrower prevailing-wage scope** ("public works" only) and **good-faith local-hiring goal** (not a hard requirement/default trigger) (Arts. 8–9).
- **Key Person approach** to change-of-control in lieu of rigid percentage thresholds, with broadened permitted transfers and a 60-day cure period (Art. 10).
- **Lender protections incorporated** (cure rights, consent to amendments, subordination, foreclosure assignment, estoppels) so the loan can close (Art. 14).
- **Phased conveyance** option to protect the Phase I groundbreaking deadline (Art. 2).

## Principal cross-document conflicts / open items flagged (47 bracketed drafting notes)
The most critical:
1. **Reversionary interest vs. Lender prohibition** — Resolution Cond. 8 requires it; Lender prohibits it (loan impossible to close); Lakeshore requires consent. (Art. 11)
2. **36-month reversionary window vs. Sept 30, 2028 SC deadline** — the 36-month clock from conveyance would expire before the agreed completion date. (Art. 11)
3. **6-month Phase I commencement trigger vs. March 1, 2026 groundbreaking** — removed in favor of the groundbreaking deadline. (Art. 4.2 / 12.3)
4. **Change-of-control thresholds** — 50% (Term Sheet) / [50%] (Lender, negotiable) / 51% (Lakeshore). (Art. 10)
5. **TIF shortfall risk** — Corp Counsel estimates the $48M cap may fall $6–10M short with the abatement; recommends shortfall not be a City default. (Art. 5.2 / 12.6)
6. **Prevailing wage scope** — "all construction" (Term Sheet) vs. "public works" (Resolution). (Art. 9.1)
7. **Living wage / first-source hiring** — required by Resolution, silent in Term Sheet. (Art. 8.3–8.4)
8. **Environmental cost overruns** — who bears costs above $3.14M. (Art. 6.3)
9. **Parcel acquisition history discrepancy** — Resolution/TIF memo vs. Phase II ESA disagree on how Parcel 016 was acquired. (Art. 2.1 / 15.2)
10. **Equity demonstration deadline** — April 19, 2025 (Resolution) vs. 60 days from definitive Agreement approval (Term Sheet). (Art. 16.1)

A consolidated 30-item summary of open items appears at the end of the draft.

## Validation
`python skills/docx/scripts/validate.py output/development-agreement-draft.docx` → **valid** (exit 0). ZIP integrity, XML well-formedness, content-type registration, and relationship consistency all pass. The document contains 4 tables and ~14,655 words.