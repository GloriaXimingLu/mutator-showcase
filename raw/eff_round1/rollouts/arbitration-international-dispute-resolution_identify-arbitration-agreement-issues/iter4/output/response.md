# Arbitration & Dispute Resolution Issues Memo — Summary

## Deliverable
`output/arbitration-issues-memo.docx` — a severity-rated issues memo reviewing the arbitration and dispute resolution provisions across the five attached documents. Validated against ECMA-376 (WordprocessingML) schema; ZIP/XML integrity confirmed.

## Documents reviewed
1. **Exclusive Supply Agreement** (SA) — execution draft, Art. 14 (ICC, Singapore seat, London venue, NY law)
2. **Quality Assurance Side Letter** (QA Letter) — §7 (SIAC expert determination → arbitration, Singapore seat, Singapore law)
3. **IP License Agreement** (IPLA) — §9 (LCIA, London seat, England & Wales law)
4. **Internal Greenleaf email chain** (June 30–July 1, 2025) — negotiating priorities and commercial concerns
5. **Harmon & Grey LLP summary memorandum** (July 3, 2025) — drafting rationale

## Memo structure
- Executive summary with severity summary table
- Dispute resolution map (cross-document comparison table)
- Severity rating scale (Critical / High / Medium / Low)
- 12 issues, each with provision citations, analysis, "why it matters," and recommendations
- Consolidated negotiation priorities
- U.S. enforceability note (FAA Ch. 2 / New York Convention; NC & Delaware)
- Conclusion

## Issues identified (by severity)
- **Critical (2):** (1) Conflicting forum-selection/consolidation clauses across IPLA §9.3, SA §15.8, and QA §8.1 — a "pathological" clause that recreates the 14-month enforcement-delay risk HG was retained to avoid; (2) Consequential-damages waiver (SA §14.11) stacked with exclusivity, the liability cap, and the self-defeating QA §6.6 cross-reference.
- **High (5):** (3) Fragmented architecture (3 institutions / 2 seats / 3 laws); (4) no joinder mechanism for non-signatory co-manufacturers; (5) one-year limitation period at the UCC §2-725 floor; (6) statutory appeal on questions of law to the Singapore High Court (finality + NY/Singapore law mismatch); (7) blanket discovery prohibition that would cripple quality/contamination claims.
- **Medium (3):** (8) expert determination "final and binding" yet freely challengeable; (9) indemnification vs. damages-waiver interaction; (10) inconsistent costs/fee-shifting and tribunal-size provisions.
- **Low (2):** (11) seat/venue split, interim-relief breadth, confidentiality carve-out (acceptable, minor harmonization); (12) no pre-arbitration escalation/mediation step (optional).

## Method
Drafted as structured markdown, converted to .docx via the docx skill (`generate_from_md.py` / Pandoc), and validated with `validate.py` (exit code 0). Intermediate markdown removed; output directory contains only the deliverable.