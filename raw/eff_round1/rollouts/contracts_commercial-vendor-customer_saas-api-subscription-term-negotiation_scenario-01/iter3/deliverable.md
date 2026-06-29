### FILE: compromise-proposals.md
# COMPROMISE PROPOSALS — CONTESTED TERMS

## Master AI Services Agreement (ClinIQ™ Platform v4.2)

**Between Meridian Health Systems, Inc. ("Customer" / "Meridian") and Cognitive Foundry, Inc. ("Vendor" / "Cognitive Foundry")**

---

**PRIVILEGED & CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION / ATTORNEY WORK PRODUCT**

Prepared by Whitfield Ames LLP (Elaine Sutter, Partner; Jessica Fong; David Ouellette) at the direction of the Office of the General Counsel of Meridian Health Systems, Inc. (Dr. Priya Narayanan, SVP & General Counsel; Marcus Delgado, VP, Digital Health & Technology Transactions). This memorandum is protected by the attorney-client privilege and the work-product doctrine and is intended exclusively for the Meridian negotiation team. Do not disclose to Cognitive Foundry, its counsel (Kessler Pratt & Lowe LLP — Sandra Hu, Rafael Bowen), or any other party without GC authorization.

**Date:** July 14, 2025 | **Joint negotiation session:** July 18, 2025 | **Target execution:** August 15, 2025 | **Target go-live:** January 6, 2026

---

## I. EXECUTIVE SUMMARY AND CONCESSION STRATEGY

This memorandum sets forth seven compromise proposals addressing the contested terms remaining in the Master AI Services Agreement (the "Agreement") between Meridian and Cognitive Foundry. Each proposal follows the four-component format directed by Elaine Sutter: (i) Proposed Contract Clause Language; (ii) Negotiation Rationale and Fallback Ladder; (iii) Acceptability Analysis for the Vendor Team; and (iv) Regulatory and Compliance Constraints.

The proposals are presented in Meridian's **priority order** (1 = highest), which governs the allocation of negotiating capital and the sequencing of concessions at the July 18 session. The Contested Terms Matrix (July 1, 2025) term number and Agreement section references are cross-referenced for each proposal.

### Meridian Priority Ranking and Concession Posture

| Priority | Contested Term | Matrix Term | Agreement § | Concession Posture |
|---|---|---|---|---|
| 1 | Patient-Safety Liability / Super-Cap | Term 1 | §12.1–12.4, §15.1 | **Hold the line.** Patient-safety floor (3× ACV) is non-negotiable. Concede general cap to 1.5× ACV only if super-cap includes patient-safety. |
| 2 | Audit Rights / Model Transparency | Term 3 | §10.1–10.4 | **Secure the Langford tiered framework.** Regulatory mandate (NJ Act) drives this; vendor has signaled flexibility. |
| 3 | Termination Flexibility / ETF / Transition | Term 7 | §14.3–14.6 | **Accept graduated ETF** (50%/25%/0%) as workable; pair with robust transition + data-export. |
| 4 | Aggregated / De-Identified Data Usage | Term 4 | §5.1–5.4, Ex. D | **Deploy as concession currency.** Offer calibrated flexibility here in exchange for movement on Priorities 1–3. |
| 5 | SLA / AI Accuracy Benchmarks | Term 6 | §9.1–9.4, Ex. C | **Push for binding benchmarks;** accept 3-miss termination trigger per playbook fallback. |
| 6 | IP Ownership (Model Weights) | Term 2 | §6.1–6.5 | **Accept vendor ownership with irrevocable perpetual license + functional portability.** Do not spend capital fighting the CTO's "hard no." |
| 7 | Indemnification Scope & Defense | Term 5 | §13.1–13.7 | **Most tradeable.** Accept shared defense + super-cap backstop; hold firm on patient-harm inclusion. |

**Critical Rule (Playbook §2.5):** Negotiators must not concede on a higher-priority item to gain advantage on a lower-priority item without express GC approval. The priority ranking is most relevant during final-stage package deals.

### Dr. Narayanan's Four Absolute Red Lines (Floors — Non-Negotiable)

1. **General Liability Cap:** Never below 1.5× trailing 12-month fees (~$14.4M).
2. **Patient-Safety Liability:** Separate, higher cap; never capped below 3× ACV (~$28.8M). Uncapped preferred.
3. **Meaningful Audit Rights:** Langford tiered access (Tier 2 baseline annual; Tier 3 for cause). Summary reports alone are insufficient.
4. **Termination for Convenience:** ETF must not make exit economically prohibitive at any point in the term.

### Key Deal Parameters (Reference)

- **TCV:** $38.4M over 4-year Initial Term | **ACV:** $9.6M/yr | **Year 1 Implementation Fee:** $4.2M (one-time) | **Annual Recurring Fee:** $8.55M/yr | **Quarterly Fee:** $2,137,500 | **Monthly Fee:** $712,500
- **Deployment:** 14 hospitals (DE, PA, NJ); 6,200 named licensed users; ~2.1M annual patient encounters; hosted on AWS GovCloud (us-east-1); integrated with Epic (MeridianConnect), Philips PACS, BD Pyxis
- **Governing law:** Delaware | **Dispute resolution:** AAA Commercial arbitration, Wilmington, DE
- **BAA (Exhibit F):** executed June 2, 2025

### Strategic Intelligence Informing These Proposals

1. **Comparable-deal precedent:** Through market reference checks, Meridian has confirmed that Cognitive Foundry recently closed a comparable deal with another multi-hospital health system (12 hospitals) at a **1.5× ACV general cap** and a **3× ACV super-cap** covering IP infringement and data breach. This directly undermines the vendor's "1× is standard" opening and supports a 1.5×/3× landing zone. Use this intelligence carefully at the table — anchor indirectly ("market practice for deals of this scope supports 1.5–2× ACV") unless Elaine authorizes direct reference.
2. **Sandra Hu's private acknowledgment:** Hu has acknowledged that Cognitive Foundry can likely accept a qualified third-party audit (not merely the annual summary report), subject to defined scope and a mutually agreed auditor.
3. **CTO "hard no" on raw model weights:** Access to raw model weights is a hard no from the technical leadership for *routine* access. A cause-based/regulatory carve-out (Tier 3 secure enclave, no extraction) may be palatable.
4. **Data usage is the vendor's highest-priority term:** Cognitive Foundry's ML pipeline depends on aggregated data from Meridian's 14-hospital network. This is Meridian's natural bargaining chip.
5. **CFO openness to graduated ETF:** The CFO is reportedly amenable to a graduated ETF (50% Year 1, 25% Year 2, 0% Years 3–4), driven by revenue-recognition concerns.

### Concession Sequencing (Package Approach)

Per the Delgado memo and Sutter guidance, Meridian should **hold firm on Priorities 1–3 through the early rounds** and **deploy calibrated concessions on Priority 4 (data usage) in exchange for movement on Priorities 1–3**. The data-usage concession is the primary currency. Priorities 5–7 are resolved largely on the playbook fallback positions, with Priority 6 (IP) conceded to the final fallback given the CTO's hard no.

---

## II. THE SEVEN COMPROMISE PROPOSALS

---

### PROPOSAL 1 — PATIENT-SAFETY LIABILITY / SUPER-CAP STRUCTURE
**Priority 1 | Matrix Term 1 | §12.1–12.4, §15.1 | Exhibits B, F, G**

#### (i) Proposed Contract Clause Language

**§12.2 General Liability Cap.** EXCEPT AS SET FORTH IN SECTION 12.3, EACH PARTY'S TOTAL CUMULATIVE LIABILITY ARISING OUT OF OR RELATED TO THIS AGREEMENT, WHETHER IN CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY, OR OTHERWISE, SHALL NOT EXCEED AN AMOUNT EQUAL TO ONE AND ONE-HALF TIMES (1.5×) THE TRAILING TWELVE (12)-MONTH FEES PAID OR PAYABLE BY CUSTOMER UNDER THIS AGREEMENT (THE "GENERAL CAP"). AS OF THE FIRST CONTRACT YEAR, THE GENERAL CAP IS FOURTEEN MILLION FOUR HUNDRED THOUSAND DOLLARS ($14,400,000).

**§12.3 Super-Cap Carve-Outs.** THE FOLLOWING CATEGORIES OF LIABILITY SHALL NOT BE SUBJECT TO THE GENERAL CAP AND SHALL INSTEAD BE SUBJECT TO A SEPARATE AGGREGATE LIABILITY CAP EQUAL TO THREE TIMES (3×) THE TRAILING TWELVE (12)-MONTH FEES PAID OR PAYABLE BY CUSTOMER (THE "SUPER-CAP"). AS OF THE FIRST CONTRACT YEAR, THE SUPER-CAP IS TWENTY-EIGHT MILLION EIGHT HUNDRED THOUSAND DOLLARS ($28,800,000):

> (a) **Patient-Safety Liability** — any third-party claim, regulatory proceeding, or enforcement action arising out of or related to bodily injury, clinical misdiagnosis, treatment error, or other patient harm attributable to AI-generated Outputs, recommendations, alerts, or decision-support results produced by the Platform;
>
> (b) **HIPAA / PHI Breach Liability** — any liability arising from a breach of either Party's obligations under the BAA, including any unauthorized access to, use of, or disclosure of Protected Health Information;
>
> (c) **IP Indemnification** — Vendor's indemnification obligations under Section 13.1(a) (IP Infringement Claims); and
>
> (d) **Willful Misconduct or Gross Negligence** — any liability arising from the willful misconduct or gross negligence of either Party, its employees, agents, or subcontractors.

**§12.4 Consequential Damages.** EXCEPT FOR (A) EITHER PARTY'S BREACH OF ARTICLE 11 (CONFIDENTIALITY), (B) EITHER PARTY'S INDEMNIFICATION OBLIGATIONS UNDER ARTICLE 13, (C) CUSTOMER'S OBLIGATION TO PAY FEES, (D) PATIENT-SAFETY LIABILITY, (E) VENDOR'S BREACH OF ARTICLE 5 (DATA GOVERNANCE) OR THE BAA, AND (F) CLAIMS COVERED BY VENDOR'S INSURANCE UNDER ARTICLE 15, NEITHER PARTY SHALL BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, PUNITIVE, OR EXEMPLARY DAMAGES.

**§15.1(c) Insurance — Cyber/E&O Coverage Commitment.** Vendor shall maintain Cyber Liability and Technology E&O Insurance of not less than Thirty Million Dollars ($30,000,000) per occurrence and Sixty Million Dollars ($60,000,000) in the aggregate. Vendor's current coverage under Northfield Mutual Insurance Co. Policy No. NM-CY-2025-04417 is $25,000,000 per occurrence / $50,000,000 aggregate. Vendor covenants to increase such coverage to the foregoing minimums no later than the earlier of (x) the next annual renewal date of such policy or (y) twelve (12) months following the Effective Date. During the interim period, Vendor shall (i) provide written confirmation from its broker that the coverage increase has been requested and is reasonably expected to be obtained, and (ii) provide Customer with an updated certificate of insurance evidencing the increased coverage within ten (10) business days of obtaining it. If Vendor fails to obtain the required coverage by the deadline, Customer may, at its election and upon written notice, (A) obtain supplemental coverage at Vendor's expense, (B) withhold up to ten percent (10%) of each quarterly invoice in escrow until the coverage requirement is met, or (C) terminate this Agreement for convenience without early termination fee. Carrier must be rated A- or better by A.M. Best.

#### (ii) Negotiation Rationale and Fallback Ladder

**Positions mapped:**

| Component | Vendor Opening (6/6) | Customer Opening (6/20) | Vendor Counter (6/30) | **Proposed Compromise** |
|---|---|---|---|---|
| General Cap | 1× ACV (~$9.6M) | 2× ACV (~$19.2M) | 1.5× ACV (~$14.4M) | **1.5× ACV (~$14.4M)** |
| Patient-Safety | General cap only (excluded from super-cap) | Uncapped | Excluded from super-cap (3× for IP + willful only) | **3× ACV super-cap (~$28.8M)** |
| HIPAA/PHI | General cap only | Uncapped | Excluded from super-cap | **3× ACV super-cap (~$28.8M)** |
| IP Indemnity | 2× super-cap | Uncapped | 3× super-cap | **3× ACV super-cap (~$28.8M)** |
| Willful Misconduct | 2× super-cap | Uncapped | 3× super-cap | **3× ACV super-cap (~$28.8M)** |

**Why this landing zone:** The general cap is the easy convergence point — the vendor's own counter (1.5× ACV) lands precisely at Meridian's absolute floor and matches the comparable-deal precedent (1.5× ACV). Meridian accepts 1.5× ACV on the general cap **as a bargaining chip**, not a gift, extracting in return the vendor's agreement to bring **patient-safety and HIPAA into the 3× super-cap** — the central dispute. The vendor's June 30 counter excluded patient-safety and HIPAA from the super-cap entirely (leaving them subject to the $14.4M general cap), which is a non-starter given the Tier 1 enterprise risk designation. The compromise places patient-safety at exactly Meridian's absolute floor (3× ACV, ~$28.8M) and at the vendor's stated maximum super-cap (3×). This is the meeting point: Meridian gives up "uncapped" and "4× ACV"; the vendor gives up its attempt to exclude patient-safety and HIPAA. The 3× ACV figure is directly supported by the comparable-deal intelligence (3× ACV super-cap for IP + data breach).

**Fallback ladder:**

- **Position A (Proposed):** 1.5× ACV general cap; 3× ACV super-cap for patient-safety, HIPAA, IP, willful misconduct. *(Meets patient-safety floor exactly; matches comparable deal.)*
- **Position B (if vendor resists HIPAA at 3×):** 1.5× ACV general cap; 3× ACV super-cap for patient-safety + IP + willful misconduct; HIPAA/PHI breach subject to general cap BUT backed by the enhanced insurance commitment (§15.1(c)) and BAA indemnification. *(Keeps patient-safety at floor; gives vendor partial relief on HIPAA in exchange for the binding insurance commitment.)*
- **Position C (last resort — requires Board Risk Committee approval):** 1.5× ACV general cap; 3× ACV super-cap for patient-safety only; IP + willful misconduct at 3×; HIPAA at general cap with insurance backstop. *(Holds patient-safety floor; maximum vendor relief elsewhere.)*
- **Absolute floor:** Patient-safety liability never below 3× ACV (~$28.8M). General cap never below 1.5× ACV. Any position at or below the second-fallback level requires Dr. Narayanan's approval.

**Insurance linkage:** The super-cap is only meaningful if collectable. The vendor's current $25M/$50M coverage leaves a gap against a $28.8M super-cap. The §15.1(c) commitment bridges this with a binding coverage-increase covenant and step-in rights, consistent with Playbook §11.2.

#### (iii) Acceptability Analysis for Vendor Team

**Rafael Bowen (liability exposure):** Bowen will push to exclude patient-safety and HIPAA from the super-cap, arguing these are clinical-malpractice matters outside a software vendor's scope and that uncapped/3× exposure is unquantifiable. **Response:** (1) The 3× ACV super-cap is a *cap*, not uncapped — it is bounded, insurable, and consistent with the vendor's own Board/insurer position that uncapped liability is unacceptable. (2) The comparable-deal precedent (3× ACV for IP + data breach) establishes that Cognitive Foundry has already accepted 3× super-cap exposure for comparable categories in a deal of similar scope — extending it to patient-safety is a calibrated, not unprecedented, step. (3) The super-cap is backstopped by the insurance commitment, addressing collectability. (4) Excluding patient-safety from any heightened cap — leaving it at the $14.4M general cap — is commercially untenable for a 14-hospital, 2.1M-encounter deployment and will not pass Meridian's Board Risk Committee, which has classified AI-related liability as Tier 1 enterprise risk. Frame this as: "We are not asking you to go beyond what you've done elsewhere; we are asking you to apply the same 3× structure to the one category that matters most clinically."

**Sandra Hu (commercial flexibility / precedent):** Hu will be concerned about setting a precedent that patient-safety is always a super-cap carve-out. **Response:** (1) The patient-safety super-cap is justified by the specific facts — clinical decision-support deployed at scale across 14 hospitals directly influencing ~2.1M annual encounters. (2) The 3× cap (not uncapped) preserves the vendor's ability to model and reserve against the exposure. (3) Meridian is conceding the general cap to the vendor's own counter (1.5× ACV) — this is a balanced package, not a one-sided demand. (4) The insurance commitment gives the vendor a concrete path to backstop the exposure at renewal.

#### (iv) Regulatory and Compliance Constraints

- **HIPAA / HITECH:** The BAA (Exhibit F, executed June 2, 2025) governs PHI obligations. The super-cap for HIPAA/PHI breach liability is consistent with the BAA's breach-notification and indemnification framework and ensures Meridian's PHI-breach remedies are not subsumed by the general commercial cap. The 24-hour breach-notification standard (Meridian's BAA position) is unaffected.
- **NJ AI Healthcare Transparency Act (effective March 1, 2025):** Civil penalties up to $50,000 per violation (each day of continuing violation = separate violation) are assessed against Meridian as the covered entity. The patient-safety super-cap and the regulatory-penalty indemnification (Proposal 7) together address the exposure created by the vendor's clinical outputs at the 3 NJ facilities. The Act's anti-waiver provision (§7(b)) prohibits contractual terms that prevent Meridian from satisfying its statutory obligations — a sub-$14.4M cap on patient-safety liability would be difficult to defend as compliant.
- **FDA clinical decision-support guidance:** The ClinIQ™ modules (sepsis, radiology, medication interaction) may be subject to FDA oversight depending on the 21st Century Cures Act §3060 four-part exemption analysis. The radiology module's interaction with medical imaging raises particular questions. The patient-safety super-cap ensures liability allocation is robust regardless of the platform's evolving FDA regulatory status.
- **Board Risk Committee (Tier 1 enterprise risk):** AI-related liability is a Tier 1 enterprise risk. The Board requires a pre-execution briefing on liability and indemnification terms. A patient-safety cap below 3× ACV will not pass Board review. The 3× ACV super-cap is the minimum defensible position for the Board briefing (target week of August 4, 2025).

---

### PROPOSAL 2 — AUDIT RIGHTS / MODEL TRANSPARENCY
**Priority 2 | Matrix Term 3 | §10.1–10.4 | NJ AI Healthcare Transparency Act**

#### (i) Proposed Contract Clause Language

**§10.1 Annual Transparency Documentation.** Vendor shall provide Customer, on an initial basis (within thirty (30) days following the Go-Live Date) and on an ongoing basis (updated within thirty (30) days following any material change to the Platform, including model updates, retraining, or changes to training data), with the following transparency documentation for each ClinIQ™ clinical module: (a) training data sources, including provenance, demographic composition, and representativeness analysis; (b) validation methodology, including validation datasets, performance metrics, and statistical methods; (c) known limitations, including identified failure modes, edge cases, and population subgroups for which performance may be degraded; and (d) bias testing results, including differential performance across race, ethnicity, sex, age, socioeconomic status, language, and disability status. This documentation shall be sufficient to satisfy Customer's algorithmic-transparency obligations under the NJ AI in Healthcare Transparency Act and shall be made available to the New Jersey Department of Health upon request.

**§10.2 Annual Independent Audit (Tier 2).** Customer shall have the right, exercisable without Vendor's prior consent (subject to reasonable advance notice and scheduling coordination), to engage the Independent Auditor — initially Langford AI Assurance Group, LLC (Dr. Anil Cherian, Managing Director), 101 Federal Street, Suite 1900, Boston, MA 02110, pre-approved by both Parties — to conduct one (1) annual independent audit of the Platform's AI/ML models. The annual audit shall be conducted at **Tier 2 access**, which includes: (i) model architecture documentation (network topology, layer configurations, activation functions); (ii) training data provenance records; (iii) validation and test results, including performance metrics by subpopulation; (iv) test-query access (the ability to submit defined test cases to the model in a controlled environment and observe outputs); (v) bias and fairness testing results and methodologies; and (vi) change logs and version history. Tier 2 access does not require disclosure of raw model weights, proprietary source code, or training pipeline code. The annual audit satisfies the independent annual audit requirement of the NJ AI in Healthcare Transparency Act for Customer's three (3) New Jersey Covered Facilities.

**§10.3 Tier 3 Cause-Based / Regulatory Audits.** Notwithstanding the annual cadence, Customer may request an additional audit at **Tier 3 access** — model weights and embeddings reviewed within a Vendor-controlled secure enclave, with no data extraction, copying, or removal permitted — upon the occurrence of any of the following triggers: (a) a documented patient-safety event at any Covered Facility potentially attributable, in whole or in part, to a ClinIQ™ Output; (b) receipt of a formal regulatory inquiry or investigation from the NJ Department of Health, the FDA, or another governmental authority concerning the Platform; (c) the Tier 2 annual audit identifies anomalies or concerns that cannot be resolved without examination of model internals; (d) any clinical module fails to meet its Performance Benchmark for two (2) or more consecutive quarters; or (e) mutual written agreement of the Parties. Tier 3 access shall be conducted exclusively within Vendor's designated secure enclave; no model weights, embeddings, or source code may be extracted, copied, photographed, or removed.

**§10.4 Auditor Confidentiality and Cooperation.** The Independent Auditor shall (i) execute a separate NDA with Vendor prior to any audit; (ii) conduct all Tier 2 and Tier 3 reviews within Vendor's designated secure environment; (iii) not extract, copy, or remove any Vendor Confidential Information; (iv) destroy all work product, notes, and interim analyses within thirty (30) days of delivering the final audit report and certify such destruction in writing to both Parties; and (v) deliver the audit report to Customer's designated representatives (Dr. Priya Narayanan and Marcus Delgado) and to Vendor. Vendor shall cooperate fully with each audit, designate a technical liaison, and provide access within twenty (20) business days' advance notice for scheduled audits and five (5) business days for cause-based Tier 3 audits. Vendor shall not seek protective orders or confidential treatment that would prevent Customer from satisfying its regulatory obligations under the NJ Act, except with Customer's prior written consent.

**§10.5 Regulatory Cooperation and Anti-Waiver.** Vendor shall cooperate fully with Customer in responding to any NJ Department of Health inquiry related to the Platform, including (a) making qualified personnel available for interviews upon reasonable notice; (b) producing additional documentation through Customer within fifteen (15) business days of a DOH request; and (c) providing technical assistance in preparing responses. Vendor shall provide Customer with accurate, current descriptions of ClinIQ™ functionality, known limitations, and clinician-review protocols in a form suitable for patient-facing notification materials, updated upon material changes. **No provision of this Agreement shall be construed to waive, limit, or condition Customer's rights or obligations under the NJ AI in Healthcare Transparency Act or any comparable state or federal law.**

**Audit Cost Allocation.** Vendor shall bear the cost of the annual Tier 2 audit (as a regulatory compliance obligation that Vendor's cooperation enables). Customer shall bear the cost of any ad hoc Tier 3 audit, unless the audit confirms Vendor non-compliance, in which case Vendor shall bear the cost.

#### (ii) Negotiation Rationale and Fallback Ladder

**Positions mapped:**

| Component | Vendor Opening (6/6) | Customer Opening (6/20) | Vendor Counter (6/30) | **Proposed Compromise** |
|---|---|---|---|---|
| Frequency | Annual summary report | Quarterly audits | Annual audit (very limited scope) | **Annual independent audit (Tier 2)** |
| Access depth | No model internals; output logs + vendor docs only | Full model internals incl. weights/embeddings | Bias/fairness + aggregate accuracy + governance summary only (NO architecture, provenance, validation, test queries) | **Tier 2 (architecture, provenance, validation, test queries, bias); Tier 3 (weights/enclave) for cause** |
| Auditor | Vendor pre-approves; vendor NDA | Customer selects; no vendor approval | Vendor pre-approves; vendor NDA; vendor may redact | **Langford pre-approved by both; NDA; no vendor consent to audit (scheduling coordination only)** |
| Regulatory cooperation | General clause | Full NJ Act compliance; reports to NJ DOH | Subject to scope limitations; vendor may seek protective orders | **Full cooperation; 15-business-day production; no protective orders that block compliance; anti-waiver** |

**Why this landing zone:** This is the Playbook's second-fallback / floor position, and it is exactly the architecture recommended in the Delgado memo and Sutter email. The vendor's June 30 counter is *below* the regulatory floor — it excludes architecture documentation, training data provenance, validation results, and test queries, all of which the NJ Act's statutory audit scope (§5(b)) expressly requires. The Langford Tier 2 framework provides the independent verification the NJ Act demands *without* requiring raw model weights (addressing the CTO's "hard no" on routine weight access). Tier 3 enclave access for cause-based/regulatory triggers provides a deeper-review pathway without extraction — directly addressing the CTO's IP-protection concern. Sandra Hu has privately acknowledged that a qualified third-party audit is acceptable; this proposal operationalizes that acknowledgment.

**Fallback ladder:**

- **Position A (Proposed):** Annual Tier 2 audit by Langford (no vendor consent); Tier 3 for cause; full regulatory cooperation; anti-waiver; vendor bears annual audit cost.
- **Position B (if vendor resists cost or scope):** Annual Tier 2 audit by Langford; Tier 3 for cause; **shared audit cost (50/50)** for the annual audit; vendor bears cost of any audit confirming vendor non-compliance. *(Concede cost-sharing to preserve scope.)*
- **Position C (if vendor resists Tier 2 depth):** Annual audit at a defined "Tier 2-minus" scope (architecture documentation, validation results, bias testing, test queries — but training data provenance provided as summary rather than full records), with Tier 3 for cause. *(Narrow concession on provenance detail; requires GC + VP approval as below annual/Tier 2 minimum.)*
- **Absolute floor:** Annual independent audit at no less than Tier 2 access; must be independent; must satisfy the NJ Act. Below this floor = regulatory non-compliance and is non-negotiable.

#### (iii) Acceptability Analysis for Vendor Team

**Rafael Bowen (IP protection):** Bowen will resist any access to model architecture, provenance, or weights, citing trade-secret protection. **Response:** (1) Tier 2 access does *not* require disclosure of raw model weights, source code, or training pipeline code — it provides documentation and test-query access sufficient for independent verification without exposing extractable IP. (2) Langford's confidentiality framework (NDA, secure-environment-only access, no data extraction, mandatory work-product destruction with certification) is specifically designed to neutralize trade-secret concerns — the vendor's IP never leaves its controlled environment. (3) Tier 3 enclave access for cause-based triggers provides *no extraction* — the auditor reviews weights within a controlled environment from which no data can be removed. This is the precise mechanism the NJ Act analysis identifies as reconciling the CTO's "hard no" with regulatory requirements. (4) This is a *regulatory compliance baseline*, not a commercial preference — the NJ Act mandates independent annual audits with reports available to NJ DOH, and the Act's anti-waiver provision makes contractual restrictions on audit access unenforceable to the extent they block compliance.

**Sandra Hu (commercial flexibility / precedent):** Hu may be concerned about the no-vendor-consent audit right and cost allocation. **Response:** (1) Hu has already privately acknowledged that a qualified third-party audit is acceptable — this proposal is the logical implementation of that acknowledgment. (2) Langford is pre-approved by *both* parties, so the "no consent" right is theoretical — the only auditor currently designated is one the vendor has already approved. (3) Removing the vendor's consent right is essential because the NJ Act requires the audit as a matter of right, not discretion; a consent-based right would be unenforceable under the Act's anti-waiver provision. (4) On cost: the annual audit is a regulatory compliance cost that the vendor's cooperation enables; vendor-bearing is the Playbook standard position, but Meridian will share cost (Position B) if needed to close.

#### (iv) Regulatory and Compliance Constraints

- **NJ AI Healthcare Transparency Act (effective March 1, 2025):** This is the dispositive constraint. The Act mandates (§5) an independent annual audit covering, at minimum: (1) model architecture documentation and training data provenance; (2) validation results and ongoing performance metrics; (3) bias and fairness across demographic groups; (4) incident reports and adverse-event correlation; (5) data governance practices. The vendor's June 30 counter does not satisfy elements (1), (2), or (4). The Act's vendor-contracting requirements (§7(a)) mandate contractual rights to (1) model documentation access and (2) independent audit rights. The anti-waiver provision (§7(b)) prohibits contractual terms that prevent compliance. Civil penalties: up to $50,000 per violation, each day a separate violation; NJ DOH may order mandatory suspension of non-compliant AI systems. First audit due by January 6, 2027 (12 months after go-live); audit fieldwork should commence no later than Q4 2026. **Whitfield Ames cannot advise Meridian to execute an Agreement that fails to include these provisions.**
- **HIPAA:** The audit framework's data-governance component (Tier 2 element (vi) — change logs; Tier 3 — secure enclave) is coordinated with the BAA (Exhibit F). The auditor's NDA and no-extraction protocols ensure no PHI is improperly disclosed during audit.
- **FDA clinical decision-support guidance:** The audit's regulatory compliance verification component (per Langford's proposal, §3.6) assesses each module against the 21st Century Cures Act §3060 four-part exemption. The audit clause is drafted broadly enough ("as required by applicable law or regulation, including but not limited to the NJ Act and any FDA regulation") to accommodate evolving FDA guidance without amendment.
- **Multi-state expansion:** Similar legislation is pending in Delaware (H.B. 412) and Pennsylvania (draft legislation). Structuring uniform audit rights across all 14 facilities positions Meridian for future compliance. Recommend a "regulatory expansion" clause extending audit/cooperation obligations to any facility where ClinIQ™ becomes subject to comparable state/federal requirements.

---

### PROPOSAL 3 — TERMINATION FOR CONVENIENCE / ETF / TRANSITION
**Priority 3 | Matrix Term 7 | §14.3–14.6 | Exhibit D**

#### (i) Proposed Contract Clause Language

**§14.3 Termination for Convenience.**

> (a) **Customer Termination for Convenience.** Customer may terminate this Agreement for convenience at any time upon one hundred fifty (150) days' prior written notice to Vendor, subject to the graduated Early Termination Fee set forth in subsection (b).
>
> (b) **Graduated Early Termination Fee.** In the event Customer terminates for convenience, Customer shall pay an Early Termination Fee ("ETF") calculated as a percentage of the remaining unpaid Fees that would have been payable over the balance of the then-current Initial Term, as follows: (i) **fifty percent (50%)** if the effective date of termination occurs during Contract Year 1; (ii) **twenty-five percent (25%)** if the effective date of termination occurs during Contract Year 2; and (iii) **zero percent (0%)** if the effective date of termination occurs during Contract Year 3 or Contract Year 4. The ETF is payable within thirty (30) days of the effective date of termination and is in addition to all Fees accrued through the effective date of termination. For illustration: a Year 1 termination (remaining value ~$25.65M) yields an ETF of ~$12.83M; a Year 2 termination (remaining value ~$17.1M) yields an ETF of ~$4.28M; a Year 3 or 4 termination yields no ETF.
>
> (c) **No Vendor Termination for Convenience.** Vendor shall not have the right to terminate this Agreement for convenience during the Initial Term or any Renewal Term.

**§14.5 Transition Assistance.** Upon expiration or termination for any reason, Vendor shall provide transition assistance for a period of up to **twelve (12) months** (the "Transition Period") at Vendor's **verified direct cost plus a five percent (5%) administrative markup**. "Verified direct costs" means documented, out-of-pocket expenses directly attributable to the transition, excluding overhead allocations, profit margins beyond the 5% markup, and costs Vendor would incur regardless of the transition. Transition assistance shall include: (i) continued operation of the Platform during the Transition Period; (ii) cooperation in migrating Customer Data and Outputs to a successor platform; (iii) export of all Customer Data in FHIR R4 and HL7 v2 interoperable formats; (iv) maintained API access for MeridianConnect, Philips PACS, and BD Pyxis throughout the Transition Period; (v) up to four (4) knowledge-transfer sessions; and (vi) reasonable assistance validating the successor platform's integration. Customer shall not pay the Annual Recurring Fee during the Transition Period following the effective date of termination.

**§14.6 Data Return and Destruction.** Within **forty-five (45) calendar days** following the effective date of termination or expiration (or the end of the Transition Period, if applicable), Vendor shall, at Customer's written election: (a) **Return** all Customer Data and Outputs in FHIR R4, HL7 v2, and such other interoperable formats as Customer may reasonably specify; or (b) **Destroy** all Customer Data and certify destruction in writing, executed by an officer of Vendor, in accordance with NIST SP 800-88. During the 45-day period, all Customer Data shall remain encrypted (AES-256) and access-restricted, with no Vendor personnel accessing Customer Data except as necessary to complete the data return process. Vendor shall not withhold, delay, or condition data return on payment of any disputed fees, provided Customer has paid all undisputed amounts then due.

#### (ii) Negotiation Rationale and Fallback Ladder

**Positions mapped:**

| Component | Vendor Opening (6/6) | Customer Opening (6/20) | Vendor Counter (6/30) | **Proposed Compromise** |
|---|---|---|---|---|
| Notice period | No unilateral TFC | 120 days | 180 days | **150 days** |
| ETF | 75% of remaining (standard) | $0 | 50% flat | **Graduated 50%/25%/0%** |
| Transition duration | 12 months | 18 months | 12 months | **12 months** |
| Transition pricing | Standard rates + 15% | At-cost (no markup) | Standard rates + 10% | **Cost + 5%** |
| Data return | 60 days | 30 days | 60 days (45 min) | **45 days (encrypted)** |
| Data formats | Machine-readable | FHIR R4 + HL7 v2 | FHIR R4 feasible; HL7 v2 needs scoping | **FHIR R4 + HL7 v2 (non-negotiable)** |

**Why this landing zone:** The graduated ETF (50%/25%/0%) is the CFO-intelligence framework that both the Delgado memo and Sutter email identify as "workable" and consistent with Sutter's red line that the ETF "must not make exit economically prohibitive at any point in the term." By Year 3, termination is effectively no-cost — satisfying Meridian's need for back-half flexibility. The 150-day notice bridges the customer's 120 and the vendor's 180. Transition at cost + 5% is the Playbook fallback pricing, accepting the vendor's 12-month duration (vs. the customer's preferred 18) as a concession balanced by the cost + 5% pricing (vs. the vendor's standard + 10%). The 45-day data return bridges the customer's 30 and the vendor's 60 (the vendor stated 45 is its operational minimum), with encryption during the period per the Playbook's 60-day-with-encryption condition. FHIR R4 + HL7 v2 is a non-negotiable Playbook red line for MeridianConnect (Epic) interoperability.

**Note on Playbook deviation:** The Playbook's stated red line is "No ETF under any structure," and any ETF requires GC escalation (presumptive rejection). However, the Sutter email (Section IV(d)) and Delgado memo both reframe the red line as "the ETF must not make exit economically prohibitive" and endorse the graduated structure as satisfying that red line. **This proposal therefore requires Dr. Narayanan's approval** as a deviation from the Playbook's no-ETF position, justified by the strategic guidance that the graduated structure is workable and aligns incentives.

**Fallback ladder:**

- **Position A (Proposed):** 150-day notice; graduated ETF 50%/25%/0%; 12-month transition at cost + 5%; 45-day encrypted data return in FHIR R4 + HL7 v2.
- **Position B (if vendor resists 0% in Years 3–4):** 150-day notice; graduated ETF 50%/25%/10% (Year 3)/0% (Year 4); 12-month transition at cost + 5%; 45-day data return. *(Small Year 3 residual; still not economically prohibitive.)*
- **Position C (if vendor resists cost + 5%):** 150-day notice; graduated ETF 50%/25%/0%; 12-month transition at cost + 10% (vendor's counter premium, reduced from 15%); 45-day data return. *(Concede transition markup to preserve 0% back-half ETF.)*
- **Position D (if vendor resists 45-day data return):** 150-day notice; graduated ETF 50%/25%/0%; 12-month transition at cost + 5%; **60-day data return with mandatory encryption + access restrictions + written confirmation no vendor access except for return process** (Playbook fallback). *(Concede timeline; hold encryption + format requirements.)*
- **Absolute floor:** ETF must not make exit economically prohibitive at any point (graduated structure with 0% by Year 3 satisfies this); data return must include FHIR R4 + HL7 v2 export. No position eliminating FHIR R4/HL7 v2 is acceptable.

#### (iii) Acceptability Analysis for Vendor Team

**Sandra Hu (commercial flexibility):** Hu will resist any termination-for-convenience right and any ETF below 50%. **Response:** (1) The graduated ETF directly addresses the CFO's stated revenue-recognition concern — it provides meaningful recovery in Years 1–2 (when implementation investment is being recouped) and steps to zero by Year 3 (when the vendor has recovered its investment and the relationship is recurring-revenue only). (2) The 150-day notice gives the vendor adequate planning runway. (3) This is a balanced package: Meridian concedes a 50% Year 1 ETF (~$12.83M) — a substantial sum — in exchange for back-half flexibility. (4) The cost + 5% transition pricing ensures the vendor is not out-of-pocket for transition assistance, addressing the vendor's margin concern without imposing a punitive exit barrier.

**Rafael Bowen (liability/exposure):** Bowen may be concerned that termination-for-convenience undermines the liability framework. **Response:** Termination rights do not affect the survival of liability, indemnification, confidentiality, or insurance obligations (§16.7), which continue post-termination. The ETF compensates the vendor for lost revenue; it does not waive accrued liability.

#### (iv) Regulatory and Compliance Constraints

- **HIPAA / HITECH:** Data return/destruction (§14.6) must be coordinated with the BAA (Exhibit F), which governs PHI return/destruction upon termination. The 45-day timeline with encryption is consistent with the BAA's PHI-protection obligations. NIST SP 800-88 destruction standards satisfy the BAA's "return or destroy" requirement.
- **NJ AI Healthcare Transparency Act:** Termination does not relieve Meridian of its NJ Act obligations during any period ClinIQ™ remains operational at the 3 NJ facilities. The transition assistance must support continued NJ Act compliance (audit access, documentation) during the Transition Period. The data-return obligation ensures Meridian can produce records to NJ DOH post-termination.
- **FDA:** If ClinIQ™ is subject to FDA regulation at termination, the transition must not disrupt any FDA-mandated post-market surveillance. The transition clause preserves API access and platform operation during the Transition Period to avoid clinical-workflow disruption.
- **Operational/clinical continuity:** The 12-month transition with maintained API access for MeridianConnect (Epic), Philips PACS, and BD Pyxis is essential to avoid disrupting clinical workflows for 6,200 users across 14 hospitals during migration to a successor. The "no data hostage" provision (data not conditioned on disputed-fee payment) protects patient care continuity.

---

### PROPOSAL 4 — AGGREGATED / DE-IDENTIFIED DATA USAGE RIGHTS
**Priority 4 | Matrix Term 4 | §5.1–5.4 | Exhibits D, F**

#### (i) Proposed Contract Clause Language

**§5.4 Aggregated and De-Identified Data Usage.**

> (a) **Permitted Use.** Subject to Vendor's compliance with the de-identification standards in Section 5.3, Vendor may use Aggregated Data and De-Identified Data (collectively, "Derived Data") solely for the purposes of (i) improving, training, and enhancing the Platform and Vendor's AI/ML models, and (ii) internal benchmarking. Vendor shall not use Derived Data for commercial sale to third parties, for unrelated product lines, or for marketing purposes. "Aggregated Data" means data combined with data from at least two (2) other unaffiliated sources such that the Meridian-specific contribution is not separately extractable. "De-Identified Data" means data meeting the HIPAA Safe Harbor (45 C.F.R. § 164.514(b)(2)) or Expert Determination (45 C.F.R. § 164.514(b)(1)) standard, with the burden of demonstrating compliance resting on Vendor.
>
> (b) **Opt-Out Right.** Customer may elect to opt out of Vendor's use of Derived Data under subsection (a) at any time by providing written notice to Vendor. The opt-out shall take effect **thirty (30) days** following Vendor's receipt of the notice. The opt-out right is not subject to any cure period, notice of deficiency, or Vendor consent, and may be exercised for any reason or no reason.
>
> (c) **Verified Deletion.** Upon the effective date of an opt-out notice, Vendor shall: (i) delete all Derived Data derived from Customer Data that has **not yet been incorporated** into trained models or derivative works, within sixty (60) days, and certify such deletion in writing, signed by an officer of Vendor, within five (5) business days of completion; and (ii) with respect to Derived Data **already incorporated** into trained models or derivative works, Vendor shall, within one hundred eighty (180) days, either (A) retrain the affected models without Meridian-derived data and certify that the Meridian contribution has been eliminated, or (B) if Vendor demonstrates to Customer's reasonable satisfaction that retraining is technically infeasible, segregate and quarantine the Meridian-influenced model components such that no commercial deployment, sale, or transfer of Meridian-specific adaptations to any third party occurs, and certify such segregation in writing. Vendor shall not deploy, sell, license, or transfer any model adaptation that incorporates Meridian-derived data to any third party following the opt-out effective date.
>
> (d) **Transparency and Documentation.** Vendor shall maintain records identifying the sources of Derived Data used for model improvement, with sufficient detail to determine the Meridian contribution. Vendor shall provide Customer with an annual summary report (by March 31 of each year) describing the categories of use to which Meridian-derived Derived Data has been applied. Vendor shall document any use of Meridian-derived data in the transparency materials provided under Section 10.1 and shall update training data provenance documentation to reflect any retraining incorporating Meridian-derived data, consistent with the NJ AI in Healthcare Transparency Act.
>
> (e) **No Implied License; No Sale.** Nothing in this Agreement grants Vendor any implied license to use Customer Data, Aggregated Data, or De-Identified Data except as expressly set forth in this Section 5.4. Vendor shall not sell, rent, lease, or otherwise commercially exploit Customer Data or Derived Data, except as expressly authorized herein.

#### (ii) Negotiation Rationale and Fallback Ladder

**Positions mapped:**

| Component | Vendor Opening (6/6) | Customer Opening (6/20) | Vendor Counter (6/30) | **Proposed Compromise** |
|---|---|---|---|---|
| Vendor use right | Unrestricted (training, benchmarking, product dev, commercial) | None without per-use-case consent | 60-day opt-out; prospective-only deletion | **Model improvement + benchmarking only; 30-day opt-out; verified deletion (retraining/segregation alternative)** |
| Opt-out notice | 90 days (standard) / 60 days (counter) | N/A (consent-based) | 60 days | **30 days (Playbook fallback)** |
| Deletion scope | Prospective only | Verified deletion incl. incorporated | Prospective only (unincorporated deleted) | **Unincorporated: delete within 60 days; Incorporated: retrain within 180 days or segregate/quarantine** |
| Permitted purposes | Broad (incl. commercial, product dev) | None without consent | Model improvement + benchmarking + product dev | **Model improvement + benchmarking only (no commercial sale, no unrelated products)** |

**Why this landing zone:** This is the Playbook fallback (§6.3) with a creative deletion mechanism that addresses the vendor's "technical infeasibility" argument while holding Meridian's substantive protections. Data usage is the vendor's **highest-priority commercial term** and Meridian's **Priority 4** — the asymmetry that makes this Meridian's primary concession currency. The proposal grants the vendor a meaningful, ongoing right to use aggregated/de-identified data for model improvement (the vendor's core need) but bounds it to model improvement + benchmarking (excluding commercial sale and unrelated products), holds the 30-day opt-out (Playbook fallback / red line), and replaces the binary "delete incorporated data or nothing" impasse with a two-track deletion mechanism: (1) delete unincorporated data within 60 days, and (2) for incorporated data, either retrain without Meridian data within 180 days or, if retraining is genuinely infeasible, segregate/quarantine Meridian-influenced components and prohibit their commercial deployment/transfer. This is the "alternative mechanism" the Playbook (§6.4(b)) expressly contemplates when retroactive deletion is technically infeasible.

**Concession strategy:** Per the Delgado memo, Meridian should **hold this position through the early rounds** and deploy concessions here in exchange for movement on Priorities 1–3. The opening compromise (Position A) holds the 30-day opt-out and the retraining/segregation deletion mechanism. If the vendor makes meaningful concessions on patient-safety (Priority 1), audit (Priority 2), or termination (Priority 3), Meridian can relax the opt-out window (Positions B/C) as the trade.

**Fallback ladder:**

- **Position A (Proposed):** Model improvement + benchmarking only; 30-day opt-out; unincorporated deletion (60 days) + incorporated retraining (180 days) or segregation/quarantine; no commercial sale.
- **Position B (concede opt-out window — requires GC + VP approval as > 30 days):** Same as A but **45-day opt-out**. *(Deploy if vendor concedes on Priorities 1–3.)*
- **Position C (maximum concession — requires GC + VP approval):** Same as A but **60-day opt-out** (vendor's counter); incorporated-data deletion limited to segregation/quarantine (no retraining mandate) + binding prohibition on commercial deployment/transfer of Meridian-specific adaptations. *(Deploy only for significant vendor concessions on Priorities 1–3.)*
- **Absolute floor (red lines):** No unrestricted use; no opt-out exceeding 30 days without GC + VP escalation; no purely prospective-only deletion with no mechanism for incorporated data (the retraining-or-segregation alternative satisfies this). Any opt-out > 30 days requires escalation to Marcus Delgado (VP) + Dr. Narayanan (GC).

#### (iii) Acceptability Analysis for Vendor Team

**Sandra Hu (commercial flexibility — this is the vendor's highest-priority term):** Hu will push hard for unrestricted use, a 60–90 day opt-out, and prospective-only deletion. **Response:** (1) Meridian is granting the vendor a **meaningful, ongoing right** to use aggregated/de-identified data for model improvement — the vendor's core commercial need — rather than the customer's opening position of per-use-case consent (which would have effectively blocked the vendor's data pipeline). This is a substantial concession from Meridian's opening. (2) The 30-day opt-out is a *right*, not an expectation — Meridian does not intend to exercise it absent a specific concern; it preserves Meridian's control over its exceptionally valuable 14-hospital, 2.1M-encounter dataset. (3) The retraining-or-segregation mechanism is a *pragmatic alternative* to immediate retroactive deletion, which Meridian acknowledges is technically challenging — it gives the vendor a realistic path (180-day retraining) rather than an impossible one, while preserving Meridian's substantive protection (no commercial deployment of Meridian-specific adaptations post-opt-out). (4) Bounding use to model improvement + benchmarking (excluding commercial sale) is consistent with the vendor's own stated primary purpose ("model improvement pipeline"). (5) Frame the package: Meridian's flexibility here is the consideration for vendor movement on patient-safety, audit, and termination.

**Rafael Bowen (IP/liability):** Bowen may be concerned that the retraining obligation creates operational burden. **Response:** The 180-day retraining window is generous, and the segregation/quarantine alternative provides an off-ramp if retraining is genuinely infeasible. The vendor retains ownership of all model IP; this provision governs *use* of Meridian-derived data, not IP ownership.

#### (iv) Regulatory and Compliance Constraints

- **HIPAA de-identification:** The clause requires de-identification per Safe Harbor (45 C.F.R. § 164.514(b)(2)) or Expert Determination (§ 164.514(b)(1)), with the burden on Vendor. The Expert Determination certifying expert must be independent and pre-approved by Meridian (Langford pre-approved per Exhibit D §3.3.2). The prohibition on re-identification (Exhibit D §3.3.4) applies.
- **NJ AI Healthcare Transparency Act:** The Act's transparency requirements (§4) extend to how training data is sourced and used. If the vendor uses Meridian-derived data to retrain the model, this must be documented and Meridian must have access to updated transparency documentation (§10.1). The clause's documentation requirement (subsection (d)) ensures NJ Act compliance. The Act's data-governance vendor-contracting requirement (§7(a)(3)) is satisfied by the Exhibit D framework, which this clause complements.
- **BAA (Exhibit F) coordination:** This clause governs de-identified/aggregated data; the BAA governs PHI. The order of precedence (Exhibit D §9.2) ensures the BAA controls on PHI-specific matters. The de-identification standards are consistent across both.
- **State privacy laws:** The "no sale" provision (subsection (e)) is drafted to satisfy "sale" definitions under the CCPA, Colorado Privacy Act, and analogous state laws, regardless of direct applicability.

---

### PROPOSAL 5 — SLA / AI ACCURACY BENCHMARKS
**Priority 5 | Matrix Term 6 | §9.1–9.4 | Exhibit C**

#### (i) Proposed Contract Clause Language

**§9.3 AI Model Accuracy — Binding Performance Benchmarks.**

> (a) **Binding Benchmarks.** Vendor warrants that the Platform's clinical decision-support modules shall meet or exceed the following minimum Performance Benchmarks, measured on a quarterly basis using the validation methodology set forth in Exhibit C:

| Clinical Module | Sensitivity (Minimum) | Specificity (Minimum) |
|---|---|---|
| Sepsis Prediction | ≥ 92% | ≥ 88% |
| Radiology Triage | ≥ 90% | ≥ 85% |
| Medication-Interaction Alerts | ≥ 95% | ≥ 90% |

> (b) **Measurement Methodology.** Benchmarks shall be measured quarterly using a prospective evaluation methodology based on actual clinical encounters during the measurement quarter, with a statistically significant random sample (minimum sample size per NIST AI 100-1 guidelines) drawn from all 14 Covered Facilities, and a 95% confidence interval reported for all metrics. Validation shall be performed by the Independent Auditor (Langford AI Assurance Group) at Tier 2 access. A benchmark "miss" occurs only where the measured metric falls below the threshold by more than one (1) percentage point and outside the 95% confidence interval, to account for inherent statistical variability in clinical AI performance.
>
> (c) **Escalating Service Credits.** If any module fails to meet its Benchmark in a given quarter (as defined in subsection (b)), Vendor shall credit Customer against the next quarterly invoice: (i) **five percent (5%)** of quarterly fees (~$106,875) for the first quarterly miss; (ii) **ten percent (10%)** (~$213,750) for the second consecutive quarterly miss of the same module; and (iii) **fifteen percent (15%)** (~$320,625) for the third or subsequent consecutive quarterly miss of the same module. Credits are cumulative for consecutive misses and reset to 5% after any quarter in which the Benchmark is met. Aggregate quarterly credits (uptime + response-time + accuracy) shall not exceed twenty percent (20%) of quarterly fees (~$427,500), exclusive of termination rights.
>
> (d) **Remediation Plan.** Vendor shall submit a written remediation plan to Customer within fifteen (15) business days of each quarterly miss, identifying the root cause, corrective actions, expected timeline, and interim risk-mitigation measures. Customer's clinical informatics team shall approve the remediation plan within ten (10) business days.
>
> (e) **Termination for Persistent Failure.** If any module fails to meet its Benchmark for **three (3) consecutive calendar quarters**, Customer shall have the right to terminate this Agreement for cause upon sixty (60) days' written notice, without early termination fee, with transition assistance under Section 14.5. This right is in addition to, and does not limit, Customer's other termination rights.

#### (ii) Negotiation Rationale and Fallback Ladder

**Positions mapped:**

| Component | Vendor Opening (6/6) | Customer Opening (6/20) | Vendor Counter (6/30) | **Proposed Compromise** |
|---|---|---|---|---|
| Benchmark status | Informational only; CRE | Binding | Non-binding targets; improvement plan | **Binding (with materiality threshold)** |
| Credits | None for accuracy | 5%–15% escalating | None | **5%/10%/15% escalating** |
| Termination trigger | None (general breach only) | 2 consecutive misses | None (executive escalation) | **3 consecutive misses** |
| Aggregate cap | 10% monthly (uptime) | 25% quarterly | 15% quarterly | **20% quarterly (exclusive of termination)** |

**Why this landing zone:** This is the Playbook fallback (§8.3): binding benchmarks with escalating credits and termination after 3 consecutive quarterly misses. The Sutter email directs: "Push for binding benchmarks but be prepared to accept the 3-miss termination trigger per playbook." The benchmarks themselves (sepsis ≥92%/≥88%, radiology ≥90%/≥85%, med-interaction ≥95%/≥90%) are not subject to negotiation under the fallback — they are clinically calibrated by Meridian's CMO. The **materiality threshold** (subsection (b): a miss counts only if >1 percentage point below threshold and outside the 95% CI) is the calibrated concession that addresses the vendor's central objection — that "accuracy metrics cannot be binding given inherent variability in clinical AI." By requiring statistical significance and a materiality floor, the compromise makes the benchmarks binding *while accommodating legitimate variability*, neutralizing the vendor's "commercially reasonable efforts is industry standard" argument. The aggregate quarterly cap of 20% bridges the vendor's 15% and the customer's 25%.

**Fallback ladder:**

- **Position A (Proposed):** Binding benchmarks with materiality threshold; 5%/10%/15% escalating credits; 3-miss termination; 20% aggregate quarterly cap.
- **Position B (if vendor resists termination trigger):** Binding benchmarks with materiality threshold; 5%/10%/15% credits; **termination after 3 consecutive misses OR executive escalation to a joint SLA Governance Committee with binding remediation milestones after the 3rd miss, escalating to termination if milestones are not met within 90 days.** *(Adds a remediation off-ramp before termination.)*
- **Position C (if vendor resists binding status):** **"Binding subject to documented data-quality / population-shift causation"** — benchmarks are binding, but Vendor may avoid a miss by demonstrating, with documented evidence reviewed by Langford, that the shortfall was caused by Customer data-quality issues or population-mix changes beyond Vendor's control. *(Addresses vendor's data-quality concern while keeping benchmarks binding.)*
- **Absolute floor (red line):** Benchmarks must be **binding**, not informational or aspirational. Minimum termination trigger is 3 consecutive quarterly misses — no further concession. Any position reducing benchmarks to informational must be rejected.

#### (iii) Acceptability Analysis for Vendor Team

**Sandra Hu (commercial flexibility):** Hu will resist binding benchmarks and accuracy-based credits, arguing model variability makes binding commitments inappropriate. **Response:** (1) The **materiality threshold** directly addresses the variability concern — a miss is not triggered by statistical noise, only by a material, statistically significant shortfall. This is a meaningful accommodation that the vendor's "commercially reasonable efforts" position does not offer in return. (2) Binding benchmarks with consequences are standard for clinical decision-support tools that directly influence patient care across 2.1M annual encounters — "informational only" is not a defensible posture for a sepsis early-warning system. (3) The 3-miss termination trigger (vs. the customer's opening of 2) gives the vendor a full extra quarter to remediate before termination exposure arises. (4) The 20% aggregate cap limits the vendor's credit exposure. (5) Validation by Langford (an independent auditor the vendor has pre-approved) ensures measurement integrity and neutrality.

**Rafael Bowen (liability):** Bowen may be concerned that binding benchmarks create a breach-of-warranty cause of action that interacts with the liability framework. **Response:** The credits and termination right are the *agreed remedies* for benchmark misses (§9.4 sole-remedy framing), bounded by the aggregate cap, and do not automatically trigger uncapped liability. The patient-safety super-cap (Proposal 1) addresses any patient-harm claims arising from accuracy failures separately.

#### (iv) Regulatory and Compliance Constraints

- **NJ AI Healthcare Transparency Act:** The Act's annual audit (§5(b)(2)) requires "assessment of validation results and ongoing performance metrics." Binding benchmarks with quarterly measurement and Langford validation directly support this statutory requirement and provide the documentation Meridian must maintain and produce to NJ DOH. The bias/fairness component of the benchmarks (reported quarterly in the Transparency Report) supports the Act's bias-evaluation requirement (§5(b)(3)).
- **FDA clinical decision-support guidance:** Binding accuracy benchmarks are consistent with FDA post-market surveillance expectations for AI/ML-based SaMD (predetermined change control plans, performance monitoring). If ClinIQ™ becomes subject to FDA regulation, the benchmark framework supports compliance. The measurement methodology (prospective, statistically significant, 95% CI) aligns with FDA validation expectations.
- **Patient safety:** The sepsis module's high sensitivity threshold (≥92%) reflects the clinical reality that false negatives (missed sepsis) carry greater patient-safety risk than false positives. Binding benchmarks are the contractual mechanism that ensures the platform's clinical performance matches its patient-safety significance — directly supporting Meridian's Tier 1 enterprise risk management.
- **Clinical governance:** The remediation-plan requirement (subsection (d)) and clinical informatics team approval ensure that performance failures trigger clinical governance review, not just financial credits.

---

### PROPOSAL 6 — IP OWNERSHIP (MODEL WEIGHTS, FINE-TUNED ADAPTATIONS)
**Priority 6 | Matrix Term 2 | §6.1–6.5 | Article 6**

#### (i) Proposed Contract Clause Language

**§6.1 Vendor IP.** Vendor retains all right, title, and interest in and to the Platform, the Base Model, all base model architectures, pre-trained neural network weights and parameters existing prior to or independently of Customer's engagement, Vendor's proprietary training data and validation datasets that do not incorporate Customer Data, all source code, algorithms, and Documentation. No transfer of ownership of any Vendor IP is intended or effected under this Agreement.

**§6.2 Fine-Tuned Models and Derivative Data — Vendor Ownership with Irrevocable Perpetual License and Functional Portability.**

> (a) **Vendor Ownership.** All fine-tuned model weights, parameters, configurations, embeddings, and Derivative Data generated through the operation of the Platform are and shall remain the sole and exclusive property of Vendor, regardless of whether Customer Data was used in the fine-tuning, training, or generation process.
>
> (b) **Irrevocable Perpetual Output and Derivative-Data License.** Vendor hereby grants Customer a non-exclusive, **perpetual, irrevocable, royalty-free, fully paid-up** license to use, copy, modify, distribute (internally), and create derivative works from all Outputs and derivative data sets (excluding base model weights, parameters, embeddings, and model architecture) generated by the Platform using Customer Data, for any purpose, including use in connection with any successor platform or clinical decision-support system following termination or expiration of this Agreement. This license shall survive termination or expiration of this Agreement for any reason, including termination for cause by Vendor, and may not be revoked.
>
> (c) **Functional Portability.** Upon termination or expiration of this Agreement for any reason, Vendor shall provide Customer with **functional portability** to enable Customer to transition to a successor platform and recreate equivalent fine-tuned model behavior using Customer Data, including: (i) export of all Customer Data and Outputs in FHIR R4 and HL7 v2 interoperable formats; (ii) delivery of documentation sufficient to recreate equivalent fine-tuned model performance, including the fine-tuning methodology, configuration parameters, training data composition (de-identified), and validation results; (iii) maintained API access during the Transition Period (Section 14.5); and (iv) reasonable technical assistance and knowledge transfer to Customer or its successor vendor. Vendor acknowledges that Customer's clinical data, workflows, and clinician feedback contributed substantial value to any fine-tuned adaptations, and that functional portability is essential to prevent vendor lock-in.
>
> (d) **No Reverse Engineering.** The foregoing license and portability rights do not authorize Customer to reverse-engineer, reconstruct, or derive the Base Model or Vendor's pre-existing proprietary technology. Customer's rights are limited to the fine-tuned layer and derivative data generated from Customer Data.

**§2.4 Output License** (conforming amendment): Customer is granted a non-exclusive, perpetual, irrevocable, royalty-free license to use, store, reproduce, display, and distribute Outputs generated by the Platform for Customer's internal clinical, operational, regulatory, legal, compliance, and quality-improvement purposes, including use with any successor platform following termination. The Output License survives termination or expiration for any reason.

#### (ii) Negotiation Rationale and Fallback Ladder

**Positions mapped:**

| Component | Vendor Opening (6/6) | Customer Opening (6/20) | Vendor Counter (6/30) | **Proposed Compromise** |
|---|---|---|---|---|
| Fine-tuned weight ownership | Vendor | Customer | Vendor ("technically inseparable") | **Vendor** |
| Output/derivative-data license | Non-exclusive, term-limited | Customer ownership | Perpetual irrevocable (excl. weights) | **Perpetual, irrevocable (excl. base weights)** |
| Portability | None | Full weight export + portability | Customer Data only; no weight portability | **Functional portability (data + methodology docs + API + assistance)** |
| Survival | Terminates on agreement termination | Survives | Perpetual for outputs/data sets | **Perpetual, irrevocable; survives termination for any reason** |

**Why this landing zone:** This is the Playbook's **second (final) fallback** (§4.4): Vendor ownership with irrevocable perpetual license + portability. Both the Delgado memo and Sutter email explicitly recommend accepting this fallback: "Raw weight access/ownership is the CTO's 'hard no' — this is not where we should spend negotiation capital, and the perpetual license with portability gives us what we functionally need" (Delgado); "focus on securing the irrevocable perpetual license with portability rights rather than fighting for ownership — that's where the practical value lies for Meridian" (Sutter). The vendor's June 30 counter already concedes a perpetual, irrevocable license for Outputs and derivative data sets — the compromise extends this to **functional portability** (methodology documentation, configuration parameters, API access, technical assistance) so that Meridian can recreate equivalent fine-tuned behavior with a successor without requiring export of raw weights (which the CTO blocks). This respects the CTO's "hard no" on raw weight export while giving Meridian the functional equivalent of portability.

**Note on Playbook conformance:** The Playbook's final fallback requires "full portability rights, including the right to export fine-tuned model weights and run them on alternative infrastructure." The proposed "functional portability" (recreation via methodology + data + assistance, rather than raw weight export) is a pragmatic operationalization of portability given the CTO's hard no. **This requires Dr. Narayanan's approval** as it is at the final-fallback level and involves a portability mechanism that differs from raw weight export. If the vendor refuses even functional portability, the matter must be escalated to GC (potential deal termination per Playbook §4.4).

**Fallback ladder:**

- **Position A (Proposed):** Vendor ownership; irrevocable perpetual output/derivative-data license; functional portability (data + methodology docs + API + assistance); survives termination for any reason.
- **Position B (if vendor resists functional portability documentation):** Vendor ownership; irrevocable perpetual output/derivative-data license; portability limited to Customer Data + Outputs export (FHIR R4/HL7 v2) + API access during Transition Period + reasonable technical assistance (no methodology documentation). *(Reduced portability; still enables transition.)*
- **Position C (if vendor resists irrevocable license):** Vendor ownership; **perpetual (but revocable only for uncured material breach by Customer)** output/derivative-data license; functional portability. *(Narrow revocation right tied to Customer breach, not unilateral vendor termination.)*
- **Absolute floor (red line):** Must include an irrevocable/perpetual license to Outputs and derivative data + meaningful portability rights. If the vendor refuses both perpetual license and portability, escalate to GC (Playbook §4.4: potential deal termination).

#### (iii) Acceptability Analysis for Vendor Team

**Rafael Bowen (IP protection — the CTO's "hard no"):** Bowen will resist any portability that touches model weights. **Response:** (1) This proposal **accepts Vendor ownership of all model IP, including fine-tuned weights** — Meridian is not seeking weight ownership or raw weight export, respecting the CTO's hard no. (2) The irrevocable perpetual license covers **Outputs and derivative data sets, excluding base model weights, parameters, embeddings, and architecture** — exactly the scope the vendor's own June 30 counter already offered. (3) "Functional portability" does **not** require export of raw weights — it requires data export, methodology documentation, API access, and technical assistance, all of which the vendor already provides during transition (§14.5). The only incremental ask is the fine-tuning methodology documentation, which is necessary for a successor to recreate equivalent performance and does not expose the base model. (4) The no-reverse-engineering clause (subsection (d)) protects the Base Model. (5) This is the Playbook's final fallback — Meridian is conceding ownership entirely; the perpetual license + functional portability is the minimum Meridian needs to avoid vendor lock-in.

**Sandra Hu (commercial flexibility):** Hu may be concerned that the irrevocable perpetual license undermines the vendor's ability to terminate. **Response:** The license is for Outputs and derivative data *already generated* — it does not obligate the vendor to generate new outputs post-termination. It simply ensures Meridian can continue using what it already received, which is essential for medical-record retention and clinical continuity.

#### (iv) Regulatory and Compliance Constraints

- **NJ AI Healthcare Transparency Act:** The Act does not require Meridian to own model weights. It requires documentation access (§4, §7(a)(1)) and audit rights (§7(a)(2)) — both addressed by Proposal 2. The IP ownership concession is therefore consistent with NJ Act compliance, provided the audit/transparency framework (Proposal 2) is in place. The Delgado memo conditions acceptance of this fallback on the Langford audit framework being secured.
- **HIPAA:** Derivative data sets that contain PHI remain subject to the BAA. The perpetual license does not authorize disclosure of PHI beyond what HIPAA permits.
- **FDA:** If ClinIQ™ is FDA-regulated, the methodology documentation provided under functional portability supports any regulatory transfer/recreation obligations. The no-reverse-engineering clause does not impede FDA-mandated transparency.
- **Vendor lock-in / antitrust:** Functional portability is the contractual mechanism that prevents the relationship from becoming a dependency. Without it, the cost of switching vendors could become prohibitive — the precise outcome the Playbook (§4.1) is designed to prevent.

---

### PROPOSAL 7 — INDEMNIFICATION SCOPE & DEFENSE PROCEDURE
**Priority 7 | Matrix Term 5 | §13.1–13.7 | Exhibits F, G; Article 15**

#### (i) Proposed Contract Clause Language

**§13.1 Vendor Indemnification — Scope.** Vendor shall indemnify, defend, and hold harmless Customer and its Affiliates, officers, directors, employees, agents, and medical staff members (collectively, "Customer Indemnitees") from and against any and all third-party claims, governmental investigations, regulatory enforcement actions, suits, proceedings, demands, judgments, damages, liabilities, penalties, fines, losses, costs, and expenses (including reasonable attorneys' fees and expert witness fees) (collectively, "Losses") arising out of or related to:

> (a) **IP Infringement Claims** — any allegation that Customer's authorized use of the Platform infringes or misappropriates any third-party patent, copyright, trademark, or trade secret;
>
> (b) **Data Breach Claims** — any claim, regulatory action, or proceeding arising from a Security Incident or Breach of Unsecured PHI (as defined in the BAA) attributable to Vendor, its subprocessors, or its systems, including notification costs, credit monitoring, forensic investigation, and regulatory fines;
>
> (c) **Patient-Harm Claims (AI-Output Error)** — any claim, suit, or proceeding by or on behalf of a patient, patient's family member, or estate alleging bodily injury, adverse clinical outcome, wrongful death, or emotional distress arising from or related to any Output, recommendation, alert, risk score, or clinical decision-support result generated by the Platform, **where the proximate cause of the patient harm is an erroneous, misleading, biased, delayed, or otherwise deficient AI-generated Output** (i.e., claims directly attributable to AI-output error, as distinguished from claims arising from clinician override or independent clinical judgment); and
>
> (d) **Regulatory Penalty Claims (NJ Act)** — any civil penalty, fine, or enforcement action assessed against Customer under the NJ AI in Healthcare Transparency Act to the extent such penalty arises from or is attributable to Vendor's breach of its documentation, audit-cooperation, or regulatory-cooperation obligations under this Agreement.

**§13.5 Defense Control — Shared Defense for Patient-Safety Claims.**

> (a) **General.** For IP Infringement Claims (§13.1(a)) and Data Breach Claims (§13.1(b)), Vendor shall have primary control of the defense and settlement, provided no settlement shall impose liability or admit fault on behalf of Customer without Customer's prior written consent (not to be unreasonably withheld).
>
> (b) **Patient-Harm Claims — Vendor Primary for AI-Output Errors.** For Patient-Harm Claims under §13.1(c) where the proximate cause is an AI-output error, Vendor shall be primarily responsible for the defense and indemnification, and shall bear the cost of defense and indemnity. Customer shall have the right to participate with counsel of its own choosing and shall have consent rights over any settlement that affects Customer's clinical reputation, regulatory standing, or patient relationships. Vendor shall not settle any such claim without Customer's prior written consent.
>
> (c) **Clinician-Override Claims — Customer Primary.** For claims arising from clinician override or independent clinical judgment (where a clinician received a correct AI Output but chose not to follow it, or where the clinician's independent decision-making was the proximate cause), Customer shall be primarily responsible for the defense and indemnification.
>
> (d) **Mixed-Causation Claims.** For claims involving both AI-output error and clinician judgment, the Parties shall cooperate in good faith in a shared defense, each bearing its proportionate share of defense costs and indemnification obligations. Failing agreement, allocation shall be determined through the dispute resolution process in Section 16.2.

**§13.7 Indemnification Cap.** Vendor's aggregate liability under this Article 13 shall not exceed the Super-Cap set forth in Section 12.3 (3× trailing 12-month fees, ~$28.8M as of the first Contract Year). The regulatory penalty indemnification under §13.1(d) is included within the Super-Cap and is not subject to the General Cap.

**§13.8 Insurance Backstop (cross-reference to §15.1).** Vendor's indemnification obligations under this Article 13 are backstopped by the insurance coverage required under Article 15, including the binding commitment to increase Cyber/E&O coverage to $30M per occurrence / $60M aggregate (§15.1(c)). Vendor shall provide certificates of insurance annually and upon material change, naming Meridian as additional insured on CGL and Umbrella policies.

#### (ii) Negotiation Rationale and Fallback Ladder

**Positions mapped:**

| Component | Vendor Opening (6/6) | Customer Opening (6/20) | Vendor Counter (6/30) | **Proposed Compromise** |
|---|---|---|---|---|
| Scope | IP only | IP + regulatory + patient harm + data breach | IP + data breach (declines patient-harm, regulatory) | **IP + data breach + patient-harm (AI-output error) + NJ Act regulatory penalties** |
| Defense control | Vendor controls all | Customer controls patient-safety | Shared (each bears own costs) | **Shared: Vendor primary for AI-output errors; Customer primary for clinician-override; mixed = proportionate** |
| Cap | General cap (dollar-for-dollar) | Excluded from general cap (uncapped) | Super-cap (3×) | **Super-cap (3× ACV, ~$28.8M)** |

**Why this landing zone:** This is the Playbook fallback (§7.2): shared defense with Vendor primary for AI-output claims, subject to the super-cap. Indemnification is Meridian's **lowest priority (7)** and the "most readily tradeable" category (Playbook §7.3). The compromise accepts the vendor's super-cap backstop (3× ACV, consistent with Proposal 1) and the vendor's willingness to add data breach to IP. The critical hold is **patient-harm inclusion** — the Playbook red line requires "patient harm + IP at minimum." The compromise narrows patient-harm to **AI-output-error claims** (where proximate cause is the AI output), directly addressing the vendor's argument that patient-harm is "clinical malpractice outside the software vendor's scope" — claims arising from clinician override or independent judgment remain Customer's responsibility (subsection (c)). This is a calibrated scope that gives the vendor meaningful relief (no blanket patient-harm indemnity) while preserving Meridian's core protection (vendor stands behind its AI outputs). The NJ Act regulatory-penalty indemnification (subsection (d)) is supported by the NJ Act analysis: penalties are assessed against Meridian, and if attributable to the vendor's breach of documentation/audit/cooperation obligations, Meridian's only recourse is contractual.

**Fallback ladder:**

- **Position A (Proposed):** IP + data breach + patient-harm (AI-output error) + NJ Act regulatory penalties; shared defense (vendor primary for AI-output); super-cap (3×).
- **Position B (if vendor resists patient-harm scope):** IP + data breach + patient-harm (AI-output error, **with a sub-cap or deductible for patient-harm claims** to limit vendor exposure per claim) + NJ Act regulatory penalties; shared defense; super-cap. *(Add a per-claim patient-harm threshold to address vendor exposure concern.)*
- **Position C (if vendor resists NJ Act regulatory penalties):** IP + data breach + patient-harm (AI-output error); NJ Act regulatory penalties **subject to the general cap rather than the super-cap** (reduced backstop); shared defense; super-cap for IP/data breach/patient-harm. *(Concede regulatory-penalty cap level; hold patient-harm inclusion.)*
- **Absolute floor (red line):** Must include patient-harm (at least AI-output-error scope) + IP at minimum. Indemnification never less than the super-cap floor (3× ACV). Any trade-off that eliminates patient-harm indemnification entirely must be escalated to the GC (Playbook §7.3).

**Trade-off guidance (Playbook §7.3):** If the vendor offers meaningful concessions on patient-safety liability (Priority 1) or audit rights (Priority 2), moderate flexibility on indemnification scope is acceptable. For example, if the vendor accepts the 3× patient-safety super-cap (Proposal 1) in exchange for narrowing patient-harm indemnification to AI-output-error claims only (excluding clinician-override), this trade is favorable under the priority ranking.

#### (iii) Acceptability Analysis for Vendor Team

**Rafael Bowen (liability exposure):** Bowen will resist patient-harm and regulatory indemnification, arguing these are outside a software vendor's scope. **Response:** (1) The patient-harm indemnification is **narrowly scoped to AI-output-error claims** — where the proximate cause is a deficient AI Output — not blanket patient-harm. This directly addresses the vendor's "clinical malpractice" objection: claims arising from clinician override or independent judgment remain Customer's responsibility. The vendor is being asked to stand behind *its own product's outputs*, which is the core premise of selling clinical decision-support software. (2) The super-cap (3× ACV, ~$28.8M) bounds the exposure and is backstopped by the insurance commitment. (3) The NJ Act regulatory-penalty indemnification is limited to penalties *attributable to the vendor's breach* of its own documentation/audit/cooperation obligations — if the vendor performs its obligations, there is no indemnification exposure. This is a "pay for your own breach" provision, not a blanket penalty transfer. (4) The shared-defense structure gives the vendor primary control of AI-output claims (its area of expertise) while preserving Customer's participation and consent rights for claims affecting clinical reputation.

**Sandra Hu (commercial flexibility / precedent):** Hu may be concerned about precedent for patient-harm indemnification. **Response:** (1) The AI-output-error scoping is a *narrower* patient-harm indemnity than Meridian's opening (which covered all patient harm), and is justified by the specific facts (clinical AI deployed at scale). (2) The super-cap backstop and insurance commitment make the exposure bounded and insurable. (3) This is the Playbook's fallback position, not the standard — Meridian is already conceding from its opening (uncapped, customer defense control) to a capped, shared-defense structure.

#### (iv) Regulatory and Compliance Constraints

- **NJ AI Healthcare Transparency Act:** Civil penalties (up to $50,000/violation, per-day accrual) are assessed against Meridian as the covered entity, not the vendor. The NJ Act analysis (Section IV.E) recommends that the Agreement expressly address allocation of penalty exposure arising from the vendor's failure to provide required documentation, audit access, or cooperation. The §13.1(d) regulatory-penalty indemnification implements this recommendation. The anti-waiver provision (§10.5) ensures the indemnification does not limit Meridian's statutory rights.
- **HIPAA / HITECH:** The data-breach indemnification (§13.1(b)) is coordinated with the BAA (Exhibit F), which governs breach-notification obligations. The 24-hour breach-notification standard (Meridian BAA position) is preserved. The indemnification covers breach costs (notification, credit monitoring, forensic investigation, regulatory fines) attributable to the vendor.
- **FDA:** If ClinIQ™ is FDA-regulated, the regulatory-penalty indemnification framework extends to FDA enforcement actions attributable to the vendor's failure to maintain clearances (Playbook §10.3(d)). Recommend conforming language to capture FDA enforcement actions attributable to vendor non-compliance.
- **Board Risk Committee (Tier 1):** The indemnification terms will be briefed to the Board Risk Committee before execution. The patient-harm indemnification (AI-output-error scope) and the super-cap backstop are the minimum defensible structure for the Board briefing. The insurance commitment (§15.1(c)) is essential to the Board's collectability analysis.
- **Insurance collectability:** The indemnification is only valuable if collectable. The current $25M/$50M coverage gap against a $28.8M super-cap is addressed by the §15.1(c) binding coverage-increase commitment (cross-referenced in §13.8). Without the insurance commitment, the indemnification backstop is incomplete.

---

## III. CROSS-CUTTING ISSUE: INSURANCE COVERAGE GAP

The insurance gap ($25M/$50M current vs. $30M/$60M required; delta +$5M occ / +$10M agg) cuts across Proposals 1 (liability) and 7 (indemnification). The vendor's current Northfield Mutual policy (NM-CY-2025-04417) falls below Meridian's Playbook minimum (§11.1). The vendor is evaluating an increase at its 2026 renewal but resists a binding contractual floor.

**Recommended approach (Playbook §11.2):** Do not waive the insurance minimum. Instead, secure a **time-limited gap with a binding coverage-increase commitment and step-in rights**, as drafted in §15.1(c) of Proposal 1:

1. Vendor covenants to increase Cyber/E&O to $30M/$60M by the earlier of the next policy renewal or 12 months post-execution.
2. During the gap, vendor provides broker confirmation that the increase has been requested and is reasonably expected.
3. If the vendor fails to obtain the coverage by the deadline, Meridian may (A) obtain supplemental coverage at vendor's expense, (B) withhold up to 10% of quarterly fees in escrow, or (C) terminate for convenience without ETF.
4. Carrier must be rated A- or better by A.M. Best; certificates provided annually; Meridian named additional insured on CGL and Umbrella policies; 30-day cancellation notice required.

This structure is the only acceptable approach to a vendor coverage shortfall (Playbook §11.2). Jessica and David should flag this explicitly in the regulatory/compliance sections of Proposals 1 and 7.

---

## IV. BOARD RISK COMMITTEE BRIEFING — REQUIRED BEFORE EXECUTION

The Board Risk Committee has classified AI-related liability as a **Tier 1 enterprise risk**. Per Playbook §12.1 and §2.6, any AI/technology agreement with TCV exceeding $10M (this Agreement: $38.4M) must be briefed to the Board Risk Committee before execution. The briefing (target: week of August 4, 2025) must include:

1. Summary of key commercial terms (ACV, TCV, term length).
2. Summary of liability/risk allocation: general cap (1.5× ACV, ~$14.4M), super-cap (3× ACV, ~$28.8M, including patient-safety), and any deviations from the Playbook standard position.
3. Description of the Platform's clinical applications and patient populations affected (sepsis, radiology, medication interaction across 14 hospitals, 2.1M encounters).
4. Assessment of regulatory compliance (NJ Act, HIPAA, FDA).
5. GC recommendation regarding execution.

**Proposals requiring specific Board attention:** Proposal 1 (patient-safety super-cap at the 3× ACV floor — the minimum defensible position); Proposal 3 (graduated ETF — a deviation from the Playbook's no-ETF position, requiring GC endorsement); Proposal 7 (indemnification at the super-cap backstop with patient-harm inclusion). Dr. Narayanan should reserve the Board briefing slot and confirm the package is Board-defensible before the July 18 session concludes.

---

## V. CONCESSION SEQUENCING FOR THE JULY 18 SESSION

Based on the Delgado memo and Sutter guidance, the recommended sequencing at the joint session:

1. **Open with Priorities 1–3 (patient-safety, audit, termination).** Lead with the comparable-deal intelligence on liability (indirectly). Present the Langford tiered audit framework as a regulatory compliance baseline (not a commercial preference). Present the graduated ETF as a workable, incentive-aligned structure. Hold firm on the patient-safety floor (3× ACV) and the audit floor (annual Tier 2).

2. **Deploy Priority 4 (data usage) as concession currency.** Once the vendor engages on Priorities 1–3, offer calibrated flexibility on data usage (Position A → B → C) in exchange for vendor movement on patient-safety, audit, and termination. The vendor's highest-priority term is Meridian's most valuable trade chip.

3. **Resolve Priorities 5–7 on the playbook fallbacks.** SLA (binding benchmarks, 3-miss termination), IP (vendor ownership + perpetual license + functional portability), and indemnification (shared defense + super-cap + patient-harm) are largely resolved at the fallback positions. Spend remaining capital only on holding the patient-harm indemnification inclusion (Priority 7 red line).

4. **Close the insurance gap** as part of the liability/indemnification package — it is the collectability backstop that makes the cap structure real.

5. **Confirm Board-defensibility** with Dr. Narayanan before finalizing any package, particularly on the patient-safety super-cap (floor), the graduated ETF (Playbook deviation), and the indemnification scope.

---

*Prepared by Whitfield Ames LLP for Meridian Health Systems, Inc. This memorandum is privileged and confidential attorney work product. All clause language is draft, redline-ready, and subject to final review by Dr. Priya Narayanan (SVP & GC) and the Meridian negotiation team before transmission to Cognitive Foundry. Cross-references to the Meridian AI/Technology Vendor Negotiation Playbook (2025 Edition) and the Contested Terms Matrix (July 1, 2025) are incorporated throughout.*