# Summary

## Deliverable
`output/mkpoly-jva-compromise-provisions.docx` — a validated Word document containing compromise contract provisions for the five contested sections of the MKPoly Joint Venture Agreement.

## What I did
1. **Reviewed all source documents** representing both parties' positions, drafts, and supporting materials:
   - Position papers: `kastor-position-summary.docx` (Kastor's positions/minima) and `meridian-negotiation-playbook.docx` (Meridian's fallback ladders, red lines, comparable-transaction benchmarks).
   - Negotiation emails: Falk↔Escalante (process/deliverable format) and Cordero→Falk (Meridian's internal priority ranking and trade architecture).
   - The actual contested clause language: `mkpoly-jva-v4-redline.docx` (Sections 4.03, 5.01/5.02, 10.01/10.03–10.04, 11.01, 12.05 + Schedules 2.04, 12.01, 12.02, 12.05).
   - Supporting data: `capital-contribution-schedule.xlsx`, `frazier-whitmore-valuation-benchmarks.xlsx` (12 comparable transactions; 6.2×–8.1× EBITDA range, 7.1× median), `ip-schedule-contributed.xlsx` (23 Meridian items/$28.6M; 9 Kastor items).
   - `term-sheet-executed.docx` (agreed framework) and `non-compete-enforceability-memo.docx` (DE/TX/NY/CA enforceability analysis).

2. **Drafted compromise provisions** for the five contested sections, each as a self-contained, independently evaluable section containing: (a) both sides' opening positions; (b) ready-to-insert clause language keyed to the JVA's section numbers and defined terms; (c) a negotiation rationale explaining concessions and gains for **both** sides; and (d) cross-references.

3. **Built a summary concession matrix** (6-column table) showing each side's opening, the landing point, and the concessions/gains per party, plus an overall-balance assessment.

## The five compromises (landing points)
1. **Governance (§5.01/5.02/6.01):** 3-2 board (Meridian) + Supermajority (4-of-5, ≥1 Kastor) on 11 Reserved Matters; CEO casting vote on non-Reserved matters only, after escalation+mediation; forced buyout for Reserved-Matter deadlocks.
2. **Capital calls (§4.03):** 60-day cure (~75 days total) + penalty interest (SOFR+500) + secured loan alternative (auto-conversion, single-use) + 15%/yr dilution cap + forced-sale backstop + FX accommodation.
3. **Non-compete (§11.01):** 18 months (scaling to 12 for early exit); MKPoly actual products + substantially-similar; US+Canada + jurisdictions with >$500K revenue/24-mo; DE/TX forum; reformation clause.
4. **Exit valuation (§10.01/10.03–10.04):** 7.0× reference multiple with optional independent appraisal in a 6.5×–7.5× collar; single jointly-selected independent firm (not Frazier Whitmore) with AAA fallback; EBITDA-only; all four triggers + intra-group carve-outs.
5. **IP license-back (§12.05):** non-exclusive, royalty-free, perpetual co-developed IP license to both parties; reciprocal territorial sublicensing (M: Americas; K: outside Americas) subject to global Restricted Competitors + 25%-revenue covenant + audit; non-sublicensable internal-use contributed-IP license; absolute no-sublicensing of contributed IP; improvements revert to contributor + license on co-dev terms ("primarily derivative" test).

Each party's two highest-priority positions are preserved; concessions balance in aggregate and track the comparable-transaction benchmarks and the multi-jurisdictional enforceability analysis.

## Build
Authored as markdown, converted to .docx via Pandoc (using the standard JVA template as the reference doc for legal styling), and validated with `skills/docx/scripts/validate.py` (ZIP integrity, XML well-formedness, relationship consistency — passed).