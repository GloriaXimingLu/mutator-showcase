# Arbitration & Dispute Resolution — Issues Memo (Delivered)

**Deliverable:** `output/arbitration-issues-memo.docx` (validated, ECMA-376 compliant)

## What was done

Reviewed the arbitration and dispute-resolution provisions across all five attached documents:

1. **Exclusive Supply Agreement** (execution draft) — Article 14 (ICC; Singapore seat; London venue; New York law)
2. **Quality Assurance Side Letter** — Section 7 (SIAC expert determination + arbitration; Singapore law)
3. **IP License Agreement** (execution draft) — Section 9 (LCIA; London seat; English law)
4. **Harmon & Grey LLP memo** — Pacifica's counsel's rationale for the architecture
5. **Internal Greenleaf email chain** — dispute-resolution priorities for the W&C review

The memo is framed as Whitfield & Crane LLP's privileged review for Greenleaf's deal team (Matsuda/Heller/Park), dated July 9, 2025, ahead of the July 11 review deadline and July 18 signing.

## Structure of the memo

- Executive summary with a severity-rating legend and a 16-issue summary table
- Documents reviewed & three-tier architecture overview table
- 16 severity-rated issues, each with **Provisions / Analysis / Severity / Recommendation**, grouped into: (A) Structural & Cross-Document, (B) Enforceability & Pathological-Clause Risk, (C) Multi-Party, (D) Procedural Inconsistencies, (E) Miscellaneous
- Cross-cutting recommendations
- Recommended negotiation priority sequence
- Conclusion

## Severity distribution

- **Critical (3):** (1) consequential-damages waiver + exclusivity + QA §6.6 contradiction; (2) IPLA §9.3 consolidation clause conflicting with SA Art. 14 (LCIA vs. ICC) — a pathological-clause risk; (3) SA §14.6 appeal on questions of law to the Singapore High Court, which is likely ineffective because Singapore's IAA/UNCITRAL Model Law has no English s.69 equivalent.
- **High (6):** fragmented three-institution/three-law architecture; conflicting hierarchy clauses; no joinder mechanism for non-signatory co-manufacturers; blanket discovery bar (evidentiary asymmetry + "unable to present case" enforcement risk); circular expert-determination finality; recall cost allocation capturing only "direct" costs.
- **Medium (6):** expert-determination not Convention-enforceable; IPLA §2.2(b) sharing restriction; cost-allocation inconsistency; arbitrator-number inconsistency; one-year limitation period; interim-relief inconsistency.
- **Low (1, grouping three):** confidentiality inconsistency; vague SA §14.4 gap-filler; no Ridgeway intervention mechanism.

## Key analytical points

- Several defects recreate the very "pathological clause"/enforcement-delay risk that Pacifica's 2023 Hong Kong ICC arbitration (14-month delay) prompted the architecture to avoid — a point leveraged in the recommendations.
- The memo aligns its negotiation priority sequence with Greenleaf's internal priorities from the email chain (consequential damages → joinder → cross-document consistency → U.S. enforceability, plus limitation period and discovery).

## Tooling

Authored in markdown, converted to `.docx` via the docx skill's `generate_from_md.py` (Pandoc), and passed `validate.py` (ZIP integrity, XML well-formedness, ECMA-376 schema validation, content-type registration, relationship consistency). Three tables (severity legend, 16-issue summary, architecture overview) and full heading hierarchy rendered correctly.