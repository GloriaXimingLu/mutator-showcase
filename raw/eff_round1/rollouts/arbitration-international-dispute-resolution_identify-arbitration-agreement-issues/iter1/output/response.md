# Work Summary

## Task
Review the arbitration and dispute resolution provisions across five attached documents and prepare a severity-rated issues memo with recommendations, delivered as `arbitration-issues-memo.docx`.

## Documents reviewed
1. `ip-license-agreement.docx` — IPLA, §9 (LCIA, London seat, England & Wales law, consolidation clause §9.3)
2. `supply-agreement-execution-draft.docx` — SA, Art. 14 (ICC, Singapore seat/London venue, NY law, §§14.1–14.11) and Art. 15
3. `qa-side-letter.docx` — QA Letter, §7 (SIAC expert determination → arbitration, Singapore law) and §6 (recall costs)
4. `internal-email-chain.eml` — Greenleaf/Ridgeway priorities (consequential damages, joinder, consistency, enforceability, limitation, discovery)
5. `hg-markup-summary.docx` — Harmon & Grey drafter's rationale memo (July 3, 2025)

## Deliverable
`output/arbitration-issues-memo.docx` — a privileged issues review memo (Whitfield & Crane LLP → Greenleaf GC) containing:
- Executive summary + severity summary table
- Documents reviewed
- Side-by-side comparison matrix of DR provisions across the three agreements
- Severity definitions (Critical / High / Medium / Low)
- 17 issues, each with Provision(s), Analysis, Why it matters, and Recommendation:
  - **Critical (3):** C1 fragmented architecture (ICC/SIAC/LCIA; 3 seats; 3 laws); C2 circular conflicting precedence/consolidation clauses (pathological-clause risk); C3 overbroad consequential damages waiver (SA 14.11) compounded by indemnification conflict (11.2) and QA 6.6 trap, amplified by exclusivity
  - **High (5):** H1 arbitration-agreement governing law (NY vs Singapore seat); H2 no co-manufacturer joinder; H3 blanket discovery bar; H4 one-year limitation period + latent-defect timing conflicts; H5 U.S. enforceability (NY Convention/FAA) cumulative risk
  - **Medium (5):** M1 appeal on law to Singapore High Court; M2 inconsistent cost allocation; M3 inconsistent arbitrator count; M4 overbroad interim-relief carve-out; M5 expert-determination finality undermined
  - **Low (4):** L1 confidentiality; L2 language; L3 notice/contact discrepancies; L4 fallback-law/escalation/survival
- Consolidated recommendation: a unified Dispute Resolution Schedule (single institution/seat, single arbitration-agreement governing law, single precedence rule, consolidation+joinder, IBA-style production, harmonized limitation, damages carve-outs, no appeal on law)
- Negotiation priority/sequencing aligned to the client's stated priorities
- Conclusion

## QA
- Generated via `skills/docx/scripts/generate_from_md.py` (Pandoc).
- Validated via `skills/docx/scripts/validate.py` — **OK: valid** (ZIP integrity, XML well-formedness, ECMA-376 schema, content-type registration, relationship consistency).
- Content read back to confirm tables, headings, and special characters (§, →, $) rendered correctly.