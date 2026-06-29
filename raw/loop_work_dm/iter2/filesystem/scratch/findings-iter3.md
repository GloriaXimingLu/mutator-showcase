# Mutator findings — iteration 3 (after two "emit deliverable as prose" edits)

## Pass rates (worst first)
- environmental ESA: 0.17 (44/53 fail) — 261-line memo, full prose, NOT a cover-note
- employment markup: 0.58 (22/52)
- H-1B: 0.67 (13/39)
- trusts exhibits: 0.72 (17/60)
- JV contracts: 0.73 (15/56)
- cyber SEC: 0.73 (12/45)
- immigration compare: 0.74 (11/43)
- intercreditor: 0.81 (10/52)

## Prior edits already fixed FORMAT/emission
- emit-deliverable-not-work-summary, deliverable-file-not-cover-note
- Confirmed: every deliverable now IS full prose in the output file. Content on the page.
  Remaining failures are SUBSTANTIVE (coverage), not format.

## DOMINANT MODE (this iteration): incomplete extraction of specific issues/figures
Across 5/8 tasks the agent writes a polished thematic deliverable but DROPS a cluster of
granular rubric-graded findings. It mines the primary doc + writes an essay around chosen
themes; it does NOT exhaustively enumerate every distinct issue/figure/discrepancy across
the FULL document set, especially from SUPPORTING docs.

### Environmental (clearest): agent READ ESA + 6 supporting docs (transcript confirms).
Source docs CONTAIN rubric entities (Tank 3, Triton Metals, Central Valley Chemical,
NFA covers 2.3/14.7, PCB transformer, western yard, water well, floor drain — all in
transcript). Deliverable has 0 hits for those. Agent wrote deep memo on PCE plume +
UST + data gaps + lender + indemnity (own themes), dropped ~12 named issues.

### H-1B: 15 issues (MORE than rubric's ~11) but re-derived its own list — numbering
doesn't map to rubric's. Missed: immigration status gap/unauthorized work, alt-
qualification language, SOC code mismatch, TensorFlow/PyTorch/SageMaker gap. Also
failed a distractor (flagged OPT expiration as gap; rubric says don't).

### Employment: strong 18-issue memo, missed cluster requiring SUPPORTING docs:
ORS 656.236, $25K liquidated damages (policy), 409A savings clause, tax indemnification,
12-month noncompete cap (policy; kept 18mo statutory), IP assignment confirmation,
board-approved-range flag.

### Trusts: failures = specific FIGURES not extracted from records ($123,300, $23,400,
$6,200, $12,300, $619,900, $241,700, $981,435, $4,750). Agent generalizes numbers.

### Cyber: missed IRT composition gap, CIRP materiality framework, 10-K Item1C,
CISO bottleneck, legal hold, "file 8-K immediately", CIRP predates rules.

## Lever (method, not memorization)
Make the agent treat the deliverable as an EXHAUSTIVE EXTRACTION pass over the WHOLE
document set, not a thematic essay:
1. Enumerate every distinct issue/discrepancy/figure across ALL docs (primary + every
   supporting doc), each its own numbered finding.
2. Cross-reference every supporting doc (policies, records, valuations, appendices,
   letters, database summaries) AGAINST the primary; each mismatch = a finding.
3. Extract SPECIFIC figures/names/dates/entity IDs verbatim — never generalize a number
   the record states exactly.
4. Self-check COMPLETENESS: list docs read; each should yield findings; a supporting doc
   with zero findings = you skipped it.

Sanity: helps ANY issue/memo/markup task regardless of practice area; reads no task facts.
