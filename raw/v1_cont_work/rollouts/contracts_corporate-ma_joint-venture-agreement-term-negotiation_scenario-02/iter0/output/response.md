# MKPoly JVA Compromise Provisions — Summary of Work

## Deliverable
`output/mkpoly-jva-compromise-provisions.docx` — a validated Word document containing ready-to-insert compromise clause language, per-provision negotiation rationale, and a summary concession matrix for the five contested sections of the MKPoly Coatings, LLC Joint Venture Agreement.

## Source documents reviewed
All 14 provided documents were reviewed to establish both parties' positions, fallback ladders, and supporting data:
- **Position/strategy documents:** Kastor position summary (Rennert Krieger Solano); Meridian negotiation playbook (Whitfield Ames & Trotter).
- **Negotiation correspondence:** Falk→Escalante path-forward email; Escalante→Falk response; Cordero→Falk internal guidance (priority ranking).
- **Drafts:** MKPoly JVA v.3 (clean) and v.4 (redline) — used to match section numbering, defined terms, and drafting style; standard JVA template.
- **Executed term sheet** (March 15, 2025) and **non-compete enforceability memo** (DE/TX/NY/CA survey).
- **Schedules (Excel):** capital-contribution schedule; Frazier Whitmore valuation benchmarks (comparables + EBITDA multiple analysis); contributed-IP schedule (23 Meridian items @ $28.6M; 9 Kastor items).

## The five contested provisions and proposed compromises

| # | Provision (JVA §) | Compromise landing point |
|---|---|---|
| 1 | Management Committee & Voting (§ 5.01) | 3-2 board (Meridian majority) + supermajority (4 of 5, incl. ≥1 Kastor) on a defined list of existential Reserved Matters; CEO casting vote on operational matters only; escalation → mediation → buy-sell for Reserved-Matter deadlocks. |
| 2 | Capital Calls & Dilution (§ 4.03) | 75 days total (15-day notice + 60-day cure); default interest SOFR + 350 bps; secured bridge loan (SOFR + 350, 12-mo, auto-convert, once/24 mo); 15%/yr dilution cap with forced-sale trigger at 15%/24 mo (modeled on Comparable #2). |
| 3 | Post-Exit Non-Compete (§ 11.01) | 18 months (12 if exit within first 24 months); JV Products + substantially similar/directly competitive; U.S., Canada + jurisdictions with >$500K revenue in prior 24 months; DE choice-of-law + forum selection + severability. |
| 4 | Exit Valuation (§§ 10.03–10.04) | 7.0× fixed trailing-12-month EBITDA; single independent Big Four appraiser (not Frazier Whitmore, no pre-existing engagement) with AAA fallback; optional baseball arbitration by mutual consent; triggers = CoC + breach + deadlock + involuntary transfer (intra-group carve-outs). |
| 5 | IP License-Back (§ 12.05) | Non-exclusive, royalty-free, perpetual license to **both** parties; territorial sublicensing (Meridian: Americas; Kastor: rest of world); global Restricted-Competitors prohibition + 25% NA-revenue catch-all (reciprocal, named entities, annual update); no license of Meridian contributed IP to Kastor; improvements revert to contributor with territorial license + "primarily derivative" classification test. |

## Document structure
- Title/metadata block; Introduction & Purpose.
- **Executive Summary** tying the five provisions together.
- **Summary Concession Matrix** (6-column: provision, both openings, compromise, and concessions/gains for each side).
- Five self-contained provision sections, each with: (A) Positions Summary table, (B) Ready-to-Insert Clause Language, (C) Negotiation Rationale (explicit concessions and gains for each side + "why this is a fair middle ground"), (D) Cross-References.
- Overall Balance Assessment, Market Support Summary table (anchored to Comparable Transactions #1–#3), and Recommended Next Steps.

## Design principles applied
- Each compromise is anchored to the comparable-transaction dataset (6.2×–8.1×, median 7.1×) and to Delaware/Texas enforceability safe harbors.
- Concessions are calibrated to each side's stated priorities: Meridian holds its two red lines (no competitive sublicensing of its contributed IP; operational control) while moving on non-compete, multiple, appraiser independence, and capital-call flexibility; Kastor obtains its two priorities (independent appraiser; broad co-developed IP license-back with sublicensing) while accepting a 3-2 board, 18-month non-compete, and capital-call discipline.
- No party's stated red line is crossed, and the package is internally consistent (governance/deadlock → exit valuation; capital-call forced sale → same valuation; non-compete geography ↔ IP territorial structure).
- Per the principals' instruction, the document reads as a principled, evenhanded middle-ground proposal rather than a concession memo.

## Validation
`python3 skills/docx/scripts/validate.py` → **OK: valid** (exit code 0). Schema-valid against ECMA-376 WordprocessingML XSDs; ZIP integrity and content-type registration confirmed.