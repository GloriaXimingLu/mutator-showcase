# Arbitration & Dispute Resolution Issues Memo — Summary

## Deliverable
`output/arbitration-issues-memo.docx` — a severity-rated issues memorandum reviewing the arbitration and dispute resolution provisions across the five attached documents. Validated (ZIP integrity, XML well-formedness, content-type/relationship consistency) via `skills/docx/scripts/validate.py`.

## Documents reviewed
1. **Exclusive Supply Agreement (SA)** — Article 14 (ICC, seat Singapore, venue London, NY law)
2. **Quality Assurance Side Letter (QA Letter)** — Section 7 (SIAC expert determination → SIAC arbitration, Singapore law)
3. **IP License Agreement (IPLA)** — Section 9 (LCIA, seat London, English law)
4. **Harmon & Grey rationale memorandum (HG Memo)** — explanatory
5. **Internal Greenleaf email chain** — negotiating priorities / commercial context

## Approach
Read all five documents, extracted the dispute-resolution architecture and the commercial context (USD 178M+ exclusive supply, 13-year horizon, co-manufacturing model, Pacifica's 2023 "pathological clause" enforcement delay, Ridgeway recall precedent), then identified and severity-rated 17 issues with concrete drafting recommendations.

## Issues identified (17 total)
- **Critical (3):** C1 dueling hierarchy/consolidation clauses (SA §15.8 vs QA §8.1 vs IPLA §9.3/§10.3) — pathological-clause risk; C2 appeal on questions of law to the Singapore High Court (SA §14.6) — likely unenforceable under Singapore's IAA (modeled on English s.69, which Singapore lacks); C3 consequential-damages waiver (SA §14.11) + exclusivity + illusory recall preservation (QA §6.6) — deal-blocker.
- **High (6):** H1 fragmented three-institution/seat/law architecture; H2 no third-party joinder / co-man parallel proceedings; H3 blanket discovery prohibition; H4 one-year limitation period; H5 non-final expert determination + $5M threshold ambiguity; H6 indemnification/consequential-damages tension.
- **Medium (4):** M1 inconsistent cost allocation; M2 governing-law fragmentation + "general principles" fallback; M3 arbitrator-number inconsistency; M4 expert neutrality/timeline strictness.
- **Low (4):** L1 interim-relief carve-out; L2 confidentiality; L3 seat/venue split; L4 survival/termination × limitation period.

## Memo structure
Executive Summary → Documents & Architecture Overview (with comparison tables) → Severity Methodology → Critical / High / Medium / Low issues (each with provisions, analysis, recommendation) → Consolidated Issues Table → Recommended Action Plan → Conclusion.

## Method
Authored as markdown, converted to .docx via `skills/docx/scripts/generate_from_md.py` (Pandoc), then validated. No reference template was available, so Pandoc default styling was used; tables and headings rendered correctly on read-back.