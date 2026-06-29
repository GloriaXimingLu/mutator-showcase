# Key-Terms Extraction Memo — Deliverable Summary

**Deliverable:** `output/key-terms-extraction-memo.docx` (validated Microsoft Word document)

## What was reviewed
- **`kbi-whitmore-term-sheet.docx`** — Non-binding term sheet (16 sections + Exhibits A/B) for a PredictIQ technology license, prepared by KBI's counsel (Bergström Hecht Rechtsanwälte), dated May 29, 2025.
- **`kbi-mfc-side-letter.docx`** — Most-favored-customer pricing side letter from KBI to Whitmore, dated May 29, 2025.
- **`whitmore-internal-emails.eml`** — Internal Whitmore email thread (Kendrick/Yin/Malhotra, June 3, 2025) flagging concerns and requesting outside counsel prepare a board-ready key-terms extraction memo for the June 18 board meeting.

## Framing
The memo is written from the perspective of **Whitmore's outside counsel (Ferndale Hale & Seward LLP)** to **Whitmore's Board of Directors**, consistent with the internal emails' request. It analyzes the KBI-drafted documents from Whitmore's (licensor's) perspective, identifying risks to Whitmore and recommending negotiation positions.

## Memo structure
1. **Executive Summary** — commercial significance (~$9.556M Year 1; ~20% of FY24 revenue; ~$24.5M illustrative 5-year value) and the four red lines.
2. **Transaction Overview & Key Commercial Terms** — extraction table of all principal commercial and legal terms with citations.
3. **Risk Flags** — 37 issues classified by severity:
   - **4 Critical (Red)** red lines: data-rights cluster (§§ 3.5/4.2/4.3/4.4); exclusivity (§ 12); MFC pricing (Side Letter § 2); uncapped IP indemnity under German law (§§ 9.1/10.3/14.1).
   - **11 High (Orange):** perpetual wind-down license, derivative-works joint ownership, feedback/KBI-Inspired Improvements contradiction, escrow release triggers, performance warranty, cash-flow mismatch, asymmetric indemnity caps, liability cap/gross-negligence gap, perpetual term/no Whitmore convenience termination, assignment asymmetry, German governing law.
   - **12 Medium (Yellow):** expansion pricing, exclusivity scope/survival, maintenance-suspension/escrow cross-reference, SLA/performance asymmetry, no-shop, trade-secret confidentiality, permitted disclosures, undefined system requirements, KBI-caused delay, escalation/perpetual service term, arbitration/costs, Output Data deletion impracticality.
   - **10 Lower-priority/Favorable (Green):** deemed acceptance, late-payment interest, USD pricing, no refunds, consequential-damages exclusion, knowledge-qualified IP warranty, warranty disclaimer, escrow fee split, escrow verification limit, and the Fenwick/Ferndale firm-name discrepancy.
4. **Negotiation Priorities & Counter-Proposal Framework** — Tier 1 (red lines), Tier 2 (high-priority restructuring), Tier 3 (targeted adjustments), plus management's commercial counter-proposal (40/30/30 license split, front-loaded implementation, 18-month named-only exclusivity, permitted anonymized data use, time-limited MFC).
5. **Process & Timeline** — key dates through the June 23 response deadline and August 15 execution target, with recommended immediate actions.
6. **Conclusion** + signature block + privilege footer.

## Key cross-document findings highlighted
- The **data-rights cluster** (Output Data ownership of model weights + training restriction + KBI-Inspired Improvements license-back) collectively threatens PredictIQ's core IP — confirmed and amplified from the internal emails.
- The **triple lock**: MFC (best price, no sunset) + exclusivity (3-year market lockout) + expansion right (5-year frozen pricing) compound to severely constrain Whitmore's commercial freedom.
- The **perpetual theme**: perpetual license + perpetual term + perpetual wind-down license + no-sunset MFC.
- **Asymmetries** throughout (termination for convenience, assignment, indemnity caps) favor KBI.
- Noted the General Counsel's email reference to a "24-month" wind-down license and a "January 1, 2024" MFC look-back — neither appears in the operative documents as drafted (the wind-down license is in fact *perpetual*); flagged both as data points rather than asserting them as document terms.
- Noted the Side Letter's "Fenwick Hale & Seward LLP" vs. the emails' "Ferndale Hale & Seward LLP" firm-name discrepancy (minor).

## Validation
- Generated via Pandoc (`skills/docx/scripts/generate_from_md.py`).
- Passed `skills/docx/scripts/validate.py` (ZIP integrity, XML well-formedness, content-type registration, relationship consistency) — exit code 0.