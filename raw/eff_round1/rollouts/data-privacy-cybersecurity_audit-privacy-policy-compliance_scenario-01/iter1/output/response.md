# Privacy Issue Identification Memo — Summary

## Deliverable
`output/privacy-issue-identification-memo.docx` — a privileged & confidential attorney-client / work-product issues memorandum from Thornbury & Locke LLP to Vaultline's General Counsel, dated March 28, 2025, in connection with the Series C due diligence (deadline April 15, 2025) and Q3 2025 EU launch.

## Documents Reviewed (cross-document)
1. **Privacy Policy** — Vaultline, last updated Jan 15, 2023
2. **Data Inventory** — Vaultline, v3.4, last updated Feb 18, 2025 (xlsx)
3. **Data Sharing Agreement** — Vaultline / Brightly Analytics, eff. Sept 1, 2022, amended June 15, 2024
4. **Breach Log** — Incident Response Log VT-IRL-2024-003 (Aug 2024 breach)
5. **Investor Counsel Email** — Elena Marchetti (Ashford Barnes) → Catherine Aldridge (Thornbury & Locke), March 3, 2025

## Approach
Read all five documents, then identified compliance gaps that emerge specifically from comparing the documents against one another (contradictions, practices disclosed in one document that contradict representations in another, and internal records confirming non-compliance visible only when read together).

## Findings — 15 issues
- **Critical (4):** (1) invalidated EU-U.S. Privacy Shield as sole transfer mechanism; (2) undisclosed/non-consented biometric processing (Selfie Verify) — BIPA exposure $87M–$435M (IL alone), plus TX CUBI and GDPR Art. 9; (3) undisclosed automated decision-making (Smart Insights) — GDPR Art. 22, no DPIA, fair-lending risk; (4) Aug 2024 breach — GDPR Art. 33/34 notification failures, 47-day consumer delay, missing state AG notifications.
- **High (6):** (5) Brightly "sale"/"sharing" undisclosed + DSA/policy inconsistency + uncapped indemnity; (6) GDPR governance (no DPO, no Art. 27 rep, no lawful basis, no DPIAs, minimal Art. 13/14); (7) potential GLBA applicability; (8) incomplete CCPA/CPRA rights & sensitive-PI disclosures; (9) indefinite data retention; (10) cookie consent non-compliance.
- **Medium (5):** (11) EU data-location inconsistency (Dublin vs. Virginia); (12) policy staleness/readability; (13) partner-referral potential "sale"; (14) DSA §9.2 breach-notice + indemnity; (15) security representations vs. actual controls.

Each issue includes documents implicated, the gap, legal/regulatory implications, and recommended remediation. A consolidated 12-row cross-document inconsistencies table and a prioritized remediation roadmap (sequenced to the April 15, 2025 and Q3 2025 deadlines) are included.

## Production
Authored as markdown, converted to .docx via the docx skill (`generate_from_md.py` / Pandoc), and validated with `validate.py` (exit 0 — ZIP integrity, XML well-formedness, content-type registration, and relationship consistency all pass).