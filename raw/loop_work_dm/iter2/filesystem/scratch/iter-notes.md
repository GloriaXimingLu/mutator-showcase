# Mutator iteration notes (2026-06-26)

## Pass rates (current rollouts)
- environmental ESA: 0.509 (26 fail)  <- worst
- employment markup: 0.538 (24 fail)  <- 2nd worst
- corporate-governance/cyber: 0.733 (12)
- trusts exhibits: 0.783 (13)
- litigation invoice: 0.796 (10)
- corporate-ma CIM: 0.805 (8)
- contracts intercreditor: 0.808 (10)
- capital-markets S-1: 0.811 (17)

Prior memory: format fixes (deliverable-as-prose, output-file-is-deliverable) confirmed
working — all deliverables are full prose in the output file. env went 0.17->0.51,
employment format recovered. Remaining failures are SUBSTANTIVE coverage.

## Two worst — deep dive

### environmental ESA (0.509)
Agent produced a thorough 502-line memo BUT misidentified the subject property.
It treated the Greenfield Toledo ESA as primary and branded the Terravista
Dayton/Millrace ESA (E1527-13, Triton Metals @2900 Millrace, Central Valley Chemical,
Dayton Forge & Die, 2.3/14.7 NFA Parcel A, 145 Commerce Park dry cleaner, City of
Dayton bldg records) as "misfiled different property — DO NOT RELY", demoted to a
secondary appendix. ~20 of 26 failed criteria are Dayton facts it DID extract (D1-D9)
but did NOT carry to required form (drum outside NFA, western yard outside NFA + TCE,
private well search + ASTM requirement, vapor intrusion, pre-1987 records gap,
dry-cleaner PCE plume + directional ambiguity, PCB testing rec, western yard TCE rec,
NFA doesn't cover Building 2, NFA 2.3/14.7 quant). Graded as absent because in
"do-not-rely" appendix or missing the specific required element (e.g. exact figure,
ASTM section cite, BFPP linkage).
KEY: agent DISCARDED a produced document as irrelevant and the gradable findings
went with it.

### employment markup (0.538)
Strong 25-issue memo + real redline, applied EXTERNAL law well (OWBPA, Cal 16600,
DTSA) but did NOT enforce the CLIENT'S OWN internal settlement POLICY. Failures:
workers' comp release (ORS 656.236, WCB approval — release §4(xii) actually releases
WC claims, never flagged/carved out), $25K/breach liquidated damages, 12-month
non-compete cap (kept 18mo), mutual confidentiality, dates/title-only references
(softened to "neutral factual" instead), strike re-employment eligibility (kept it),
409A savings clause, tax indemnification Delano->Greenleaf, IP assignment
confirmation, board-approved range $275K-$425K exceeded. Policy facts (409A, $25K)
appear in transcript (52x, 51x) — agent read past them, never converted to findings.
Memo even says it didn't review "Greenleaf's personnel policies beyond Employment
Records." KEY: agent never treated the internal POLICY doc as a controlling authority.

## Cross-task pattern (all 8)
- capital-markets: missing required S-1 SECTIONS (Use of Proceeds, Capitalization
  actual+pro forma, Management, non-employee directors, Principal Stockholders,
  Shares Eligible for Future Sale, Legal Matters) — deliverable's own required
  components absent.
- contracts/intercreditor: missing specific negotiating TERMS (early-termination
  triggers, WAL test, LC cash collateral, MFN window) the rubric wants.
- litigation: missing specific DOLLAR computations ($21,375, $10,312.50, $1,200) and
  fee-agreement-section-keyed reductions (§6.1, block-billing 25%).
- trusts: missing exact FIGURES ($123,300 equity, $23,400, $12,300, $619,900) +
  asset-summary structural completeness.
- corporate-ma: missing specific computations/cross-refs (EBITDA bridge $17.1M vs
  $16.8M, capex/revenue disconnect, concentration quantification).
- cyber: missing specific findings (IRT comp gap, 10-K Item 1C, CISO bottleneck,
  legal hold) + immediate action ("file 8-K Item 1.05 immediately").

## Dominant mode (synthesis)
The agent under-produces the SPECIFIC content the controlling record/standard requires:
(A) DOCUMENT DEMOTION — discards/discounts a produced document (env: "wrong property";
employment: never treats internal policy as authority), so its gradable findings never
reach the primary deliverable as first-class items.
(B) REQUIRED-COMPONENT / REQUIRED-COMPUTATION incompleteness — doesn't enumerate the
deliverable's own required parts (sections, exhibits, per-line computations, policy
mandates) and self-check each is actually produced with its exact value; computes or
omits instead of carrying to the specific figure/provision.

Both are METHOD-fixable (no memorization). Prior §2 "read every doc / pull verbatim"
helps but doesn't explicitly forbid DEMOTION and doesn't require enumerating the
deliverable's required components/computations.

## EDIT PLAN
Add to §2 (extraction): explicit anti-demotion rule — every document produced is a
source of gradable findings; never reclassify a produced document as "wrong
property/not relevant/background/duplicate" and relegate its findings to a
secondary/appendix/"do-not-rely" section; findings from every doc go into the PRIMARY
deliverable as first-class numbered items. If two docs seem to describe different
subjects, surface that as its own finding but still mine BOTH fully for the subject(s)
the task names.
Add to §3/§4 (framework + format): required-component & required-computation
completeness — before drafting, enumerate (i) every section/exhibit/element the task
or controlling standard requires the deliverable to contain, (ii) every line-item
computation or figure the controlling record demands, (iii) every mandate in the
client's governing policy/agreement/plan; self-check each is actually present as
written-out content with its exact value (a section named-but-empty, a computation
not carried to its specific number, a policy mandate not enforced in the markup, all
score as absent).
