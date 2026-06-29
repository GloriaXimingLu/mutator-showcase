### FILE: compromise-proposals.md
# COMPROMISE PROPOSALS — MASTER AI SERVICES AGREEMENT

**Meridian Health Systems, Inc. ("Meridian" or "Customer") and Cognitive Foundry, Inc. ("Cognitive Foundry" or "Vendor")**

**ClinIQ™ Platform (Version 4.2) — Enterprise Clinical Decision-Support Deployment**

---

**PRIVILEGED & CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION / ATTORNEY WORK PRODUCT**

*Prepared by Whitfield Ames LLP (Elaine Sutter, Partner; Jessica Fong; David Ouellette) at the direction of the Office of the General Counsel of Meridian Health Systems, Inc. (Dr. Priya Narayanan, SVP & General Counsel; Marcus Delgado, VP, Digital Health & Technology Transactions). This document is protected by the attorney-client privilege and the work-product doctrine and is intended exclusively for the Meridian negotiation team and authorized outside counsel. The proposed clause language in Component (i) of each proposal is drafted in redline-ready form for inclusion in the next markup and may be shared with Cognitive Foundry's negotiating team (Sandra Hu, VP, Commercial Legal; Rafael Bowen, Kessler Pratt & Lowe LLP) at the July 18, 2025 joint session. The negotiation rationale, fallback ladders, and acceptability analyses (Components (ii)–(iv)) constitute Meridian internal negotiation strategy and are not for disclosure to Cognitive Foundry or its counsel.*

**Date: July 14, 2025**

**Re: Preparation of compromise proposals for the July 18, 2025 joint negotiation session**

---

## I. EXECUTIVE SUMMARY AND NEGOTIATION FRAMEWORK

### 1.1 Purpose

This document sets forth seven compromise proposals addressing the contested terms remaining in the Master AI Services Agreement (the "Agreement") between Meridian and Cognitive Foundry, as identified in the Contested Terms Matrix finalized July 1, 2025. Each proposal is presented in the four-component format directed by Elaine Sutter on July 3, 2025: **(i)** proposed contract clause language (redline-ready); **(ii)** negotiation rationale and fallback ladder; **(iii)** acceptability analysis for the Vendor team; and **(iv)** regulatory and compliance constraints. The proposals are calibrated against Meridian's internal priority ranking, the Meridian AI/Technology Vendor Negotiation Playbook (2025 Edition) (the "Playbook") fallback ladders and absolute floors, Dr. Narayanan's four absolute red lines, and the strategic intelligence gathered by Marcus Delgado.

### 1.2 Deal Context

| Parameter | Value |
|---|---|
| Platform | ClinIQ™ v4.2 (sepsis prediction, radiology triage, medication interaction) |
| Total Contract Value (TCV) | $38.4M over 4-year Initial Term |
| Annual Contract Value (ACV) | $9.6M/year |
| Implementation Fee | $4.2M (one-time, Year 1) |
| Annual Recurring Fee (ARF) | $8.55M/year (quarterly installments of $2,137,500) |
| Covered Facilities | 14 acute-care hospitals (DE, PA, NJ); 3 NJ facilities subject to the NJ AI in Healthcare Transparency Act |
| Named Licensed Users | 6,200 |
| Annual Patient Encounters | ~2.1 million |
| Hosting | AWS GovCloud (us-east-1); integrated with Epic "MeridianConnect," Philips PACS, BD Pyxis |
| Governing Law / Disputes | Delaware / AAA Commercial Arbitration, Wilmington, DE |
| BAA (Exhibit F) | Executed June 2, 2025 |
| Target Execution / Go-Live | August 15, 2025 / January 6, 2026 |
| Board Risk Committee briefing | Week of August 4, 2025 (mandatory; AI-related liability = Tier 1 enterprise risk) |

### 1.3 Meridian Priority Ranking (Governs Concession Sequencing)

The Office of the General Counsel and the Board Risk Committee have approved the following priority ranking. Negotiating capital is allocated in this order, and no concession on a higher-priority item may be traded for advantage on a lower-priority item without General Counsel approval.

| Priority | Contested Term | Agreement Section | Matrix Term # |
|---|---|---|---|
| 1 | Patient-Safety Liability / Super-Cap Structure | §12.1–12.5 | 1 |
| 2 | Audit Rights / Model Transparency | §10.1–10.4 | 3 |
| 3 | Termination for Convenience / ETF / Transition | §14.3–14.6 | 7 |
| 4 | Aggregated / De-Identified Data Usage Rights | §5.4 | 4 |
| 5 | SLA / AI Accuracy Benchmarks | §9.1–9.4 | 6 |
| 6 | IP Ownership (Model Weights, Fine-Tuned Adaptations) | §6.1–6.5 | 2 |
| 7 | Indemnification Scope and Structure | §13.1–13.7 | 5 |

### 1.4 Dr. Narayanan's Absolute Red Lines (Floors — Non-Negotiable)

(a) **General Liability Cap** — floor of 1.5× trailing 12-month fees (~$14.4M).
(b) **Patient-Safety Liability** — separate, higher cap or uncapped; never capped below 3× ACV (~$28.8M).
(c) **Meaningful Audit Rights** — summary reports alone are insufficient; Langford tiered framework (Tier 2 baseline annual; Tier 3 for cause) is the minimum acceptable architecture.
(d) **Termination for Convenience** — Customer must retain the right to terminate without an early termination fee that makes exit economically prohibitive at any point in the term.

### 1.5 Strategic Intelligence Informing the Proposals

- **Comparable-deal precedent (Delgado intelligence).** Cognitive Foundry recently closed a comparable deal with another multi-hospital health system (12 hospitals) at a **1.5× ACV general cap** and a **3× ACV super-cap** covering IP infringement and data breach. This directly undermines Cognitive Foundry's "1× standard" opening and confirms that 1.5× / 3× is an achievable landing zone. *Use carefully at the table — anchor indirectly ("market practice for deals of this scope supports 1.5–2× ACV") rather than disclosing the source.*
- **Vendor's highest-priority term is data usage.** The aggregated, de-identified data from Meridian's 14-hospital network is highly valuable to Cognitive Foundry's model-training pipeline. Data usage (Priority 4) is Meridian's primary **concession currency** — calibrated flexibility here should be deployed in exchange for movement on Priorities 1–3.
- **CFO openness to graduated ETF.** Cognitive Foundry's CFO is concerned about revenue-recognition impact of unrestricted convenience termination but is amenable to a graduated early termination fee (50% Year 1 / 25% Year 2 / 0% Years 3–4). This structure satisfies Dr. Narayanan's red line (exit is not economically prohibitive by Year 3) and is the recommended landing zone, subject to General Counsel approval (any ETF triggers Playbook escalation).
- **Sandra Hu's private acknowledgment on third-party audit.** Hu acknowledged Cognitive Foundry can likely accept a qualified third-party audit (conditions: scope defined in advance; auditor mutually agreed). The CTO's "hard no" on raw model weights appears to apply to *routine* access; the Langford Tier 3 secure-enclave protocol (no extraction) may be acceptable for cause-based/regulatory triggers.
- **Vendor firm positions.** Model IP protection (weights, architecture, fine-tuned adaptations = Vendor property) and the data-usage opt-out window are areas where Cognitive Foundry is very firm.

### 1.6 Board Risk Committee Flag

The Board Risk Committee has classified AI-related liability as a **Tier 1 enterprise risk**. The Committee will require a briefing on final liability and indemnification terms before execution (week of August 4, 2025). Proposals 1, 2, 5, and 7 in particular must be defensible in that governance context — the deal team must be able to present terms the risk committee will approve, not merely terms the deal team can live with.

---

## II. CONCESSION STRATEGY AND SEQUENCING

The proposals are designed to operate as a **coordinated package**, not seven independent terms. The sequencing logic at the July 18 session should be:

1. **Anchor on Priority 1 (patient-safety liability).** Lead with the comparable-deal intelligence (indirectly) to establish that 1.5× ACV general cap and 3× ACV super-cap are market-achievable. Hold firm on the *scope* of the super-cap (patient-safety, HIPAA, and data breach must be included) even while conceding on the *dollar amounts* (1.5× / 3×). This is Meridian's hill.

2. **Secure Priority 2 (audit rights) as a regulatory mandate, not a preference.** Reframe the Langford tiered framework as a compliance baseline required by the NJ AI in Healthcare Transparency Act for Meridian's three New Jersey facilities. The Act's anti-waiver provision (§7(b)) means Cognitive Foundry cannot contractually prevent Meridian from accessing the documentation and audit rights necessary for compliance. This shifts the discussion from "Customer preference" to "legal floor."

3. **Close Priority 3 (termination) as a package.** Pair any ETF concession with robust transition assistance and data-export obligations (FHIR R4 / HL7 v2). These terms must travel together — an ETF without adequate transition support creates economic lock-in, which is the precise outcome Dr. Narayanan's red line prohibits.

4. **Deploy Priority 4 (data usage) as concession currency.** Hold the opening position (no use without per-use-case consent) through the early rounds. Offer calibrated flexibility on the *scope* of permitted use (model improvement + benchmarking) and the *opt-out window* in exchange for Vendor movement on Priorities 1–3. Hold the deletion red line (no purely prospective-only deletion without an alternative mechanism).

5. **Accept the Playbook fallback on Priorities 5–7 where strategic guidance directs.** Binding SLA benchmarks with a 3-miss termination trigger (Priority 5); Vendor IP ownership with an irrevocable perpetual license and portability (Priority 6); shared defense with broad indemnification scope capped at the super-cap (Priority 7). These are lower-priority terms where the Playbook fallbacks represent the right landing zone.

---

## III. CROSS-CUTTING REGULATORY CONSTRAINTS

Three regulatory regimes constrain Meridian's flexibility across multiple terms and must be reflected throughout the proposals:

- **HIPAA / HITECH.** The BAA (Exhibit F, executed June 2, 2025) governs PHI. De-identification must satisfy the Safe Harbor method (45 C.F.R. § 164.514(b)(2)) or Expert Determination method (45 C.F.R. § 164.514(b)(1)). Breach notification to Meridian within 24 hours of discovery (Meridian standard). Data governance terms in Exhibit D must be coordinated with the BAA; the BAA controls on PHI-specific conflicts.

- **New Jersey AI in Healthcare Transparency Act (S.2314, effective March 1, 2025).** Applies to Meridian's three New Jersey hospitals (Meridian Atlantic Medical Center, Meridian South Jersey Regional Hospital, Meridian Princeton Medical Center). Mandates: (i) independent annual audit of each covered AI system at minimum scope (model architecture documentation, training data provenance, validation results, bias/fairness, incident reports, data governance) — §5(b); (ii) audit reports available to NJ DOH within 15 business days of request; (iii) vendor contractual requirements for documentation access, audit rights, data governance, and regulatory cooperation — §7(a); (iv) anti-waiver provision — §7(b) (contractual terms that prevent compliance are unenforceable); (v) civil penalties up to $50,000 per violation, with each day of a continuing violation constituting a separate violation, assessed against Meridian as the covered entity. The Act materially strengthens Meridian's posture on audit rights (Priority 2) and indemnification for regulatory penalties (Priority 7).

- **FDA clinical decision-support software guidance.** The ClinIQ™ modules' regulatory status under the 21st Century Cures Act § 3060 exemption is fact-specific (the radiology module's interaction with medical imaging raises particular questions). The Agreement must require Vendor to maintain any necessary FDA clearances, notify Meridian of adverse regulatory actions within 24 hours, cooperate with FDA inquiries, and indemnify for failures to maintain clearances. A change-of-law provision should accommodate evolving FDA guidance.

---

## IV. THE SEVEN COMPROMISE PROPOSALS

*The proposals below are presented in Meridian's priority order. Each contains the four required components.*

---

### PROPOSAL 1 — PATIENT-SAFETY LIABILITY / SUPER-CAP STRUCTURE

**Priority Rank: 1 (highest) | Agreement §12.1–12.5; §15.1 (insurance) | Matrix Term 1 | Related: Exhibit B, Exhibit F (BAA), Exhibit G**

#### A. Positions Summary

| Component | Vendor Opening (Jun 6) | Customer Counter (Jun 20) | Vendor Response (Jun 30) |
|---|---|---|---|
| General Cap | 1× trailing fees (~$9.6M) | 2× trailing fees (~$19.2M) | 1.5× trailing fees (~$14.4M) |
| Super-Cap (amount) | 2× (~$19.2M) | Uncapped | 3× (~$28.8M) |
| Super-Cap (scope) | IP indemnity + willful misconduct only | IP, willful misconduct, HIPAA, patient-safety (all uncapped) | IP indemnity + willful misconduct/fraud only — **excludes patient-safety, HIPAA, data breach** |
| Consequential damages carve-outs | Narrow | Broad (patient-safety, data governance, audit, insurance) | Narrowed to confidentiality + indemnification only |
| Insurance (cyber/E&O) | $25M/$50M; no floor | $30M/$60M binding; increase within 90 days | $25M/$50M; "commercially reasonable efforts to increase" (non-binding) |

**Gap.** The Vendor's June 30 counter accepts a 1.5× general cap (meeting Meridian's floor) and a 3× super-cap amount (matching the comparable-deal precedent), but **excludes patient-safety, HIPAA, and data breach from the super-cap entirely** — leaving those categories subject only to the 1.5× general cap (~$14.4M). This is the single most important unresolved issue in the deal. Patient-safety liability must never be capped below 3× ACV (Board Risk Committee Tier 1 floor).

#### B. Proposed Compromise Clause Language (Redline-Ready)

> **§12.2 General Liability Cap.** EXCEPT AS SET FORTH IN SECTION 12.3, EACH PARTY'S TOTAL CUMULATIVE LIABILITY ARISING OUT OF OR RELATED TO THIS AGREEMENT, WHETHER IN CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY, OR OTHERWISE, SHALL NOT EXCEED AN AMOUNT EQUAL TO ONE AND ONE-HALF TIMES (1.5×) THE FEES PAID OR PAYABLE BY CUSTOMER TO VENDOR IN THE TWELVE (12) MONTH PERIOD IMMEDIATELY PRECEDING THE EVENT GIVING RISE TO THE CLAIM (THE "GENERAL CAP"). AS OF THE FIRST CONTRACT YEAR, THE GENERAL CAP IS FOURTEEN MILLION FOUR HUNDRED THOUSAND DOLLARS ($14,400,000).
>
> **§12.3 Super-Cap Carve-Outs.** THE FOLLOWING CATEGORIES OF LIABILITY SHALL NOT BE SUBJECT TO THE GENERAL CAP AND SHALL INSTEAD BE SUBJECT TO A SEPARATE AGGREGATE LIABILITY CAP EQUAL TO THREE TIMES (3×) THE FEES PAID OR PAYABLE BY CUSTOMER IN THE PRECEDING TWELVE (12) MONTHS (THE "SUPER-CAP"). AS OF THE FIRST CONTRACT YEAR, THE SUPER-CAP IS TWENTY-EIGHT MILLION EIGHT HUNDRED THOUSAND DOLLARS ($28,800,000):
>
> (a) **Patient-Safety Liability** — any liability arising from bodily injury, clinical misdiagnosis, treatment error, delayed diagnosis, adverse drug event, or other patient harm attributable in whole or in part to an Output, recommendation, alert, risk score, or clinical decision-support result generated by the Platform (as defined in Section 1.22);
>
> (b) **IP Indemnification** — Vendor's indemnification obligations under Section 13.1(a) (IP Infringement Claims);
>
> (c) **Willful Misconduct or Gross Negligence** — liability arising from the willful misconduct, fraud, or gross negligence of either Party; and
>
> (d) **PHI / Data Breach** — liability arising from a breach of either Party's obligations under the BAA (Exhibit F) or Article 5, including any unauthorized access to, use of, or disclosure of Protected Health Information, and any data breach attributable to Vendor's systems, infrastructure, personnel, or subcontractors.
>
> **§12.4 Uncapped Liabilities.** THE FOLLOWING SHALL NOT BE SUBJECT TO ANY CAP: (a) CUSTOMER'S OBLIGATION TO PAY FEES; AND (b) EITHER PARTY'S LIABILITY THAT CANNOT BE LIMITED OR EXCLUDED UNDER APPLICABLE LAW.
>
> **§12.1 Consequential Damages — Carve-Outs.** [Restore the Customer redline carve-outs so that the exclusion of indirect/consequential damages does not apply to:] (A) a Party's breach of Article 11 (Confidentiality); (B) a Party's indemnification obligations under Article 13; (C) Customer's obligation to pay Fees; (D) Patient-Safety Liability (Section 1.22); (E) Vendor's breach of Article 5 (Data Governance and HIPAA Compliance); (F) Vendor's breach of Article 10 (AI Model Transparency and Audit); and (G) claims covered by Vendor's insurance under Article 15.
>
> **§15.1(c) Cyber/E&O Insurance — Binding Increase Covenant.** CYBER LIABILITY AND TECHNOLOGY ERRORS & OMISSIONS INSURANCE: THIRTY MILLION DOLLARS ($30,000,000) PER OCCURRENCE AND SIXTY MILLION DOLLARS ($60,000,000) IN THE AGGREGATE. VENDOR'S CURRENT COVERAGE UNDER NORTHFIELD MUTUAL INSURANCE CO. POLICY NO. NM-CY-2025-04417 IS $25,000,000 PER OCCURRENCE / $50,000,000 AGGREGATE. VENDOR COVENANTS TO INCREASE SUCH COVERAGE TO THE MINIMUMS SET FORTH HEREIN NO LATER THAN THE EARLIER OF (i) THE NEXT POLICY RENEWAL DATE OR (ii) MARCH 31, 2026. DURING THE PERIOD PRIOR TO SUCH INCREASE, VENDOR SHALL PROVIDE WRITTEN CONFIRMATION FROM ITS BROKER THAT THE COVERAGE INCREASE HAS BEEN REQUESTED AND IS REASONABLY EXPECTED TO BE OBTAINED. IF VENDOR FAILS TO OBTAIN THE REQUIRED COVERAGE BY THE DEADLINE, CUSTOMER MAY, AT ITS ELECTION AND AT VENDOR'S EXPENSE: (x) OBTAIN SUPPLEMENTAL COVERAGE; (y) WITHHOLD UP TO TEN PERCENT (10%) OF THEN-DUE FEES IN ESCROW PENDING COMPLIANCE; OR (z) TERMINATE THIS AGREEMENT WITHOUT PENALTY PURSUANT TO SECTION 14.1.
>
> **§15.4 Tail Coverage.** VENDOR SHALL MAINTAIN TAIL OR EXTENDED-REPORTING-PERIOD COVERAGE UNDER ITS PROFESSIONAL LIABILITY AND CYBER LIABILITY POLICIES FOR A PERIOD OF NOT LESS THAN THREE (3) YEARS FOLLOWING EXPIRATION OR TERMINATION OF THIS AGREEMENT.

#### C. Negotiation Rationale and Fallback Ladder

**Why this landing zone.** The proposal concedes on the *dollar amounts* (1.5× general cap; 3× super-cap) — both of which match the comparable-deal precedent and the Vendor's own June 30 counter — and holds firm on the *scope* of the super-cap. The decisive move is **adding patient-safety, HIPAA/PHI breach, and data breach to the 3× super-cap**, which the Vendor's June 30 draft excluded. This satisfies Dr. Narayanan's absolute floor (patient-safety never below 3× ACV) while staying within the Vendor's stated 3× super-cap maximum and avoiding the uncapped exposure the Vendor's Board and insurers have categorically refused. The 1.5× general cap is at Meridian's floor but is acceptable because the super-cap captures the catastrophic-risk categories.

**Playbook linkage note.** The Playbook's coordinated ladder pairs a 1.5× general cap with a 4× all-carve-outs super-cap (second fallback). The proposed 3× all-carve-outs super-cap at 1.5× general is a coordinated variant that (i) meets the absolute patient-safety floor (≥3× ACV), (ii) matches the comparable-deal precedent (3×), and (iii) remains within the Vendor's stated 3× maximum. General Counsel approval is recommended for this variant, as it departs from the strict second-fallback pairing; however, it is more achievable than 4× and captures all four catastrophic categories within the super-cap.

**Fallback ladder (real-time adjustments at the table):**

| Position | General Cap | Super-Cap Amount | Super-Cap Scope | When to Deploy |
|---|---|---|---|---|
| **A (Primary)** | 1.5× ($14.4M) | 3× ($28.8M) | Patient-safety + IP + willful + HIPAA/breach | Opening compromise |
| **B (First fallback)** | 1.75× ($16.8M) | 3× ($28.8M) | Patient-safety only; IP/willful/HIPAA uncapped | If Vendor refuses to include HIPAA/breach at 3× — raise general cap in exchange for keeping other carve-outs uncapped (Playbook first fallback) |
| **C (Second fallback)** | 1.5× ($14.4M) | 4× ($38.4M) | All carve-outs | If Vendor refuses patient-safety at 3× — offer higher dollar cap (4×) in exchange for scope inclusion (Playbook second fallback) |
| **Floor** | Never below 1.5× | Patient-safety never below 3× | Patient-safety must be in super-cap | If Vendor refuses patient-safety ≥3× → escalate to GC + Board Risk Committee; deal at risk |

**Insurance rationale.** The super-cap structure is only meaningful if it is collectable. The Vendor's current $25M/$50M cyber/E&O coverage is below the 3× super-cap ($28.8M). The binding increase covenant (to $30M/$60M by March 31, 2026 or next renewal) with broker confirmation and step-in rights closes the collectability gap without requiring the Vendor to obtain the increase pre-signing (which it has represented it cannot do). Three-year tail coverage backstops the survival of liability and indemnification obligations.

#### D. Acceptability Analysis for the Vendor Team

**Sandra Hu (commercial flexibility / precedent concerns).** Hu's principal objection will be that including patient-safety, HIPAA, and data breach in the super-cap departs from Cognitive Foundry's "standard" framework. **Response:** (i) the comparable-deal precedent establishes that Cognitive Foundry has already agreed to a 3× super-cap covering IP *and data breach* for a comparable health system — the proposal merely extends that established precedent to the two additional categories (patient-safety, HIPAA) that are uniquely implicated by a 14-hospital clinical deployment; (ii) the proposal accepts Cognitive Foundry's 1.5× general cap and 3× super-cap *amounts* without demanding the 2× / uncapped positions — a substantial concession that should be reciprocated on scope; (iii) no category is uncapped, respecting the Vendor's categorical refusal of uncapped liability. Frame the scope expansion as the price of Meridian accepting the Vendor's dollar amounts.

**Rafael Bowen (liability exposure / IP protection).** Bowen's principal objection will be that patient-safety liability is a clinical-malpractice matter outside a software vendor's indemnification scope and that a 3× cap on patient-safety is unbounded exposure. **Response:** (i) the 3× super-cap is a *ceiling*, not uncapped exposure — it is the same dollar amount Bowen has already accepted for IP and willful misconduct; (ii) patient-safety liability is allocated to the super-cap (not the indemnification scope in Proposal 7), preserving the Vendor's argument that clinical malpractice is a separate matter; (iii) the binding insurance increase to $30M/$60M ensures the super-cap is backed by coverage, addressing collectability; (iv) the consequential-damages carve-outs are restored only to the extent necessary to make the super-cap meaningful — they do not create additional uncapped exposure. Emphasize that the Board Risk Committee will not approve a deal in which patient-safety liability is capped at 1.5× ACV ($14.4M) — this is a governance constraint, not a negotiating preference.

#### E. Regulatory and Compliance Constraints

- **HIPAA.** The BAA (Exhibit F) governs PHI breach liability. The super-cap carve-out for PHI/data breach (§12.3(d)) must be coordinated with the BAA's breach-notification and indemnification provisions; the BAA controls on PHI-specific conflicts. The 24-hour breach-notification standard (Meridian) is preserved.
- **NJ AI in Healthcare Transparency Act.** Civil penalties (up to $50,000 per violation, per day) are assessed against Meridian as the covered entity. To the extent penalties arise from Vendor's failure to provide required documentation, audit access, or cooperation, they are addressed through the regulatory-indemnification carve-out in Proposal 7 (carved out from the general cap). The super-cap structure does not displace this regulatory indemnification.
- **FDA.** Patient-safety liability arising from AI outputs is relevant to the FDA's clinical decision-support framework. The §12.1(F) carve-out for insurance-covered claims and the §15.1 insurance backstop ensure that FDA-related adverse-action costs are recoverable. The change-of-law provision (Playbook §10.4) should be incorporated to accommodate evolving FDA guidance.
- **Board Risk Committee.** The Tier 1 enterprise-risk designation requires that patient-safety liability be protected at no less than 3× ACV. This proposal meets that floor and is structured to be defensible at the August 4 briefing.

---

### PROPOSAL 2 — AUDIT RIGHTS / MODEL TRANSPARENCY

**Priority Rank: 2 | Agreement §10.1–10.4; Exhibit H | Matrix Term 3 | Related: §5.7 (NJ Act), Exhibit D (data governance), Exhibit E (security)**

#### A. Positions Summary

| Component | Vendor Opening (Jun 6) | Customer Counter (Jun 20) | Vendor Response (Jun 30) |
|---|---|---|---|
| Transparency report | Annual summary (internal team) | Quarterly, detailed | Annual summary (60 days after contract year) |
| Independent audit | Third-party at Customer cost; pre-approved; NDA; **no model internals**; 1/year; Vendor 30-day review | Quarterly Langford audit; Tier 2 + Tier 3 (secure enclave); full architecture/provenance/validation/feature-importance/weights | Annual audit at Customer cost; **scope limited to bias/fairness + aggregate accuracy + governance summary**; no architecture/weights/provenance/feature-importance/SHAP; Vendor pre-approval + NDA; Vendor redact right |
| Exhibit H (auditor terms) | Not present | Added (Langford tiered framework) | **Deleted entirely** |
| Regulatory cooperation | Limited; Vendor protective-order rights | Full cooperation; no protective orders blocking compliance | Cooperation subject to scope limits; Vendor retains protective-order right |

**Gap.** The Vendor's June 30 audit scope is **insufficient to satisfy the NJ AI in Healthcare Transparency Act**, which requires the annual audit to cover, at minimum, model architecture documentation, training data provenance, validation results, bias/fairness, incident reports, and data governance (§5(b)). The Vendor's limited scope (bias/fairness + aggregate accuracy + governance summary) omits architecture, provenance, validation, and incident review. The Act's anti-waiver provision (§7(b)) renders unenforceable any contractual term that prevents Meridian from accessing the documentation and audit rights necessary for compliance. This is a legal floor, not a commercial preference.

#### B. Proposed Compromise Clause Language (Redline-Ready)

> **§10.1 Transparency Reports.** ON OR BEFORE THE THIRTIETH (30TH) DAY FOLLOWING THE END OF EACH CALENDAR QUARTER, VENDOR SHALL PROVIDE CUSTOMER WITH A QUARTERLY TRANSPARENCY REPORT DESCRIBING: (a) THE TYPES AND VERSIONS OF AI/ML MODELS DEPLOYED AT EACH COVERED FACILITY; (b) ALL CHANGES TO MODEL ARCHITECTURES, TRAINING METHODOLOGIES, OR TRAINING DATA SOURCES DURING THE PRECEDING QUARTER; (c) PERFORMANCE METRICS BY CLINICAL MODULE (SENSITIVITY, SPECIFICITY, PPV, NPV, AUC-ROC); (d) FEATURE-IMPORTANCE RANKINGS; (e) BIAS AND FAIRNESS TESTING RESULTS ACROSS PATIENT SUBPOPULATIONS (RACE, ETHNICITY, AGE, SEX, INSURANCE STATUS); (f) MODEL GOVERNANCE PRACTICES; AND (g) A SUMMARY OF ADVERSE EVENTS, CLINICAL SAFETY SIGNALS, OR MODEL-RELATED INCIDENTS. THE QUARTERLY TRANSPARENCY REPORT SHALL BE MARKED AS VENDOR'S CONFIDENTIAL INFORMATION UNDER ARTICLE 11.
>
> **§10.3 Independent Audit Rights.**
>
> (a) **Annual Independent Audit.** CUSTOMER SHALL HAVE THE RIGHT, AT CUSTOMER'S EXPENSE, TO ENGAGE THE INDEPENDENT AUDITOR (INITIALLY LANGFORD AI ASSURANCE GROUP, LLC, UNDER THE DIRECTION OF DR. ANIL CHERIAN, A PRE-APPROVED INDEPENDENT AUDITOR) TO CONDUCT ONE (1) ANNUAL AUDIT OF THE PLATFORM'S AI/ML MODELS. THE ANNUAL AUDIT SHALL BE CONDUCTED AT **TIER 2 ACCESS**, COMPRISING: (i) MODEL ARCHITECTURE DOCUMENTATION (NETWORK TOPOLOGY, LAYER SPECIFICATIONS, ACTIVATION FUNCTIONS); (ii) TRAINING DATA PROVENANCE RECORDS (DATA SOURCES, PREPARATION METHODOLOGIES, DE-IDENTIFICATION PROCEDURES, DEMOGRAPHIC COMPOSITION); (iii) VALIDATION AND TEST DATASETS AND RESULTS, INCLUDING PERFORMANCE METRICS BY SUBPOPULATION; (iv) TEST QUERY ACCESS (THE ABILITY TO SUBMIT DEFINED TEST CASES AND OBSERVE OUTPUTS); (v) BIAS AND FAIRNESS TESTING RESULTS AND METHODOLOGIES; (vi) REVIEW OF INCIDENT REPORTS AND ADVERSE-EVENT CORRELATION DATA; AND (vii) REVIEW OF DATA GOVERNANCE PRACTICES. TIER 2 ACCESS DOES NOT REQUIRE DISCLOSURE OF RAW MODEL WEIGHTS, PROPRIETARY SOURCE CODE, OR TRAINING PIPELINE CODE. VENDOR SHALL PROVIDE ACCESS WITHIN FIFTEEN (15) BUSINESS DAYS OF CUSTOMER'S WRITTEN AUDIT REQUEST.
>
> (b) **Tier 3 Access for Cause.** NOTWITHSTANDING THE ANNUAL CADENCE, CUSTOMER MAY REQUEST AN ADDITIONAL AUDIT AT **TIER 3 ACCESS** (MODEL WEIGHTS AND EMBEDDINGS REVIEWED SOLELY WITHIN A VENDOR-DESIGNATED SECURE COMPUTATIONAL ENCLAVE, WITH NO DATA EXTRACTION, COPYING, PHOTOGRAPHING, OR REMOVAL PERMITTED) UPON THE OCCURRENCE OF ANY OF THE FOLLOWING: (i) A DOCUMENTED PATIENT-SAFETY EVENT AT ANY COVERED FACILITY POTENTIALLY ATTRIBUTABLE TO A PLATFORM OUTPUT; (ii) CONSECUTIVE FAILURE OF PERFORMANCE BENCHMARKS UNDER SECTION 9.3 FOR TWO (2) OR MORE QUARTERLY MEASUREMENT PERIODS; (iii) RECEIPT OF A FORMAL REGULATORY INQUIRY OR INVESTIGATION FROM THE NEW JERSEY DEPARTMENT OF HEALTH, THE FDA, OR ANOTHER REGULATORY AUTHORITY; OR (iv) IDENTIFICATION OF ANOMALIES DURING A TIER 2 AUDIT THAT CANNOT BE RESOLVED WITHOUT EXAMINATION OF MODEL INTERNALS.
>
> (c) **Auditor Confidentiality.** THE INDEPENDENT AUDITOR SHALL (i) EXECUTE A NON-DISCLOSURE AGREEMENT WITH VENDOR, IN A FORM REASONABLY ACCEPTABLE TO VENDOR, PRIOR TO COMMENCING ANY AUDIT; (ii) CONDUCT ALL TIER 3 REVIEWS SOLELY WITHIN VENDOR'S DESIGNATED SECURE ENCLAVE; (iii) NOT EXTRACT, COPY, OR REMOVE ANY VENDOR CONFIDENTIAL INFORMATION; (iv) DESTROY ALL WORKING PAPERS CONTAINING VENDOR CONFIDENTIAL INFORMATION WITHIN THIRTY (30) DAYS OF DELIVERING THE AUDIT REPORT; AND (v) CERTIFY SUCH DESTRUCTION IN WRITING TO VENDOR WITHIN FIVE (5) BUSINESS DAYS.
>
> (d) **Audit Reports.** THE INDEPENDENT AUDITOR SHALL DELIVER A WRITTEN AUDIT REPORT TO BOTH PARTIES. VENDOR SHALL PROVIDE A WRITTEN RESPONSE AND REMEDIATION PLAN WITHIN THIRTY (30) DAYS OF RECEIPT OF ANY REPORT IDENTIFYING MATERIAL FINDINGS. AUDIT REPORTS SHALL BE PREPARED IN A FORM SUITABLE FOR PRODUCTION TO THE NEW JERSEY DEPARTMENT OF HEALTH UPON REQUEST.
>
> (e) **Substitute Auditors.** IF LANGFORD IS UNABLE OR UNWILLING TO SERVE, CUSTOMER MAY PROPOSE AN ALTERNATIVE INDEPENDENT AUDITOR SUBJECT TO VENDOR'S REASONABLE APPROVAL (NOT TO BE UNREASONABLY WITHHELD, CONDITIONED, OR DELAYED), PROVIDED THE SUBSTITUTE IS NOT A DIRECT COMPETITOR OF VENDOR AND EXECUTES THE CONFIDENTIALITY OBLIGATIONS IN SUBSECTION (c).
>
> (f) **Regulatory Cooperation.** IN CONNECTION WITH REGULATORY EXAMINATIONS UNDER THE NJ AI IN HEALTHCARE TRANSPARENCY ACT OR ANY COMPARABLE STATE OR FEDERAL REGULATION, VENDOR SHALL (i) COOPERATE FULLY WITH CUSTOMER AND THE INDEPENDENT AUDITOR IN RESPONDING TO REGULATORY INQUIRIES; (ii) PROVIDE ALL DOCUMENTATION REQUIRED BY THE APPLICABLE REGULATORY AUTHORITY; (iii) MAKE QUALIFIED PERSONNEL AVAILABLE FOR INTERVIEWS; AND (iv) NOT SEEK PROTECTIVE ORDERS OR CONFIDENTIAL TREATMENT THAT WOULD PREVENT CUSTOMER FROM SATISFYING ITS REGULATORY OBLIGATIONS, EXCEPT WITH CUSTOMER'S PRIOR WRITTEN CONSENT. VENDOR ACKNOWLEDGES THAT THREE (3) OF THE FOURTEEN (14) COVERED FACILITIES ARE LOCATED IN NEW JERSEY AND ARE SUBJECT TO THE NJ ACT, INCLUDING MANDATORY INDEPENDENT ANNUAL AUDITS WITH REPORTS AVAILABLE TO THE NJ DEPARTMENT OF HEALTH.
>
> (g) **Cost Allocation.** VENDOR SHALL BEAR THE COST OF THE ANNUAL INDEPENDENT AUDIT TO THE EXTENT REQUIRED FOR COMPLIANCE WITH THE NJ AI IN HEALTHCARE TRANSPARENCY ACT. CUSTOMER SHALL BEAR THE COST OF ANY ADDITIONAL OR AD HOC AUDITS BEYOND THE ANNUAL COMPLIANCE AUDIT; PROVIDED THAT IF AN AD HOC OR TIER 3 AUDIT IS TRIGGERED BY VENDOR NON-COMPLIANCE OR CONFIRMS A MATERIAL DEFICIENCY, VENDOR SHALL BEAR THE FULL COST THEREOF.
>
> **§10.4 Anti-Waiver.** NO PROVISION OF THIS AGREEMENT SHALL BE CONSTRUED TO WAIVE, LIMIT, OR CONDITION CUSTOMER'S RIGHTS OR OBLIGATIONS UNDER THE NJ AI IN HEALTHCARE TRANSPARENCY ACT OR ANY COMPARABLE STATE OR FEDERAL LAW IN A MANNER THAT WOULD PREVENT CUSTOMER FROM SATISFYING ITS STATUTORY OBLIGATIONS.
>
> **Exhibit H — Independent Auditor Engagement Terms.** [Reinstate the Customer redline Exhibit H, incorporating the Tier 2 / Tier 3 framework, Langford confidentiality protocols, designated recipients (Dr. Narayanan; Mr. Delgado), and regulatory cooperation terms set forth above.]

#### C. Negotiation Rationale and Fallback Ladder

**Why this landing zone.** The Langford tiered framework is the landing zone endorsed by both the Contested Terms Matrix and the Delgado intelligence, and it is the only structure that simultaneously (i) satisfies the NJ Act's mandatory annual-audit scope (§5(b)), (ii) respects the CTO's "hard no" on raw model-weight access (Tier 3 uses a secure enclave with no extraction — the auditor reviews weights *within* a controlled environment from which no data can be removed), and (iii) preserves Vendor's trade-secret protections (NDA, secure-environment-only, mandatory work-product destruction). The proposal reframes audit rights as a **regulatory compliance baseline** rather than a commercial preference — per the Whitfield Ames NJ Act compliance brief, the Act's anti-waiver provision means the Vendor cannot contractually prevent Meridian from accessing the documentation and audit rights necessary for compliance.

**Key concessions to the Vendor.** (i) Annual (not quarterly) independent audit cadence — the quarterly *transparency reports* (Vendor-prepared, informational) provide ongoing visibility, while the rigorous independent audit is annual (matching the NJ Act minimum and the Vendor's position). (ii) Tier 2 access does not require raw model weights — addressing the CTO's hard no for routine audits. (iii) Vendor bears only the NJ Act compliance audit cost; Customer bears additional/ad hoc audits. (iv) Vendor retains reasonable approval of substitute auditors and NDA form.

**Fallback ladder:**

| Position | Audit Cadence | Access Level | Cost | When to Deploy |
|---|---|---|---|---|
| **A (Primary)** | Annual independent (Tier 2) + Tier 3 for cause + quarterly transparency reports | Tier 2 baseline; Tier 3 secure-enclave for cause | Vendor bears NJ Act audit; Customer bears additional | Opening compromise |
| **B (First fallback)** | Annual independent (Tier 2 "lite": architecture + provenance + validation + bias + incidents — the NJ Act §5(b) minimum) + Tier 3 for cause; semi-annual transparency reports | Tier 2-lite; Tier 3 for cause | 50/50 cost-sharing on annual audit | If Vendor resists full Tier 2 scope |
| **C (Second fallback)** | Annual independent at NJ Act statutory minimum scope (§5(b) elements) with secure-enclave review; Tier 3 for cause only | NJ Act §5(b) minimum; Tier 3 for cause | Vendor bears NJ Act audit; Customer bears excess | If Vendor resists any Tier 2 beyond statutory minimum |
| **Floor** | Annual independent audit at NJ Act §5(b) minimum scope; Tier 3 available for cause/regulatory; reports to NJ DOH | Must include architecture docs, provenance, validation, bias, incidents, data governance | — | If Vendor refuses NJ Act minimum → non-compliant; deal at risk (anti-waiver) |

#### D. Acceptability Analysis for the Vendor Team

**Sandra Hu (precedent / commercial flexibility).** Hu privately acknowledged that Cognitive Foundry can likely accept a qualified third-party audit with scope defined in advance and a mutually agreed auditor. **Response:** (i) Langford is already pre-approved by both parties — the auditor-identity question is resolved; (ii) Tier 2 access is the Langford framework's standard annual-compliance tier and does not require raw model weights, directly addressing the CTO's hard no; (iii) the annual cadence matches the Vendor's own position and the NJ Act minimum; (iv) the secure-enclave, NDA, no-extraction, and mandatory-destruction protocols provide trade-secret protection equivalent to or stronger than the Vendor's standard auditor NDA. Frame the proposal as implementing the framework Hu already signaled is acceptable.

**Rafael Bowen / CTO (trade-secret protection).** The CTO's hard no on raw model weights is the principal obstacle. **Response:** (i) Tier 2 (routine annual) does not touch model weights at all — it covers architecture *documentation*, provenance, validation, test queries, bias, and incidents, all of which are necessary for the NJ Act audit and none of which require weight disclosure; (ii) Tier 3 (cause-based only) uses a secure computational enclave with no data extraction — the auditor reviews weights *within* a controlled environment from which no data can be copied, downloaded, or removed, eliminating the reverse-engineering risk that motivates the CTO's objection; (iii) the NJ Act's anti-waiver provision means that, regardless of contract terms, Meridian must be able to access the documentation and audit rights necessary for compliance — a contract that blocks this is unenforceable as to the three New Jersey facilities. The proposal gives the Vendor a *controlled, protected* path to compliance rather than leaving the issue to be imposed by regulation or litigation. Emphasize that operating under two audit frameworks (one for NJ, one for the other 11 facilities) creates administrative complexity and compliance-gap risk — uniform Tier 2/Tier 3 rights across all 14 facilities is operationally cleaner and positions Meridian for anticipated DE/PA legislation.

#### E. Regulatory and Compliance Constraints

- **NJ AI in Healthcare Transparency Act (S.2314).** §5(b) mandates the annual audit cover model architecture documentation, training data provenance, validation results, bias/fairness, incident reports, and data governance — all captured in Tier 2 access. §5(c) requires audit reports within 90 days of audit-period close and production to NJ DOH within 15 business days of request. §7(a) requires the contract to include documentation access, audit rights, data governance terms, and regulatory cooperation. §7(b) anti-waiver provision renders unenforceable any term blocking compliance. The first mandatory audit must be completed by January 6, 2027 (12 months after go-live); audit fieldwork should commence no later than Q4 2026. The Vendor's June 30 scope (bias/fairness + aggregate accuracy + governance summary) **fails** §5(b)(1)–(2) and (4) and is non-compliant.
- **HIPAA.** Tier 2 access to training data provenance and validation datasets must be coordinated with the BAA; de-identified validation datasets constructed from Meridian EHR data must comply with HIPAA de-identification standards (Exhibit D §3.3). Langford's no-extraction protocol supports HIPAA compliance.
- **FDA.** The annual audit's regulatory-compliance component (Langford §3.6) assesses each ClinIQ™ module against the 21st Century Cures Act § 3060 exemption criteria — particularly relevant to the radiology module's interaction with medical imaging. The audit framework accommodates evolving FDA guidance without contract amendment.
- **Multi-state expansion.** Comparable legislation is pending in Delaware (H.B. 412) and Pennsylvania. Uniform Tier 2/Tier 3 rights across all 14 facilities position Meridian for compliance with anticipated future legislation without amendment.

---

### PROPOSAL 3 — TERMINATION FOR CONVENIENCE / ETF / TRANSITION ASSISTANCE

**Priority Rank: 3 | Agreement §14.3–14.6; §2.5 (portability); Exhibit B §6–7 | Matrix Term 7 | Related: §6.2 (IP), §14.6 (data return)**

#### A. Positions Summary

| Component | Vendor Opening (Jun 6) | Customer Counter (Jun 20) | Vendor Response (Jun 30) |
|---|---|---|---|
| Convenience termination | Mutual written agreement only (no unilateral) | 120 days notice; no ETF | 180 days notice; **50% ETF** (flat) |
| Transition period | 12 months; standard rates + 15% surcharge | 18 months; at-cost (no margin) | 12 months; standard rates + 10% premium; **Customer pays ARF during transition** |
| Data return | 60 days; FHIR/HL7 | 30 days; FHIR R4 + HL7 v2; Customer Derivative Data | 60 days; FHIR R4 + HL7 v2; **no Customer Derivative Data**; Aggregated/Derivative Data retained as Vendor IP |
| ETF structure | 75% of remaining contract value | None | 50% flat (graduated 50/25/0 reportedly available) |

**Gap.** The Vendor's June 30 counter introduces a 50% flat ETF and requires Customer to continue paying the Annual Recurring Fee during the transition period (in addition to transition-service rates) — a structure that creates economic lock-in. The strategic intelligence indicates the CFO is amenable to a **graduated ETF (50% Year 1 / 25% Year 2 / 0% Years 3–4)**, which satisfies Dr. Narayanan's red line (exit is not economically prohibitive by Year 3). The transition and data-export terms must travel with any ETF concession.

#### B. Proposed Compromise Clause Language (Redline-Ready)

> **§14.3 Termination for Convenience.**
>
> (a) **Customer Termination for Convenience.** CUSTOMER MAY TERMINATE THIS AGREEMENT FOR CONVENIENCE AT ANY TIME UPON ONE HUNDRED FIFTY (150) DAYS' PRIOR WRITTEN NOTICE TO VENDOR, SUBJECT TO PAYMENT OF A GRADUATED EARLY TERMINATION FEE (THE "ETF") CALCULATED AS A PERCENTAGE OF THE REMAINING UNPAID ANNUAL RECURRING FEES THAT WOULD HAVE BEEN PAYABLE OVER THE BALANCE OF THE THEN-CURRENT INITIAL TERM:
>
> | Termination Effective During | ETF (% of Remaining Unpaid ARF) |
> |---|---|
> | Contract Year 1 | 50% |
> | Contract Year 2 | 25% |
> | Contract Year 3 or 4 | 0% (no ETF) |
>
> THE ETF IS PAYABLE WITHIN THIRTY (30) DAYS OF THE EFFECTIVE DATE OF TERMINATION. THE ETF REFLECTS A REASONABLE ESTIMATE OF VENDOR'S UNRECOVERED IMPLEMENTATION COSTS AND LOST REVENUE ASSOCIATED WITH EARLY TERMINATION AND IS NOT A PENALTY. CUSTOMER'S SOLE FINANCIAL OBLIGATIONS UPON TERMINATION FOR CONVENIENCE SHALL BE (i) ALL FEES ACCRUED THROUGH THE EFFECTIVE DATE OF TERMINATION, (ii) THE ETF (IF ANY), AND (iii) TRANSITION PERIOD COSTS AT THE RATES SPECIFIED IN SECTION 14.5(c).
>
> (b) **No Vendor Termination for Convenience.** VENDOR SHALL NOT HAVE THE RIGHT TO TERMINATE THIS AGREEMENT FOR CONVENIENCE DURING THE INITIAL TERM OR ANY RENEWAL TERM.
>
> **§14.5 Transition Assistance.** UPON EXPIRATION OR TERMINATION OF THIS AGREEMENT FOR ANY REASON, VENDOR SHALL PROVIDE TRANSITION ASSISTANCE SERVICES TO CUSTOMER FOR A PERIOD OF UP TO FIFTEEN (15) MONTHS FOLLOWING THE EFFECTIVE DATE OF TERMINATION (THE "TRANSITION PERIOD"), SUBJECT TO THE FOLLOWING:
>
> (a) **Scope.** TRANSITION ASSISTANCE SHALL INCLUDE: (i) continued operation of the Platform for Customer's use during the Transition Period; (ii) full cooperation in migrating Customer Data and Outputs to a successor platform or in-house system; (iii) export of all Customer Data in FHIR R4 and HL7 v2 interoperable formats and such other industry-standard formats as Customer may reasonably request; (iv) maintained API access for Customer's integration systems (MeridianConnect, Philips PACS, BD Pyxis) throughout the Transition Period to avoid clinical workflow disruptions; (v) knowledge transfer sessions (minimum eight (8) sessions of four (4) hours each) for Customer's technical and clinical staff; and (vi) reasonable assistance in validating the successor platform's integration with Customer's systems.
>
> (b) **Transition Fees.** VENDOR SHALL PROVIDE ALL TRANSITION ASSISTANCE SERVICES DURING THE TRANSITION PERIOD AT VENDOR'S ACTUAL, DOCUMENTED COST PLUS A FIVE PERCENT (5%) ADMINISTRATIVE OVERHEAD. CUSTOMER SHALL NOT BE REQUIRED TO PAY THE ANNUAL RECURRING FEE DURING ANY PORTION OF THE TRANSITION PERIOD FOLLOWING THE EFFECTIVE DATE OF TERMINATION. FOR THE AVOIDANCE OF DOUBT, VENDOR SHALL NOT CHARGE EARLY TERMINATION FEES, WIND-DOWN FEES, OR ANY OTHER PENALTY IN CONNECTION WITH TRANSITION ASSISTANCE BEYOND THE ETF (IF ANY) PROVIDED IN SECTION 14.3(a).
>
> (c) **Continued Obligations.** DURING THE TRANSITION PERIOD, ALL TERMS AND CONDITIONS OF THIS AGREEMENT SHALL REMAIN IN FULL FORCE AND EFFECT, INCLUDING VENDOR'S OBLIGATIONS UNDER ARTICLE 5 (DATA GOVERNANCE), ARTICLE 9 (SLAs), ARTICLE 10 (TRANSPARENCY AND AUDIT), ARTICLE 12 (LIMITATION OF LIABILITY), AND ARTICLE 13 (INDEMNIFICATION).
>
> **§14.6 Data Return and Destruction.** WITHIN FORTY-FIVE (45) CALENDAR DAYS FOLLOWING THE EFFECTIVE DATE OF TERMINATION OR EXPIRATION (OR THE END OF THE TRANSITION PERIOD, IF APPLICABLE), VENDOR SHALL, AT CUSTOMER'S WRITTEN ELECTION:
>
> (a) **Return.** RETURN TO CUSTOMER ALL CUSTOMER DATA AND OUTPUTS IN VENDOR'S POSSESSION OR CONTROL, IN FHIR R4, HL7 v2, AND SUCH OTHER INTEROPERABLE, INDUSTRY-STANDARD FORMATS AS CUSTOMER MAY REASONABLY SPECIFY; OR
>
> (b) **Destruction.** CERTIFY TO CUSTOMER IN WRITING, EXECUTED BY AN OFFICER OF VENDOR AT THE LEVEL OF VICE PRESIDENT OR ABOVE, THE COMPLETE AND IRREVERSIBLE DESTRUCTION OF ALL CUSTOMER DATA IN VENDOR'S POSSESSION, CUSTODY, OR CONTROL, INCLUDING ALL COPIES, BACKUPS, AND ARCHIVES, IN ACCORDANCE WITH NIST SPECIAL PUBLICATION 800-88 (GUIDELINES FOR MEDIA SANITIZATION) OR AN EQUIVALENT STANDARD. SUCH CERTIFICATION SHALL BE PROVIDED WITHIN FIVE (5) BUSINESS DAYS OF COMPLETION.
>
> (c) **PHI Retention.** VENDOR MAY RETAIN COPIES OF CUSTOMER DATA CONTAINING PHI ONLY AS REQUIRED BY APPLICABLE LAW OR REGULATION, AND ONLY FOR THE MINIMUM RETENTION PERIOD REQUIRED. ANY RETAINED PHI SHALL REMAIN SUBJECT TO THE BAA (EXHIBIT F) AND THE CONFIDENTIALITY OBLIGATIONS OF THIS AGREEMENT IN PERPETUITY.

#### C. Negotiation Rationale and Fallback Ladder

**Why this landing zone.** The graduated ETF (50/25/0) is the landing zone endorsed by the Delgado intelligence (CFO openness) and the Sutter guidance (workable framework; not economically prohibitive). By Year 3, the ETF is zero — Customer may exit at no cost, satisfying Dr. Narayanan's red line. The 150-day notice period bridges Customer's 120-day opening and the Vendor's 180-day counter while giving the Vendor reasonable planning time. The transition package (15 months at cost + 5%; no ARF during transition; full scope including API access and knowledge transfer) ensures that the ETF does not become a lock-in mechanism — Customer can exit and migrate without paying the full subscription again. The 45-day data-return window bridges Customer's 30-day opening and the Vendor's 60-day counter (the Vendor has represented that 30 days is operationally infeasible across 14 facilities; 45 days is the stated minimum).

**Playbook escalation note.** The Playbook (§9.4 and the escalation matrix) provides that any ETF — regardless of structure, amount, or graduation — must be escalated to the General Counsel for review, with presumptive rejection. The graduated ETF is therefore presented as the **recommended landing zone subject to General Counsel approval**, not as a position the deal team can accept unilaterally. The General Counsel's red line (exit not economically prohibitive at any point) is satisfied: the Year 1 ETF (50% of remaining ARF) is a meaningful but not prohibitive charge that declines to zero by Year 3. If the General Counsel declines to approve any ETF, Position B (no ETF) is the fallback.

**Fallback ladder:**

| Position | Notice | ETF | Transition | Data Return | When to Deploy |
|---|---|---|---|---|---|
| **A (Primary)** | 150 days | Graduated 50/25/0 [GC approval] | 15 months; cost + 5%; no ARF | 45 days; FHIR R4 + HL7 v2 | Opening compromise |
| **B (No-ETF fallback)** | 150 days | None | 18 months; cost + 5%; no ARF | 30 days; FHIR R4 + HL7 v2 | If GC rejects any ETF, or if Vendor rejects graduated ETF |
| **C (Capped-ETF fallback)** | 150 days | Capped graduated (25% Y1 / 0% Y2–4) | 18 months; cost + 5%; no ARF | 30 days; FHIR R4 + HL7 v2 | If Vendor insists on some ETF but GC caps it |
| **Floor** | ≤180 days | No ETF that makes exit economically prohibitive at any point | At-cost (≤ cost + 5%); no ARF during transition | ≤60 days; FHIR R4 + HL7 v2 mandatory | If Vendor demands flat ETF + ARF-during-transition lock-in → escalate to GC |

#### D. Acceptability Analysis for the Vendor Team

**Sandra Hu (commercial terms / revenue protection).** Hu's principal concern is revenue-recognition impact and the precedent of a no-ETF convenience-termination right. **Response:** (i) the graduated ETF provides meaningful revenue protection in the early years (50% Year 1, 25% Year 2) when the Vendor's unrecovered implementation costs are highest — directly addressing the CFO's revenue-recognition concern; (ii) the ETF declines to zero by Year 3, by which point the Vendor has recovered its implementation investment and earned substantial recurring revenue; (iii) the 150-day notice period gives the Vendor a full quarter-plus to plan resource reallocation; (iv) this structure is more favorable to the Vendor than the Customer's no-ETF opening and is a substantial concession that should be reciprocated on transition terms. Frame the graduated ETF as the compromise that lets the Vendor book the deal without the revenue-recognition risk of a pure no-ETF structure.

**Rafael Bowen (transition economics / data).** Bowen may object to the at-cost-plus-5% transition pricing and the no-ARF-during-transition term. **Response:** (i) the transition pricing (cost + 5%) is modestly above the Customer's at-cost opening and well below the Vendor's standard-rates-plus-10% counter — it covers the Vendor's incremental cost without creating a profit center from a departing customer; (ii) requiring Customer to pay the full ARF *during* transition (the Vendor's June 30 position) is a double-charge that converts the transition into a lock-in mechanism — the cost + 5% structure is the industry-standard approach for healthcare-IT transitions of this complexity; (iii) the 15-month duration reflects the genuine complexity of migrating 6,200 users across 14 facilities with three integration points (Epic, PACS, Pyxis) — a shorter window creates clinical-continuity risk that neither party wants; (iv) the data-return terms (FHIR R4 + HL7 v2, NIST SP 800-88) are non-negotiable per the Playbook red line and are consistent with the Vendor's own June 30 acceptance of FHIR R4 + HL7 v2 export. Emphasize that the transition package is what makes the graduated ETF acceptable to Meridian's governance — the two terms travel together.

#### E. Regulatory and Compliance Constraints

- **HIPAA.** §14.6(c) preserves the BAA's PHI-retention and destruction requirements. Data return in FHIR R4 / HL7 v2 supports Meridian's medical-record retention obligations. The 45-day window is coordinated with the BAA's termination provisions.
- **NJ AI in Healthcare Transparency Act.** Upon termination, Meridian must retain audit records and documentation for the three New Jersey facilities for the Act's retention period. The transition-period continued obligations (§14.5(c)) preserve audit and transparency rights during wind-down, ensuring no compliance gap. Data-return terms must preserve the audit trail required by the Act.
- **FDA.** Transition assistance must preserve the regulatory documentation (validation records, adverse-event logs) necessary for Meridian's ongoing FDA obligations following termination. The data-export scope (§14.5(a)(iii)) includes audit logs and metadata.
- **Data portability (cross-reference Proposal 6).** The §14.6 data-return obligation covers Customer Data and Outputs. The portability of fine-tuned model artifacts is addressed in Proposal 6 (irrevocable perpetual license + portability). The two proposals are complementary — §14.6 returns the data; Proposal 6 secures the ongoing right to use the derivative outputs.

---

### PROPOSAL 4 — AGGREGATED / DE-IDENTIFIED DATA USAGE RIGHTS

**Priority Rank: 4 | Agreement §5.4; Exhibit D (data governance) | Matrix Term 4 | Related: §5.1, §5.3, §6.1, §10.1 (transparency)**

#### A. Positions Summary

| Component | Vendor Opening (Jun 6) | Customer Counter (Jun 20) | Vendor Response (Jun 30) |
|---|---|---|---|
| Permitted use | Unrestricted (model training, benchmarking, product development, commercial) | None without per-use-case consent | Model improvement + new products + research + benchmarking + publications |
| Opt-out window | 90 days (standard) | 30-day withdrawal | 60 days |
| Deletion scope | Prospective only | Verified deletion within 30 days, including incorporated data | Prospective only; delete unincorporated data only; incorporated data "technically inseparable" |
| Sale to third parties | Permitted (implied) | Prohibited | Prohibited (agreed) |

**Gap.** Data usage is the Vendor's **highest-priority commercial term** — the aggregated, de-identified data from Meridian's 14-hospital network (~2.1M annual encounters) is highly valuable to Cognitive Foundry's model-training pipeline. Per the Delgado intelligence and the Playbook, this is Meridian's primary **concession currency**: calibrated flexibility here should be deployed in exchange for Vendor movement on Priorities 1–3. The hard red lines are (i) no unrestricted use, (ii) opt-out window ≤30 days (Playbook; exceeding requires VP/GC escalation), and (iii) no purely prospective-only deletion without an alternative mechanism.

#### B. Proposed Compromise Clause Language (Redline-Ready)

> **§5.4 Aggregated and De-Identified Data Use.**
>
> (a) **Permitted Use.** SUBJECT TO VENDOR'S COMPLIANCE WITH THE DE-IDENTIFICATION STANDARDS IN SECTION 5.3, VENDOR MAY USE, PROCESS, AND INCORPORATE AGGREGATED DATA AND DE-IDENTIFIED DATA (EACH AS DEFINED IN SECTION 1.2 AND EXHIBIT D) DERIVED FROM CUSTOMER DATA SOLELY FOR THE PURPOSES OF (i) IMPROVING, TRAINING, AND ENHANCING THE PLATFORM AND VENDOR'S AI/ML MODELS, AND (ii) INTERNAL BENCHMARKING OF MODEL PERFORMANCE. FOR THE AVOIDANCE OF DOUBT, AGGREGATED DATA AND DE-IDENTIFIED DATA HAVE BEEN DE-IDENTIFIED IN COMPLIANCE WITH 45 C.F.R. § 164.514(a)–(c) AND DO NOT CONSTITUTE PHI. VENDOR SHALL NOT USE AGGREGATED DATA OR DE-IDENTIFIED DATA FOR THE DEVELOPMENT OF SEPARATELY MARKETED PRODUCTS OR SERVICES, FOR COMMERCIAL SALE, OR FOR PUBLICATIONS OR REPORTS THAT IDENTIFY OR COULD REASONABLY BE USED TO IDENTIFY CUSTOMER, ANY PATIENT, OR ANY COVERED FACILITY, WITHOUT CUSTOMER'S PRIOR WRITTEN CONSENT ON A PER-USE-CASE BASIS.
>
> (b) **Aggregation Standard.** AGGREGATED DATA SHALL MEET THE DEFINITION IN SECTION 1.2 AND SHALL, AT A MINIMUM, BE COMBINED WITH DATA DERIVED FROM AT LEAST TWO (2) OTHER UNAFFILIATED VENDOR CUSTOMERS OR OTHER SOURCES SUCH THAT CUSTOMER'S CONTRIBUTION IS NOT SEPARATELY EXTRACTABLE OR IDENTIFIABLE. THE BURDEN OF DEMONSTRATING COMPLIANCE WITH THIS AGGREGATION STANDARD AND THE APPLICABLE DE-IDENTIFICATION METHOD SHALL BE ON VENDOR.
>
> (c) **Opt-Out Right.** CUSTOMER MAY ELECT TO OPT OUT OF VENDOR'S USE OF AGGREGATED DATA AND DE-IDENTIFIED DATA UNDER SUBSECTION (a) BY PROVIDING WRITTEN NOTICE TO VENDOR. ANY OPT-OUT NOTICE SHALL BE EFFECTIVE THIRTY (30) DAYS FOLLOWING VENDOR'S RECEIPT THEREOF. THE OPT-OUT RIGHT IS NOT SUBJECT TO CURE PERIODS, CONSENT REQUIREMENTS, OR ANY OTHER CONDITION, AND MAY BE EXERCISED AT ANY TIME.
>
> (d) **Effect of Opt-Out.** UPON THE EFFECTIVE DATE OF AN OPT-OUT NOTICE, VENDOR SHALL: (i) CEASE ALL NEW USE OF AGGREGATED DATA AND DE-IDENTIFIED DATA DERIVED FROM CUSTOMER DATA FOR THE PERMITTED PURPOSES; (ii) DELETE ALL AGGREGATED DATA AND DE-IDENTIFIED DATA DERIVED FROM CUSTOMER DATA THAT HAS NOT YET BEEN INCORPORATED INTO TRAINED MODELS OR DERIVATIVE WORKS, AND CERTIFY SUCH DELETION IN WRITING WITHIN SIXTY (60) DAYS; AND (iii) WITH RESPECT TO AGGREGATED DATA AND DE-IDENTIFIED DATA ALREADY INCORPORATED INTO TRAINED MODELS OR DERIVATIVE WORKS, EITHER (A) RETRAIN THE AFFECTED MODELS TO EXCLUDE CUSTOMER-DERIVED DATA WITHIN TWELVE (12) MONTHS OF THE OPT-OUT EFFECTIVE DATE, OR (B) IF VENDOR DEMONSTRATES IN WRITING, WITH REASONABLE TECHNICAL DETAIL, THAT RETRAINING IS TECHNICALLY OR COMMERCIALLY INFEASIBLE, IMPLEMENT DOCUMENTED ALTERNATIVE MITIGATION MEASURES (WHICH MAY INCLUDE DIFFERENTIAL PRIVACY TECHNIQUES, MODEL ISOLATION, OR CONTRACTUAL RESTRICTIONS ON THE USE OF CUSTOMER-INFLUENCED MODEL CAPABILITIES FOR CUSTOMER-IDENTIFIABLE BENEFIT) SUBJECT TO CUSTOMER'S REASONABLE APPROVAL. VENDOR SHALL PROVIDE AN OFFICER CERTIFICATION OF COMPLIANCE WITH THIS SUBSECTION WITHIN FIVE (5) BUSINESS DAYS OF COMPLETION.
>
> (e) **No Sale.** VENDOR SHALL NOT SELL AGGREGATED DATA OR DE-IDENTIFIED DATA TO THIRD PARTIES. VENDOR MAY SHARE AGGREGATED DATA AND DE-IDENTIFIED DATA WITH SUBPROCESSORS SOLELY FOR THE PERMITTED PURPOSES DESCRIBED IN SUBSECTION (a), SUBJECT TO CONFIDENTIALITY OBLIGATIONS NO LESS PROTECTIVE THAN THOSE SET FORTH IN ARTICLE 11.
>
> (f) **Transparency and Documentation.** VENDOR SHALL DOCUMENT EACH USE OF AGGREGATED DATA AND DE-IDENTIFIED DATA DERIVED FROM CUSTOMER DATA IN THE QUARTERLY TRANSPARENCY REPORT UNDER SECTION 10.1, INCLUDING THE USE CASE, DATA CATEGORIES, AND AGGREGATION METHODOLOGY. VENDOR SHALL UPDATE TRAINING DATA PROVENANCE RECORDS TO REFLECT THE INCLUSION OF CUSTOMER-DERIVED AGGREGATED DATA, CONSISTENT WITH THE NJ AI IN HEALTHCARE TRANSPARENCY ACT.
>
> (g) **No Implied License.** NOTHING IN THIS AGREEMENT GRANTS VENDOR ANY IMPLIED LICENSE OR RIGHT TO USE CUSTOMER DATA, AGGREGATED DATA, OR DE-IDENTIFIED DATA EXCEPT AS EXPRESSLY SET FORTH IN THIS SECTION 5.4. THE PARTIES ACKNOWLEDGE THAT CUSTOMER'S DATA ASSETS, INCLUDING DE-IDENTIFIED AND AGGREGATED DATASETS REFLECTING THE CLINICAL EXPERIENCE OF FOURTEEN (14) HOSPITALS AND APPROXIMATELY 2.1 MILLION ANNUAL PATIENT ENCOUNTERS, ARE COMMERCIALLY VALUABLE AND PROPRIETARY TO CUSTOMER.

#### C. Negotiation Rationale and Fallback Ladder

**Why this landing zone.** The proposal grants the Vendor its core need — the right to use aggregated, de-identified data for model improvement and benchmarking — which is the highest-value term to Cognitive Foundry. This is the concession that should be deployed in exchange for Vendor movement on Priorities 1–3 (patient-safety super-cap scope, audit rights, and the graduated ETF). The proposal holds the Playbook red lines: (i) use is limited to model improvement + benchmarking (not product development, commercial sale, or identifying publications — those require per-use-case consent); (ii) the opt-out window is 30 days (Playbook position); (iii) deletion is not purely prospective — the Vendor must either retrain affected models within 12 months or implement documented alternative mitigation measures, addressing the "technically infeasible" concern with a real remedy rather than accepting zero obligation for incorporated data.

**Strategic deployment.** Hold the Customer's opening position (no use without per-use-case consent) through the early rounds. Introduce the §5.4(a) permitted-use concession only after securing movement on Priority 1 (super-cap scope) and Priority 2 (audit rights). The opt-out window (30 vs. 45 vs. 60 days) and the deletion mechanism (retraining vs. alternative mitigation) are the secondary levers — concede on the opt-out window (toward 45–60 days with VP/GC approval) only if needed to close, but hold the deletion-mechanism red line.

**Fallback ladder:**

| Position | Permitted Use | Opt-Out | Deletion of Incorporated Data | When to Deploy |
|---|---|---|---|---|
| **A (Primary)** | Model improvement + benchmarking only | 30 days | Retrain within 12 months OR documented alternative mitigation | Opening compromise (deploy after P1/P2 movement) |
| **B (First fallback)** | Model improvement + benchmarking + internal research (not commercial/publications) | 45 days [VP approval] | Prospective cessation + documented alternative mitigation (no retraining mandate) | If Vendor resists retraining mandate |
| **C (Second fallback)** | Model improvement + benchmarking + product development (excluding sale/identifying publications) | 60 days [GC approval] | Prospective cessation + deletion of unincorporated data + annual transparency report of uses | If Vendor demands broader use + longer opt-out |
| **Floor** | No unrestricted use; no sale; HIPAA de-id + ≥2-customer aggregation | Opt-out mechanism exists | Some remedy for incorporated data (not pure prospective-only with zero obligation) | If Vendor demands unrestricted use + prospective-only deletion + no alternative → escalate to GC |

#### D. Acceptability Analysis for the Vendor Team

**Sandra Hu (commercial value / data pipeline).** Data usage is the Vendor's highest-priority term. Hu will push for the broadest permitted-use scope and the longest opt-out window. **Response:** (i) the proposal grants the Vendor's core need — model improvement and benchmarking use of aggregated, de-identified data — which is the use that drives the model-training pipeline value; (ii) the exclusion of product development, commercial sale, and identifying publications (without per-use-case consent) protects Meridian's commercial interest in its proprietary data assets while leaving the Vendor's primary research-and-development use intact; (iii) the 30-day opt-out is the Playbook position and is consistent with healthcare-industry data-governance norms; (iv) this is a substantial concession from Meridian's no-use-without-consent opening and should be treated as the quid pro quo for Vendor concessions on patient-safety liability and audit rights. Frame the data-usage grant as the deal's value exchange — Meridian gives the Vendor its most-valued commercial term in exchange for the Vendor accepting the patient-safety and audit terms Meridian most needs.

**Rafael Bowen (deletion feasibility / IP).** Bowen will argue that retraining models to exclude Customer-derived data is technically infeasible (would require retraining from scratch) and that the incorporated data is "technically inseparable" from the model. **Response:** (i) the proposal does not mandate immediate retraining — it provides a 12-month window and, critically, an **alternative-mitigation path** (differential privacy, model isolation, contractual restrictions) if retraining is genuinely infeasible, with the burden of demonstrating infeasibility on the Vendor; (ii) this is the Playbook's prescribed approach to the "infeasible deletion" objection — it does not accept the Vendor's position that incorporated data is simply exempt from any remedy; (iii) the alternative-mitigation measures are flexible and can be tailored to the Vendor's technical architecture; (iv) the aggregation standard (≥2 unaffiliated customers) and the de-identification burden on the Vendor protect against re-identification risk. Emphasize that a purely prospective-only deletion with zero obligation for incorporated data is a Playbook red line — the alternative-mitigation mechanism is the compromise that gives the Vendor a feasible path while preserving Meridian's data-governance rights.

#### E. Regulatory and Compliance Constraints

- **HIPAA.** De-identification must satisfy the Safe Harbor method (45 C.F.R. § 164.514(b)(2)) or Expert Determination method (§ 164.514(b)(1)); the burden is on the Vendor (§5.4(b)). The aggregation standard (≥2 unaffiliated customers) and the no-re-identification covenant (§5.3) support HIPAA compliance. The BAA (Exhibit F) controls on PHI-specific conflicts; the data-governance terms in Exhibit D must be coordinated with the BAA.
- **NJ AI in Healthcare Transparency Act.** §5.4(f) requires the Vendor to document data uses in the quarterly transparency report and update training data provenance records — directly supporting the Act's documentation and audit requirements (§5(b)(1)–(2)). The aggregation and de-identification standards support the Act's data-governance requirements. Any use of Customer-derived data in model training must be reflected in the audit trail available to the NJ DOH.
- **State law (DE, PA, NJ).** The proposal preserves Meridian's compliance with state data-privacy and breach-notification laws. The opt-out mechanism supports Meridian's patient-data-governance obligations. Anticipated DE/PA legislation may impose additional restrictions; the §5.4(g) no-implied-license provision preserves Meridian's flexibility to respond.
- **Exhibit D coordination.** The §5.4 terms must be reflected in Exhibit D's data-governance framework (retention limits, use categories, audit trail, four-tier data classification). The order of precedence (BAA > Exhibit D > Agreement) is preserved.

---

### PROPOSAL 5 — SLA / AI ACCURACY BENCHMARKS

**Priority Rank: 5 | Agreement §9.1–9.4; Exhibit D (SLA) | Matrix Term 6 | Related: §10.1 (transparency), §14.7 (performance termination)**

#### A. Positions Summary

| Component | Vendor Opening (Jun 6) | Customer Counter (Jun 20) | Vendor Response (Jun 30) |
|---|---|---|---|
| Accuracy benchmarks | Informational only; commercially reasonable efforts | Binding (Sepsis 92/88; Radiology 90/85; Med 95/90) | Non-binding "Performance Targets" (same numbers) |
| Credits for accuracy misses | None | Escalating 5%/10%/15% of quarterly fees | None |
| Termination for accuracy | None | After 2 consecutive misses | None |
| Uptime | 99.5%; credits capped 10% | 99.9%; credits 5/10/15 | 99.5%; credits 5/10/15 capped 15%; sole remedy |
| Measurement | Not specified | Quarterly; NIST AI 100-1; 95% CI | Quarterly informational report within 45 days |

**Gap.** The Vendor's June 30 position makes accuracy metrics purely informational with no binding obligation, no credits, and no termination right — even though the Vendor uses the *same benchmark numbers* (92/88, 90/85, 95/90) as "targets." The dispute is therefore not about the numbers but about **binding vs. informational** and the **remedies** for persistent underperformance. The Playbook red line is that benchmarks must be binding (not purely informational), with termination no later than 3 consecutive misses.

#### B. Proposed Compromise Clause Language (Redline-Ready)

> **§9.3 AI Model Accuracy — Binding Performance Benchmarks.**
>
> (a) **Binding Benchmarks.** VENDOR WARRANTS THAT THE PLATFORM'S CLINICAL DECISION-SUPPORT MODULES SHALL MEET OR EXCEED THE FOLLOWING MINIMUM PERFORMANCE BENCHMARKS, MEASURED ON A QUARTERLY BASIS USING THE VALIDATION METHODOLOGY SET FORTH IN SUBSECTION (b) (THE "PERFORMANCE BENCHMARKS"):
>
> | Clinical Module | Sensitivity (Minimum) | Specificity (Minimum) |
> |---|---|---|
> | Sepsis Prediction | ≥ 92% | ≥ 88% |
> | Radiology Image Analysis | ≥ 90% | ≥ 85% |
> | Medication Interaction Checking | ≥ 95% | ≥ 90% |
>
> (b) **Measurement Methodology.** PERFORMANCE BENCHMARKS SHALL BE MEASURED QUARTERLY BY THE INDEPENDENT AUDITOR (LANGFORD) AT TIER 2 ACCESS (SECTION 10.3) USING A PROSPECTIVE EVALUATION OF ACTUAL CLINICAL ENCOUNTERS ACROSS THE COVERED FACILITIES, WITH SAMPLE SIZES DETERMINED IN ACCORDANCE WITH NIST AI 100-1 AND REPORTED AT A 95% CONFIDENCE INTERVAL. THE METHODOLOGY SHALL CONTROL FOR PATIENT-POPULATION CHARACTERISTICS, DATA QUALITY, AND CLINICAL-WORKFLOW ADHERENCE. THE PARTIES SHALL AGREE UPON THE DETAILED VALIDATION PROTOCOL IN THE SLA GOVERNANCE COMMITTEE PRIOR TO THE FIRST MEASUREMENT PERIOD.
>
> (c) **Quarterly Reporting.** VENDOR SHALL DELIVER WRITTEN VALIDATION REPORTS WITHIN THIRTY (30) DAYS OF THE END OF EACH CALENDAR QUARTER, INCLUDING SENSITIVITY AND SPECIFICITY METRICS FOR EACH CLINICAL MODULE, SAMPLE SIZE, CONFIDENCE INTERVALS, AND METHODOLOGY DESCRIPTION.
>
> (d) **Escalating Performance Credits.** IN THE EVENT ANY CLINICAL MODULE FAILS TO MEET ITS PERFORMANCE BENCHMARK IN ANY QUARTER, CUSTOMER SHALL BE ENTITLED TO A SERVICE CREDIT CALCULATED AS A PERCENTAGE OF THE QUARTERLY FEES ($2,137,500), GRADUATED BY THE SEVERITY OF THE MISS:
>
> | Magnitude of Miss (below benchmark) | Service Credit (% of Quarterly Fees) |
> |---|---|
> | Up to 2.0 percentage points | 5% ($106,875) |
> | 2.0 to 5.0 percentage points | 10% ($213,750) |
> | More than 5.0 percentage points | 15% ($320,625) |
>
> CREDITS SHALL BE APPLIED PER BENCHMARK PER QUARTER AND ARE IN ADDITION TO (NOT IN LIEU OF) THE UPTIME CREDITS UNDER SECTION 9.2. THE AGGREGATE QUARTERLY CREDIT (UPTIME PLUS ACCURACY) SHALL NOT EXCEED TWENTY PERCENT (20%) OF THE QUARTERLY FEES ($427,500).
>
> (e) **Remediation Plan.** UPON ANY QUARTERLY MISS, VENDOR SHALL DELIVER A WRITTEN REMEDIATION PLAN TO CUSTOMER WITHIN FIFTEEN (15) BUSINESS DAYS, DESCRIBING THE STEPS VENDOR WILL TAKE TO RESTORE PERFORMANCE. CUSTOMER'S CLINICAL INFORMATICS TEAM SHALL APPROVE OR REQUEST REVISIONS TO THE REMEDIATION PLAN WITHIN TEN (10) BUSINESS DAYS. VENDOR SHALL IMPLEMENT THE APPROVED REMEDIATION PLAN PROMPTLY AND AT ITS OWN COST.
>
> (f) **Termination for Persistent Underperformance.** IF ANY CLINICAL MODULE FAILS TO MEET ITS PERFORMANCE BENCHMARK FOR THREE (3) CONSECUTIVE CALENDAR QUARTERS, CUSTOMER MAY TERMINATE THIS AGREEMENT UPON SIXTY (60) DAYS' WRITTEN NOTICE WITHOUT PAYMENT OF ANY EARLY TERMINATION FEE, PURSUANT TO SECTION 14.7, WITH TRANSITION ASSISTANCE UNDER SECTION 14.5.
>
> (g) **Bias and Fairness.** BIAS AND FAIRNESS TESTING METRICS (DEMOGRAPHIC PARITY, EQUALIZED ODDS, DISPARATE-IMPACT ANALYSIS ACROSS PATIENT SUBPOPULATIONS) SHALL BE REPORTED QUARTERLY AS INFORMATIONAL SLA COMPONENTS IN THE TRANSPARENCY REPORT UNDER SECTION 10.1. A STATISTICALLY SIGNIFICANT DISPARATE-IMPACT FINDING SHALL TRIGGER A REMEDIATION PLAN UNDER SUBSECTION (e) AND, IF UNRESOLVED ACROSS TWO (2) CONSECUTIVE QUARTERS, A TIER 3 AUDIT UNDER SECTION 10.3(b).
>
> **§9.1(a) Uptime.** [Accept the Vendor's 99.5% monthly availability commitment, with the Customer redline credit structure (5%/10%/15% of Monthly Fee) and a 15% monthly cap, as set forth in Exhibit D.]
>
> **§9.4 Sole Remedy.** THE SERVICE CREDITS SET FORTH IN SECTION 9.2 (UPTIME) AND SECTION 9.3(d) (ACCURACY) SHALL CONSTITUTE CUSTOMER'S SOLE AND EXCLUSIVE MONETARY REMEDY FOR SERVICE-LEVEL FAILURES, EXCEPT THAT THE TERMINATION RIGHT UNDER SECTION 9.3(f) IS PRESERVED AND NOTHING HEREIN LIMITS CUSTOMER'S RIGHTS UNDER ARTICLE 12 (LIMITATION OF LIABILITY) OR ARTICLE 13 (INDEMNIFICATION) FOR CLAIMS ARISING FROM PATIENT-SAFETY EVENTS OR DATA BREACHES.

#### C. Negotiation Rationale and Fallback Ladder

**Why this landing zone.** The proposal makes the benchmarks **binding** (the Playbook red line) while addressing the Vendor's legitimate concern about AI-accuracy variability through a defined measurement methodology (NIST AI 100-1, 95% CI, prospective evaluation, controls for population/data/workflow factors). The Vendor's June 30 draft already uses the same benchmark numbers — the proposal simply makes them enforceable rather than aspirational. The termination trigger is set at **3 consecutive misses** (the Playbook fallback), conceding from the Customer's 2-miss opening. The escalating credits are graduated by severity (a miss of 0.5pp is not penalized the same as a 6pp miss), which is fairer than the flat 5/10/15 structure and more defensible to the Vendor. Uptime is accepted at the Vendor's 99.5% (conceding the Customer's 99.9% opening) because the binding accuracy benchmarks and termination right are the patient-safety-critical terms.

**Fallback ladder:**

| Position | Binding? | Credits | Termination | Aggregate Cap | When to Deploy |
|---|---|---|---|---|---|
| **A (Primary)** | Binding | 5/10/15 graduated by severity | 3 consecutive misses | 20% quarterly | Opening compromise |
| **B (First fallback)** | Binding | 5/10/15 flat | 3 consecutive misses OR 4 misses in any 12-month period | 15% quarterly | If Vendor resists termination trigger |
| **C (Second fallback)** | Binding with variance tolerance (binding only if miss exceeds 2pp below target for 2+ consecutive quarters, accounting for statistical significance) | 5/10% | 3 consecutive material misses | 15% quarterly | If Vendor resists strict binding |
| **Floor** | Must be binding (not purely informational) | Some credit/fee consequence | Termination right after persistent failure (≤3 consecutive misses) | — | If Vendor insists on purely informational with no remedies → escalate (Playbook red line) |

#### D. Acceptability Analysis for the Vendor Team

**Sandra Hu (commercial remedies / precedent).** Hu's principal objection will be that binding accuracy benchmarks with credits and termination are not Cognitive Foundry's standard and that AI accuracy is inherently variable. **Response:** (i) the Vendor's own June 30 draft uses these exact benchmark numbers as "targets" — the proposal merely makes them enforceable, which is appropriate for a clinical decision-support tool deployed across 14 hospitals where accuracy directly affects patient safety; (ii) the defined measurement methodology (NIST AI 100-1, 95% CI, prospective evaluation, controls) directly addresses the variability concern — a benchmark miss is measured against a statistically rigorous, controlled evaluation, not a raw point-in-time snapshot; (iii) the credits are graduated by severity, so a marginal miss (0.5pp) incurs only a 5% credit while a severe miss (>5pp) incurs 15% — this is proportionate and fair; (iv) the 3-miss termination trigger (conceded from the Customer's 2-miss opening) gives the Vendor a full three quarters to remediate before termination exposure arises, and the remediation-plan process provides a structured cure path; (v) the aggregate quarterly cap (20%) bounds the Vendor's credit exposure. Frame the binding benchmarks as the patient-safety governance requirement that the Board Risk Committee expects for a Tier 1 enterprise-risk deployment.

**Rafael Bowen (liability exposure).** Bowen may object that binding benchmarks create breach exposure beyond the credits. **Response:** (i) §9.4 preserves the credits as the sole *monetary* remedy for service-level failures — binding benchmarks do not open uncapped breach damages; (ii) the termination right is the only non-monetary remedy, and it requires 3 consecutive misses (a high bar); (iii) patient-safety and data-breach claims remain governed by Articles 12 and 13 (the super-cap structure in Proposal 1), not by the SLA — the SLA credits and the liability structure are separate remedial regimes; (iv) the bias/fairness informational component (§9.3(g)) is reported but does not generate credits — it triggers remediation and, if unresolved, a Tier 3 audit, which is a collaborative process rather than a penalty.

#### E. Regulatory and Compliance Constraints

- **NJ AI in Healthcare Transparency Act.** The Act requires performance metrics and bias/fairness testing to be reported (§5(b)(3)) and available for audit. The §9.3 quarterly reporting and §9.3(g) bias/fairness components directly support Act compliance for the three New Jersey facilities. The Langford Tier 2 measurement methodology aligns with the Act's audit framework.
- **HIPAA.** The prospective evaluation of actual clinical encounters (§9.3(b)) uses de-identified or limited-data-set evaluation protocols coordinated with the BAA. The measurement methodology must not expose PHI beyond the permitted purposes.
- **FDA.** The binding benchmarks support Meridian's FDA post-market surveillance obligations for clinical decision-support software. The remediation-plan process (§9.3(e)) aligns with FDA adverse-event response expectations. The radiology module's benchmark (90/85) is particularly relevant given the FDA's heightened scrutiny of AI-enabled medical imaging.
- **Board Risk Committee.** Binding accuracy benchmarks with a termination right are necessary for the Tier 1 enterprise-risk governance framework. A purely informational SLA would not be defensible at the August 4 briefing for a clinical decision-support tool deployed at patient-safety-critical scale.

---

### PROPOSAL 6 — IP OWNERSHIP (MODEL WEIGHTS, FINE-TUNED ADAPTATIONS, DERIVATIVE DATA)

**Priority Rank: 6 | Agreement §6.1–6.5; §2.4–2.5 (licenses) | Matrix Term 2 | Related: §14.6 (data return), Proposal 3 (portability)**

#### A. Positions Summary

| Component | Vendor Opening (Jun 6) | Customer Counter (Jun 20) | Vendor Response (Jun 30) |
|---|---|---|---|
| Model IP ownership | All Vendor (weights, architecture, fine-tuned) | Customer owns fine-tuned weights + Customer Derivative Data; Vendor assigns | All Vendor; fine-tuned "technically inseparable" from base model |
| Output license | Term-only, non-exclusive | Perpetual, royalty-free, survives termination | Perpetual, royalty-free (excludes weights) — **agreed in principle** |
| Portability of fine-tuned layer | None | Full portability of fine-tuned weights | None — model weights "not subject to export, transfer, or portability" |
| Reverse engineering | Prohibited | Prohibited (base model) | Prohibited |

**Gap.** The Vendor's CTO has issued a "hard no" on raw model-weight access or transfer — including fine-tuned weights, which the Vendor characterizes as "technically inseparable" from the base model. The Customer's opening position (Customer ownership of fine-tuned weights) is therefore not achievable. Per the Delgado and Sutter guidance, the right landing zone is the **Playbook final fallback**: Vendor ownership of all model IP, with an **irrevocable, perpetual, fully paid-up license** to Customer for Outputs and derivative data sets, plus **portability rights** that survive termination. The practical value to Meridian is the perpetual license and portability, not ownership of the weights themselves.

#### B. Proposed Compromise Clause Language (Redline-Ready)

> **§6.1 Vendor IP.** VENDOR RETAINS ALL RIGHT, TITLE, AND INTEREST IN AND TO THE PLATFORM, ALL MODEL IP (INCLUDING BASE MODEL WEIGHTS, PARAMETERS, EMBEDDINGS, ARCHITECTURES, AND FINE-TUNED ADAPTATIONS), ALL UPDATES, AND ALL IMPROVEMENTS, MODIFICATIONS, ENHANCEMENTS, AND DERIVATIVE WORKS THEREOF, WHETHER DEVELOPED BEFORE, DURING, OR AFTER THE TERM. NO TRANSFER OF OWNERSHIP OF ANY VENDOR IP IS INTENDED OR EFFECTED UNDER THIS AGREEMENT.
>
> **§6.2 Fine-Tuned Models and Derivative Data.**
>
> (a) **Vendor Ownership.** ALL FINE-TUNED MODEL WEIGHTS, PARAMETERS, CONFIGURATIONS, EMBEDDINGS, AND DERIVATIVE DATA GENERATED THROUGH THE OPERATION OF THE PLATFORM ARE AND SHALL REMAIN THE PROPERTY OF VENDOR. CUSTOMER ACKNOWLEDGES THAT IT DOES NOT SEEK, AND THIS AGREEMENT DOES NOT CONVEY, OWNERSHIP OF ANY MODEL WEIGHTS, PARAMETERS, EMBEDDINGS, OR MODEL ARCHITECTURES, WHETHER BASE OR FINE-TUNED.
>
> (b) **Irrevocable Perpetual License.** VENDOR HEREBY GRANTS TO CUSTOMER AN IRREVOCABLE, PERPETUAL, FULLY PAID-UP, NON-EXCLUSIVE, ROYALTY-FREE LICENSE TO USE, COPY, STORE, REPRODUCE, DISPLAY, DISTRIBUTE, AND CREATE DERIVATIVE WORKS FROM ALL OUTPUTS AND DERIVATIVE DATA SETS (EXCLUDING MODEL WEIGHTS, PARAMETERS, EMBEDDINGS, AND MODEL ARCHITECTURE COMPONENTS) GENERATED BY THE PLATFORM USING CUSTOMER DATA, FOR CUSTOMER'S INTERNAL CLINICAL, OPERATIONAL, REGULATORY, LEGAL, COMPLIANCE, QUALITY-IMPROVEMENT, AND RESEARCH PURPOSES, INCLUDING USE IN CONNECTION WITH ANY SUCCESSOR PLATFORM OR CLINICAL DECISION-SUPPORT SYSTEM FOLLOWING TERMINATION OR EXPIRATION OF THIS AGREEMENT. THIS LICENSE SHALL SURVIVE TERMINATION OR EXPIRATION OF THIS AGREEMENT FOR ANY REASON, INCLUDING TERMINATION FOR CAUSE BY EITHER PARTY.
>
> (c) **Portability.** UPON TERMINATION OR EXPIRATION OF THIS AGREEMENT, CUSTOMER MAY EXPORT AND USE ALL OUTPUTS AND DERIVATIVE DATA SETS (EXCLUDING MODEL WEIGHTS, PARAMETERS, EMBEDDINGS, AND MODEL ARCHITECTURE COMPONENTS) ON ALTERNATIVE INFRASTRUCTURE, WITH A SUCCESSOR VENDOR, OR ON CUSTOMER-OWNED COMPUTING RESOURCES. VENDOR SHALL PROVIDE REASONABLE TECHNICAL DOCUMENTATION AND ASSISTANCE, AT NO CHARGE TO CUSTOMER DURING THE TRANSITION PERIOD, TO ENABLE SUCH PORTABILITY, INCLUDING DOCUMENTED DATA SCHEMAS, API SPECIFICATIONS, AND EXPORT TOOLS. CUSTOMER SHALL NOT REVERSE-ENGINEER, DECOMPILE, OR ATTEMPT TO RECONSTRUCT VENDOR'S BASE MODEL OR PROPRIETARY ALGORITHMS FROM THE EXPORTED OUTPUTS AND DERIVATIVE DATA SETS.
>
> (d) **Transition Access to Fine-Tuned Models.** DURING THE TRANSITION PERIOD (SECTION 14.5), VENDOR SHALL MAINTAIN API ACCESS TO THE FINE-TUNED MODELS CONFIGURED FOR CUSTOMER'S COVERED FACILITIES SO THAT CUSTOMER MAY CONTINUE TO GENERATE OUTPUTS AND DERIVATIVE DATA SETS FOR PORTABILITY PURPOSES UNTIL THE SUCCESSOR PLATFORM IS OPERATIONAL.
>
> **§2.4 Output License.** [Confirm the Vendor's June 30 perpetual, royalty-free Output License, with the survival and successor-platform-use rights set forth in §6.2(b)–(c).]
>
> **§2.5 Data Portability.** [Confirm the Vendor's June 30 data-portability export obligation (FHIR R4 / HL7 v2), with the perpetual license and portability rights for Outputs and derivative data sets set forth in §6.2(b)–(c). For the avoidance of doubt, the perpetual license and portability rights apply to Outputs and derivative data sets; model weights, parameters, embeddings, and model architectures remain Vendor's proprietary Model IP and are not subject to export or transfer.]
>
> **§6.4 Feedback.** [Retain the Vendor's standard Feedback license, with the clarification that Feedback does not include Customer Data, Outputs, or derivative data sets, which are governed by §§2.4, 5.1, and 6.2.]

#### C. Negotiation Rationale and Fallback Ladder

**Why this landing zone.** This is the Playbook final fallback, endorsed by the Delgado and Sutter guidance. The proposal concedes ownership of all model IP to the Vendor (respecting the CTO's hard no) and secures the practical value Meridian needs: (i) an **irrevocable, perpetual, fully paid-up license** to Outputs and derivative data sets that survives termination for any reason (including termination for cause by the Vendor — a critical protection against lock-in); (ii) **portability rights** to use the Outputs and derivative data sets on a successor platform or Meridian-owned infrastructure; (iii) **transition API access** to the fine-tuned models during the Transition Period so Meridian can continue generating Outputs until the successor is operational; and (iv) **technical documentation and assistance** at no charge during transition. The proposal does not seek base-model weights (the CTO's hard no) and does not seek ownership of fine-tuned weights (not achievable); instead, it secures the ongoing *use* of the separable artifacts (Outputs, derivative data sets) plus transition access to the fine-tuned models.

**Distinction (Playbook §4.5).** The proposal clarifies that Customer does not seek base-model weights and that the perpetual license and portability apply to the separable layer (Outputs and derivative data sets). Where fine-tuned weights are technically inseparable from the base model, the perpetual license and portability apply to the Outputs and derivative data sets (which are separable), and the transition API access (§6.2(d)) provides the bridge to a successor platform. This threads the needle between the Playbook's preference for fine-tuned-weight portability and the CTO's hard no.

**Fallback ladder:**

| Position | Ownership | License | Portability | When to Deploy |
|---|---|---|---|---|
| **A (Primary)** | Vendor (all model IP) | Irrevocable perpetual license to Outputs + derivative data sets | Portability of Outputs + derivative data sets; transition API access to fine-tuned models | Opening compromise (Playbook final fallback) |
| **B (Stretch — if CTO flexibility)** | Vendor (all model IP) | Irrevocable perpetual license to Outputs + derivative data sets + fine-tuned weights (the delta) | Portability of fine-tuned weights to run on alternative infrastructure | If CTO signals any flexibility on fine-tuned-weight transfer |
| **C (Joint ownership — if Vendor open)** | Joint ownership of fine-tuned adaptations | Customer exclusive-use license (DE/PA/NJ); Vendor uses only outside territory in de-identified aggregated form | Full portability | If Vendor signals openness to joint ownership (Playbook first fallback) |
| **Floor** | Vendor ownership acceptable | Irrevocable perpetual license to Outputs + derivative data sets + portability + survival | Must include portability + survival | If Vendor refuses perpetual license + portability entirely → escalate to GC (Playbook red line; potential deal termination) |

#### D. Acceptability Analysis for the Vendor Team

**Sandra Hu (commercial terms / precedent).** Hu's principal concern will be the irrevocable, perpetual license and the survival-for-any-reason provision. **Response:** (i) the Vendor's own June 30 draft already grants a perpetual, irrevocable, royalty-free license to Outputs and derivative data sets (§§2.4, 6.2(b)) — the proposal confirms and slightly extends that grant with the successor-platform-use and portability rights, which are the natural consequence of a perpetual license; (ii) the proposal concedes the Vendor's core IP position (ownership of all model IP, including fine-tuned weights) — a substantial concession from the Customer's ownership opening; (iii) the survival-for-any-reason provision (including termination for cause by the Vendor) is necessary to prevent the perpetual license from being rendered meaningless by a for-cause termination — without it, the Vendor could terminate for a minor curable breach and extinguish the perpetual license, which would be a lock-in mechanism; (iv) the no-reverse-engineering covenant (§6.2(c)) protects the Vendor's base model and algorithms. Frame the proposal as confirming the Vendor's own June 30 license grant and adding only the portability and survival protections that make the perpetual license meaningful.

**Rafael Bowen / CTO (trade-secret protection).** The CTO's hard no on raw model weights is the principal obstacle. **Response:** (i) the proposal does **not** seek base-model weights, fine-tuned weights, parameters, embeddings, or model architecture — it explicitly excludes these from the license and portability (§6.2(b)–(c)); (ii) the license and portability apply only to Outputs and derivative data sets (the separable artifacts generated from Customer Data), which the Vendor's June 30 draft already licenses to Customer; (iii) the transition API access (§6.2(d)) gives Meridian continued *use* of the fine-tuned models during transition without *receiving* the weights — the models remain on the Vendor's infrastructure, accessed via API, which preserves the trade-secret protection the CTO requires; (iv) the no-reverse-engineering covenant is explicit. Emphasize that this proposal fully respects the CTO's hard no — no weights are transferred — while giving Meridian the ongoing use and portability it needs to avoid lock-in.

#### E. Regulatory and Compliance Constraints

- **HIPAA.** Outputs and derivative data sets that contain or are derived from PHI remain subject to the BAA and HIPAA de-identification standards. The portability export (§6.2(c)) must comply with HIPAA transmission-security requirements (Exhibit E). Derivative data sets used on a successor platform must maintain the same de-identification and security standards.
- **NJ AI in Healthcare Transparency Act.** The perpetual license and portability support Meridian's ongoing obligation to maintain documentation and audit records for the three New Jersey facilities following termination. The transition API access (§6.2(d)) ensures no documentation gap during the successor-platform transition.
- **FDA.** The portability of Outputs and derivative data sets supports Meridian's FDA post-market surveillance and record-retention obligations. The transition access ensures continuity of clinical decision-support during migration, avoiding a regulatory gap.
- **Lock-in prevention (cross-reference Proposal 3).** The irrevocable perpetual license and portability (§6.2(b)–(c)) are the IP-side complement to the transition assistance and data-return terms in Proposal 3. Together, they ensure that Meridian can exit the relationship with its data, its Outputs, and the ongoing right to use them — preventing the economic lock-in that Dr. Narayanan's red line prohibits.

---

### PROPOSAL 7 — INDEMNIFICATION SCOPE AND STRUCTURE

**Priority Rank: 7 (lowest) | Agreement §13.1–13.7 | Matrix Term 5 | Related: §12.3 (super-cap), §15.1 (insurance), Proposal 1 (liability)**

#### A. Positions Summary

| Component | Vendor Opening (Jun 6) | Customer Counter (Jun 20) | Vendor Response (Jun 30) |
|---|---|---|---|
| Indemnification scope | IP infringement only | Broad (IP, regulatory, patient-harm, data breach) | IP infringement only (deleted regulatory, patient-harm, data breach) |
| Defense control | Vendor sole control | Customer controls patient-safety defense | Vendor sole control; shared defense for complex claims (each bears own costs) |
| Indemnification cap | General cap (dollar-for-dollar) | Excluded from general cap (uncapped) | Super-Cap (3×) — **conceded** |
| Data breach indemnity | Excluded | Included | Excluded (but Vendor "willing to add" per matrix) |

**Gap.** The Vendor's June 30 position limits indemnification to IP infringement only — excluding regulatory penalties, patient-harm claims, and data breach. The Playbook red line requires that indemnification include **patient-harm and IP at minimum**, and never be capped below the super-cap floor. The Vendor has signaled willingness to add data breach indemnity (per the Contested Terms Matrix). The strategic guidance (Priority 7, lowest) permits flexibility here *provided* Meridian has secured gains on Priorities 1–2 (which these proposals do — the patient-safety super-cap and audit rights). However, the Board Risk Committee's Tier 1 designation means indemnification still requires a defensible scope.

#### B. Proposed Compromise Clause Language (Redline-Ready)

> **§13.1 Vendor Indemnification.** VENDOR SHALL INDEMNIFY, DEFEND, AND HOLD HARMLESS CUSTOMER AND THE CUSTOMER INDEMNITEES FROM AND AGAINST ANY AND ALL LOSSES ARISING OUT OF OR RELATED TO:
>
> (a) **IP Infringement Claims** — any allegation that Customer's authorized use of the Platform infringes or misappropriates any third-party patent, copyright, trademark, or trade secret;
>
> (b) **Data Breach Claims** — any claim, regulatory action, or proceeding arising from a Security Incident or Breach of Unsecured PHI (as defined in the BAA) attributable to Vendor, its subprocessors, or its systems, including the costs of notification, credit monitoring, forensic investigation, and regulatory fines;
>
> (c) **Regulatory Enforcement Claims** — any investigation, enforcement action, or proceeding by a governmental authority (including HHS, the New Jersey Department of Health, or any state attorney general) arising from Vendor's acts or omissions in connection with the Platform, including noncompliance with HIPAA, HITECH, the NJ AI in Healthcare Transparency Act, or other applicable healthcare or data-privacy laws, to the extent such claims arise from Vendor's breach of its obligations under this Agreement or the BAA; and
>
> (d) **Patient-Harm Claims (AI-Output)** — any claim by or on behalf of a patient alleging bodily injury, adverse clinical outcome, or wrongful death arising from an Output, recommendation, alert, risk score, or clinical decision-support result generated by the Platform that is alleged to be inaccurate, misleading, biased, delayed, or otherwise deficient, to the extent such claim arises from the Platform's Output and not from Customer's independent clinical judgment or clinician override.
>
> **§13.2 Exclusions.** [Retain the Vendor's standard exclusions (Customer modifications, combination with non-Vendor products, non-compliant use, failure to implement Updates, Customer Data), with the clarification that the patient-harm exclusion does not apply where the AI Output was a contributing proximate cause.]
>
> **§13.5 Indemnification Procedures.**
>
> (a) **Notice.** [Standard prompt-notice provision, with material-prejudice qualifier.]
>
> (b) **Shared Defense for Complex Claims.** FOR ANY CLAIM INVOLVING ALLEGATIONS RELATED TO BOTH VENDOR'S PLATFORM AND CUSTOMER'S CLINICAL OPERATIONS OR CLINICAL JUDGMENT (INCLUDING ANY CLAIM INVOLVING ADVERSE PATIENT OUTCOMES), THE PARTIES SHALL COOPERATE IN A SHARED DEFENSE ARRANGEMENT:
>
> (i) **Vendor-Primary Claims.** VENDOR SHALL HAVE PRIMARY CONTROL OF THE DEFENSE OF CLAIMS WHERE THE PROXIMATE CAUSE IS AN ERRONEOUS, MISLEADING, BIASED, OR DEFICIENT AI OUTPUT, INCLUDING SELECTION OF COUNSEL, SUBJECT TO CUSTOMER'S CONSENT RIGHTS ON SETTLEMENT (SUBSECTION (d));
>
> (ii) **Customer-Primary Claims.** CUSTOMER SHALL HAVE PRIMARY CONTROL OF THE DEFENSE OF CLAIMS WHERE THE PROXIMATE CAUSE IS CLINICIAN OVERRIDE, INDEPENDENT CLINICAL JUDGMENT, OR CUSTOMER'S CLINICAL OPERATIONS;
>
> (iii) **Mixed-Causation Claims.** FOR CLAIMS INVOLVING MIXED CAUSATION, THE PARTIES SHALL COOPERATE IN A SHARED DEFENSE, EACH SELECTING ITS OWN COUNSEL AND BEARING ITS OWN DEFENSE COSTS, WITH THE ALLOCATION OF ANY DAMAGES OR SETTLEMENT AMOUNTS NEGOTIATED IN GOOD FAITH AND, FAILING AGREEMENT, DETERMINED THROUGH THE DISPUTE RESOLUTION PROCESS IN SECTION 16.2 ON A PROPORTIONAL-FAULT BASIS.
>
> (c) **Cooperation.** [Standard cooperation provision, at the Indemnifying Party's expense.]
>
> (d) **Settlement Consent.** NO SETTLEMENT THAT IMPOSES LIABILITY OR ADMISSION OF FAULT ON THE INDEMNIFIED PARTY, OR THAT AFFECTS CUSTOMER'S CLINICAL REPUTATION OR REGULATORY STANDING, SHALL BE MADE WITHOUT THE INDEMNIFIED PARTY'S PRIOR WRITTEN CONSENT (NOT TO BE UNREASONABLY WITHHELD).
>
> **§13.7 Indemnification Cap.** VENDOR'S AGGREGATE LIABILITY UNDER THIS ARTICLE 13 SHALL NOT EXCEED THE SUPER-CAP SET FORTH IN SECTION 12.3. REGULATORY PENALTIES UNDER SECTION 13.1(c) ARISING FROM VENDOR'S BREACH SHALL BE CARVED OUT FROM THE GENERAL CAP AND SUBJECT TO THE SUPER-CAP, CONSISTENT WITH THE NJ AI IN HEALTHCARE TRANSPARENCY ACT.
>
> **§13.6 Sole Remedy.** [Revise to provide that indemnification is Customer's sole and exclusive remedy for third-party IP infringement claims, but is not the sole remedy for data breach, regulatory, or patient-harm claims, which remain subject to Articles 12 and 13 in their entirety.]

#### C. Negotiation Rationale and Fallback Ladder

**Why this landing zone.** This is the Playbook fallback, calibrated to the strategic guidance. The proposal secures the four scope categories the Playbook and Board Risk Committee require — IP (agreed), data breach (Vendor has signaled willingness), regulatory (NJ Act requires), and patient-harm (Playbook red line) — while conceding on defense control (shared defense with Vendor-primary for AI-output claims, rather than Customer's standard of controlling patient-safety defense). The concession on defense control is the trade that secures the Vendor's acceptance of patient-harm indemnification scope. The cap is set at the super-cap (3× ACV), consistent with the Vendor's June 30 §13.7 concession and the Proposal 1 super-cap structure. Regulatory penalties are carved out from the general cap (per the NJ Act compliance brief) and subject to the super-cap.

**Strategic calibration.** Priority 7 is the lowest priority, and the Playbook permits flexibility here if Meridian has secured gains on Priorities 1–2. These proposals secure the patient-safety super-cap (Proposal 1) and the audit rights (Proposal 2), so flexibility on indemnification defense control is appropriate. However, the scope must include patient-harm and IP at minimum (Playbook red line), and the cap must never be below the super-cap floor. The Board Risk Committee's Tier 1 designation means the patient-harm indemnification scope is backstopped by the super-cap (Proposal 1) even if the indemnification defense structure is shared.

**Fallback ladder:**

| Position | Scope | Defense Control | Cap | When to Deploy |
|---|---|---|---|---|
| **A (Primary)** | IP + data breach + regulatory + patient-harm (AI-output) | Shared (Vendor-primary AI-output; Customer-primary clinician override; mixed proportional) | Super-Cap (3×); regulatory carved from general cap | Opening compromise |
| **B (First fallback)** | IP + data breach + regulatory + patient-harm (limited to gross negligence/willful misconduct or actual-knowledge defects) | Shared | Super-Cap (3×) | If Vendor resists broad patient-harm scope |
| **C (Second fallback)** | IP + data breach + regulatory (no patient-harm indemnification; patient-safety covered by super-cap liability structure in Proposal 1) | Shared for complex claims | Super-Cap (3×) | If Vendor refuses patient-harm indemnification entirely [requires GC escalation per Playbook §7.3] |
| **Floor** | IP + data breach at minimum; regulatory (NJ Act) for Vendor-attributable penalties | — | Never below super-cap floor (3×) | If Vendor refuses even data breach + regulatory → escalate |

#### D. Acceptability Analysis for the Vendor Team

**Sandra Hu (scope expansion / precedent).** Hu's principal objection will be that patient-harm indemnification is outside a software vendor's scope and that regulatory indemnification is unprecedented. **Response:** (i) IP and data breach indemnification are within the Vendor's signaled willingness (the Contested Terms Matrix confirms the Vendor is willing to add data breach to IP); (ii) regulatory indemnification is limited to penalties arising from the Vendor's *own* breach of its obligations (documentation, audit cooperation, data governance) — it does not indemnify Meridian for penalties arising from Meridian's own conduct; (iii) patient-harm indemnification is limited to claims where the AI Output is a contributing proximate cause, and the shared-defense structure (Vendor-primary for AI-output claims, Customer-primary for clinician-override claims) allocates responsibility fairly — the Vendor is not indemnifying Meridian for clinician malpractice; (iv) the cap is the super-cap (3× ACV), which the Vendor has already accepted for IP and willful misconduct — no category is uncapped; (v) the proposal concedes the Customer's standard position of controlling patient-safety defense in exchange for the Vendor accepting patient-harm scope — a fair trade. Frame the scope expansion as the natural complement to the patient-safety super-cap (Proposal 1): the super-cap caps the exposure; the indemnification provides the defense and funding mechanism.

**Rafael Bowen (liability exposure / defense control).** Bowen may object to the shared-defense structure and the patient-harm scope. **Response:** (i) the shared-defense structure is the Playbook fallback and is more favorable to the Vendor than the Customer's standard (Customer controls patient-safety defense) — the Vendor retains primary control of AI-output claims, which is where the Vendor's exposure lies; (ii) the Customer-primary allocation for clinician-override claims protects the Vendor from indemnifying Meridian's clinical malpractice; (iii) the mixed-causation proportional-fault allocation (§13.5(b)(iii)) is fair and uses the existing dispute-resolution mechanism; (iv) the settlement-consent provision (§13.5(d)) protects both parties from settlements that affect their respective reputations or regulatory standing; (v) the super-cap (3×) bounds the total indemnification exposure, and the binding insurance increase (Proposal 1, §15.1(c)) ensures the cap is backed by coverage. Emphasize that the Board Risk Committee will not approve a deal in which patient-harm from AI outputs is entirely unindemnified — the shared-defense structure is the compromise that makes patient-harm indemnification acceptable to both sides.

#### E. Regulatory and Compliance Constraints

- **NJ AI in Healthcare Transparency Act.** Penalties (up to $50,000 per violation, per day) are assessed against Meridian as the covered entity. §13.1(c) provides indemnification for regulatory penalties arising from the Vendor's breach of its documentation, audit-cooperation, and data-governance obligations — directly addressing the Act's vendor-contractual requirements (§7(a)). The carve-out from the general cap (§13.7) ensures regulatory indemnification is not swallowed by the 1.5× general cap. The anti-waiver provision (§7(b)) means this indemnification cannot be contracted away for the three New Jersey facilities.
- **HIPAA.** §13.1(b) data-breach indemnification is coordinated with the BAA (Exhibit F), which governs PHI-breach liability. The BAA controls on PHI-specific conflicts; the indemnification provides the contractual funding mechanism for BAA-based claims.
- **FDA.** §13.1(c) regulatory indemnification extends to FDA enforcement actions arising from the Vendor's failure to maintain necessary clearances or to notify Meridian of adverse regulatory actions. The change-of-law provision (Playbook §10.4) should be incorporated to accommodate evolving FDA guidance.
- **Board Risk Committee.** The Tier 1 enterprise-risk designation requires that patient-harm from AI outputs be addressed through both the super-cap (Proposal 1) and the indemnification scope (this proposal). The shared-defense structure and super-cap cap make the patient-harm indemnification defensible at the August 4 briefing. If the patient-harm indemnification is narrowed (Position C), the General Counsel must approve, and the Board Risk Committee must be briefed on the reliance on the super-cap as the sole patient-safety protection.

---

## V. PACKAGE INTEGRATION AND BOARD RISK COMMITTEE NOTE

### 5.1 The Seven Proposals as a Coordinated Package

The proposals are designed to be negotiated as a package, with concessions on lower-priority terms (data usage, IP ownership, indemnification defense control) deployed in exchange for the Vendor's acceptance of the higher-priority terms (patient-safety super-cap scope, audit rights, graduated ETF). The key value exchanges are:

- **Data usage (Priority 4) ↔ Patient-safety super-cap scope (Priority 1) and audit rights (Priority 2).** Meridian grants the Vendor its highest-value commercial term (aggregated data use for model improvement) in exchange for the Vendor accepting patient-safety, HIPAA, and data breach in the 3× super-cap and the Langford tiered audit framework.
- **IP ownership (Priority 6) ↔ Perpetual license + portability.** Meridian concedes ownership of all model IP (respecting the CTO's hard no) in exchange for the irrevocable perpetual license, portability, and transition access that prevent lock-in.
- **Indemnification defense control (Priority 7) ↔ Patient-harm indemnification scope.** Meridian concedes the Customer's standard of controlling patient-safety defense (accepting shared defense) in exchange for the Vendor accepting patient-harm indemnification scope.
- **Graduated ETF (Priority 3) ↔ Robust transition + data export.** Meridian accepts a graduated ETF (subject to GC approval) in exchange for at-cost transition assistance, no ARF during transition, and FHIR R4 / HL7 v2 data export.

### 5.2 Items Requiring General Counsel Approval Before the July 18 Session

The following elements of these proposals depart from the Playbook's standard positions and require Dr. Narayanan's explicit approval before they are presented at the table:

1. **Graduated ETF (Proposal 3, Position A).** Any ETF triggers Playbook escalation (presumptive rejection). The graduated 50/25/0 structure is the recommended landing zone but requires GC approval.
2. **3× all-carve-outs super-cap at 1.5× general cap (Proposal 1, Position A).** This is a coordinated variant of the Playbook's second fallback (which pairs 1.5× general with 4× super-cap). The 3× all-carve-outs variant is more achievable and meets the absolute floor, but departs from the strict second-fallback pairing.
3. **Opt-out window exceeding 30 days (Proposal 4, Positions B–C).** The Playbook provides that opt-out periods exceeding 30 days require VP/GC escalation.
4. **Elimination or narrowing of patient-harm indemnification (Proposal 7, Position C).** The Playbook provides that eliminating patient-harm indemnification entirely requires GC escalation.

### 5.3 Board Risk Committee Briefing (Week of August 4, 2025)

The deal team must be prepared to present the final liability and indemnification terms to the Board Risk Committee before execution. The Tier 1 enterprise-risk designation means the Committee will scrutinize: (i) the patient-safety super-cap scope and amount (Proposal 1); (ii) the audit-rights framework and NJ Act compliance (Proposal 2); (iii) the binding SLA benchmarks and termination rights (Proposal 5); and (iv) the indemnification scope and cap (Proposal 7). The proposals are structured to be defensible in that governance context — each meets or exceeds the absolute floors, and the fallback ladders preserve the floors under all realistic negotiation outcomes.

### 5.4 Reservation of Rights and Next Steps

This document reflects Meridian's negotiation preparation as of July 14, 2025, based on the documents reviewed (the Vendor draft, the Customer redline, the Vendor response redline, the Contested Terms Matrix, the Playbook, the Delgado internal memo, the Sutter instruction email, the Langford audit scope proposal, the NJ Act compliance brief, the Cognitive Foundry contract standards summary, and Exhibits C and D). The proposed clause language is draft compromise text for inclusion in the next markup and is subject to refinement based on the July 18 session. The fallback ladders and acceptability analyses are internal strategy and are not for disclosure to Cognitive Foundry or its counsel. The deal team should confirm General Counsel approval of the items in §5.2 before the session and should be prepared to escalate to the Board Risk Committee if any absolute floor is at risk.

---

*End of Compromise Proposals — July 14, 2025*

*PRIVILEGED & CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION / ATTORNEY WORK PRODUCT*