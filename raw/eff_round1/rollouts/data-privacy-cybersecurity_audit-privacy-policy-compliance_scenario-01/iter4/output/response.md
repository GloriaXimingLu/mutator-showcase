# Privacy Issue Identification Memo — Summary

## Deliverable
`output/privacy-issue-identification-memo.docx` — a privileged issues memo (Thornbury & Locke LLP → Vaultline GC) identifying cross-document privacy/data-protection compliance gaps ahead of the Series C due diligence deadline (April 15, 2025) and EU launch (Q3 2025).

## Documents reviewed
1. **Privacy Policy** (vaultline-privacy-policy.docx) — Last Updated Jan 15, 2023
2. **Data Inventory** (vaultline-data-inventory.xlsx) — v3.4, Feb 18, 2025
3. **Brightly Data Sharing Agreement** (brightly-data-sharing-agreement.docx) — eff. Sept 1, 2022, amended June 15, 2024
4. **Incident Response Log** (incident-response-log-aug2024.docx) — Aug 2024 breach
5. **Investor counsel email** (investor-dd-privacy-memo.eml) — Mar 3, 2025

## Method
Triangulated public-facing representations (Privacy Policy) against internal records (Data Inventory), contractual commitments (Brightly DSA), incident history (Breach Log), and the investor's preliminary findings (Investor Letter). Gaps arise where documents conflict or where internal records reveal practices not disclosed to consumers.

## Findings — 18 issues identified
- **5 Critical:** (1) undisclosed biometric data / Selfie Verify — BIPA exposure $87M–$435M, GDPR Art. 9; (2) invalidated Privacy Shield with no valid EU transfer mechanism; (3) undisclosed automated decision-making / Smart Insights — GDPR Art. 22, no DPIA; (4) Brightly data sharing likely a CPRA "sale"/"sharing" with no disclosure or opt-out; (5) Aug 2024 breach — missed/undocumented GDPR Art. 33 and CA AG notifications, 47-day delay.
- **7 High:** GDPR Art. 13/14 transparency (no DPO, no Art. 27 rep); no DPIAs; sensitive PI not classified / no right to limit; incomplete CPRA rights; indefinite retention with no periods disclosed; "does not sell" statement contradicted by revenue sharing; non-compliant cookie banner (29 third-party cookies).
- **6 Medium:** GLBA applicability; browsewrap-only lawful basis; incomplete third-party recipient disclosure; partner referral fees as potential sale; Brightly DSA contractual gaps (no DPA, perpetual retention, indemnity risk, false reps); stale/unreadable policy.

Plus a dedicated section on **6 cross-document factual inconsistencies** (e.g., EU data location: Breach Log says "partially replicated" in Dublin vs. Data Inventory says "all on Virginia servers").

## Structure of the memo
I. Introduction & Scope · II. Executive Summary · III. Risk matrix table · IV. Detailed analysis (Issues 1–18, each with cross-document evidence, legal authority, and risk) · V. Cross-document inconsistencies · VI. Prioritized remediation · VII. Conclusion.

## Validation
Generated via Pandoc (docx skill `generate_from_md.py`); passed `validate.py` (ZIP integrity, XML well-formedness, content-type/relationship consistency) with exit code 0.