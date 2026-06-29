# Summary of Work

## Deliverable
`output/mkpoly-jva-compromise-provisions.docx` — a validated Word document containing compromise contract provisions for the five contested terms of the MKPoly Coatings, LLC Joint Venture Agreement.

## Source Documents Reviewed
All 14 documents in the workspace were read in full:
- **Negotiation correspondence:** Falk→Escalante (July 28), Escalante→Falk (July 30), Cordero→Falk internal guidance (July 31)
- **Position papers:** Kastor position summary (Escalante, Aug 1); Meridian negotiation playbook & fallback positions (Falk, Aug 1, privileged)
- **Operative drafts:** Term sheet (executed Mar 15); JVA v.3 clean (Meridian); JVA v.4 redline-tracked and v.4 redline (Kastor); standard JVA template
- **Supporting analysis:** Non-compete enforceability memo (DE/TX/NY/CA survey); Frazier Whitmore valuation benchmarks (12 comparable transactions, EBITDA multiple analysis, DCF comparison); capital-contribution schedule; IP schedule (23 Meridian items @ $28.6M; 9 Kastor items)

## The Five Contested Terms and Compromise Landing Points
1. **Management Committee & Governance (Art. IV, §§4.01/4.03/4.04):** 3–2 board (Meridian majority) + supermajority (4 of 5, incl. ≥1 Kastor) on 9 narrow Reserved Matters + tiered deadlock (escalation → mediation → CEO casting vote on operational matters; buyout on Reserved Matters).
2. **Capital Calls & Dilution (Art. V, §5.01):** 75-day total window (30-day funding + 45-day cure) + penalty interest (SOFR+500bps or 10%) + 15% annual dilution cap with forced-sale backstop + limited Cure Loan at SOFR+500bps.
3. **Post-Exit Non-Compete (Art. XIV, §14.01):** 18 months (12 if early exit) + JV products plus substantially similar/directly competitive products + North America plus revenue-threshold jurisdictions + enforceability safeguards.
4. **Exit Valuation (Art. X, §§10.03–10.04):** 7.0× EBITDA (EBITDA-only, no DCF) + single jointly-selected independent appraiser (not the JV auditor) with AAA fallback + four triggers + no discounts.
5. **IP License-Back (Art. XII, §§12.04–12.05):** Contributed IP reverts; no license of Meridian contributed IP to Kastor; non-exclusive co-developed IP license to both with territorial sublicensing outside North America subject to Restricted Competitors schedule + 25% revenue negative covenant; improvements revert to contributor with territorial license to the other party.

## Document Structure (per Escalante's requested format)
- Purpose / transaction context
- Executive summary with summary table
- Five self-contained sections, each with: (A) opening positions, (B) ready-to-insert clause language keyed to JVA sections, (C) negotiation rationale explaining concessions and gains for both sides, (D) cross-references
- Summary concession matrix (8-column table: opening positions, compromise, and concession/gain for each side)
- Overall balance assessment

## Drafting Approach
- Clause language uses the JVA's defined terms and is drafted to replace the corresponding v.4 sections.
- Rationale is evenhanded and commercially accessible (per Cordero's instruction that the document to Escalante present a balanced middle ground without revealing internal flexibility).
- Every figure, threshold, and market reference is grounded in the source documents (contribution totals, Frazier Whitmore comparables, enforceability safe harbors, comparable-transaction structures).
- Concessions are calibrated so each side holds firm on its highest-priority items and concedes on lower-priority items, producing a package balanced as a whole.

## Validation
`validate.py` confirms the .docx is schema-valid (ECMA-376 WordprocessingML), with intact ZIP, well-formed XML, and consistent relationships. Two tables and 204 paragraphs render correctly.