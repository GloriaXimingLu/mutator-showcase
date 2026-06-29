# Governance Diligence Memo — Deliverable Summary

**Deliverable:** `output/governance-diligence-memo.docx` (validated, ~20 pages)

## What was done

Reviewed all seven governance documents for the proposed acquisition of Terravox Systems, Inc. by Hargrove Capital Partners III, LP (reverse triangular merger; $485M EV / ~$473M equity value):

- Third Amended & Restated Certificate of Incorporation (Nov 3, 2021)
- Amended & Restated Bylaws (Nov 3, 2021)
- Stockholders' Agreement (Nov 3, 2021)
- Voting Agreement (Nov 3, 2021)
- Registration Rights Agreement (Nov 3, 2021)
- Board Minutes, Jan 2023 – Sep 2024 (8 meetings)
- Hsieh diligence scoping email (Oct 14, 2024)

The memo is organized per the email's instructions: privilege/work-product marking, Executive Summary, ten numbered diligence sections, Recommended Next Steps/Action Items, a Consent/Approval Matrix (Appendix A, 12-row table), and a Severity Classification (Appendix B).

## Headline findings

1. **Stonemill holds a hard, non-circumventable blocking right.** Stonemill owns 100% of the Series C Preferred (7,800,000 of 7,800,000 shares). Charter §4.3.6(b)(i) requires 66⅔% Series C separate-class consent to effect any Liquidation Event, and the merger is unambiguously a Liquidation Event. The transaction **cannot close without Stonemill's affirmative consent.**

2. **The drag-along cannot override the Charter veto.** The drag-along is triggerable without Stonemill (Ridgeline + Northbridge clear the Preferred-majority and "2-of-3" prongs; the Common-majority prong needs ~950K additional shares), but under Delaware law a contractual drag-along cannot reliably override an express charter protective provision requiring a separate-class vote. The Charter also cannot be amended to remove the veto without Stonemill's own consent (catch-22). **No viable path to closing over Stonemill's objection.**

3. **SensorLink LOI exclusivity — CRITICAL/time-sensitive.** The LOI's exclusivity auto-renews in 90-day increments unless terminated by 15-days-prior written notice; the CEO could not confirm a termination notice was sent before the Sep 8, 2024 expiration. A live exclusivity may conflict with signing a definitive agreement.

4. **Clearfield $12M term loan — apparent Charter violation.** Exceeds the $5M indebtedness threshold in §4.3.6(a)(v); Board Minutes show only Board approval, no Preferred consent.

5. **Special Committee composition — Okafor (Northbridge designee) not disinterested** → Revlon/sale-process vulnerability.

6. **RRA "Deemed Liquidation Event" is undefined** → registration rights may survive the merger; needs express termination at closing.

7. **Waterfall error in the Board record** — Sep 25 minutes incorrectly state all Preferred would receive more than their preferences as-converted; Series C's $18.50 preference exceeds the ~$12.59–$13.95 as-converted value, so Series C takes its $144.3M preference.

8. **Document gaps** — 2021 Equity Incentive Plan, individual award agreements, and stockholder consent records not yet produced.

## Method

Drafted the memo in markdown, generated the .docx via the docx skill's Pandoc generator (`generate_from_md.py`), and ran the mandatory `validate.py` gate (passed: schema-valid, ZIP/XML integrity confirmed). Numerical analysis (liquidation waterfall, drag-along thresholds, consent math) was verified with a Python script.