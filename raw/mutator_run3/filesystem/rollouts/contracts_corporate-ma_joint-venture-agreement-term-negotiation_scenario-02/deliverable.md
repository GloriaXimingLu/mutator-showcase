# Summary of Work

## Deliverable
`output/mkpoly-jva-compromise-provisions.docx` — a validated Word document containing compromise contract provisions for the five contested sections of the MKPoly Coatings, LLC Joint Venture Agreement.

## Source documents reviewed
- **Position papers:** `kastor-position-summary.docx` (Kastor's positions, minimums, flexibility), `meridian-negotiation-playbook.docx` (Meridian's playbook, fallback ladders, red lines)
- **Emails:** `cordero-to-falk-internal-guidance.eml` (Meridian CEO's business-side mandate), `falk-to-escalante-negotiation-email.eml` and `escalante-to-falk-response.eml` (counsel exchange confirming process, deliverable format, and priority signaling)
- **Drafts:** `mkpoly-jva-v3-clean.docx` and `mkpoly-jva-v4-redline.docx` (extracted the actual contested section text and competing tracked-changes markups for Sections 4.03, 5.01, 10.03, 11.01, 12.05), `standard-jva-template.docx` (used as the Pandoc reference template for styling), `term-sheet-executed.docx`
- **Supporting data:** `capital-contribution-schedule.xlsx`, `frazier-whitmore-valuation-benchmarks.xlsx` (comparable multiples 6.2×–8.1×, median 7.1×), `ip-schedule-contributed.xlsx` (23 Meridian / 9 Kastor IP items)
- **Legal analysis:** `non-compete-enforceability-memo.docx` (Delaware/Texas/NY/CA safe-harbor survey)

## Document structure
- **I. Executive Summary** — transaction economics, guiding principles, overall balance
- **II–VI.** One self-contained section per contested provision, each with: (a) ready-to-insert clause language; (b) a positions summary table; (c) a negotiation rationale explaining concessions and gains for both sides; (d) cross-references
- **VII. Summary Concession Matrix** — three tables (landing points at a glance; concessions/gains by party; overall balance assessment)

## The five compromise landing points
1. **Management Committee (§5.01):** 3–2 board (Meridian majority) + supermajority (4 of 5, incl. 1 Kastor) on a 9-item existential Reserved Matters list; CEO casting vote on ordinary matters only; tiered escalation→mediation→buy-sell for Reserved Matter deadlocks.
2. **Capital Calls (§4.03):** 15-day notice + 60-day cure (75 days total); penalty interest at SOFR+500 bps/10%; 15% annual dilution cap with a forced-sale backstop at 15% cumulative in 24 months; a secured bridge-loan alternative (Default Rate, 12-month repayment, auto-conversion, single-use); EUR-funding accommodation.
3. **Non-Compete (§11.01):** 18 months (12 if exit within first 24 months); JV products + substantially similar/directly competitive products; US + Canada + jurisdictions with >$500K revenue in prior 24 months; Delaware governing law and forum; reformation clause.
4. **Exit Valuation (§§10.03–10.04):** EBITDA-only methodology; 7.0× presumptive multiple within a 6.5×–7.5× range; a single independent appraiser (Frazier Whitmore excluded) selected by mutual agreement with an AAA fallback; all four trigger events (change of control, material breach, deadlock, involuntary transfer) with intra-group restructuring carve-outs.
5. **IP License-Back (§12.05):** contributed IP reversion + symmetric non-sublicensable internal-use licenses; non-exclusive co-developed IP license to both parties; reciprocal territorial sublicensing (Meridian: Americas; Kastor: outside N.A.) with a global Restricted Competitors prohibition and a 25% North-American-revenue anti-circumvention covenant; a "primarily derivative" improvements classification; absolute prohibition on contributed-IP sublicensing.

## Validation
`python skills/docx/scripts/validate.py` → exit code 0 (ZIP integrity, XML well-formedness, ECMA-376 schema validation, content-type registration, and relationship consistency all passed).