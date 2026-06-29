# PRIVILEGED & CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION AND/OR ATTORNEY WORK PRODUCT

**HARGROVE, TEMPLETON & BLISS LLP**
1750 K Street NW, Suite 900, Washington, DC 20006

---

## INTERNAL ISSUE MEMORANDUM

| | |
|---|---|
| **TO:** | Katherine "Kate" Pressman, Partner |
| **FROM:** | Daniel J. Yoo, Senior Associate |
| **CC:** | Linda Fessenden, VP Regulatory Affairs, Clearfield Medical Devices, Inc.; Dr. Evelyn Marsh, RAC, Ridgepoint Consulting Group |
| **DATE:** | May 19, 2025 |
| **RE:** | Prioritized Issue Review — Draft Pre-Submission (Q-Sub) Package, VascuClear 3000 Thrombectomy System (Traditional 510(k); Product Code GXD; 21 CFR 870.1250) |
| **PRIVILEGE:** | Prepared in anticipation of the May 19, 2025 internal review deadline. Contains attorney work product and attorney-client communications. |

---

## I. Introduction and Scope

At Kate's request, I have conducted a comprehensive review of the draft Pre-Submission (Q-Sub) package prepared for the VascuClear 3000 Thrombectomy System ("VascuClear 3000" or "the Device") in advance of the June 15, 2025 target filing date. The package reviewed consists of the following five enclosures plus the predicate's 510(k) summary and the internal strategy email chain:

1. **Cover Letter** (`presub-cover-letter.docx`) — dated May 19, 2025;
2. **Device Description and Predicate Comparison** (`device-description-predicate-comparison.docx`);
3. **Proposed Testing Plan** (`proposed-testing-plan.docx`, Draft 2.1);
4. **Clinical Study Synopsis** (`clinical-study-synopsis.docx`, Protocol CLR-VC3-001, Draft 1.0);
5. **Draft Instructions for Use** (`draft-ifu-vasculear-3000.docx`, IFU-VC3000-001, Rev. A); and
6. **ThrombEx 200 510(k) Summary** (`thrombex-200-510k-summary.docx`, K192847).

This memorandum identifies regulatory, scientific, and strategic deficiencies in the package as currently drafted and prioritizes them for resolution before the package is finalized. It also responds to the two open questions Kate raised in the strategy email chain — (a) whether the VascuClear 3000 should be treated as a combination product under 21 CFR Part 3, and (b) whether an Investigational Device Exemption (IDE) is required for the proposed clinical study — and recommends whether corresponding questions should be added to the Pre-Submission.

My review confirms that the two issues Kate flagged are real and material, and that the package contains a number of additional deficiencies that FDA is likely to raise at the Pre-Submission meeting if they are not addressed first. Several of these are internal inconsistencies among the enclosures that can be corrected quickly; others are substantive gaps in the regulatory strategy or testing program that warrant attention before filing.

---

## II. Executive Summary

The table below summarizes the issues identified, organized by priority tier. Tier 1 issues are pathway-defining and should be resolved before the package is filed; they could change the regulatory pathway, the reviewing division, or the evidentiary burden. Tier 2 issues are significant testing or strategy gaps that FDA will very likely flag and that should be addressed in the package before filing. Tier 3 issues affect completeness and credibility and should be corrected. Tier 4 issues are consistency and clean-up items.

| # | Tier | Issue | One-line description |
|---|---|---|---|
| 1 | 1 | Combination product classification | Device has a purpose-built drug-delivery lumen and an indication claiming drug delivery; no question to FDA on 21 CFR Part 3 status is included. |
| 2 | 1 | IDE requirement | Clinical study is mischaracterized as "post-clearance" though the Device is not cleared; no question to FDA on IDE is included. |
| 3 | 1 | Predicate lacks drug-delivery capability | Sole predicate (K192847) is purely mechanical with no drug lumen and no rotating impeller; no predicate precedent for the pharmacomechanical approach. |
| 4 | 1 | Biocompatibility contact-duration misclassification | IFU/protocol permit 72-hour indwell, but biocompatibility is classified "limited (<24h)," excluding subchronic toxicity, implantation, and genotoxicity. |
| 5 | 1 | Impeller fatigue test is definitionally flawed | 500 "rotational cycles" defined as 360° revolutions = ~2.5 seconds at 12,000 RPM; provides no meaningful durability data. |
| 6 | 2 | Software level of concern likely understated | "Minor" classification is lower than the predicate's "Moderate" (which has no impeller); relies on outdated 2005 guidance. |
| 7 | 2 | Bench testing excludes the combined pharmacomechanical function | Simulated-use testing does not activate the infusion lumen; the Device's core claimed indication is not tested at the bench. |
| 8 | 2 | Drug-delivery characterization uses saline only | No tPA / material-compatibility testing; the IFU itself admits compatibility is unverified. |
| 9 | 2 | EMC testing omitted | IEC 60601-1-2 not in the electrical-safety plan; the predicate performed a full EMC battery. |
| 10 | 2 | Shelf-life / sterile-barrier testing omitted | No accelerated aging or package-integrity testing; the predicate validated a 2-year shelf life. |
| 11 | 2 | Indication inconsistent with combination-product strategy | Co-primary drug-delivery claim conflicts with the strategy of de-emphasizing drug delivery to avoid combination-product treatment. |
| 12 | 2 | Program timeline is internally infeasible | Testing completes Nov–Dec 2025; clearance milestone is Dec 31, 2025; clinical data not available until Q4 2026. |
| 13 | 3 | Comparison table misrepresents predicate indication | Appendix A lists the predicate as "Adults with acute DVT, iliofemoral" — the predicate is actually cleared for the broad "peripheral vasculature." |
| 14 | 3 | Console dimensions inconsistent across documents | Device description: 40×35×20 cm, 15 kg; IFU: 30×25×15 cm, 4.5 kg. |
| 15 | 3 | Impeller material inconsistent across documents | Device description: 316L stainless steel; testing plan: nitinol. |
| 16 | 3 | MRI safety labeling incomplete | IFU contains "[TBD]" placeholders for temperature rise and field strength. |
| 17 | 3 | Console reprocessing validation not in testing plan | Referenced as "separate" but not included in the formal plan. |
| 18 | 3 | Hydrophilic-coating integrity testing absent | No coating adhesion/particulate testing despite FDA guidance on lubricious coatings. |
| 19 | 3 | Clinical performance goal lacks justified benchmark | 70% performance goal asserted without a cited objective performance criterion or literature basis. |
| 20 | 3 | Clinical study governance incomplete | No DSMB/CEC; venographic scoring methodology "in development"; core lab unspecified. |
| 21 | 3 | Clinical tPA dosing lacks safety guardrails | No maximum cumulative tPA dose or bleeding stopping rules despite extended infusion up to 72 hours. |
| 22 | 3 | Cover-letter pathway statement is premature | Asserts traditional 510(k)/GXD as settled before FDA has weighed in on combination-product status. |
| 23 | 4 | IFU allergy/contraindication materials list incomplete | Omits nitinol and PTFE; lists barium sulfate (a predicate material) without clear basis. |
| 24 | 4 | Hemocompatibility gaps for rotating impeller / nitinol | No impeller-specific hemolysis or nitinol nickel-leach evaluation. |
| 25 | 4 | Clinical follow-up duration may be insufficient | 30-day follow-up may not capture post-thrombotic syndrome outcomes. |

The two issues Kate raised (Items 1 and 2) are the most consequential. I recommend that **both** a combination-product question and an IDE question be added to the Pre-Submission before filing, for the reasons set forth in Sections III.A and III.B below. I do not recommend proceeding with the package as currently drafted on those two points.

---

## III. Tier 1 — Critical Issues (Pathway-Defining)

### A. Combination Product Classification — No Question to FDA Is Included

**Where:** Cover Letter §§ II, IV, VII; Device Description §§ 2.1, 2.4, 5.1; Clinical Synopsis §§ 2, 4.1, 8.2; Draft IFU §§ 1, 2, 9; email chain (Pressman, May 5 and May 12, 2025).

**Analysis.** The VascuClear 3000 incorporates a "proprietary integrated thrombolytic infusion lumen" that is "purpose-built" for drug delivery, terminates in side ports positioned to direct infusate into the thrombus, and is described throughout the package as a "core functional feature" enabling "pharmacomechanical thrombectomy." The proposed indication expressly claims "simultaneous local delivery of physician-specified thrombolytic agents" as a therapeutic function, and the clinical protocol calls for administration of alteplase (tPA) at 0.5–1.0 mg/hr through that lumen.

Under 21 CFR 3.2(e), a "combination product" includes a device that is "intended for use with" a drug where the device and drug are required to achieve the intended use, purpose, or effect. The relevant inquiry is not solely whether Clearfield *supplies* the drug; it is whether the Device, as designed and labeled, is intended to be used with a drug to achieve its therapeutic effect. The physical design (a dedicated drug-delivery lumen), the labeling (a co-primary drug-delivery indication), and the clinical protocol (tPA delivered through the lumen) all point toward an intended combined use. Evelyn's "infusion pump analogy" is distinguishable: a general-purpose infusion pump is indicated for fluid delivery without reference to any specific drug or therapeutic effect, whereas the VascuClear 3000's indication ties the lumen to a specific therapeutic class (thrombolytics) and a specific therapeutic purpose (thrombolysis at the treatment site).

I am not concluding that the Device *is* a combination product — that is a determination FDA (and, if contested, the Office of Combination Products via a Request for Designation) would make. I am concluding that the question is genuinely open, that reasonable reviewers could reach either answer, and that the package currently forecloses the issue without asking FDA. If FDA concludes the Device is a combination product, the consequences are significant: a Request for Designation may be required (21 CFR 3.7); the lead review center and/or review division could change; additional drug-related data (e.g., drug-device compatibility, leachables/extractables in the presence of the drug, delivery-dose accuracy) may be required; and the review timeline could extend well beyond the December 31, 2025 clearance milestone in the Braddock Ventures term sheet.

**Recommendation.** Add a direct question to FDA in the Pre-Submission asking whether the VascuClear 3000, as designed and labeled, should be classified as a combination product under 21 CFR Part 3, and, if so, what the implications are for the review pathway, reviewing division, and required data. State Clearfield's present position (not a combination product) and the rationale, but frame the question so that FDA's view is solicited before Clearfield commits to the pathway. This is consistent with Kate's recommendation and is, in my view, the prudent course. The cost of asking is negligible; the cost of being wrong after filing is substantial.

### B. IDE Requirement — Study Mischaracterized as "Post-Clearance"

**Where:** Clinical Synopsis § 6 (Regulatory Status and IDE Determination); §§ 5, 8.2, 15; email chain (Pressman, May 5, 2025; Marsh, April 28 and May 9, 2025).

**Analysis.** The synopsis states that "an IDE is not anticipated" because the study "is designed as a post-clearance data collection effort, and the VascuClear 3000 is expected to have received 510(k) clearance prior to study initiation." This characterization is internally inconsistent with the package's own timeline. The study is scheduled to begin enrolling in Q4 2025 (Synopsis § 15). The 510(k) testing program does not complete until November–December 2025 (Testing Plan § 9.2), and the clearance milestone is December 31, 2025. On the package's own timeline, the Device will not be cleared when enrollment begins. A study of an uncleared device used as the object of a clinical investigation is, by definition, a study of an "investigational device" under 21 CFR 812.3(m), regardless of whether the data are characterized as "supportive."

Evelyn's distinction between "supportive" 510(k) clinical data and "primary" PMA clinical data does not control the IDE question. The IDE regulations turn on whether the device is investigational and whether the study presents a significant risk — not on whether the data are the primary basis for clearance. The study involves (i) an uncleared device with a rotating 12,000 RPM impeller in the venous vasculature, (ii) concurrent delivery of a thrombolytic (alteplase) through the device lumen at specified doses, and (iii) optional extended indwell infusion for up to 72 hours. Each of these features is reasonably subject to a significant-risk (SR) determination by an IRB, and the synopsis itself concedes that "the IRBs at the clinical sites will need to make their own significant risk / non-significant risk determination." If any site IRB determines the study is SR, an IDE is required before enrollment at that site (21 CFR 812.2, 812.3). Proceeding on the assumption that all five IRBs will classify the study as non-significant risk (NSR) is not a safe foundation for a Q4 2025 enrollment target.

**Recommendation.** Add a direct question to FDA asking whether an IDE is required for the proposed clinical study design, and, if FDA's view is that an IDE is required (or that the study is SR), what the implications are for the timeline. Internally, the synopsis should be revised to remove the "post-clearance" characterization, which is not supportable on the current timeline, and to describe the study accurately as a pre-clearance clinical study conducted to generate supportive evidence for the 510(k). The IRB SR/NSR strategy should be addressed proactively, including a contingency for an IDE application. This is consistent with Kate's recommendation.

### C. Predicate Device Lacks Drug-Delivery Capability (and Has No Rotating Impeller)

**Where:** Cover Letter § III; Device Description §§ 3.2, 3.3, 4.2, 4.3, 5; ThrombEx 200 510(k) Summary §§ 2, 3, 4, 6; email chain (Pressman, May 5, 2025).

**Analysis.** The sole proposed predicate, the ThrombEx 200 (K192847), is a purely mechanical, Bernoulli-effect aspiration catheter. Its 510(k) summary states unambiguously that the device "does not deliver any pharmaceutical agents, thrombolytic drugs, or therapeutic substances to the patient" and "is not indicated for use in conjunction with any drug delivery or drug infusion procedure," and that it contains "no rotating impeller, no mechanical maceration component, and no drug infusion lumen." The VascuClear 3000 differs from the predicate on two of the most consequential technological axes: it adds (i) a rotating helical impeller for mechanical maceration and (ii) an integrated drug-delivery lumen. Neither feature has any predicate precedent in the proposed predicate chain (K192847 → K171034, both purely mechanical aspiration catheters).

The cover letter and device description assert that these differences "do not raise new questions of safety and effectiveness." That assertion is aggressive. The addition of a drug-delivery function that the predicate expressly disclaims is, at minimum, a candidate for a "different technological characteristic" that could be viewed as raising new questions of safety and effectiveness — particularly when combined with the combination-product question above. FDA may take the position that the drug-delivery capability constitutes a new intended use or that a reference predicate with drug-delivery capability is needed to bridge the technological gap. The package identifies "no secondary or reference predicates" (Device Description § 3.1), which leaves the SE argument resting entirely on a predicate that lacks the Device's two distinguishing features.

**Recommendation.** (1) Strengthen the SE discussion by identifying and analyzing one or more reference devices that possess the missing technological characteristics — e.g., a cleared catheter-based thrombectomy device with a rotating impeller, and/or a cleared catheter with an infusion lumen for local drug delivery — and present a bridging analysis. The cover letter's Question 1 (predicate appropriateness) and the device description's Question 4 (additional reference devices) should be retained and sharpened. (2) Be prepared for FDA to question whether the drug-delivery function can be supported through the GXD/510(k) pathway at all without a combination-product analysis (see Item A). (3) Consider whether the indication should be restructured so that the mechanical thrombectomy function is the primary indication and the drug-delivery capability is described as a feature, which would both strengthen the SE argument and reduce combination-product risk (see Item K).

### D. Biocompatibility Contact-Duration Misclassification

**Where:** Draft IFU §§ 1, 8.4; Clinical Synopsis § 8.2 (step 8); Device Description § 2.2 and comparison table (§ 4.2); Proposed Testing Plan §§ 2.1, 2.2.

**Analysis.** The IFU expressly permits the catheter to "remain in situ for up to 72 hours for extended thrombolytic infusion therapy," and the clinical protocol incorporates the same 72-hour extended-indwell option. Under ISO 10993-1:2018, contact duration categories are: limited (< 24 hours), prolonged (24 hours to 30 days), and permanent (> 30 days). A 72-hour indwell falls squarely in the **prolonged** category, not "limited."

The testing plan, however, classifies the catheter as a blood-contacting device with "limited contact duration (less than 24 hours)" and, on that basis, **excludes** subchronic systemic toxicity (ISO 10993-11), implantation testing (ISO 10993-6), and genotoxicity (ISO 10993-3). For a prolonged-contact, blood-contacting device, ISO 10993-1:2018 Table A.1 indicates that additional endpoints — including subchronic toxicity and, depending on the risk assessment, implantation and genotoxicity — may be appropriate. The device description's own comparison table captures the contradiction in adjacent rows: "Device Contact Duration: Up to 72 hours (per draft IFU)" versus "Biocompatibility: contact duration classified as 'limited' (<24 hours)."

This is not a minor drafting error. It drives the exclusion of three biocompatibility endpoints that FDA may require, and it will be immediately apparent to the reviewer because the package states both facts in the same table. FDA will very likely ask why the contact-duration classification does not match the labeled indwell time.

**Recommendation.** Reconcile the contact-duration classification with the labeled maximum indwell time. Two options: (a) if the 72-hour extended indwell is retained in the indication and IFU, reclassify the device as prolonged contact and add the endpoints indicated by ISO 10993-1:2018 Table A.1 for prolonged blood contact (at minimum, subchronic systemic toxicity; evaluate implantation and genotoxicity via the risk-based process and document the rationale); or (b) if the 72-hour indwell is not essential to the indication, remove the extended-indwell claim from the IFU and protocol so that the limited-contact classification is supportable. Option (a) is more conservative and aligns with the Device's apparent clinical intent; option (b) is faster but narrows the claim. The package should present FDA with the intended contact duration and ask FDA to concur on the resulting endpoint set (Testing Plan Question 1 should be revised accordingly).

### E. Impeller Fatigue Test Is Definitionally Flawed

**Where:** Proposed Testing Plan § 3.3 (Impeller Fatigue Testing); Device Description § 2.2; ThrombEx 200 510(k) Summary § 5.2.

**Analysis.** The testing plan states that the impeller "shall undergo fatigue testing for a minimum of 500 rotational cycles at maximum rated speed (12,000 RPM)" and defines "one rotational cycle" as "one complete revolution (360°) of the impeller." At 12,000 RPM, 500 revolutions are completed in approximately **2.5 seconds** (500 ÷ 12,000 × 60 s). A 2.5-second test provides no meaningful fatigue or durability data for a rotating component that may operate across multiple passes in a procedure. The device description separately refers to "500 complete activation cycles," which more naturally reads as 500 activation events; but the testing plan's explicit definition of a "cycle" as a single revolution controls the test as written and renders it meaningless.

For context, the predicate's catheter fatigue testing comprised 100 insertion/withdrawal cycles plus 50,000 flexural fatigue cycles at ±45° deflection — a far more rigorous protocol, and the predicate has no rotating component at all. A rotating impeller operating at up to 12,000 RPM in blood should be validated over a clinically representative cumulative operating time and/or a large number of revolutions, with a realistic duty cycle, and should evaluate fatigue at the impeller-to-shaft bond, the drive shaft, and the protective cage.

**Recommendation.** Redefine the fatigue test in clinically meaningful terms. At minimum, specify (i) the maximum anticipated cumulative impeller operating time per procedure (and across the labeled number of procedures/activation events), (ii) a test duration or revolution count that provides a meaningful safety margin over that operating time (e.g., operating at 12,000 RPM for a defined multiple of the worst-case cumulative procedure time, or a revolution count in the hundreds of thousands to millions), and (iii) post-test inspection criteria (which the plan already includes). Resolve the inconsistency between the device description's "500 activation cycles" and the testing plan's "500 revolutions." This should be corrected before filing; FDA will flag it, and it undermines the credibility of the mechanical testing program if left as written.

---

## IV. Tier 2 — High-Priority Issues (Significant Gaps FDA Will Likely Flag)

### F. Software Level of Concern Likely Understated ("Minor")

**Where:** Proposed Testing Plan § 5; Device Description § 2.3; ThrombEx 200 510(k) Summary § 5.6.

**Analysis.** The console firmware is classified "Minor" on the rationale that independent hardware safety mechanisms (a mechanical over-speed governor and a hardware pressure-relief valve) mitigate software-failure risks. Three concerns:

1. **Inconsistency with the predicate.** The ThrombEx 200's software was classified **"Moderate"** — and that device has *no* rotating impeller and controls only aspiration. It is difficult to justify a *lower* classification for the VascuClear console, which controls a 12,000 RPM rotating impeller inside a blood vessel, where software failure (e.g., over-speed, failure to stop, uncommanded restart) could cause serious injury (vessel perforation, dissection, hemolysis, embolization). FDA will see this inconsistency.

2. **Reliance on hardware mitigations.** The existence and effectiveness of the "mechanical over-speed governor" and "hardware pressure relief valve" are asserted but not substantiated in the package. If these are the basis for the Minor classification, their design and verification should be documented. Even with hardware backups, FDA may view software that commands a 12,000 RPM impeller as warranting at least a Moderate (or, under the current framework, Enhanced) documentation level.

3. **Outdated guidance.** The package relies on FDA's 2005 software guidance throughout. FDA's current framework is the 2023 guidance *Content of Premarket Submissions for Device Software Functions*, which uses a "Documentation Level" (Basic vs. Enhanced) rather than the 2005 "Level of Concern" (Minor/Moderate/Major). The package should be updated to the current framework. The plan also proposes to *exclude* hazard analysis, detailed architecture, and unresolved-anomaly documentation from the submission — items typically expected at the Enhanced documentation level.

**Recommendation.** Reassess the documentation level using the 2023 guidance. I expect the appropriate level is Enhanced (analogous to Moderate), given the impeller control function. Update the testing plan and device description to the current guidance framework, and plan to include hazard analysis, architecture description, and anomaly disposition consistent with the Enhanced level. Substantiate the hardware safety mechanisms or remove reliance on them. Add a question to FDA concurring on the documentation level (Testing Plan Question 4 should be reframed to the 2023 framework).

### G. Simulated-Use Bench Testing Excludes the Combined Pharmacomechanical Function

**Where:** Proposed Testing Plan § 7.2; Cover Letter § IV; Device Description § 2.4; Clinical Synopsis §§ 2, 4.1.

**Analysis.** The Device's claimed indication and central differentiating feature is *combined* pharmacomechanical thrombectomy — "simultaneous mechanical thrombus removal and localized drug delivery." Yet the simulated-use bench testing explicitly states that "the thrombolytic infusion lumen is not activated during simulated-use bench testing" and that "combined pharmacomechanical testing … is not included in this bench test protocol." The bench program therefore validates only the mechanical thrombectomy function, not the combined function that is the basis of the indication and the SE argument's distinguishing feature. FDA is likely to ask how the combined function — including the interaction of mechanical maceration with concurrent local thrombolysis — is validated.

**Recommendation.** Add a bench test that evaluates the combined pharmacomechanical function (e.g., simulated-use testing with a thrombolytic surrogate or tPA analog delivered through the infusion lumen concurrently with impeller operation), or, at minimum, provide a scientific rationale for why separate mechanical and drug-delivery characterization is sufficient to support the combined indication. The package's Testing Plan Question 5 should be expanded to ask FDA to concur on the adequacy of the bench approach for the combined function.

### H. Drug-Delivery Characterization Uses Saline Only; No Material-Compatibility Testing

**Where:** Proposed Testing Plan § 8; Draft IFU § 9.

**Analysis.** The drug-delivery characterization uses normal saline as the test fluid. The IFU itself states that "drug compatibility with catheter lumen materials has not been independently verified" and that "specific compatibility testing with individual thrombolytic agents, diluents, or drug formulations has not been performed." If the Device is intended to deliver tPA (and the indication and protocol so provide), the compatibility of tPA and its diluents with the patient-contacting and lumen materials (polyurethane/Pebax, PTFE liner, adhesives, hydrophilic coating) should be evaluated — including whether the materials affect drug activity/stability and whether the drug/diluents affect the materials (e.g., swelling, leaching, degradation). This is also directly relevant to the combination-product question: if FDA treats the Device as a combination product (or as a device intended for use with a drug), drug-material compatibility and delivery-dose accuracy data are typically expected.

**Recommendation.** Add tPA (alteplase) and its representative diluents to the drug-delivery characterization, including (i) material compatibility (effect of drug/diluent on materials and effect of materials on drug activity), (ii) delivery-dose accuracy across the flow-rate range, and (iii) evaluation of the side-port distribution with a representative drug solution. The package's Testing Plan Question 6 already asks whether saline is sufficient; I recommend the package present a plan that includes tPA testing and ask FDA to concur, rather than asking whether saline alone is acceptable.

### I. Electromagnetic Compatibility (EMC) Testing Omitted

**Where:** Proposed Testing Plan § 4; ThrombEx 200 510(k) Summary § 5.3.

**Analysis.** The electrical-safety plan addresses IEC 60601-1 but does not include IEC 60601-1-2 (EMC). The predicate's 510(k) summary documents a full EMC battery (IEC 60601-1-2:2014: radiated/conducted emissions, ESD, radiated RF, EFT/burst, surge, conducted RF, power-frequency magnetic field, and voltage dips/interruptions). EMC testing is a standard expectation for an AC-powered electromedical console operating in a catheterization laboratory. Its omission will be flagged.

**Recommendation.** Add IEC 60601-1-2 EMC testing to the electrical-safety plan, to be performed by Pinnacle Standards Testing, Inc. (which is identified as NRTL-accredited for the IEC 60601 series). Update Testing Plan Question 3 to ask FDA to concur on the combined IEC 60601-1 / IEC 60601-1-2 program.

### J. Shelf-Life and Sterile-Barrier Package-Integrity Testing Omitted

**Where:** Proposed Testing Plan § 6; ThrombEx 200 510(k) Summary § 5.4.

**Analysis.** The testing plan includes EtO sterilization validation (ISO 11135) and EtO residuals (ISO 10993-7) but does not include shelf-life validation or sterile-barrier package-integrity testing. The predicate validated a 2-year shelf life using accelerated aging (ASTM F1980) and package integrity (ASTM D4169 distribution simulation; ASTM F2095 seal strength). For a sterile single-use catheter, shelf-life and sterile-barrier integrity data are standard 510(k) expectations. The VascuClear catheter's labeled expiration date (printed on the pouch per the IFU) is not supported by any validation in the plan.

**Recommendation.** Add a shelf-life/sterile-barrier validation program: accelerated aging per ASTM F1980 to support the labeled shelf life, package integrity per ASTM D4169 (distribution simulation) and ASTM F2095 (seal strength), and real-time aging confirmation as appropriate. Specify the target shelf-life claim.

### K. Indication Inconsistent with the Combination-Product-Avoidance Strategy

**Where:** Cover Letter § IV; Device Description § 2.4; Draft IFU § 2; email chain (Marsh, May 9, 2025; Pressman, May 5 and May 12, 2025).

**Analysis.** There is an internal tension in the package's regulatory strategy. On one hand, the strategy (per Evelyn's emails) is to de-emphasize drug delivery so that the Device is not treated as a combination product — positioning the mechanical thrombectomy as the primary function and the infusion lumen as a "feature." On the other hand, the proposed indication states that the Device is "indicated for the percutaneous removal of thrombus **and simultaneous local delivery of physician-specified thrombolytic agents**," making drug delivery a co-primary indicated function. The clinical protocol and IFU reinforce the co-primary framing. These positions are in tension: an indication that claims drug delivery as a therapeutic function is harder to reconcile with a "not a combination product" position, and harder to reconcile with a predicate that has no drug-delivery capability (Item C).

**Recommendation.** Decide deliberately which framing the package will adopt and make all enclosures consistent. If the goal is to minimize combination-product and SE risk, restructure the indication so that the primary indicated function is mechanical thrombectomy (e.g., "indicated for the percutaneous removal of thrombus from the iliofemoral venous segment in adult patients with acute DVT (symptom onset ≤14 days)"), and describe the infusion lumen in the device description and IFU as an integrated feature that *may* be used for physician-specified local delivery. If, conversely, the combined pharmacomechanical function is essential to the commercial value proposition, then the package should lean into it — but should then expect (and prepare for) combination-product treatment and the need for a reference predicate with drug-delivery capability. The current package tries to occupy both positions simultaneously, which weakens both. This decision should be made before the Pre-Submission is filed and should drive the resolution of Items A, C, and G.

### L. Program Timeline Is Internally Infeasible

**Where:** Cover Letter §§ V, VIII; Proposed Testing Plan § 9.2; Clinical Synopsis §§ 6, 15; email chain (Fessenden, April 22, 2025; Pressman, May 12, 2025).

**Analysis.** Several timeline statements in the package are mutually inconsistent and, taken together, are not feasible against the December 31, 2025 clearance milestone:

1. **Testing initiation vs. Q-Sub feedback.** The testing plan states that testing initiation is "July 2025, following receipt of FDA feedback from the anticipated Q-Sub meeting (scheduled for August/September 2025)." Testing cannot begin in July based on feedback received in August/September. This is an internal contradiction.

2. **Testing completion vs. 510(k) submission vs. clearance.** Testing completes November–December 2025. The 510(k) is to be submitted "as early as practical following completion of all testing." FDA's 510(k) review is 90 FDA days (plus any Additional Information/RTQ cycles). A submission in December 2025 cannot clear by December 31, 2025. To clear by December 31, 2025, the 510(k) would need to be submitted by approximately early October 2025 — before testing completes.

3. **Clinical data vs. clearance milestone.** The synopsis states that the clinical data "is intended to support the 510(k) submission." But enrollment completes Q2 2026 and the clinical study report finalizes Q4 2026 — roughly a year after the December 31, 2025 clearance milestone. The clinical data therefore cannot be part of a 510(k) that clears by December 31, 2025. Either the 510(k) will be submitted without clinical data (contradicting the synopsis), or the clearance milestone is not achievable on this plan.

These inconsistencies have strategic consequences. The Braddock Ventures Series D term sheet requires 510(k) clearance by December 31, 2025. If the pathway changes (e.g., combination product), or if an IDE is required, or if testing slips, the milestone is at risk — which Kate correctly noted has corporate implications that should be surfaced to Kendrick & Hale.

**Recommendation.** Reconcile the timeline into a single, internally consistent critical path that is honest about the December 31, 2025 milestone. Specifically: (i) correct the testing-initiation date to follow the Q-Sub meeting; (ii) state explicitly whether the 510(k) will include clinical data or will rely on bench/predicate evidence alone (and, if the latter, reconcile the synopsis); and (iii) flag to the Clearfield board, via Linda, the risk that the milestone may not be achievable and the corporate implications, so that Kendrick & Hale can be engaged as Kate suggested. The Pre-Submission itself need not disclose the milestone, but the internal strategy should reflect a realistic plan.

---

## V. Tier 3 — Medium-Priority Issues (Completeness and Credibility)

### M. Comparison Table Misrepresents the Predicate's Cleared Indication

**Where:** Device Description, Appendix A, Table A-1; cf. id. § 4.2 (correct); ThrombEx 200 510(k) Summary § 2.

**Analysis.** Table A-1 lists the ThrombEx 200's "Intended Use Population" as "Adults with acute DVT, iliofemoral venous segment." The predicate's actual cleared indication is "percutaneous removal of thrombus from the peripheral vasculature" — broadly encompassing both arterial and venous peripheral vasculature, with no limitation to DVT, no limitation to the iliofemoral segment, and no symptom-onset window. The main comparison table in § 4.2 states the predicate's indication correctly; Appendix A does not. The misstatement in Appendix A overstates the similarity between the predicate and the Device and could undermine the package's credibility if FDA compares it against the public 510(k) summary (which is enclosed).

**Recommendation.** Correct Table A-1 to reflect the predicate's actual cleared indication verbatim, and reframe the SE discussion to acknowledge that the Device's indication is a *narrowing* (venous-only, iliofemoral, acute DVT ≤14 days) relative to the predicate's broader peripheral indication — which is the argument the device description makes in § 5.1 and should make consistently.

### N. Console Dimensions and Weight Inconsistent Across Documents

**Where:** Device Description § 2.3; Draft IFU § 13.

**Analysis.** The device description states the console is "approximately 40 cm (W) × 35 cm (D) × 20 cm (H)" and "weighs approximately 15 kilograms." The IFU technical specifications state "30 cm × 25 cm × 15 cm" and "4.5 kg." These are materially different and cannot both be correct.

**Recommendation.** Reconcile to a single set of specifications and use it consistently in the device description, IFU, and any figures.

### O. Impeller Material Inconsistent Across Documents

**Where:** Device Description § 2.2; Proposed Testing Plan § 2.3.

**Analysis.** The device description states the impeller is "medical-grade stainless steel (316L)" and that "certain structural components within the distal tip housing incorporate nitinol." The testing plan's materials section lists the "Helical Impeller" as "Nitinol (nickel-titanium alloy)." The impeller is a dynamic, blood-contacting component; its material identity is material to biocompatibility (nickel leaching/sensitization), to MRI safety labeling, and to the SE comparison. The documents disagree on what it is made of.

**Recommendation.** Confirm the impeller material and correct all documents to a single, accurate specification. If the impeller (or any patient-contacting component) is nitinol, add nickel-ion leach testing and ensure the sensitization evaluation (ISO 10993-10) accounts for nickel exposure; update the MRI safety evaluation accordingly.

### P. MRI Safety Labeling Incomplete

**Where:** Draft IFU § 6; Device Description comparison table (§ 4.2).

**Analysis.** The IFU's MR Conditional labeling contains "[TBD]" placeholders for the temperature rise and the MRI system field strength, and refers to "Clearfield Medical Devices technical documentation" for complete data. The comparison table lists the Device as "MRI Conditional (per draft IFU)." An MR Conditional claim must be supported by completed testing and specific, finalized labeling conditions (per ASTM F2503 / IEC 62570). Placeholder labeling is not appropriate for a Pre-Submission that asks FDA to concur on the package.

**Recommendation.** Either complete the MRI safety testing and finalize the MR Conditional labeling before filing, or remove the MR Conditional claim from the IFU and comparison table until the data are available. If MR Conditional is retained, specify the complete test conditions.

### Q. Console Reprocessing Validation Not Included in the Testing Plan

**Where:** Proposed Testing Plan § 6.1; Draft IFU § 11.

**Analysis.** The console is reusable, and the IFU provides cleaning and disinfection instructions. The testing plan states that reprocessing validation will be performed "separately under Clearfield's reusable device reprocessing validation protocol" but does not include it in the formal testing program. FDA's guidance *Reprocessing Medical Devices in Health Care Settings: Validation Methods and Labeling* (2015) expects validated reprocessing instructions and validation data for reusable devices. Omitting it from the plan leaves a gap FDA may identify.

**Recommendation.** Add a reprocessing validation section to the testing plan (validation of the labeled cleaning/disinfection instructions, including worst-case soiling, inoculation, and recovery), or, at minimum, describe the reprocessing validation protocol and timeline and ask FDA to concur.

### R. Hydrophilic-Coating Integrity Testing Absent

**Where:** Proposed Testing Plan § 2.3; Device Description § 2.2; ThrombEx 200 510(k) Summary § 3.1.

**Analysis.** The catheter has a hydrophilic coating on the distal tip. The testing plan lists the coating for chemical characterization (ISO 10993-18) but does not include coating-integrity testing (adhesion, abrasion, durability under simulated use) or coating-particulate evaluation. FDA has issued guidance on lubricious/hydrophilic coatings on intravascular catheters and has expressed concern about coating separation and particulate embolization. The predicate also employed a hydrophilic coating.

**Recommendation.** Add coating-integrity testing (adhesion/durability under simulated insertion and use, and particulate evaluation for coating debris) to the mechanical or bench testing program.

### S. Clinical Performance Goal Lacks a Justified Benchmark

**Where:** Clinical Synopsis §§ 9.1, 11.1.

**Analysis.** The primary endpoint is ≥50% thrombus removal at 24-hour venography, with a performance goal that the lower bound of the exact 95% binomial CI exceed 70% (assuming a true rate of 80%). The 70% performance goal is asserted without a cited objective performance criterion (OPC), literature benchmark, or predicate/registry comparison. FDA typically expects a performance goal to be justified by reference to an OPC, a recognized performance threshold, or published clinical data. The disconnect between the bench acceptance criterion (≥80% thrombus removal by weight, single pass) and the clinical endpoint (≥50% thrombus removal, 24 hours) should also be explained.

**Recommendation.** Provide a written justification for the 70% performance goal, citing the basis (e.g., published thrombus-removal data from comparable pharmacomechanical thrombectomy studies such as the ATTRACT or CaVenT trials, or an OPC). Reconcile the bench and clinical thrombus-removal metrics. Ask FDA to concur on the primary endpoint and performance goal (Cover Letter Question 4 / Synopsis).

### T. Clinical Study Governance Incomplete

**Where:** Clinical Synopsis §§ 9.3, 10, 12, 18.

**Analysis.** The synopsis provides for Sponsor/CRO safety monitoring but no independent Data Safety Monitoring Board (DSMB) and no Clinical Events Committee (CEC) for blinded adjudication of major adverse events (MAEs). The primary-endpoint venographic scoring methodology ("modified Marder scoring … or an equivalent validated scoring system") is listed as "in development" (Appendix C), and the independent core laboratory is referenced in the budget but not specified. For a study intended to support a regulatory submission and involving a novel device plus tPA, an independent DSMB, a CEC for MAE adjudication, a finalized and validated scoring methodology, and a named core lab are typically expected.

**Recommendation.** Add an independent DSMB and a CEC for MAE adjudication to the study design; finalize and validate the venographic scoring methodology (or specify the validated system to be used and the core lab) before seeking FDA concurrence on endpoints; and identify the core laboratory. Ask FDA to concur on the safety-monitoring and endpoint-adjudication plan.

### U. Clinical tPA Dosing Lacks Safety Guardrails

**Where:** Clinical Synopsis § 8.2 (steps 5, 8); § 9.3.

**Analysis.** The protocol specifies tPA (alteplase) at 0.5–1.0 mg/hr during thrombectomy and permits extended infusion for up to 72 hours. The total tPA dose is a secondary endpoint, but the protocol does not specify a maximum cumulative tPA dose, dose-adjustment rules, or explicit stopping rules for bleeding (e.g., fibrinogen thresholds, hematocrit drop, or clinically significant bleeding). The ATTRACT trial (cited as a reference) documented bleeding risk with pharmacomechanical thrombolysis. The absence of dosing guardrails is a safety gap and is relevant to the SR/NSR and IDE questions (Items A and B).

**Recommendation.** Add a maximum cumulative tPA dose, dose-adjustment/holding rules, and explicit bleeding stopping rules (with laboratory triggers) to the protocol. This also strengthens the case that the study can be conducted safely, which bears on the IDE/SR analysis.

### V. Cover-Letter Regulatory Pathway Statement Is Premature

**Where:** Cover Letter § VII; Device Description § 2.5.

**Analysis.** The cover letter and device description assert the traditional 510(k) pathway under GXD/21 CFR 870.1250 as settled. This presupposes the answer to the combination-product question (Item A), which the package has not yet put to FDA. If FDA concludes the Device is a combination product, the pathway, reviewing division, and required data may change.

**Recommendation.** Soften the pathway statement to reflect that the traditional 510(k)/GXD pathway is Clearfield's *proposed* pathway, subject to FDA's view on the combination-product question, rather than asserting it as concluded. This is consistent with adding the combination-product question (Item A).

---

## VI. Tier 4 — Lower-Priority Issues (Consistency and Clean-Up)

### W. IFU Contraindication/Allergy Materials List Incomplete

**Where:** Draft IFU § 3; Proposed Testing Plan § 2.3.

**Analysis.** The IFU contraindications list "polyurethane, stainless steel, and barium sulfate" as catheter component materials for allergy purposes. The testing plan's materials list includes polyurethane/Pebax, 316L stainless steel, nitinol, PTFE, a hydrophilic coating, and adhesives. The IFU omits nitinol and PTFE (both patient-contacting) and includes barium sulfate, which is identified in the predicate's 510(k) summary as the predicate's radiopaque marker material but is not clearly identified as a VascuClear material. If nitinol is patient-contacting (see Item O), a nickel allergy contraindication/warning may be warranted.

**Recommendation.** Reconcile the IFU materials list with the actual device materials, add nitinol and PTFE as appropriate, and confirm whether barium sulfate is a VascuClear material. Add a nickel-sensitivity warning if nitinol is patient-contacting.

### X. Hemocompatibility Gaps for the Rotating Impeller and Nitinol

**Where:** Proposed Testing Plan § 2.2 (ISO 10993-4); Device Description § 2.2.

**Analysis.** The hemocompatibility program includes hemolysis, complement activation, and thrombogenicity. For a device with a rotating impeller at 12,000 RPM that dynamically contacts blood and macerates thrombus, impeller-specific hemolysis (mechanical hemolysis from the rotating element, beyond static material-contact hemolysis) should be specifically evaluated. If nitinol is a patient-contacting component, nickel-ion leaching in blood contact should be evaluated. The particulate-generation test (§ 3.3) addresses debris but not hemolysis from the impeller mechanism.

**Recommendation.** Add impeller-specific (dynamic) hemolysis testing and, if applicable, nitinol nickel-leach testing to the hemocompatibility program.

### Y. Clinical Follow-Up Duration May Be Insufficient for Post-Thrombotic Syndrome

**Where:** Clinical Synopsis § 10.

**Analysis.** The study's final visit is at 30 days. Post-thrombotic syndrome (PTS) — a principal long-term outcome of iliofemoral DVT and a key rationale for pharmacomechanical thrombectomy cited in the synopsis (§ 3) — develops over months to years. A 30-day follow-up will not capture PTS outcomes. For a 510(k) supportive study this may be defensible, but FDA may recommend longer follow-up (e.g., 6 or 12 months) for effectiveness assessment.

**Recommendation.** Consider extending follow-up to at least 6 months (with a PTS assessment such as the Villalta scale) if the study is intended to support effectiveness claims, or clearly scope the study as a safety/acute-effectiveness study and ask FDA to concur on the follow-up duration.

---

## VII. Recommended Additions to the Pre-Submission Questions for FDA

The cover letter (§ VI) and the device description (§ 6) and testing plan (§ 10) each pose questions to FDA. Based on the foregoing, I recommend adding or revising the following questions before filing:

1. **Combination product status (new).** "Does FDA agree with Clearfield's position that the VascuClear 3000, as designed and labeled, is not a combination product under 21 CFR Part 3? If FDA's view differs, what are the implications for the review pathway, reviewing division, and required data?" *(See Item A.)*

2. **IDE requirement (new).** "Does FDA agree that an IDE is not required for the proposed clinical study? If FDA's view is that an IDE is required (or that the study presents significant risk), what are the implications for the timeline?" *(See Item B.)*

3. **Predicate and reference devices (revise).** Sharpen the existing predicate question and ask FDA whether one or more reference devices (e.g., a cleared rotating-impeller thrombectomy catheter and/or a cleared catheter with an infusion lumen) should be cited to bridge the technological differences. *(See Item C.)*

4. **Biocompatibility contact duration and endpoints (revise).** State the intended maximum indwell time (including any extended infusion) and ask FDA to concur on the resulting ISO 10993-1:2018 contact-duration category and endpoint set. *(See Item D.)*

5. **Software documentation level (revise).** Reframe to the 2023 guidance framework and ask FDA to concur on the documentation level (Basic vs. Enhanced) given the impeller control function and the hardware safety mechanisms. *(See Item F.)*

6. **Combined pharmacomechanical bench testing (new/expand).** Ask FDA to concur on the adequacy of the bench approach for validating the *combined* pharmacomechanical function, not only the mechanical function. *(See Item G.)*

7. **Drug-delivery characterization with tPA (revise).** Present a plan that includes tPA/material-compatibility and dose-accuracy testing and ask FDA to concur, rather than asking whether saline alone is sufficient. *(See Item H.)*

8. **EMC, shelf-life, reprocessing, and coating testing (new).** Ask FDA to concur on the addition of IEC 60601-1-2 EMC testing, shelf-life/sterile-barrier validation, console reprocessing validation, and hydrophilic-coating integrity testing. *(See Items I, J, Q, R.)*

9. **Clinical endpoints, performance goal, and follow-up (revise).** Ask FDA to concur on the primary endpoint, the 70% performance goal and its justification, the MAE adjudication/DSMB plan, and the follow-up duration. *(See Items S, T, Y.)*

---

## VIII. Cross-Cutting Recommendations and Next Steps

1. **Decide the drug-delivery framing first (Item K).** The single most important strategic decision is how the package positions the drug-delivery lumen — as a co-primary indicated function or as an integrated feature of a mechanical-thrombectomy device. That decision drives the resolution of Items A (combination product), C (predicate/SE), and G (bench testing), and should be made before any other edits. I recommend the package adopt a consistent position and revise all enclosures to match.

2. **Add the combination-product and IDE questions (Items A, B).** I recommend adding both, consistent with Kate's recommendation. The downside of asking is negligible; the downside of being wrong after filing is a potential pathway change that jeopardizes the December 31, 2025 milestone.

3. **Correct the internal inconsistencies before filing (Items D, E, M, N, O, P, W).** Several of these (the 72-hour/contact-duration contradiction, the 2.5-second fatigue test, the misstated predicate indication, the console dimensions, the impeller material, the MRI placeholders) will be immediately apparent to FDA and will undermine the package's credibility. They are inexpensive to fix and should be fixed regardless of the strategic decisions above.

4. **Close the testing-program gaps (Items F, G, H, I, J, Q, R, X).** These are substantive but addressable. Adding EMC, shelf-life, reprocessing, coating-integrity, tPA-compatibility, and combined-function bench testing — and reassessing the software documentation level — will make the testing plan credible and reduce the risk of a hold or a major RTQ cycle.

5. **Reconcile the timeline and escalate the milestone risk (Item L).** The package's timeline is not feasible against the December 31, 2025 milestone as written. Linda should be informed, and the corporate implications (Braddock Ventures term sheet) should be escalated to Kendrick & Hale as Kate suggested, so that the board can make an informed decision about the milestone, the pathway, and whether the clinical study will be part of the 510(k) or a post-clearance study.

6. **Engage Ridgepoint and the testing laboratories.** Several recommendations (reclassification of contact duration, fatigue-test redesign, software documentation level, EMC/shelf-life/reprocessing/coating additions) will affect the testing scope, schedule, and the ~$600,000 testing budget and the ~$1.4M 510(k) budget. Ridgepoint should revise the testing plan and confirm laboratory capacity and quotes before the package is finalized.

---

## IX. Conclusion

The draft Pre-Submission package is a substantial and largely well-organized document set, but it is not yet ready to file. The two issues Kate identified — combination-product classification and the IDE requirement — are genuine and material, and I recommend that corresponding questions be added to the Pre-Submission rather than proceeding on the assumption that neither applies. Beyond those two issues, the package contains a definitionally flawed impeller fatigue test, a biocompatibility contact-duration classification that contradicts the labeled indwell time, a predicate that lacks the Device's two distinguishing features, a bench program that does not test the Device's core claimed function, and several omitted testing categories (EMC, shelf-life, reprocessing, coating integrity, tPA compatibility) that FDA will very likely require. A number of internal inconsistencies across the enclosures should be corrected before filing.

Most of these items can be resolved within the time remaining before the June 15, 2025 target filing date, provided the strategic framing decision (Item K) is made promptly. I am available to discuss any of the foregoing and to assist with revisions to the cover letter, device description, testing plan, clinical synopsis, and IFU as directed.

Respectfully,

**Daniel J. Yoo**
Senior Associate
Hargrove, Templeton & Bliss LLP
1750 K Street NW, Suite 900
Washington, DC 20006
dyoo@htblaw.com

---

*PRIVILEGED & CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION AND/OR ATTORNEY WORK PRODUCT. Prepared in anticipation of the May 19, 2025 internal review deadline. This memorandum reflects the reviewer's preliminary analysis for internal use and is not a final regulatory opinion. Statutory and guidance references are current as of the date of this memorandum.*