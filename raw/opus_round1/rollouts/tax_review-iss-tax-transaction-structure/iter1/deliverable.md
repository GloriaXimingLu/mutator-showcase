### FILE: report.md
# Tax Issue Identification Report

## Review of the Transaction Structure Memorandum — Acquisition of Prism Health Analytics, Inc.

**Prepared by:** Tax Review Function

**Date of Review:** February 2025

**Subject Document Reviewed:** "Tax Structure Memorandum — Acquisition of Prism Health Analytics, Inc.," prepared by Calloway, Stern & Whitaker LLP, dated February 10, 2025 (the "Memo").

**Supporting Documents Cross-Referenced:**

1. Agreement and Plan of Merger, dated January 28, 2025 (Ridgeline Capital Partners Fund III, LP / Ridgeline Acquisition Sub, Inc. / Prism Health Analytics, Inc. / Shareholders) — selected excerpts (the "PA").
2. Tax Due Diligence Report, Thornfield Accounting Group, LLP, dated January 15, 2025 (the "Thornfield Report").
3. Preliminary Purchase Price Allocation / Asset Valuation Summary, Thornfield Accounting Group, LLP (the "Asset Valuation Summary").
4. Prism Health Analytics, Inc. Capitalization Table, as of December 31, 2024 (the "Cap Table").
5. Amended and Restated Operating Agreement of Beacon Insights, LLC, effective August 1, 2018 (the "Beacon OA").
6. Email thread re: QSBS Eligibility — Angel Investor Shareholders, Linden Rock Advisory, LLC and Calloway, Stern & Whitaker LLP, November 2024 – January 2025 (the "QSBS Email Thread").

**Privilege Note:** This report is prepared in connection with the referenced transaction and is intended for the use of the addressee and its advisors. It identifies issues, inconsistencies, and omissions in the Memo when measured against the supporting deal documents; it does not itself constitute a tax opinion.

---

## I. Executive Summary

This report reviews the Tax Structure Memorandum prepared by Calloway, Stern & Whitaker LLP ("CSW") for Ridgeline Capital Partners Fund III, LP against the six supporting deal documents listed above. The review identified **thirty-three (33) distinct issues**, ranked by severity as follows: **3 Critical, 8 High, 10 Moderate, and 12 Low**.

The three Critical issues are, in our judgment, matters that must be resolved before the transaction closes and before any tax return (including Form 8023 and Form 8883) is filed:

1. **The Aggregate Deemed Sale Price (ADSP) is overstated by $48 million.** The Memo computes ADSP as Enterprise Value ($425M) plus funded debt ($48M) = $473M. This double-counts the $48M of funded debt, because enterprise value already embeds debt (EV = equity value + net debt). Under Treas. Reg. 1.338-4, ADSP begins from the amount realized on the stock ($370M equity value) plus target liabilities. The Asset Valuation Summary computes ADSP at $425M. The $48M overstatement flows directly into the Class VII goodwill residual, inflating goodwill from approximately $196.3M (per Thornfield) to $272.8M (per the Memo) — a $76.5M goodwill variance when combined with the Class V understatement described below.

2. **The Memo asserts that there are no ineligible S corporation shareholders, directly contradicting the diligence record.** The Memo states that "all shareholders of Prism are U.S. individuals, and we are not aware of any ineligible shareholders." The Thornfield Report flags S corporation eligibility as a **Critical** open item for restricted stock holders, and the Cap Table marks three restricted stock holders as "Unconfirmed." Valid S corporation status is a threshold requirement for the Section 338(h)(10) election; if the S election was inadvertently terminated, the entire transaction structure collapses and cascading C corporation tax consequences arise. The Memo does not flag this contingency.

3. **The QSBS / Section 1202 analysis is entirely absent from the Memo.** The QSBS Email Thread documents an explicit request by the selling shareholders' advisor for a written QSBS analysis to be included in the Memo *before* the purchase agreement was signed, and CSW agreed to include it. The purchase agreement was signed January 28, 2025; the Memo is dated February 10, 2025; and the Memo contains no QSBS analysis whatsoever. The issue is material — several angel investors acquired shares during the 2016 C corporation period and may be eligible for a 100% Section 1202 exclusion, a seven-figure swing in after-tax proceeds — and the Section 338(h)(10) deemed asset sale framework may foreclose that exclusion, which is itself a critical input to the election decision.

Two additional themes run through the High-severity findings. **First, the Memo's purchase price allocation diverges materially from Thornfield's asset-level valuation** (developed technology stated at $19M versus $41.8M; government software licenses omitted entirely; aggregate tax basis stated at $42.8M versus $64.3M implied by the asset detail). Taken together with the ADSP error, the Memo's deemed sale gain of $430.2M is overstated by approximately **$69.5M** relative to a Thornfield-consistent computation ($360.7M), materially overstating the tax the Memo tells shareholders to expect. **Second, the Memo is in direct tension with the operative transaction documents** on several points: its escrow installment-sale recommendation contradicts PA Section 7.4 (which reports the escrow as amount realized in the year of closing); it glosses over the Beacon operating agreement's change-of-control ROFR (a PA closing condition) and the automatic termination of the Beacon IP license upon Prism's change of control; and its post-closing "check-the-box" recommendation is legally flawed because a Delaware corporation is a per se corporation that cannot elect partnership/disregarded classification.

The full severity-ranked catalog follows. Each issue identifies the source, the problem, why it matters, and a recommended remediation.

---

## II. Scope and Methodology

We reviewed the Memo section by section and cross-referenced each factual assertion, figure, defined term, and legal conclusion against the six supporting documents. We treated the PA as the operative transaction document, the Thornfield Report and Asset Valuation Summary as the diligence record, the Cap Table as the equity record of truth, the Beacon OA as the governing document for the Beacon subsidiary, and the QSBS Email Thread as the record of the selling shareholders' express requests and CSW's commitments. Issues were ranked by the magnitude of their potential tax, structural, or diligence consequences and by the degree to which they contradict the controlling documents. We did not independently verify facts outside the document set; where a figure could not be reconciled to any source, we identify it as a data gap rather than asserting a corrected value.

---

## III. Critical Issues

### C-1. ADSP Overstated by $48 Million — Double-Counting of Funded Debt

**Severity:** Critical

**Sources:** Memo §I, §IV.B, §V.A, Appendix B; Asset Valuation Summary, "Allocation Summary" tab (Note 1); PA §1.1 (defined terms: Enterprise Value, Equity Value, Funded Indebtedness).

**Issue:** The Memo computes the Aggregate Deemed Sale Price as:

> Enterprise Value ($425,000,000) + Assumed Liabilities / Funded Debt ($48,000,000) = **ADSP $473,000,000**.

This is incorrect. Enterprise value already includes the funded debt (EV = equity value + net debt; here $425M = $370M equity + $48M debt + $7M seller expenses). Adding the $48M of funded debt a second time double-counts it. Under Treas. Reg. 1.338-4, ADSP is the grossed-up amount realized on the sale of the target's **stock** plus the liabilities of old target. The amount realized on the stock is the equity value of $370,000,000 ($333M cash + $37M rollover equity), not the enterprise value. The Asset Valuation Summary computes ADSP at $425,000,000 ($370M + $48M + $7M seller expenses, treated conservatively as target liabilities).

The Memo also misapplies its own stated formula. Section IV.B says ADSP equals "(i) the grossed-up amount realized on the sale of the target's stock and (ii) the liabilities of old target," but then substitutes enterprise value for "amount realized on the stock" — an internal inconsistency.

**Why it matters:** The $48M overstatement inflates the entire purchase price allocation. It flows directly into the Class VII goodwill residual, which the Memo puts at $272.8M versus Thornfield's $196.3M. Goodwill amortization (Section 197, 15 years) is correspondingly overstated by approximately $5.1M per year ($18.19M vs. $13.09M), overstating Buyer's projected tax shield. The overstated ADSP also inflates the deemed sale gain reported to selling shareholders (see C-1 together with H-2). Because the parties must file Form 8883 consistent with the final allocation (PA §7.3(b)), an unreconciled ADSP creates a filing-position dispute and potential inconsistency between Buyer's and Sellers' returns.

**Recommendation:** Recompute ADSP from the amount realized on the stock ($370M) plus target liabilities, reconcile to the Asset Valuation Summary, and revise the Class VII residual and all downstream D&A and gain computations before Form 8883 is prepared. Confirm whether the $7M of seller transaction expenses are properly treated as target liabilities (see L-6).

---

### C-2. S Corporation Shareholder Eligibility Unconfirmed — Memo Contradicts the Diligence Record

**Severity:** Critical

**Sources:** Memo §II.A (Restricted Stock), §III.A ("we are not aware of any ineligible shareholders"); Thornfield Report §III.B (Critical Finding), §XI (Finding 1); Cap Table (S Corp Eligible Shareholder? column — three "Unconfirmed"); PA §4.9(a) (S corporation rep), §2.5 (restricted stock rep), §8.2(c) (closing condition).

**Issue:** The Memo states that "[n]o events causing a termination of the S election have been identified. All shareholders of Prism are U.S. individuals, and we are not aware of any ineligible shareholders." This directly contradicts the diligence record:

- The Thornfield Report identifies S corporation eligibility as a **Critical** open item for restricted stock holders, specifically (a) a Canadian national on an H-1B visa whose substantial-presence-test compliance has not been verified for all years, and (b) a possible transfer of shares to a family LLC that would be an ineligible shareholder.
- The Cap Table marks **three** restricted stock holders as "Unconfirmed": Lin Wei Zhang (H-1B visa holder, PRC citizen), Yusuf Al-Rashidi (dual U.S./Jordan citizen, documentation not on file), and Nina Petrova (Bulgarian-born, green-card status unconfirmed).
- The PA nonetheless represents (§4.9(a)) that "each shareholder is an eligible S corporation shareholder" and (§2.5) that each restricted stock holder "is an individual who is a citizen or resident of the United States," and makes maintenance of valid S status a closing condition (§8.2(c)).

There is also an internal inconsistency *between* the diligence documents: the Thornfield Report identifies two eligibility concerns (the H-1B holder and the family-LLC transfer), while the Cap Table identifies three different/unverified holders (Zhang, Al-Rashidi, Petrova) and does not clearly map to the "family LLC" concern. The Memo resolves none of this and instead asserts the all-clear.

**Why it matters:** Valid S corporation status is a threshold requirement for the Section 338(h)(10) election. If the S election was inadvertently terminated in any prior year (e.g., by a nonresident alien holder or an ineligible LLC holder), Prism would have been a C corporation for that and all subsequent years, the 338(h)(10) election would be unavailable, and cascading entity-level federal and state C corporation tax (plus penalties and interest) would arise for all open years. The Memo's "no BIG tax" conclusion (§III.B), its pass-through gain analysis (§V), and its state-tax analysis (§VI) all silently depend on continuous valid S status. The Memo's blanket eligibility assertion is both unsupported by and contrary to the record, and it understates the single largest structural risk in the transaction.

**Recommendation:** Before closing, obtain definitive documentation of every shareholder's eligibility for every year since January 1, 2017 — including immigration/residency records for the H-1B holder, citizenship documentation for Al-Rashidi, green-card confirmation for Petrova, and the operating agreement and member composition of any family LLC. Reconcile the Thornfield Report and Cap Table eligibility findings. Revise the Memo to flag S-election validity as a contingent assumption and to describe the consequences of an inadvertent termination. Consider whether the PA's S corporation representations (§4.9(a), §2.5) are adequately supported or require qualification, and whether specific indemnity/escrow coverage is warranted.

---

### C-3. QSBS / Section 1202 Analysis Entirely Omitted

**Severity:** Critical

**Sources:** Memo (no QSBS / Section 1202 content anywhere); QSBS Email Thread (Whitfield request; Calloway commitment of Nov. 20, 2024; Whitfield follow-up of Jan. 6, 2025); Thornfield Report §VIII.B (Moderate Finding 4); Cap Table (per-shareholder "Potential QSBS — not analyzed" notes); PA §7.3(a) (338(h)(10) election).

**Issue:** The Memo contains no analysis of Section 1202 qualified small business stock (QSBS). This is a complete omission of an analysis that was (a) expressly requested by the selling shareholders' financial advisor, (b) expressly committed to by CSW, and (c) promised *before* the purchase agreement was signed:

- The QSBS Email Thread shows Linden Rock Advisory requesting, on behalf of several angel investors, a written QSBS analysis "ideally as a dedicated section in the transaction structure memorandum," before the shareholders committed to the definitive documents.
- CSW responded on November 20, 2024 that it would "include a QSBS analysis as part of the transaction structure memorandum" and that its "goal is to have the QSBS section drafted and incorporated into the memorandum well before the purchase agreement is executed."
- On January 6, 2025, Linden Rock followed up to state that no analysis had been received and to reiterate the request, adding a specific question about the escrow component.
- The PA was signed January 28, 2025; the Memo is dated February 10, 2025. The promised analysis was never delivered, and the shareholders signed the definitive agreement without it.

The Cap Table confirms that the two founders and four seed-round angel investors acquired shares during the 2016 C corporation period (June 14 – December 31, 2016) and are potentially QSBS-eligible, while shares issued after January 1, 2017 are not (Section 1202(c)(1) requires issuance by a C corporation). The Thornfield Report (§VIII.B) flags the interaction of Section 1202 with the 338(h)(10) deemed asset sale as unresolved and recommends a definitive analysis by tax counsel.

**Why it matters:** Section 1202 can exclude up to 100% of gain on qualified small business stock held more than five years. For the affected shareholders, the difference between a 100% federal exclusion and full capital-gains taxation is, in several cases, a seven-figure swing in after-tax proceeds. Critically, the Section 338(h)(10) election recharacterizes the transaction as a deemed asset sale followed by a deemed liquidation rather than a stock sale; because Section 1202 applies to gain on the "sale or exchange" of QSBS, the deemed asset sale treatment may foreclose the exclusion. This means the QSBS question is not merely a shareholder-side concern — it is a direct input to the election decision itself. If the 338(h)(10) election eliminates QSBS for eligible holders, an alternative structure (e.g., a stock sale without the election) may be value-maximizing for those shareholders, and the Memo's failure to analyze this deprives the parties of information needed to evaluate the trade-off. The Memo's silence is also a failure to deliver on an express, documented commitment.

**Recommendation:** Prepare and circulate a definitive QSBS analysis immediately, addressing: (i) whether shares issued during the 2016 C corporation period retain QSBS character through the intervening S corporation years and the sale; (ii) whether the 338(h)(10) deemed asset sale / deemed liquidation forecloses the Section 1202 exclusion; (iii) the $50M aggregate-gross-assets test at issuance; (iv) the per-taxpayer/per-issuer limitations; (v) the California non-conformance issue for the two California-resident holders; and (vi) the escrow component (whether any exclusion applies to gain attributable to escrow amounts released after closing). The analysis should be delivered to the selling shareholders and should inform any reconsideration of the election or the structure.

---

## IV. High-Severity Issues

### H-1. Class V Allocation Understated by $28.5 Million — Developed Technology and Government Software Licenses

**Severity:** High

**Sources:** Memo §IV.C (Class V table), Appendix B; Asset Valuation Summary, "Asset Detail" tab (A-006, A-007) and "Allocation Summary" tab (Class V variance note).

**Issue:** The Memo's Class V allocation totals $68,500,000, comprised of real property ($14.2M), furniture/fixtures/equipment ($6.8M), software/developed technology ($19.0M), and the Beacon interest ($28.5M). The Asset Valuation Summary's Class V totals $97,000,000. Two components drive the $28.5M difference:

- **Developed technology / proprietary software platform:** the Memo states $19,000,000; Thornfield's relief-from-royalty valuation (Asset A-006) is **$41,800,000** — a $22.8M understatement in the Memo.
- **Government-sector software licenses** (held by Prism Data Services): Thornfield values these at **$5,700,000** (Asset A-007); the Memo does not list this asset at all.

(The Beacon interest ($28.5M), real property ($14.2M), and FF&E ($6.8M) are consistent between the two documents. The NC data processing license is $0 in both — see H-4.)

We note that the Asset Valuation Summary's reconciliation note (Note 2) attributes the Class V variance to the Beacon interest being "excluded" from the Memo. That attribution appears to be erroneous: the Memo's Class V total of $68.5M can only be reached by *including* the $28.5M Beacon interest ($14.2M + $6.8M + $19.0M + $28.5M = $68.5M). The true drivers are developed technology and the omitted government software licenses. This is itself an inconsistency between the supporting documents that the Memo should have surfaced and reconciled.

**Why it matters:** The $28.5M Class V understatement, combined with the $48M ADSP overstatement (C-1), produces the $76.5M goodwill variance. It also misstates the character and amortization profile of the step-up: Thornfield classifies developed technology as a Class V intangible amortizable under Section 167 over five years (not Section 197), which would generate roughly $8.36M/year of amortization on the $41.8M value — an item the Memo's buyer-benefit analysis omits entirely (see M-10). The omission of the government software licenses likewise omits a depreciable/amortizable asset.

**Recommendation:** Revise Class V to reflect Thornfield's asset-level values for developed technology and government software licenses, reconcile the Asset Valuation Summary's Note 2 attribution, and recompute the Class VII residual. Add the developed-technology Section 167 amortization to the buyer D&A schedule.

---

### H-2. Aggregate Adjusted Tax Basis Inconsistent with the Asset Detail ($42.8M vs. $64.3M)

**Severity:** High

**Sources:** Memo §III.B ("approximately $42,800,000"), §V.A (deemed sale gain computation); Asset Valuation Summary, "Asset Detail" tab (Adjusted Tax Basis column).

**Issue:** The Memo computes the total deemed sale gain as ADSP ($473M) less "Aggregate Adjusted Tax Basis of Assets" ($42.8M) = $430.2M, and states in §III.B that Prism's "current aggregate adjusted tax basis in its assets … is approximately $42,800,000." Summing the "Adjusted Tax Basis (Book)" column of the Asset Valuation Summary yields **$64,300,000** (cash $12.4M; commercial AR $18.7M; government AR $6.4M; real property $9.1M; FF&E $3.2M; developed technology $4.8M; government software licenses $1.2M; Beacon interest $6.4M; proprietary data sets $2.1M). The $21.5M difference does not reconcile to any obvious subset of the asset detail (e.g., excluding cash and receivables yields $26.8M; excluding receivables only yields $39.2M).

**Why it matters:** The aggregate basis is a direct input to the deemed sale gain that passes through to shareholders on their final K-1s. Using $42.8M rather than the $64.3M implied by the asset detail overstates the gain by $21.5M on this input alone. Combined with the $48M ADSP overstatement (C-1), the Memo's $430.2M deemed sale gain is overstated by approximately **$69.5M** relative to a Thornfield-consistent computation ($425M ADSP − $64.3M basis = $360.7M). At a 23.8% blended long-term rate, $69.5M of overstated gain corresponds to roughly $16.5M of overstated shareholder tax — and more once ordinary-income portions are considered. Shareholders relying on the Memo's per-shareholder gain figures (§V.B) are being materially misinformed.

**Recommendation:** Reconcile the aggregate adjusted tax basis to the asset-level detail in the Asset Valuation Summary, identify the source of the $42.8M figure, and recompute the deemed sale gain and all per-shareholder allocations on a reconciled basis.

---

### H-3. Escrow Tax Treatment — Memo's Installment-Sale Recommendation Contradicts the Purchase Agreement

**Severity:** High

**Sources:** Memo §V.C (installment sale treatment); PA §7.4 (Tax Treatment of Escrow Amounts); QSBS Email Thread (Jan. 6, 2025 — escrow timing question).

**Issue:** The Memo (§V.C) advises that the $22M escrow "constitutes contingent consideration" and that shareholders "may elect installment sale treatment under Section 453, deferring recognition of a proportionate share of gain until the escrow is released" (September 15, 2026). The PA states the opposite. PA §7.4 provides that "the parties intend that the Escrow Amount be reported as an amount realized by the Shareholders in the taxable year in which the Closing occurs, consistent with the treatment of the Escrow Amount as a portion of the Cash Consideration deposited with a third-party agent for the benefit of the Shareholders." The Memo's deferral recommendation is therefore in direct conflict with the agreed tax treatment in the operative agreement.

There is also a conceptual concern: in a 338(h)(10) transaction the gain is recognized through the deemed asset sale at the S corporation level and passes through to shareholders on the final short-period K-1; the Memo does not reconcile its stock-sale-style installment analysis with the deemed-sale mechanics. Finally, the QSBS Email Thread raised the escrow-timing question specifically in the QSBS context, which the Memo does not address (see C-3).

**Why it matters:** The escrow is $22M. The difference between current-year inclusion (per the PA) and deferral to 2026 (per the Memo) is material to shareholders' 2025 tax liability and cash-flow planning. The Memo's advice, if followed, would put shareholders in a return position inconsistent with the PA's expressed intent and with the position the Buyer will take. The PA also places escrow-tax-treatment responsibility on each shareholder individually, so the conflict creates real exposure for the shareholders.

**Recommendation:** Revise the Memo to reflect the PA's agreed treatment (amount realized at closing) as the baseline, and separately — and cautiously — discuss whether any deferral position is defensible and at what risk. Reconcile the installment analysis to the 338(h)(10) deemed-sale mechanics. Address the escrow component in the QSBS analysis.

---

### H-4. NC Data Processing License — Non-Transferable; Potential Deemed Termination in the 338(h)(10) Deemed Asset Sale

**Severity:** High

**Sources:** Memo §II.A, §III.C, §VI.A, §IX.A (treats license as a commercial matter; "we expect that the existing license should remain valid post-closing, subject to confirmation"); Asset Valuation Summary, Asset A-008 (non-transferable/non-assignable; $0 FMV; potential deemed termination); PA §4.9(i) (license is "non-transferable and non-assignable"), §8.2(b) (regulatory approvals closing condition).

**Issue:** The NC data processing license (No. DIT-2019-04821) held by Prism Data Services is, by its terms and as represented in PA §4.9(i), non-transferable and non-assignable. The Asset Valuation Summary (A-008) flags that in a Section 338(h)(10) deemed asset sale the license "cannot be transferred and may need to be re-obtained by the surviving entity," that Thornfield assigned it $0 FMV for PPA purposes, and that if the license is deemed terminated, "the value associated with the government business line should be reassigned to goodwill or reduced." The license underpins Prism Data Services' approximately $19M of annual government-sector revenue. The Memo repeatedly treats the license as a minor commercial/notice matter ("we expect that the existing license should remain valid post-closing, subject to confirmation with the North Carolina Department of Information Technology") and does not address the tax/valuation consequence of a deemed termination.

**Why it matters:** This is not merely a commercial notice item. If the license does not survive the deemed asset sale, (i) the $19M government-sector revenue stream is impaired, which bears directly on enterprise value and the PPA; (ii) any value implicitly attributed to the license within the Memo's "Software / Developed Technology" line should be reallocated to goodwill or written down; and (iii) the survival of the license is effectively a closing condition (PA §8.2(b) regulatory approvals). The Memo's confident "should remain valid" posture is not supported by the license terms or by the diligence flag, and it understates a material risk to both deal value and the allocation.

**Recommendation:** Obtain a definitive determination from the NC Department of Information Technology (and deal counsel) on whether the license survives the reverse triangular merger / deemed asset sale, and on what terms. If survival is uncertain, reflect that risk in the PPA (reassign or reserve value), confirm the closing condition is satisfied, and revise the Memo to characterize the license status as an open tax/valuation item rather than a routine commercial matter.

---

### H-5. Beacon Interest — Section 751 "Hot Assets," Section 754 Election, and Look-Through Analysis Omitted

**Severity:** High

**Sources:** Memo §V.A ("gain on the deemed disposition of Prism's Beacon Insights interest is expected to be long-term capital gain"), §VIII; Thornfield Report §VI.B (hot-asset observation); Asset Valuation Summary, Asset A-009 and Note 2 (no look-through; 754 election decision); Beacon OA §11.04, §11.05 (754 election authority; no 754 currently in effect).

**Issue:** The Memo treats the entire $22.1M gain on the deemed disposition of Prism's 80.5% Beacon interest as "expected to be long-term capital gain." It does not address three items flagged in the diligence record:

- **Section 751 "hot assets."** The Thornfield Report (§VI.B) notes that Beacon's underlying assets include accounts receivable (approximately $2.1M) and accrued but unbilled revenue (approximately $1.8M), which should be analyzed under Section 751 for hot-asset characterization in connection with the deemed transfer of Prism's partnership interest. Under Section 751, the portion of the gain attributable to "unrealized receivables" (including AR and unbilled revenue) is recharacterized as ordinary income, not capital gain. The Memo's blanket capital-gain assertion may therefore be incorrect.
- **Section 754 election.** The Asset Valuation Summary (Note 2) states that the amortization/depreciation treatment of the step-up allocated to the Beacon interest "will depend on the nature of Beacon's underlying assets and whether a §754 election is made by Beacon," and recommends that Buyer's counsel determine whether a 754 election is advisable and prepare the Section 743(b) basis-adjustment computations. The Beacon OA (§11.04, §11.05) confirms the Partnership Representative has 754 authority and that no 754 election is currently in effect. The Memo does not address the 754 decision.
- **Look-through analysis.** Thornfield has not performed a look-through of Beacon's underlying assets; the Memo does not flag this gap or its consequences for the character and amortization of the step-up.

**Why it matters:** The 751 hot-asset recharacterization could convert a portion of the $22.1M gain from capital gain (23.8%) to ordinary income (up to 37% plus NIIT), a material tax difference that flows through to all Prism shareholders. The 754 election directly affects Buyer's inside basis in Beacon's assets and the usability of the step-up. The Memo's "long-term capital gain" conclusion is presented without the analysis needed to support it.

**Recommendation:** Perform the Section 751 hot-asset analysis on Beacon's AR and unbilled revenue; quantify any ordinary-income recharacterization and revise the gain character accordingly. Analyze whether a Beacon 754 election is advisable and prepare the 743(b) computations. Complete (or commission) the Beacon look-through and reflect it in the PPA and the buyer D&A schedule.

---

### H-6. Beacon Operating Agreement — Change-of-Control ROFR (a Closing Condition) and Automatic IP License Termination Not Addressed

**Severity:** High

**Sources:** Memo §VIII (cursory ROFR mention; no IP license termination discussion); Beacon OA §8.03(a)(ii) (ROFR triggered by Change of Control of a member), §8.03(b)–(f) (ROFR mechanics), §9.02 (IP license auto-terminates on Prism change of control); PA §8.2(g) (consents under Beacon OA as closing condition).

**Issue:** Two provisions of the Beacon OA have direct transaction consequences that the Memo does not analyze:

- **Right of first refusal (ROFR).** Beacon OA §8.03(a)(ii) provides that a "Change of Control" of any member that is an entity is a ROFR Triggering Event. The reverse triangular merger is a Change of Control of Prism (an entity member) under §8.03(a). Upon a ROFR Notice, the non-transferring members (Delano 12.0% and Avesta 7.5%) have 45 days to elect to purchase Prism's 80.5% interest at Fair Market Value. If exercised, Prism's Beacon interest could be purchased by the minority members, frustrating the Buyer's acquisition of an asset allocated $28.5M in the PPA. The PA makes "any required consents under the operating agreement of Beacon Insights, LLC" a closing condition (§8.2(g)). The Memo mentions the ROFR only in passing ("the parties and their counsel are addressing these transfer provisions") and does not analyze the ROFR trigger, the 45-day exercise window, the FMV determination mechanics (§8.04), or the consequences of exercise.
- **Automatic IP license termination.** Beacon OA §9.02 provides that the IP License Agreement "shall terminate automatically upon a Transfer of Prism's Membership Interest in the Company (including a deemed Transfer resulting from a Change of Control of Prism), unless the parties agree otherwise in writing." Beacon relies on Prism's licensed IP to generate its approximately $11M of annual revenue. The Memo does not mention this automatic termination at all. If the IP license terminates at closing, Beacon's revenue-generating capability and the value of the $28.5M allocated interest are impaired, and Beacon's minority members are affected.

**Why it matters:** The ROFR is a potential deal blocker or restructuring trigger for a $28.5M allocated asset and is an express closing condition. The automatic IP license termination threatens the going-concern value of Beacon. The Memo's scope exclusion of "the impact of the deemed asset sale on the minority members of Beacon" (§VIII) is too narrow: both provisions bear directly on the Buyer's acquisition and on the PPA. The Memo also does not address whether the 338(h)(10) deemed transfer of Prism's Beacon interest itself constitutes a "Transfer" or "deemed Transfer … resulting from a Change of Control" under the Beacon OA, which could independently trigger the ROFR and the IP license termination.

**Recommendation:** Confirm before closing whether Delano and Avesta waive the ROFR or whether the ROFR is exercised; document the outcome. Negotiate a written agreement (under Beacon OA §9.02) to preserve or replace the IP license post-closing, or reflect the impairment in the Beacon valuation and PPA. Analyze whether the 338(h)(10) deemed transfer itself triggers the Beacon OA transfer provisions. Revise the Memo to treat these as tax/structural items, not background notes.

---

### H-7. Intercompany Transfer Pricing — $6.3M Section 482 Exposure Not Addressed; PA Representation Potentially Inaccurate

**Severity:** High

**Sources:** Memo §III.C, §VIII (mention fees but do not flag exposure); Thornfield Report §VII (management fee and IP license fee below arm's length; ~$6.3M cumulative Section 482 exposure 2019–2024); Beacon OA §9.01, §9.02 (fees never benchmarked); PA §4.9(h) (Company represents fees "are at arm's length"; admits no transfer pricing study).

**Issue:** The Memo mentions the Beacon management fee ($850K/year) and IP license fee ($400K/year) but does not flag the Section 482 exposure. The Thornfield Report (§VII) concludes that both fees appear below arm's length: the management fee's actual cost is estimated at $1.1M–$1.25M/year (vs. $850K charged), and the IP license fee of $400K is approximately 3.6% of Beacon's $11M revenue versus an industry benchmark of 8%–15%. Thornfield estimates combined cumulative Section 482 exposure of approximately $6.3M for 2019–2024. The Beacon OA (§§9.01–9.02) confirms neither fee has ever been benchmarked or subjected to a transfer pricing study. Notwithstanding this, PA §4.9(h) represents that the fees "are at arm's length" while simultaneously disclosing that "[n]o formal transfer pricing study has been prepared" — a representation that is in tension with the Thornfield conclusion.

**Why it matters:** A Section 482 reallocation would shift income between Prism (an S corporation, flowing to all Prism shareholders) and Beacon (a partnership, flowing 80.5% to Prism and 19.5% to Delano and Avesta), affecting multiple parties in different proportions. The $6.3M exposure is a pre-closing tax liability that, under PA §7.6, is the Shareholders' indemnity responsibility. The Memo's failure to flag this exposure leaves the Buyer without a clear picture of a real pre-closing liability and leaves the Shareholders without notice of their indemnity exposure. The PA's arm's-length representation may also be unsupported.

**Recommendation:** Commission a formal transfer pricing study; consider a true-up and/or amended returns for prior years; reflect the Section 482 exposure in the transaction's risk allocation and indemnity/escrow analysis; and reconcile or qualify the PA §4.9(h) representation. Revise the Memo to disclose the exposure and its indemnity consequences.

---

### H-8. Post-Closing "Check-the-Box" Recommendation Legally Flawed — A Delaware Corporation Cannot Check-the-Box

**Severity:** High

**Sources:** Memo §VII.B ("converting Prism from a C corporation to a disregarded entity or partnership for federal income tax purposes following the closing, by making a check-the-box election under Treas. Reg. 1.301-7701-3"), §IX.B.4, §IX.C.4.

**Issue:** The Memo recommends that Buyer convert post-closing Prism (the Surviving Corporation, a Delaware corporation) into a disregarded entity or partnership "by making a check-the-box election." This is not available. Under the entity-classification regulations, a business entity incorporated under a state corporate statute is a "per se corporation" (Treas. Reg. 301.7701-2(b)) and is not an "eligible entity" that may elect its classification under Treas. Reg. 301.7701-3. A Delaware corporation therefore cannot use a check-the-box election to become a disregarded entity or partnership. Achieving flow-through treatment would require an actual liquidation of the corporation (e.g., a taxable liquidation under Sections 331/336, with corporate-level tax on the appreciated stepped-up assets) or a non-taxable liquidation under Sections 332/337 (available only into an 80%-or-greater corporate parent — inapplicable here because Fund III is a partnership), followed by contribution of the assets to a new LLC/partnership. The Memo's recommendation, as written, rests on a legal error and understates the cost and complexity of achieving flow-through treatment.

**Why it matters:** The recommendation is presented to the Investment Committee as a straightforward post-closing efficiency step. If relied upon, it will not work as described, and the actual path (a taxable corporate liquidation) could trigger corporate-level tax on the very stepped-up basis assets the 338(h)(10) election was designed to create — potentially undermining a portion of the election's benefit. The Memo also cites the regulation as "Treas. Reg. 1.301-7701-3," a malformed citation (see L-3).

**Recommendation:** Withdraw or correct the check-the-box recommendation. If flow-through treatment is desired, analyze the actual mechanics (taxable liquidation vs. alternative structures), quantify the corporate-level tax cost, and present the trade-off. Correct the regulatory citation.

---

## V. Moderate-Severity Issues

### M-1. Suspended Federal R&D Credits ($3.8M) — Treatment Under 338(h)(10) Not Analyzed

**Severity:** Moderate

**Sources:** Memo §III.D ("noted and will be addressed in the post-closing tax planning"); Thornfield Report §IV.B, §IX.A (credits at significant risk of permanent expiration; PTTP and deemed-liquidation mechanics require counsel analysis); PA §4.9(g).

**Issue:** Prism carries $3.8M in unused federal R&D credits generated in its 2016 C corporation year, suspended at the corporate level during the S corporation years under Section 1371(b)(1). The Thornfield Report analyzes three utilization scenarios (BIG-tax offset — unavailable because the recognition period expired; post-termination transition period under Section 1371(e) — applicability to credits unclear; deemed liquidation / final return — a question of law) and concludes the credits are at significant risk of permanent expiration in the transaction, recommending counsel analysis. The Memo notes the credits and defers them to "post-closing tax planning" without any analysis of whether they can be salvaged.

**Why it matters:** $3.8M of credits may be permanently lost upon the deemed liquidation. The Memo's deferral is not an analysis; the salvage question (if any) must be addressed before the deemed liquidation occurs, not after.

**Recommendation:** Analyze the interaction of Sections 1371(b), 1371(e), 1374, and 338(h)(10) to determine whether any portion of the credits can be utilized or preserved, and whether any structuring modification would help. Reflect the conclusion (and the likely loss) in the Memo.

---

### M-2. Deemed Sale Gain Character (Ordinary vs. Capital) Not Quantified

**Severity:** Moderate

**Sources:** Memo §V.A (character "will be refined upon completion of the Thornfield asset valuation"); §V.B (per-shareholder gain stated as a single total figure).

**Issue:** The Memo correctly states the principle that gain character follows the underlying assets (capital/Section 1231 → long-term capital; depreciation recapture under Sections 1245/1250, accounts receivable, and other ordinary assets → ordinary), but it does not quantify the split. The deemed sale includes $24.3M of accounts receivable (Class III, ordinary income on collection/basis recovery), depreciation recapture on the real property and FF&E (ordinary), and the Section 751 hot-asset portion of the Beacon interest (ordinary, per H-5). The per-shareholder gain figures ($223.7M / $120.5M / $86.0M) are presented as undifferentiated totals.

**Why it matters:** The ordinary/capital split drives the effective tax rate (up to 37% + NIIT on ordinary vs. 23.8% on long-term capital). Without a quantified split, the Memo's shareholder tax estimates are incomplete and the installment/escrow analysis (H-3) cannot be properly applied.

**Recommendation:** Quantify the ordinary-income and capital-gain portions of the deemed sale gain by asset class (including recapture and Section 751 hot assets), and present per-shareholder character-split figures.

---

### M-3. Net Investment Income Tax (Section 1411) — Material Participation Exception Not Analyzed

**Severity:** Moderate

**Sources:** Memo §V.A (applies a blanket 3.8% NIIT to long-term capital gain).

**Issue:** The Memo applies a combined 23.8% rate (20% capital gains + 3.8% NIIT) to the long-term capital gain without analyzing whether the Section 1411 material-participation exception applies. For S corporation shareholders who materially participate in the business, gain from the disposition of assets used in a non-passive trade or business may be excluded from net investment income under Section 1411(c)(3) (read with Section 469). Several shareholders are active employees/officers (Dr. Chandra, Ms. Stowe, and the restricted-stock employee holders).

**Why it matters:** NIIT at 3.8% on a substantial portion of the gain is material (on the order of millions of dollars for the active shareholders). The blanket 23.8% rate may overstate the tax for materially participating shareholders.

**Recommendation:** Analyze the Section 1411 material-participation exception for each active shareholder and adjust the per-shareholder rate analysis accordingly.

---

### M-4. AAA / AE&P / Deemed Liquidation Distribution Characterization Not Analyzed

**Severity:** Moderate

**Sources:** Memo (no AAA/AE&P analysis); Thornfield Report §IX.C (AAA $64.2M; AE&P $792K; PTI $792K as of 12/31/2023).

**Issue:** In the deemed liquidation under Section 338(h)(10), deemed liquidating distributions are characterized first against the Accumulated Adjustments Account (tax-free to the extent of shareholder stock basis), then against Accumulated Earnings and Profits (taxable dividend), then as return of capital / capital gain. The Thornfield Report identifies an AAA balance of $64.2M and AE&P of $792K and recommends counsel confirm the characterization after the deemed-sale gain computation. The Memo does not address AAA, AE&P, PTI, or the distribution characterization at all.

**Why it matters:** The AAA ($64.2M) is large enough to absorb a substantial portion of the deemed liquidating distribution tax-free (to the extent of basis), and the $792K of AE&P could generate a small dividend. The Memo's treatment of the entire pass-through as gain, without the AAA/AE&P layering, overstates the taxable amount and misstates its character.

**Recommendation:** Incorporate the AAA/AE&P/PTI layering into the deemed-liquidation distribution analysis and revise the per-shareholder tax consequences.

---

### M-5. Shareholder Count and State Residency Inconsistent with the Cap Table

**Severity:** Moderate

**Sources:** Memo §II.A, §VI.A, §VI.B (14 other shareholders: 11 NC, 2 CA, 1 NY); Thornfield Report §III.B (same 14/11/2/1); Cap Table (17 non-founder individuals: 14 NC, 2 CA, 1 NY).

**Issue:** The Memo (and the Thornfield Report) state that the "other shareholders" comprise 14 individuals, with 11 in North Carolina, 2 in California, and 1 in New York. The Cap Table lists 17 non-founder individuals (16 unique, with Derek Hawkins holding two tranches), whose residencies aggregate to 14 NC, 2 CA, and 1 NY. The Memo therefore understates the non-founder count by 3 and the North Carolina-resident count by 3 (11 vs. 14).

**Why it matters:** The state-residency breakdown drives the state tax analysis (the number of NC-resident shareholders subject to NC tax, and the non-resident apportionment). An understated NC-resident count understates the NC tax base and the number of shareholders with NC filing obligations. It also affects the precision of the per-shareholder gain allocation (M-6).

**Recommendation:** Reconcile the shareholder count and residency to the Cap Table and revise the state tax analysis accordingly. Confirm whether the "14" reflects a definitional choice (e.g., excluding certain holders) or an error.

---

### M-6. Per-Shareholder Gain Allocation Uses Basic Ownership Percentages, Not the K-1 / Fully-Diluted Allocation

**Severity:** Moderate

**Sources:** Memo §V.B (52% / 28% / 20%); Cap Table (fully diluted: Chandra 50.83%, Stowe 27.37%, others 21.80%; basic: 52% / 28% / 20%); PA §2.5 (restricted stock accelerates and vests immediately prior to the Effective Time).

**Issue:** The Memo allocates the deemed sale gain by basic ownership (Chandra 52%, Stowe 28%, Other 20%). Because all restricted stock accelerates and vests immediately prior to the Effective Time (PA §2.5), the restricted-stock holders are full shareholders at closing, and the gain that passes through on the final short-period K-1 should be allocated on a per-share, per-day basis reflecting the fully diluted ownership (and the actual ownership during the short period). The Cap Table's Consideration Waterfall allocates the $370M consideration on a fully diluted basis; the Memo's gain allocation is on a basic basis and lumps all restricted-stock holders into "Other 20%."

**Why it matters:** The basic-vs.-fully-diluted difference (e.g., Chandra 52% basic vs. 50.83% fully diluted) misallocates gain among shareholders and does not match the K-1s that will actually be issued. The restricted-stock holders' individual gains are not separately quantified.

**Recommendation:** Allocate the deemed sale gain on the per-share/per-day basis that will appear on the final K-1s, and present the restricted-stock holders' gains individually.

---

### M-7. Rollover Equity Interaction with the 338(h)(10) Deemed Sale Not Fully Reconciled

**Severity:** Moderate

**Sources:** Memo §II.B, §V.B (rollover "treated as a separate transaction … does not reduce or defer … deemed sale gain"); PA §2.4(b)–(c) (Rollover Shares converted to Parent equity); Cap Table Consideration Waterfall note ("Memo does not address interaction of rollover with 338(h)(10) deemed sale").

**Issue:** The Memo states that Dr. Chandra's $37M rollover is "a separate transaction from the deemed sale" and that he "will recognize his full pro rata share of the deemed sale gain and then contribute a portion of his after-tax proceeds." This is correct as far as it goes (the deemed sale gain passes through on the K-1 regardless), but the Memo does not reconcile the rollover with the 338(h)(10) mechanics under which the stock sale is disregarded and all stock is deemed sold in the deemed asset sale. The Memo does not address: (i) whether the rollover contribution itself qualifies for tax-deferred treatment under Section 351 or 721 and the structure of the post-closing vehicle (corporation vs. partnership); (ii) the basis Chandra receives in the post-closing vehicle; or (iii) how the "Rollover Shares" (PA §2.4(c)) interact with a deemed sale in which all stock is deemed sold. The Cap Table expressly flags that the Memo does not address this interaction.

**Why it matters:** The rollover is a $37M component of the consideration and a key element of Chandra's post-closing economics. The tax treatment of the contribution (deferred vs. recognized) and Chandra's basis in the new vehicle are material to him and to the structure.

**Recommendation:** Reconcile the rollover mechanics with the 338(h)(10) deemed sale; confirm whether the contribution is structured for Section 351/721 deferral; specify the post-closing vehicle's classification and Chandra's basis; and document the treatment in the Memo.

---

### M-8. Section 197 Anti-Churning — Non-Compete Agreements with Selling Shareholders Not Specifically Analyzed

**Severity:** Moderate

**Sources:** Memo §VII.B (general anti-churning conclusion); Asset Valuation Summary, Asset A-013 (non-competes: Chandra $10.5M, Stowe $4.5M; total $15M, Class VI, Section 197).

**Issue:** The Memo addresses the Section 197(f)(9) anti-churning rules generally and concludes they should not apply because the sellers are unrelated to the Buyer and Chandra "will not control Buyer after the closing." The Memo does not specifically analyze the non-compete agreements ($15M allocated to Class VI), which are entered into with the selling shareholders who will become employees/consultants of the Buyer. The anti-churning rules can restrict amortization of intangibles (including certain covenants not to compete) acquired from related parties or in transactions that do not result in a meaningful change of ownership. The Memo also does not quantify Chandra's post-closing equity interest (approximately $37M of rollover into a vehicle funded with ~$143M of Fund III equity, i.e., roughly 20% of the equity), which is relevant to the "control" analysis.

**Why it matters:** If anti-churning applied to the non-competes (or to other intangibles), the $15M (and potentially more) would not be amortizable, reducing Buyer's tax shield. The Memo's general conclusion is not a substitute for a specific analysis of the non-competes and the related-party/ownership-change tests.

**Recommendation:** Perform a specific Section 197(f)(9) analysis for the non-compete agreements (and confirm the analysis for the other Section 197 intangibles), quantify Chandra's post-closing interest, and document the conclusion.

---

### M-9. California 338(h)(10) Conformity, Separate State Election, and Apportionment of Deemed Sale Gain Not Addressed

**Severity:** Moderate

**Sources:** Memo §VI.B (assumes CA conforms; 1.5% entity-level tax on "California-apportioned share of the deemed sale gain"); Thornfield Report §V.B (CA follows federal S election; requires Form 100S and 1.5% entity-level tax); PA §7.3(a) (contemplates "analogous or similar forms under applicable state or local Tax law").

**Issue:** The Memo assumes California conforms to the Section 338(h)(10) deemed asset sale treatment and applies the 1.5% entity-level S corporation tax to the "California-apportioned share of the deemed sale gain." The Memo does not address (i) whether California requires a separate state-level 338(h)(10)-type election (California has its own election regime), (ii) whether such an election must be made and on what form, or (iii) how a one-time transactional deemed sale gain (including goodwill and intangibles) is properly apportioned to California — a question that is not cleanly answered by the standard payroll/property/sales formula and that, for intangibles under market-based sourcing, could produce a materially different California factor than the Memo's "relatively modest percentage" estimate. The Memo itself acknowledges its California analysis is "noted briefly."

**Why it matters:** There are two California-resident shareholders and California operations (12 employees, a sales office). The entity-level tax on the deemed sale gain, and the apportionment methodology that determines its size, are material and are not analyzed. If California does not conform or requires a separate election that is not made, the California treatment could diverge from the federal deemed asset sale treatment.

**Recommendation:** Confirm California's conformity and any separate state election requirement; analyze the proper apportionment of the deemed sale gain (including intangibles) to California; and quantify the expected California entity-level tax. Expand the California section of the Memo accordingly.

---

### M-10. Buyer D&A Estimate Affected by the ADSP Error and Omits Developed-Technology (Section 167) Amortization

**Severity:** Moderate

**Sources:** Memo §VII.A (estimates "approximately $24,500,000 or more" annual D&A); Asset Valuation Summary, Asset A-006 (developed technology $41.8M, Section 167, 5-year life).

**Issue:** The Memo's annual D&A estimate (~$24.5M+) is built from Class VI Section 197 amortization ($95M/15 = $6.33M), Class VII goodwill amortization ($272.8M/15 = $18.19M), and Class V tangible MACRS depreciation. Two problems: (i) the goodwill figure is inflated by the $48M ADSP error and the $28.5M Class V understatement (C-1, H-1), so the $18.19M/year goodwill amortization is overstated (Thornfield's $196.3M goodwill would yield ~$13.09M/year — roughly $5.1M/year less); and (ii) the Memo omits amortization of the developed-technology intangible, which Thornfield classifies as a Class V Section 167 asset amortizable over five years (~$8.36M/year on the $41.8M value, or ~$3.8M/year on the Memo's $19M value). The Memo's D&A schedule therefore both overstates the goodwill component and omits a separate intangible component.

**Why it matters:** The D&A estimate is a "key driver of the transaction economics" (Memo §VII.A) and feeds the Buyer's tax-shield and present-value calculations presented to the Investment Committee. An estimate that is wrong in both directions (overstated goodwill amortization, omitted developed-technology amortization) misstates the benefit and its timing (5-year Section 167 vs. 15-year Section 197).

**Recommendation:** Recompute the D&A schedule on a corrected ADSP and PPA, include the developed-technology Section 167 amortization, and restate the annual tax-shield and present-value figures.

---

## VI. Low-Severity Issues

### L-1. North Carolina 2025 Individual Income Tax Rate — Likely 4.25%, Not 4.5%

**Sources:** Memo §VI.A ("the current North Carolina individual income tax rate for the 2025 tax year is 4.5%, reflecting the phased reduction schedule enacted by the North Carolina General Assembly").

**Issue:** The Memo states the 2025 NC individual rate is 4.5%. Under the phased reduction enacted by the NC General Assembly (the 2023 tax legislation), the 4.5% rate applied to tax year 2024, with a further reduction to 4.25% scheduled for tax year 2025. The Memo's 4.5% figure is thus inconsistent with the very "phased reduction schedule" it cites. (Subsequent legislation may have affected the schedule; the rate should be confirmed as of the closing/filing date.)

**Why it matters:** A 0.25% difference on a large NC-apportioned gain is meaningful (on the order of seven figures across the NC-resident shareholder group).

**Recommendation:** Confirm the applicable 2025 NC rate as of the filing date and revise the NC tax estimates.

---

### L-2. Document Naming — "Stock Purchase Agreement" vs. "Agreement and Plan of Merger"

**Sources:** Memo §I, §II.B, §IV.A, Appendix A (refers to "Stock Purchase Agreement dated January 28, 2025"); PA (titled "Agreement and Plan of Merger").

**Issue:** The Memo repeatedly refers to the operative agreement as the "Stock Purchase Agreement." The document is an "Agreement and Plan of Merger." While the 338(h)(10) analysis treats the transaction as a deemed asset sale following a qualified stock purchase, the operative instrument is a merger agreement, and the defined term in the PA is "Agreement."

**Recommendation:** Correct the document name throughout the Memo for accuracy and to avoid confusion in cross-referencing.

---

### L-3. Malformed Treasury Regulation Citations — "Treas. Reg. 1.301-7701-3"

**Sources:** Memo §II.A, §VII.B (cites "Treas. Reg. 1.301-7701-3").

**Issue:** The check-the-box regulations are at Treas. Reg. 301.7701-3 (commonly cited as "Treas. Reg. 1.7701-3"). The Memo's "Treas. Reg. 1.301-7701-3" is a malformed citation that does not correspond to any regulation. It appears in both the Prism Data Services disregarded-entity discussion (§II.A) and the check-the-box recommendation (§VII.B).

**Recommendation:** Correct the citation to "Treas. Reg. 301.7701-3" throughout.

---

### L-4. Incorrect Purchase Agreement Cross-Reference — "Section 7.04"

**Sources:** Memo §IV.A ("This requirement is reflected in Section 7.04 of the Stock Purchase Agreement"); PA §7.3(a) (shareholder consent to the 338(h)(10) election as a condition to Closing), §8.2(d) (closing condition: all Shareholders execute Form 8023).

**Issue:** The Memo cites "Section 7.04" for the shareholder-consent requirement. The PA uses Section 7.3(a) (consent as a condition to closing) and Section 8.2(d) (the related closing condition). There is no "Section 7.04" in the PA excerpts.

**Recommendation:** Correct the cross-reference to PA §7.3(a) and §8.2(d).

---

### L-5. Thornfield Report Date Misstated — "January 10, 2025" vs. January 15, 2025

**Sources:** Memo §I ("the … tax due diligence report prepared by Thornfield Accounting Group, LLP dated January 10, 2025"); Thornfield Report (dated January 15, 2025 on the cover and signature block; January 10, 2025 is the information cutoff date stated in §XII).

**Issue:** The Memo cites the Thornfield Report as "dated January 10, 2025." The report is dated January 15, 2025; January 10, 2025 is the cutoff date for information relied upon, not the report date.

**Recommendation:** Correct the report date to January 15, 2025.

---

### L-6. Seller Transaction Expenses ($7M) — Treatment in ADSP Not Addressed

**Sources:** Memo §IV.B (excludes the $7M from ADSP); Asset Valuation Summary, "Allocation Summary" tab (includes $7M "for conservatism," noting treatment depends on which party bears the obligation); PA §2.6(b) (Seller Transaction Expenses paid from shareholder proceeds or directly by the Company).

**Issue:** The Memo excludes the $7M of seller transaction expenses from ADSP. The Asset Valuation Summary includes the $7M as a target liability "for conservatism" and notes the treatment depends on which party bears the obligation. The PA (§2.6(b)) provides that the $7M is paid from proceeds otherwise payable to Shareholders or, at the Company's election, directly by the Company immediately prior to closing. The Memo does not address whether the $7M is properly a target liability for ADSP purposes.

**Why it matters:** Inclusion or exclusion changes ADSP by $7M (and the goodwill residual correspondingly).

**Recommendation:** Analyze whether the $7M is a liability of old target for ADSP purposes based on who bears the obligation, and document the conclusion.

---

### L-7. New York Sales/Use Tax Exposure ($150K–$300K) Omitted

**Sources:** Memo §VI (state tax analysis covers income tax only); Thornfield Report §X.A (Prism has not collected NY sales tax on SaaS subscription revenue sourced to NY customers; estimated exposure $150K–$300K; recommends voluntary disclosure agreement).

**Issue:** The Memo's state tax analysis addresses income tax only and does not mention the New York sales/use tax exposure identified in the Thornfield Report. The exposure is a pre-closing liability that, under PA §7.6, is the Shareholders' indemnity responsibility.

**Recommendation:** Note the NY sales tax exposure in the Memo and confirm it is addressed (e.g., via voluntary disclosure) and allocated to the Shareholders under the indemnity.

---

### L-8. New York Separate S Corporation Election (Form CT-6, Effective 2019) Not Mentioned

**Sources:** Memo §VI.C (states Prism "files S corporation returns in both states" for VA and NY); Thornfield Report §V.B (NY requires a separate state-level S election on Form CT-6; Prism filed CT-6 effective 2019).

**Issue:** The Memo does not mention that New York requires a separate state-level S corporation election (Form CT-6), which Prism filed effective 2019, or the implications of the 338(h)(10) election for New York. The "other states" analysis is cursory.

**Recommendation:** Address the NY CT-6 election and any NY-specific 338(h)(10) consequences in the state tax section.

---

### L-9. Dr. Chandra's Stock Basis Unconfirmed ($1.5M Estimate)

**Sources:** Memo §V.B ("tax basis … is to be confirmed by Thornfield Accounting Group, but is estimated at approximately $1,500,000"); Cap Table (Chandra cost basis $1,014 at $0.001 par).

**Issue:** The Memo acknowledges Chandra's stock basis is unconfirmed and estimates it at $1.5M. The Cap Table shows a cost basis of $1,014 (par value), which does not reflect actual capital contributions. While stock basis is largely irrelevant to the deemed sale gain (which is recognized at the corporate level), it matters for the deemed-liquidation distribution characterization (basis recovery against AAA — see M-4).

**Recommendation:** Confirm Chandra's actual stock basis (and the basis of all shareholders) and incorporate it into the deemed-liquidation distribution analysis.

---

### L-10. Section 163(j) EBITDA Figure ($58M) Unsourced

**Sources:** Memo §VII.B ("Prism's historical EBITDA of approximately $58,000,000 (2024 estimate)").

**Issue:** The Memo's Section 163(j) analysis relies on a 2024 EBITDA estimate of approximately $58M. This figure is not sourced to the Thornfield Report, the Asset Valuation Summary, or any other document in the set, and it appears high relative to the $87M revenue figure stated elsewhere (an implied ~67% EBITDA margin). If incorrect, the 163(j) capacity conclusion could be affected.

**Recommendation:** Source and verify the EBITDA figure used in the 163(j) analysis.

---

### L-11. Property Tax Reassessment on the Raleigh Building Change of Ownership Not Addressed

**Sources:** Memo (no property tax discussion); Thornfield Report §X.C (Raleigh building assessed value ~$12.8M; PPA allocates $14.2M FMV).

**Issue:** The Memo does not address North Carolina property tax consequences of the change of ownership of the Raleigh office building (assessed at ~$12.8M, allocated $14.2M in the PPA). A change of ownership can trigger reassessment and higher property taxes post-closing.

**Recommendation:** Note the potential property tax reassessment and its budgetary impact on the Surviving Corporation.

---

### L-12. Compensation vs. Purchase Price Characterization Not Deeply Analyzed

**Sources:** Memo §V.B (treats Stowe consulting and Chandra employment as "separate compensatory arrangements … not part of the purchase price"); PA §8.2(e)–(f) (employment and consulting agreements as closing conditions); Asset Valuation Summary, Asset A-013 (non-competete values: Chandra $10.5M, Stowe $4.5M).

**Issue:** The Memo briefly states that the Chandra employment and Stowe consulting arrangements are separate from the purchase price, but does not analyze whether any portion of the consideration (including the $15M of non-compete value allocated to Class VI) could be recharacterized as compensation (with ordinary-income and withholding consequences) rather than purchase price, or the related Section 83 / Section 1041 implications for the restricted stock that accelerates at closing.

**Recommendation:** Analyze the compensation-vs.-purchase-price characterization of the employment, consulting, and non-compete arrangements and the accelerated restricted stock, and document the conclusion.

---

## VII. Summary of Issues by Severity

| ID | Issue | Severity |
|----|-------|----------|
| C-1 | ADSP overstated by $48M (double-counted funded debt) | Critical |
| C-2 | S corp eligibility unconfirmed; Memo contradicts diligence record | Critical |
| C-3 | QSBS / Section 1202 analysis entirely omitted (promised, material, post-signing) | Critical |
| H-1 | Class V understated by $28.5M (developed technology; omitted govt software licenses) | High |
| H-2 | Aggregate adjusted tax basis inconsistent ($42.8M vs. $64.3M) | High |
| H-3 | Escrow tax treatment contradicts PA §7.4 | High |
| H-4 | NC data processing license non-transferable; deemed-termination risk | High |
| H-5 | Beacon — Section 751 hot assets, 754 election, look-through omitted | High |
| H-6 | Beacon OA — change-of-control ROFR (closing condition) and IP license auto-termination | High |
| H-7 | Intercompany transfer pricing $6.3M Section 482 exposure not addressed | High |
| H-8 | Post-closing check-the-box recommendation legally flawed | High |
| M-1 | Suspended R&D credits ($3.8M) treatment not analyzed | Moderate |
| M-2 | Deemed sale gain character (ordinary vs. capital) not quantified | Moderate |
| M-3 | NIIT material-participation exception not analyzed | Moderate |
| M-4 | AAA / AE&P deemed-liquidation distribution characterization not analyzed | Moderate |
| M-5 | Shareholder count/residency inconsistent with Cap Table | Moderate |
| M-6 | Per-shareholder gain uses basic %, not K-1/fully-diluted allocation | Moderate |
| M-7 | Rollover equity / 338(h)(10) interaction not reconciled | Moderate |
| M-8 | Section 197 anti-churning for non-competes not specifically analyzed | Moderate |
| M-9 | California 338(h)(10) conformity / election / apportionment not addressed | Moderate |
| M-10 | Buyer D&A estimate affected by ADSP error; omits developed-tech §167 amortization | Moderate |
| L-1 | NC 2025 rate likely 4.25%, not 4.5% | Low |
| L-2 | Document naming (SPA vs. Merger Agreement) | Low |
| L-3 | Malformed Treas. Reg. citations (1.301-7701-3) | Low |
| L-4 | Incorrect PA cross-reference (§7.04 vs. §7.3(a)/§8.2(d)) | Low |
| L-5 | Thornfield report date misstated (Jan 10 vs. Jan 15) | Low |
| L-6 | Seller transaction expenses ($7M) ADSP treatment not addressed | Low |
| L-7 | New York sales/use tax exposure ($150K–$300K) omitted | Low |
| L-8 | New York separate S election (CT-6) not mentioned | Low |
| L-9 | Dr. Chandra stock basis unconfirmed | Low |
| L-10 | Section 163(j) EBITDA ($58M) unsourced | Low |
| L-11 | Property tax reassessment on Raleigh building not addressed | Low |
| L-12 | Compensation vs. purchase price characterization not deeply analyzed | Low |

---

## VIII. Recommended Next Steps (Prioritized)

1. **Before closing — resolve the Critical items.** (a) Recompute ADSP from the stock amount realized and reconcile to the Asset Valuation Summary (C-1). (b) Obtain definitive S corporation eligibility documentation for every shareholder for every year since 2017, reconcile the Thornfield Report and Cap Table findings, and revise the Memo to flag S-election validity as a contingent assumption (C-2). (c) Prepare and circulate the QSBS / Section 1202 analysis, including the escrow component, and inform the election decision (C-3).

2. **Before Form 8883 is filed — reconcile the purchase price allocation.** Correct the Class V components (developed technology, government software licenses) and the aggregate adjusted tax basis; recompute the Class VII residual and the deemed sale gain; restate the per-shareholder gain and character figures (H-1, H-2, M-2, M-6).

3. **Before closing — clear the Beacon and license obstacles.** Resolve the Beacon ROFR (a closing condition) and the automatic IP license termination; complete the Section 751 hot-asset and Section 754 analyses; and obtain a definitive determination on the NC data processing license's survival (H-4, H-5, H-6).

4. **Reconcile the Memo to the operative documents.** Correct the escrow tax treatment to match PA §7.4; address the intercompany transfer-pricing exposure and the PA §4.9(h) representation; and withdraw/correct the legally flawed check-the-box recommendation (H-3, H-7, H-8).

5. **Complete the deferred analyses.** Quantify the gain character split and the NIIT material-participation analysis; incorporate the AAA/AE&P layering; analyze the suspended R&D credits; address California conformity/apportionment; and restate the buyer D&A and tax-shield figures (M-1 through M-10).

6. **Correct the Low items** (citations, dates, naming, rate verification, and the remaining data gaps) in the next revision of the Memo.

---

*End of Report.*