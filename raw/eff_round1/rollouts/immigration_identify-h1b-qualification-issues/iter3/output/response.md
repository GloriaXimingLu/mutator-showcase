# H-1B Issue-Identification Memo — Summary of Work

## Deliverable
- **`output/h1b-issue-memo.docx`** — comprehensive issue-identification memorandum (validated, schema-valid .docx).

## What was done
1. Read and extracted all **10 documents** in the petition package (beneficiary résumé, certified LCA, credential evaluation, employer support letter, JNTU transcripts, two experience letters, LCA posting notice, org chart, and PWD).
2. Cross-referenced every beneficiary, employer, position, wage, education, experience, and status data point across all documents for internal consistency, regulatory compliance, and substantive sufficiency.
3. Verified factual calculations independently (e.g., the LCA posting period of Mar. 10–19, 2025 = **8 business days**, short of the 10 required by 20 CFR § 655.734(d)).
4. Authored the memo in markdown and converted it to .docx via the docx skill (Pandoc), then ran the mandatory `validate.py` gate — **passed (valid)**.

## Memo structure
- Executive Summary; Documents Reviewed; Cross-Reference Summary table (key data points across all docs); Severity-Ranked Issue Index; detailed findings by category (Qualification, Consistency, Missing Docs, Status, Wage/LCA, Specialty Occupation, Execution) each with Finding / Standard / Risk / Recommendation; Prioritized Action Items; Conclusion.

## Headline issues identified (22 total)
**Critical**
- A-1: Degree field-of-study mismatch — Beneficiary's B.Tech is in **Electronics & Communication Engineering**, not CS/ML/AI; credential evaluation equates it to a U.S. B.S. in ECE, notes only ~7.5% CS coursework, and expressly disclaims opining on field-of-study suitability.
- A-2: Alternative qualification path (any engineering degree + 5 yrs ML) fails on documented experience — only ~3.25 yrs of ML experience is documented (NovaStar); the 3-yr consulting period is undocumented.
- E-1: F-1 OPT status asserted with **no U.S. degree, I-20, or EAD** in the record (only an Indian B.Tech from 2014) — internally inconsistent and a gating status problem.

**High**
- A-3: Three-year independent consulting period (Aug 2020–Aug 2023) entirely undocumented (no client letters, 1099s, tax/business records).
- A-4: Required tools (TensorFlow, PyTorch, AWS SageMaker, NLP/LLM) not evidenced in the only documented ML experience (NovaStar letter is silent on them).
- F-1: Wage level likely misclassified — supervisory + "independent judgment" duties map to Level 3/4, not Level 2 ("limited judgment"); offered $128,000 < Level 3 PWD of $137,946.
- A-5: Credential evaluator's own Ph.D. is from "Halford University" (unverified/unaccredited).

**Medium**: employment-date discrepancies (résumé vs. letters), four different employer phone numbers (posting notice lists the beneficiary's number), 8-business-day posting, missing cap selection notice, conclusory specialty-occupation argument, missing core filing/status docs.

**Low–Med/Low**: supervisory headcount 3 vs. 2, unexplained Jan–Mar 2017 gap, broad "any engineering degree" alternative, posting-location inconsistency, unsigned letter/LCA, "7+" vs "8+" years, current vs. petitioned title, unsupported ability-to-pay, transcript credit characterization.

## Validation
- `python3 skills/docx/scripts/validate.py output/h1b-issue-memo.docx` → **OK: valid** (ZIP integrity, XML well-formedness, ECMA-376 schema, content-type registration, relationship consistency all passed).