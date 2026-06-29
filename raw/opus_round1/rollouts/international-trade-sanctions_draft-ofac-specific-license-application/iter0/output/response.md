# Deliverables Summary

## Task
Draft an OFAC specific license application package and an internal issues memo from the attached source documents.

## Outputs (in `output/`)
1. **`ofac-specific-license-application.docx`** — Formal OFAC specific license application package prepared by Ashford & Whitmore LLP on behalf of Meridian Biotech Solutions, Inc.
2. **`issues-memorandum.docx`** — Internal attorney-client privileged / work-product issues memorandum analyzing the legal issues and recommending the approach reflected in the application.

Both files were generated via Pandoc from markdown using a custom legal-styled reference template (Times New Roman 11pt, 1" margins, styled headings) and passed the docx validation gate (ZIP integrity, XML well-formedness, relationship consistency).

## Source documents reviewed
- `client-email-transaction-summary.eml` — transaction brain-dump from Meridian's GC
- `compliance-screening-memo.docx` — CCO screening results (two SDN matches flagged)
- `dcuh-purchase-order.docx` — end-user PO (PO-DCUH-2024-0743)
- `graystone-audit-summary.docx` — independent compliance program audit
- `prior-ofac-license-syr-2021.docx` — prior specific license (precedent)
- `product-technical-datasheets.docx` — RX-700 / CalibPro 3100 / training specs
- `shipping-logistics-plan.docx` — Pinnacle five-leg shipping route
- `who-syria-needs-assessment.docx` — humanitarian justification

## Key facts captured
- **Transaction:** Export of 500 CancerDetect RX-700 reagent kits ($1,170,000), 4 CalibPro 3100 calibration units ($75,000), and ~40 hrs remote training ($35,000) = **$1,280,000 total** to Damascus Central University Hospital (DCUH), a Government-of-Syria instrumentality.
- **Classification:** Both products EAR99; OFAC authorization still required under 31 C.F.R. Part 542 / E.O. 13582.
- **Requested license period:** Sept 1, 2024 – Feb 28, 2026.
- **Prior license:** SYR-2021-384712 (TB kits to Al-Mujtahid Hospital; completed Jan 2023; no violations).

## Two material screening findings (resolved by restructuring before filing)
1. **SDN-listed 30% shareholder of original customs agent** — Samir Daoud Khoury (SDN, added Apr 15, 2024) owns 30% of ARMPC. Below the 50 Percent Rule blocking threshold, but material risk. **Resolution:** ARMPC removed; substitute a pre-screened, non-SDN customs agent disclosed to OFAC.
2. **SDN-listed remitting bank** — Central Bank of Calverley (SDN since Aug 10, 2011). **Resolution:** payment rerouted through a non-SDN Syrian commercial bank, consistent with the prior license.

## Application structure (17 parts)
Transmittal letter → Applicant info → Counsel → Summary → Transaction → Goods/services → Export classification → End-user/end-use → Parties → Shipping → Payment (restructured) → Humanitarian justification → Prior license history → Compliance program → **SDN disclosure & mitigation** → Requested license terms/conditions → Certifications → Exhibits A–I.

## Issues memo structure
Executive summary → Transaction overview → Legal framework → Issue analysis (A. Khoury/ARMPC & 50% Rule; B. CBS payment; C. governmental end-user; D. technology transfer/deemed export; E. end-use monitoring/diversion; F. EAR99 classification; G. timing) → Recommended transaction structure → Recommended license conditions → Open items/client action list → Conclusion.

## Notes
- Currency amounts render cleanly (Pandoc `tex_math_dollars` disabled so `$` is literal).
- The application discloses both SDN findings candidly and presents a clean, approvable restructured transaction; the memo provides the underlying options analysis and recommendations.
- Open items (alternative customs agent, alternative remitting bank, end-user certificate, end-use monitoring plan, encryption/EAR99 confirmation, firmware-update policy, shelf-life planning) are flagged for client action.