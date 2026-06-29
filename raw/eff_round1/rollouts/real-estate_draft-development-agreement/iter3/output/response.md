# Development Agreement Draft — Summary

## Deliverable
`output/development-agreement-draft.docx` — a developer-side draft of the definitive **Development Agreement** for the Lakemont Station Commons mixed-use transit-oriented development, between Granite City Development LLC ("Developer") and the City of Lakemont, Illinois ("City").

## Source documents reviewed
1. **Negotiated Term Sheet** (Jan 22, 2025) — principal business terms (the backbone of the draft).
2. **RFP Response Narrative** (Dec 16, 2024) — Developer's proposal, qualifications, financing.
3. **City Council Resolution No. R-2025-017** (Feb 18, 2025) — conditional approval and conditions.
4. **Construction Loan Term Sheet** (First Prairie National Bank) — lender requirements that constrain the Agreement.
5. **Lakeshore Side Letter** (Feb 10, 2025) — equity investor consent/governance rights.
6. **Phase II ESA Summary** (Greenfield, Nov 8, 2024) — environmental conditions and remediation.
7. **TIF District Summary Memo** (Corporation Counsel, Mar 5, 2025) — TIF parameters, increment projections, prevailing wage.

## Structure of the draft
- 20 Articles (Definitions; The Project; Land Conveyance; Public Incentives; Environmental Matters; Project Financing; Performance Security; Construction Standards; Community Benefits; Affordable Housing; Development Schedule; Force Majeure; Defaults & Remedies; Termination; Indemnification; Assignment & Change of Control; Lender Protections; Dispute Resolution; Conditions Precedent; Miscellaneous), plus Recitals, 10 Exhibits, and signature blocks.
- 5 tables (project summary, public incentives, sources & uses, insurance, phasing schedule).
- 53 inline bracketed drafting notes plus a consolidated index of all conflicts and open items at the end.
- Table of contents generated automatically.

## Developer-favorable drafting choices
- **No reversionary interest / defeasible fee** (Art. 14.3): eliminated the Resolution's reversionary interest (which the construction lender prohibits and which would kill the loan) and substituted a contractual repurchase option (only after all cure periods, Force Majeure, and lender cure/consent), a liquidated-damages alternative, and an enhanced completion guaranty — preserving fee simple absolute title.
- **Broad Force Majeure** (Art. 12): 18-month aggregate cap, broad definition, day-for-day extensions.
- **Cure periods** (Art. 13): 60-day monetary / 90-day non-monetary with diligent-pursuit extension, plus lender cure rights (Art. 17).
- **Developer termination rights** (Art. 14.2): expanded to include City title failure, infrastructure funding failure, condemnation >15%, and any imposition of a reversionary interest.
- **City environmental indemnity** (Art. 5.4): broad, survives termination/conveyance, covers cost overruns and third-party/governmental claims.
- **TIF** (Art. 4.2): Developer-favorable reimbursement priority (remediation and infrastructure first), good-faith TIF-extension covenant, land write-down and City infrastructure treated as separate incentives not charged against the TIF cap.
- **Assignment** (Art. 16): broader permitted transfers (internal transfers, estate planning, approved capital raises, lender foreclosure assignment), Key Person provision, 60-day cure before any assignment default.
- **Substantial Completion** (Art. 11.3): temporary CO qualifies (earlier release of performance security / next-phase clock).
- **LEED** (Art. 8.2): good-faith-efforts / LEED-Silver fallback.
- **Living wage / first-source hiring** (Art. 9.2–9.3): incorporated (Resolution-mandated) but framed as commercially reasonable efforts enforceable through lease/operator covenants, with no Developer default for tenant/operator non-compliance.
- **Lender Protections** (Art. 17): full suite (notice, cure, consent to amendments, subordination, foreclosure assignment, estoppels, TIF assignment) — required for the loan and protective of Developer.

## Key cross-document conflicts flagged (26 total; most critical)
1. **Reversionary interest / clawback** — Resolution Condition 3(h) requires it; construction loan strictly prohibits it (would render the loan impossible to close); Term Sheet silent; Lakeshore requires consent. [CRITICAL — resolved by substitution in Art. 14.3]
2. **36-month reversionary trigger vs. Phase I schedule** — the Resolution's 36-months-from-conveyance trigger would fire before the contractual Sept 30, 2028 Substantial Completion deadline. [CRITICAL]
3. **Living wage $17.50/hr** — Resolution mandates; Term Sheet silent. [Incorporated in Art. 9.2]
4. **First-source hiring for permanent jobs** — Resolution mandates; Term Sheet silent. [Art. 9.3]
5. **Equity demonstration timing** — Resolution (by Apr 19, 2025, with Clearmont certification) vs. Term Sheet (60 days from DA approval). [Art. 6.2]
6. **Assignment thresholds** — Term Sheet 50% / loan [50]% (bracketed) / Lakeshore 51%. [Harmonized in Art. 16]
7. **Insurance limits** — Term Sheet CGL $20M agg. vs. loan $25M agg. + Professional/Pollution Liability. [Art. 8.3 adopts higher]
8. **Force majeure cap** — Term Sheet 18-month aggregate vs. loan 180-day Phase I allowance. [Art. 12]
9. **Performance security dual claimants** — City (Phase I completion) vs. lender (collateral assignment). [Art. 7.3]
10. **TIF reachability** — TIF Memo projects $38–42M cumulative increment (with abatement) vs. $48M cap; Developer bears shortfall risk. [Art. 4.2]

Plus: RFP number (2024-CD-07 vs. 2024-CD-018); parcel acquisition history; parcel sizes; parcel orientation; contamination location on Parcel 016; Parcel 017 contaminants; county (Cook vs. Lake); affordable unit count (100 vs. 106); Phase I commencement triggers (internal Term Sheet inconsistency); prevailing wage scope; condemnation threshold; cure periods/lender cure rights; TIF assignment/City subordination; land write-down vs. TIF cap; City infrastructure funding source; abatement–TIF interaction.

## Open items flagged (28 total, A–BB)
Including: hotel brand; design review mechanics; community center specs/furnishing/library; phased conveyance; environmental cost-overrun allocation; remediation performer; vapor intrusion; off-site groundwater monitoring/Metra access; ESA reliance letters; $58.4M later-phase financing; TransitWorks equity; LEED failure consequences; CBA form; affordable housing covenant form/subordination; Substantial Completion definition; infrastructure schedule; later-phase incentives reopener; lender foreclosure assignment; lender's [50]% threshold; dispute venue/county; City Council approval of executed Agreement; lender closing conditions; execution authority; all Exhibits A–J; loan good-faith deposit/expiration; loan guarantors; Lakeshore 14% Minimum IRR.

## Validation
`python skills/docx/scripts/validate.py output/development-agreement-draft.docx` → **OK: valid** (ECMA-376 schema, ZIP integrity, content-type registration, relationship consistency all pass).