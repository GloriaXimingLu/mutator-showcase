# Deliverable Summary

**Output:** `output/compromise-ica-terms.docx` — a Privileged & Confidential memorandum from Borrower's counsel (Kesswick, Tanaka & Moreau LLP) to Meridian's CEO and General Counsel proposing compromise clause language for the four contested provisions of the Intercreditor Agreement.

## What the memorandum does

For each of the four contested ICA provisions, the memorandum provides (1) a summary of the impasse (each side's opening position), (2) **full contractual drafting** ready for insertion into the ICA, and (3) **negotiation rationale** explaining what each side gains and concedes, citing the 42-deal market survey and quantifying economic impacts.

| Provision | Compromise Landing Zone | Market Anchor |
|---|---|---|
| **3.01(b) Standstill** | 180 days + 3 narrow, objectively verifiable early-termination triggers (disposition/credit-bid of substantially all Collateral; sale order without 2L consent; confirming order impairing 2L) + a 2-notice / 180-day-per-year Blockage Notice cap | Median 180 days; 76% include triggers; 25/42 pair ≥180 days + triggers |
| **5.01 Purchase Right** | Par for funded debt at the non-default contract rate + fees; optional (not mandatory) revolver assumption (terminate if not assumed); trigger on 1L EOD incl. acceleration | Par 71%; non-default rate 69%; optional revolver 62% (77% in 2024); 1L acceleration 100% |
| **2.03(c) Refinancing** | 10% cap ($15M) limited to bona fide refinancing costs; maturity ≥ June 15, 2031 (later of both floors); narrowed restrictiveness test + MFN on financial maintenance covenants | Median 10% cap (79% limited to costs); narrowed test + MFN 52%; MFN on financial covenants 82% |
| **4.02 Proceeds Waterfall** | Bifurcated: ordinary-course (≤ $20M) follows 1L CA reinvestment mechanics; large/extraordinary (> $20M) hard 100% sweep overriding reinvestment; residual to 2L after 1L Discharge; robust anti-evasion; quarterly + event-driven + annual reporting | 100% sweep universal; reinvestment preserved 81%; hard sweep for large 90%; 2L residual 79%; $20M threshold median; anti-evasion 97% |

## Key features

- **Marked Privileged & Confidential** (header, body legend, and closing reservation of rights), with Without Prejudice / FRE 408 settlement-discussion legend consistent with the parties' position letters and internal emails.
- **Presented as a single indivisible package** — Section III maps the cross-linkages (standstill↔purchase right; purchase right↔refinancing; proceeds↔standstill; residual↔priority) and the recommendation is to circulate on an all-or-nothing basis, per the engagement instructions.
- **Each landing zone sits within both agents' disclosed flexibility** (from the Buchanan and Oduya internal summary emails of June 26) and at or near the market median/majority.
- **Economic impacts quantified** throughout: non-default vs. default-rate interest (~$2.375M per 90 days / ~$4.75M per 180 days on $475M); illustrative purchase price (~$485.8M at non-default rate vs. TEV $640M); refinancing cost breakdown ($6–15.25M vs. the $15M cap); Total LTV impact (97.66% → 100%); $20M ordinary-course threshold (~22.4% of LTM EBITDA); $165M first lien collateral margin.

## Validation

- Generated via `skills/docx/scripts/generate_from_md.py` (Pandoc).
- Passed `skills/docx/scripts/validate.py` (ZIP integrity, XML well-formedness, ECMA-376 schema validation, content-type registration, relationship consistency).
- Tables and blockquoted contractual drafting render correctly as native Word tables and indented clause text.