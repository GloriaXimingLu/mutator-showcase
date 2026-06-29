### FILE: credential-gap-analysis.md
# PRIVILEGED & CONFIDENTIAL — ATTORNEY WORK PRODUCT

**MEMORANDUM**

**To:** Craig Halloran, Esq.; File (Whitmore & Callahan LLP)
**Cc:** Melanie Foss, HR Director, Prismex Analytics, Inc.; Rajiv Sunderajan, CEO, Prismex Analytics, Inc.
**From:** Immigration Counsel Review Team
**Date:** June 9, 2025
**Re:** Credential Gap Analysis — Certified PERM Application (ETA-9089), Case No. A-18247-63910, *Prismex Analytics, Inc.* v. *Ananya Mehrotra* — Senior Machine Learning Engineer

---

## I. Executive Summary

This memorandum reviews the certified PERM application (ETA Form 9089, Case No. A-18247-63910, filed March 15, 2025; certified May 22, 2025) filed by Prismex Analytics, Inc. ("Prismex" / "the Employer") on behalf of Ms. Ananya Mehrotra ("the Beneficiary") for the position of Senior Machine Learning Engineer, and compares the application's stated minimum requirements and alien-qualification attestations against the Beneficiary's supporting credentials. The review was prompted by the June 4, 2025 transmittal of the petition package and the Employer's request that counsel flag (a) any missing or supplemental documents and (b) any issues with the credentials matching the PERM requirements.

**Bottom line:** The Beneficiary's education and core technical experience are well documented and satisfy the principal minimum requirements. However, the review identifies **one critical gap, one high-severity discrepancy, and several moderate-to-low issues** that, if not addressed, expose the certified PERM to audit/revocation risk and create downstream vulnerability in the I-140 immigrant petition and the concurrent H-1B filing.

The most serious finding is that the PERM requires the "AWS Certified Machine Learning – Specialty certification or equivalent," and the Employer attested in Section K.3 that the Beneficiary "possesses the special skills and other requirements" — yet the Beneficiary **does not hold that certification or any equivalent**, as confirmed by counsel's own certification-verification notes. At the priority date (March 15, 2025), the Beneficiary held only an **expired** foundational AWS Cloud Practitioner credential and an active (but non-AWS, framework-specific) TensorFlow Developer Certificate. This is a direct contradiction between the application's attestations and the supporting record.

A second, independent concern is a **Federal Employer Identification Number (FEIN) mismatch** between the PERM (84-3291756) and the Prevailing Wage Determination (84-3291047), which must be reconciled before the I-140 is filed.

Recommended remedial actions are set forth in Section VI and prioritized in the action plan (Section VI.G). In brief: (1) reconcile the FEIN; (2) make a strategic decision on the AWS certification requirement — either obtain the certification and **refile** a new PERM, or refile with the certification removed/reframed as a preference, because the current certified PERM cannot be cured retroactively; (3) bolster the R-language evidence or revisit the "proficiency in R" requirement; (4) obtain a North Carolina State University ("NC State") Research Assistant verification letter; and (5) resolve the "Dr." title inconsistency and minor precision items.

---

## II. Documents Reviewed

| # | Document | Date | Source |
|---|----------|------|--------|
| 1 | ETA Form 9089 (PERM application), Case No. A-18247-63910 | Filed Mar. 15, 2025; certified May 22, 2025 | Prismex / DOL |
| 2 | Prevailing Wage Determination, PWD No. P-200-24187-329156 | Issued Nov. 8, 2024 | DOL NPWC |
| 3 | Beneficiary résumé/CV (Dr. Ananya Mehrotra) | undated (transmitted Jun. 4, 2025) | Beneficiary |
| 4 | Experience letter — DataBridge Solutions LLC (Dr. Samuel Okonkwo, VP Data Science) | Apr. 10, 2025 | DataBridge |
| 5 | Experience letter — Evalpoint Technologies Pvt. Ltd. (Vikram Reddy, Dir. Eng.) | Mar. 28, 2025 | Evalpoint |
| 6 | NC State University official transcript (M.S. Computer Science) | Issued May 20, 2025 | NC State Registrar |
| 7 | IAE credential evaluation report (No. IAE-2025-02-4738) | Feb. 15, 2025 | Int'l Academic Evaluators (NACES) |
| 8 | Professional certifications compilation (AWS CCP; TensorFlow Developer) | June 2025 | Whitmore & Callahan LLP |
| 9 | HR-to-counsel email (M. Foss → C. Halloran) re: petition package | Jun. 4, 2025 | Prismex HR |

---

## III. Summary of PERM Minimum Requirements and Alien Attestations

**Position:** Senior Machine Learning Engineer; SOC 15-2051 (Data Scientists); Level III; 40 hrs/wk; $142,000/yr; Austin-Round Rock-Georgetown, TX MSA.

**Section J.B — Minimum Job Requirements (as attested by the Employer):**

- **J.B.1 Education:** Master's degree in Computer Science, Machine Learning, or a closely related field.
- **J.B.3 Experience:** 5 years of progressive post-master's experience in machine learning engineering or a closely related occupation.
- **J.B.4 Alternate combination:** None accepted.
- **J.B.5 Special skills / other requirements:** Experience must include — (a) designing and deploying production-grade deep learning models using TensorFlow or PyTorch; (b) experience with distributed computing frameworks including Apache Spark; (c) NLP pipeline development; (d) cloud-based ML deployment on AWS SageMaker or Google Vertex AI; (e) proficiency in Python and R. **"AWS Certified Machine Learning – Specialty certification or equivalent required."** Position requires up to 10% domestic travel and supervision of a team of 3–5 ML engineers.

**Section K — Alien Work Experience Declarations (Employer's attestations regarding the Beneficiary):**

- **K.1** Meets education minimum? **Yes** (M.S. CS, NC State, May 2018).
- **K.2** Meets experience minimum? **Yes** — "approximately 7 years of post-master's experience at DataBridge Solutions LLC (June 2018 – present)."
- **K.3** Possesses special skills/other requirements (J.B.5)? **Yes.**
- **K.4** Qualified for the job opportunity? **Yes.**
- **K.5** Gained qualifying experience with the petitioning employer? **No** (never employed by Prismex).

The Beneficiary signed the Section L alien declaration under penalty of perjury (18 U.S.C. § 1546), and the Employer certified the application under Section N.

---

## IV. Gap Analysis

The findings below are organized by severity. A consolidated summary table appears at Section IV.E.

### A. Critical Gap

#### A.1 Required AWS certification not held; Section K.3 attestation contradicted by the record

**Requirement (J.B.5):** "AWS Certified Machine Learning – Specialty certification or equivalent required."

**Attestation (K.3):** The Employer attested that the Beneficiary "possesses the special skills and other requirements stated in Section J.B.5" — i.e., **Yes**.

**Supporting evidence (Certifications Compilation, June 2025):**

| Credential | Level | Issuer | Issued | Status at priority date (Mar. 15, 2025) | Satisfies requirement? |
|------------|-------|--------|--------|------------------------------------------|------------------------|
| AWS Certified Cloud Practitioner | Foundational | Amazon Web Services | Jan. 18, 2022 | **Expired** (expired Jan. 18, 2025) | No — foundational level; "does not demonstrate specialization in any specific AWS service domain, including machine learning" |
| TensorFlow Developer Certificate | Professional/Developer | Google (TensorFlow) | Mar. 10, 2023 | Active (no expiration) | No — "framework-specific," "issued by Google," "not affiliated with Amazon Web Services (AWS)" |

Critically, counsel's own **Certification Verification Note 3** states: *"Counsel specifically inquired whether the beneficiary holds the AWS Certified Machine Learning – Specialty certification or any other AWS specialty-level certification; the beneficiary confirmed she does not hold any such certification."*

**Analysis.** The Beneficiary does not hold the AWS Certified Machine Learning – Specialty certification, nor any AWS specialty-level certification, nor any credential that is fairly "equivalent" to it. At the priority date she held **no active AWS certification at all** (the Cloud Practitioner had expired on January 18, 2025, approximately two months before filing), and her only active certification (TensorFlow Developer) is a Google-issued, framework-specific credential that counsel's compilation expressly distinguishes from an AWS specialty certification. The "or equivalent" clause should not be read to swallow the requirement entirely; an "equivalent" must be substantially comparable in scope, rigor, and subject matter (here, AWS-specific machine-learning services and ML engineering on AWS), and the TensorFlow Developer Certificate is not.

This creates a direct internal contradiction: the application attests in K.3 that the Beneficiary possesses a required special skill that the record affirmatively shows she does not possess. Under 20 CFR 656.17(i), the Employer must attest that the alien meets all job requirements and possesses the required education, training, and experience; the alien must meet the requirements as of the time of filing. A required certification is a job requirement. Because the Beneficiary did not hold the certification at filing — and does not hold it now — the K.3 attestation is not supported by the documentation.

**Risk.** If the application is selected for audit (20 CFR 656.20), the DOL will require documentation that the Beneficiary meets all stated requirements, including the certification. The absence of the certification, combined with the affirmative K.3 attestation, exposes the certification to revocation under 20 CFR 656.31 (including 656.31(b)(3), misrepresentation / failure to document) and undermines the Beneficiary's Section L perjury declaration and the Employer's Section N certification. The same gap will surface in the I-140 adjudication, where USCIS evaluates whether the Beneficiary meets all requirements as of the priority date.

**Important limitation on cure.** Because the certification must have been held at the time of filing, **obtaining the AWS Certified Machine Learning – Specialty certification now will not retroactively establish possession as of the March 15, 2025 priority date** for the current certified PERM. Obtaining it is still advisable (it supports the H-1B specialty-occupation showing, any refiling, and the Beneficiary's general qualifications), but it does not repair the existing application. See remedial recommendations at Section VI.A.

### B. High-Severity Discrepancy

#### B.1 FEIN mismatch between the PERM and the Prevailing Wage Determination

**PERM (Section C.7):** Federal Employer Identification Number — **84-3291756**.
**PWD (Section 1):** Federal Employer ID Number — **84-3291047**.

The two FEINs differ (the fifth through eighth digits are 1756 vs. 1047). The Prevailing Wage Determination must correspond to the petitioning employer; a FEIN mismatch raises a question whether the PWD was issued to the correct legal entity, or whether one document contains a clerical error. Although the PERM is already certified, the FEIN is a foundational employer-identity data element that must be consistent across the PWD, the PERM, the I-140, and the I-129.

**Risk.** An unreconciled FEIN discrepancy can trigger an I-140 Request for Evidence (RFE) or Notice of Intent to Deny (NOID) on employer identity, and can complicate the ability-to-pay analysis (which keys off the petitioning employer's FEIN and federal tax records). It should be resolved before any further filing.

### C. Moderate Gaps

#### C.1 R programming proficiency likely insufficient to satisfy J.B.5(e)

**Requirement (J.B.5(e)):** "proficiency in Python and R programming languages."

**Evidence:**

- Résumé: lists R as **"intermediate"** (vs. Python "expert"); describes "some use of R for statistical reporting."
- DataBridge experience letter (Data Scientist II duties): "Used Python as the primary programming language, with **some use of R** for statistical reporting and ad hoc data analysis."
- NC State transcript: one relevant course, **ST 558 Statistical Computing with R (grade A-)**; no other R coursework.

**Analysis.** The Beneficiary's Python proficiency is clearly established (expert; primary language across all roles). Her R exposure, by contrast, is characterized consistently — by her own résumé and by her supervisor — as "intermediate" / "some use" for "statistical reporting and ad hoc data analysis," supported by a single graduate course. This is below the "proficiency" standard the Employer set in J.B.5(e). The requirement is conjunctive ("Python **and** R"), so marginal R competence is a gap.

This is also a two-sided PERM vulnerability: (i) if "proficiency in R" is a bona fide minimum requirement, the Beneficiary does not clearly meet it; and (ii) if the position in fact uses R only minimally, the requirement may be overstated relative to the actual job, which is itself a problem because the Employer has attested that the Beneficiary meets it (K.3). Either way, the R requirement warrants attention.

#### C.2 No experience verification letter for the NC State Research Assistant position

**PERM (Experience Entry 2):** Research Assistant, NC State Department of Computer Science, Aug. 15, 2016 – May 15, 2018, 20 hrs/week, "related occupation."

**Evidence:** The HR-to-counsel email expressly flags that **no experience verification letter from NC State** has been obtained for this position. The Beneficiary contacted Professor Helen Tsai (the thesis advisor and RA supervisor), but Professor Tsai is on sabbatical and has not responded. The Employer proposes to rely on the transcript, which records the graduate assistantship appointment, supervisor, and NSF funding source.

**Analysis.** A supervisor/HR experience letter detailing duties is the preferred documentation for any experience claimed on a PERM application. The transcript confirms the *existence* of the appointment but does not describe the *duties* at the level of specificity DOL expects in an audit. Two aggravating factors: (1) the RA appointment was **part-time (20 hrs/week)**, so any credit would be pro-rated; and (2) the appointment was **concurrent with the M.S. degree** the Beneficiary was earning (Aug. 2016 – May 2018; degree conferred May 12, 2018), and experience gained concurrently with the qualifying education generally cannot be counted toward the experience requirement. Fortunately, this experience is **not needed** to satisfy the 5-year post-master's minimum (the DataBridge experience alone exceeds it — see Section V), so the practical impact is limited. Nonetheless, because the experience is listed on the application, an audit could request verification of it, and the missing letter is a documentation gap.

#### C.3 Supervisory scope — 2 (documented) vs. 3–5 (required by the position)

**Requirement (J.B.5 / job description):** "Will supervise a team of 3–5 ML engineers."

**Evidence:** Both the résumé and the DataBridge experience letter state that, as Data Scientist II, the Beneficiary "**led a team of 2 junior data scientists**."

**Analysis.** The supervisory responsibility is phrased in J.B.5 as a prospective job duty ("**Will** supervise a team of 3–5 ML engineers") rather than as a prior-experience prerequisite (the "Experience must include" list at J.B.5(a)–(e) is technical and does not include prior supervisory experience of a stated size). On that reading, this is not a strict qualification gap — the Beneficiary will perform the supervision in the new role. However, because K.3 attests that the Beneficiary possesses "the special skills and other requirements stated in Section J.B.5" (which includes the supervisory duty), and because her documented supervisory experience (2 reports) is smaller than the team she will manage (3–5), the point is worth addressing to avoid an inference that she lacks the demonstrated capacity for the supervisory scope. This is a moderate, clarifiable issue rather than a disqualifying one.

### D. Lower-Priority / Consistency Issues

#### D.1 Use of the "Dr." title without a doctoral degree

The Beneficiary is referred to as **"Dr. Ananya Mehrotra"** on the PERM (Section I.1: "also known as: Dr. Ananya Mehrotra"), the résumé, the DataBridge experience letter, the certifications compilation, and the HR email. Her highest conferred degrees, however, are a B.Tech (2013) and an M.S. (2018) — **no Ph.D. or other doctoral degree** appears in the NC State transcript, the IAE evaluation, or any other document. Notably, the Evalpoint experience letter refers to her as **"Ms. Ananya Mehrotra."** The "Dr." usage is therefore internally inconsistent and unsupported by the credential record. While likely a courtesy or stylistic usage, in a formal immigration context it can invite credibility questions or an appearance of credential inflation and should be made consistent and accurate.

#### D.2 "Approximately 7 years" experience statement is imprecise

Section K.2 states the Beneficiary has "approximately 7 years of post-master's experience at DataBridge Solutions LLC (June 2018 – present)." Measured to the priority date (March 15, 2025), the post-master's experience is **June 4, 2018 – March 15, 2025 ≈ 6 years, 9 months, 11 days (~6.77 years)** — i.e., closer to 6 years 9 months than 7 years. This is immaterial because the Beneficiary comfortably exceeds the 5-year minimum, but the I-140 experience calculation should state the figure precisely rather than rounding up to "7 years."

#### D.3 Research Assistant experience — concurrent with the degree and part-time (strategy)

As noted in C.2, the NC State RA experience (Entry 2) is both part-time and concurrent with the M.S. degree and therefore should **not** be relied upon to satisfy the 5-year *post-master's* minimum. The qualifying experience for the minimum should be attributed solely to the DataBridge post-master's employment. Listing the RA experience on the application is permissible as background, but the I-140 experience summary should not lean on it for the minimum.

#### D.4 Certifications compilation labeling

The certifications compilation is headed "Compiled for H-1B Petition Filing" yet also bears the PERM case number (A-18247-63910). This is cosmetic, but the compilation is being used to support the PERM audit file and the I-140 as well; the labeling should be corrected or generalized to avoid confusion about which filing the document supports.

#### D.5 Experience letters dated after the PERM filing date

The Evalpoint letter (Mar. 28, 2025) and the DataBridge letter (Apr. 10, 2025) are both dated after the March 15, 2025 filing. This is generally acceptable for the PERM audit file (supporting documents are retained, not submitted with the electronic filing) so long as the letters verify experience gained *before* the priority date, which they do. No action required, but the DataBridge letter describes duties "to present" (Apr. 10, 2025); the qualifying experience should be measured to the priority date, not to the letter date.

### E. Consolidated Gap Summary

| # | Gap / Discrepancy | PERM element at issue | Evidence status | Severity |
|---|-------------------|----------------------|-----------------|----------|
| A.1 | AWS Certified ML – Specialty (or equivalent) not held; K.3 "Yes" contradicted | J.B.5 special req.; K.3 attestation | Affirmatively refuted by counsel's verification notes | **Critical** |
| B.1 | FEIN mismatch (PERM 84-3291756 vs. PWD 84-3291047) | C.7 / PWD employer identity | Confirmed on face of documents | **High** |
| C.1 | R proficiency likely below "proficiency" standard | J.B.5(e); K.3 | "Intermediate" / "some use"; one course | Moderate |
| C.2 | No NC State RA experience verification letter | J.C Entry 2; audit file | HR email confirms absence | Moderate |
| C.3 | Supervisory scope 2 vs. 3–5 | J.B.5 / job duty | Resume + DataBridge letter | Moderate |
| D.1 | "Dr." title without doctoral degree | I.1; consistency | Transcript/IAE show no doctorate | Low–Mod |
| D.2 | "Approximately 7 years" imprecise (~6.77) | K.2 | Arithmetic | Low |
| D.3 | RA experience concurrent/part-time — do not rely on for minimum | J.C Entry 2 | Transcript | Low |
| D.4 | Certifications compilation mislabeled | Audit file / I-140 | Face of document | Low |
| D.5 | Experience letters post-dated to filing | J.C; audit file | Acceptable; note | Low |

---

## V. Positive Findings (Credentials That Are Solid)

The following elements are well documented and require no remedial action:

1. **Education (J.B.1 / K.1).** The Beneficiary holds an M.S. in Computer Science from NC State, conferred May 12, 2018 (GPA 3.74/4.00; 45 credit hours), which directly satisfies the "Master's degree in Computer Science, Machine Learning, or a closely related field" requirement. The foreign B.Tech in Electronics and Communication Engineering (MIT-Pune / Savitribai Phule Pune University, June 2013) was evaluated by a NACES-member agency (IAE) as equivalent to a U.S. four-year bachelor's degree, properly documenting the prior degree and admission basis. No education gap.

2. **Experience quantity and progression (J.B.3 / K.2).** Post-master's experience at DataBridge (June 4, 2018 – priority date) totals approximately 6 years 9 months, exceeding the 5-year minimum. The promotion from Data Scientist I to Data Scientist II (Jan. 4, 2021), with increased technical scope and team-leadership responsibility, documents the "progressive" element.

3. **Core technical special skills (J.B.5(a)–(d)).** The résumé and the DataBridge experience letter together document: (a) production deep learning with TensorFlow and PyTorch; (b) distributed computing with Apache Spark MLlib; (c) NLP pipeline development (NER, sentiment analysis, clinical text); and (d) cloud-based ML deployment on AWS SageMaker (and AWS EC2 in the earlier role). These four technical requirements are satisfied.

4. **Prevailing wage.** The PWD ($131,747/yr, SOC 15-2051, Level III, Austin-Round Rock-Georgetown, TX MSA) was issued Nov. 8, 2024 and is valid through Nov. 7, 2025, covering the March 15, 2025 filing date. The offered wage ($142,000/yr) exceeds the prevailing wage. No wage gap.

5. **No experience gained with the petitioning employer (K.5).** The Beneficiary has never been employed by Prismex, so there is no issue of qualifying experience having been gained with the petitioning employer (which would be impermissible under 20 CFR 656.17(i)(5)).

6. **Evalpoint experience letter.** The Evalpoint letter is well executed — signed by the Director of Engineering, confirms full-time status (40+ hrs/wk) and exact dates (July 1, 2013 – July 15, 2016), and candidly characterizes the ML exposure as ancillary. It is not needed for the post-master's minimum but is solid supporting documentation.

---

## VI. Remedial Recommendations

### A. Critical — AWS certification requirement (Gap A.1)

The Employer must make a deliberate strategic decision, because the current certified PERM cannot be retroactively cured. The options, in order of preference:

1. **Refile a new PERM with the certification requirement removed or reframed as a preference** (recommended if the certification is not, in fact, a bona fide minimum requirement for the job). This is the cleanest path to a defensible application. It requires a new PWD and a new recruitment cycle, and it resets the priority date (forfeiting the March 15, 2025 date). Given that the Beneficiary's immediate nonimmigrant bridge is the FY2026 H-1B (STEM OPT expires Sept. 15, 2025; target I-129 filing July 15, 2025), the H-1B is independent of the PERM timeline, so a PERM refiling does not jeopardize her near-term work authorization.

2. **If the certification is a genuine bona fide minimum requirement, have the Beneficiary earn the AWS Certified Machine Learning – Specialty certification and refile a new PERM.** Because she did not hold it at the current priority date, a refiling is still required; the newly earned certification will support the refiled application, the H-1B specialty-occupation showing, and the eventual I-140. Do **not** rely on the "or equivalent" clause to substitute the TensorFlow Developer Certificate — counsel's own compilation distinguishes the two, and the argument is unlikely to withstand audit or USCIS scrutiny.

3. **Do not file the I-140 on the current certified PERM without resolving this gap.** Filing the I-140 on an application whose K.3 attestation is contradicted by the record invites an RFE/NOID and, if the underlying PERM is later revoked in audit, jeopardizes the I-140 and the priority date. At minimum, counsel should obtain a written, signed Employer confirmation of the bona fide basis for the certification requirement (and for "proficiency in R") and document the analysis in the file before proceeding.

**Immediate action regardless of option chosen:** Have the Beneficiary register for and complete the AWS Certified Machine Learning – Specialty examination. This is low-cost, high-value: it strengthens the H-1B petition, positions the case for a clean refiling, and removes the most visible credential deficiency.

### B. High — FEIN reconciliation (Gap B.1)

1. Obtain the Employer's IRS-issued FEIN confirmation (CP-575 notice or Form 147C) and confirm the correct FEIN.
2. Determine which document (the PERM or the PWD) bears the erroneous FEIN.
3. Ensure the **I-140, I-129, and ability-to-pay documentation** all use the single correct FEIN and are internally consistent with the Employer's federal tax records.
4. If the PERM contains the error, note it for the file; while the PERM is already certified, the I-140 should be filed with the correct FEIN and, if an RFE issues on the point, be prepared to explain the clerical discrepancy with IRS documentation. If the PWD contains the error, assess whether a corrected PWD is needed for the refiling recommended in Section VI.A.

### C. Moderate — R proficiency (Gap C.1)

1. **Bolster the R evidence** if the Beneficiary's R competence is, in fact, stronger than the current documentation suggests: obtain a supplemental statement from DataBridge (Dr. Okonkwo) quantifying R usage — specific projects, tools/packages (e.g., tidyverse, caret, ggplot2), duration/frequency, and deliverables — to elevate the showing from "some use" to "proficiency."
2. **Revisit whether "proficiency in R" is a bona fide minimum requirement.** If the position uses R only marginally, the requirement should be softened (e.g., "working knowledge of R" or "familiarity with R") in any refiling, consistent with the actual job. An overstated requirement that the Beneficiary does not meet is a PERM vulnerability independent of the documentation.
3. If the requirement is retained as "proficiency," ensure the I-140 support package affirmatively documents R proficiency (supplemental letter + the ST 558 coursework + any R-based project artifacts).

### D. Moderate — NC State Research Assistant letter (Gap C.2)

1. Obtain a verification letter from **NC State University HR** or the **Department of Computer Science administrator** (the HR email identifies this as the backup path), confirming the RA appointment, dates (Aug. 15, 2016 – May 15, 2018), part-time hours, supervisor (Prof. Tsai), and a description of duties. A departmental/HR letter is an acceptable substitute for the supervisor's letter while Prof. Tsai is on sabbatical.
2. Continue efforts to reach Prof. Tsai (department administrator can often forward or provide an alternate contact).
3. In the I-140 experience analysis, **do not rely on the RA experience** to satisfy the 5-year post-master's minimum (it is concurrent with the degree and part-time); rely on the DataBridge post-master's experience. The RA letter is for audit-file completeness only.

### E. Moderate — Supervisory scope (Gap C.3)

1. In the I-140 support, frame the supervision of 3–5 ML engineers as a **prospective job duty** of the offered position, not as a prior-experience prerequisite.
2. Consider a supplemental DataBridge statement describing any broader leadership/mentorship beyond the two direct reports (e.g., cross-team mentorship, project leadership, code-review authority across teams, onboarding/training) to demonstrate readiness to manage a 3–5 person team.

### F. Lower-priority items (Gaps D.1–D.5)

1. **"Dr." title (D.1):** Use a single, accurate form of address across all filings. As the Beneficiary holds no doctoral degree, "Ms. Ananya Mehrotra" (consistent with the Evalpoint letter) is the accurate usage; correct the PERM alias, résumé, and counsel-prepared compilations going forward. If "Dr." reflects an honorary or cultural usage, document the basis; otherwise standardize on "Ms."
2. **Experience precision (D.2):** State the post-master's experience as approximately 6 years 9 months (as of the March 15, 2025 priority date) in the I-140, not "7 years."
3. **RA reliance (D.3):** Confine the 5-year minimum to DataBridge post-master's experience; treat the RA and Evalpoint experience as background only.
4. **Compilation labeling (D.4):** Relabel the certifications compilation to reflect its use across the PERM audit file, I-140, and H-1B (e.g., "Credential Supporting Documents — PERM A-18247-63910 / I-140 / I-129").
5. **Letter dates (D.5):** No action required; ensure the experience calculation uses the priority date, not the letter date.

### G. Prioritized Action Plan

| Priority | Action | Owner | Target |
|----------|--------|-------|--------|
| 1 | Reconcile FEIN with IRS records; confirm correct FEIN for all filings | Prismex / counsel | Before I-140 / I-129 filing |
| 2 | Strategic decision on AWS certification requirement (refile vs. remove); register Beneficiary for AWS ML – Specialty exam | Prismex / counsel / Beneficiary | Immediate; exam before any refiling |
| 3 | Decide whether to file I-140 on current PERM or after refiling (recommend refiling) | Counsel / Prismex | Before July 15, 2025 I-129; I-140 per refiling timeline |
| 4 | Bolster R-proficiency evidence or revisit the R requirement | DataBridge / counsel | Before I-140 / refiling |
| 5 | Obtain NC State RA verification letter (HR/dept. admin) | Beneficiary / counsel | Before audit response / I-140 |
| 6 | Supplement DataBridge letter re: broader leadership (supervisory scope) | DataBridge / counsel | Before I-140 |
| 7 | Standardize form of address; correct "Dr." usage; fix compilation labeling; precise experience figures | Counsel | Before next filing |

---

## VII. Risk Assessment and Downstream Impact

**PERM audit / revocation exposure.** The certified PERM remains subject to audit for the regulatory period and to revocation under 20 CFR 656.31. The AWS certification gap (A.1) is the principal exposure: an audit would require documentation that the Beneficiary met all J.B.5 requirements at filing, and the record affirmatively shows she did not hold the required certification. The FEIN mismatch (B.1) and the R-proficiency question (C.1) are secondary audit points. The missing RA letter (C.2) is a documentation gap but is mitigated by the fact that the RA experience is not needed for the minimum.

**I-140 immigrant petition.** USCIS will assess whether the Beneficiary meets all requirements as of the priority date and whether the Employer has the ability to pay the offered wage. The AWS certification gap and the FEIN mismatch are the most likely RFE/NOID triggers. Filing the I-140 on the current PERM without resolving A.1 is not recommended. The ability-to-pay analysis keys off the petitioning employer's FEIN and federal tax returns, making FEIN consistency essential.

**H-1B (I-129) — near-term bridge.** The H-1B is a nonimmigrant petition that does not depend on the PERM and is the Beneficiary's bridge past the September 15, 2025 STEM-OPT expiration. The credential gaps identified here are less acute for the H-1B specialty-occupation analysis (which turns on the degree and the specialty occupation, both of which are satisfied), but the AWS certification and R-proficiency items still bear on the Beneficiary's qualifications showing. The cap-gap extension question raised by HR (whether F-1 STEM OPT and employment authorization extend through October 1 upon timely I-129 filing) should be addressed in a separate advisory; it is outside the scope of this credential review but is time-sensitive given the September 15, 2025 expiration.

**Priority-date preservation.** If a PERM refiling is undertaken (recommended for Gap A.1), the March 15, 2025 priority date will be lost and reset to the new filing date. For an India-born beneficiary in the EB-2 category, priority-date preservation is significant; counsel should weigh this against the audit/revocation risk of proceeding on the current application. The H-1B bridge is unaffected.

---

## VIII. Conclusion

The Beneficiary's education and core machine-learning experience are strong and well documented, and the wage and recruitment fundamentals are in order. The application's vulnerability is concentrated in the **special-skills requirements**: the Employer required an AWS Certified Machine Learning – Specialty certification (or equivalent) and attested that the Beneficiary possesses it, but the Beneficiary does not hold it — a contradiction that cannot be cured retroactively for the current certified PERM and that should be resolved through a refiling decision before the I-140 is filed. The FEIN mismatch must be reconciled immediately, and the R-proficiency, NC State RA letter, supervisory-scope, and titling/precision items should be cleaned up in the ordinary course. With these remedial steps, the case can be placed on defensible footing for both the immigrant (I-140) and nonimmigrant (H-1B) tracks.

We are available to discuss the refiling strategy, the FEIN reconciliation, and the cap-gap advisory at your convenience.

---

## Appendix A — Requirement-to-Evidence Cross-Reference

| PERM requirement (Section J.B) | Beneficiary evidence | Met? | Notes |
|--------------------------------|----------------------|------|-------|
| J.B.1 Master's in CS/ML/closely related field | M.S. CS, NC State, May 12, 2018 (transcript); B.Tech ECE evaluated by IAE (NACES) | **Yes** | Direct match |
| J.B.3 5 yrs progressive post-master's in ML eng./related | DataBridge DS I/II, June 4, 2018 – priority date (~6 yrs 9 mo); promotion DS I→DS II | **Yes** | Exceeds minimum; progressive via promotion |
| J.B.5(a) DL models, TensorFlow/PyTorch | DataBridge DS II (TF + PyTorch); DS I (TF); résumé | **Yes** | — |
| J.B.5(b) Apache Spark | DataBridge DS II (Spark MLlib); résumé | **Yes** | — |
| J.B.5(c) NLP pipelines | DataBridge (NER, sentiment, clinical); NC State RA (NLP research) | **Yes** | — |
| J.B.5(d) AWS SageMaker or Google Vertex AI | DataBridge DS II (SageMaker); DS I (EC2) | **Yes** | SageMaker satisfies "or" |
| J.B.5(e) proficiency in Python and R | Python: expert (yes); R: "intermediate"/"some use," one course | **Partial** | R below "proficiency" — Gap C.1 |
| J.B.5 AWS Certified ML – Specialty or equivalent | AWS Cloud Practitioner (foundational, **expired** Jan 2025); TensorFlow Developer (Google, not AWS) | **No** | Gap A.1 — critical; K.3 contradicted |
| J.B.5 up to 10% domestic travel | Job condition (not a credential) | N/A | — |
| J.B.5 supervise 3–5 ML engineers | Documented supervision of 2 (DataBridge) | **Partial** | Prospective duty; Gap C.3 |
| K.5 no qualifying experience with petitioner | Never employed by Prismex | **Yes** | No issue |

## Appendix B — Document Inventory and Status

| Document | Date | Status / Notes |
|----------|------|----------------|
| ETA-9089 (PERM A-18247-63910) | Filed Mar. 15, 2025; certified May 22, 2025 | Certified; contains K.3 attestation gap (A.1) and FEIN 84-3291756 (B.1) |
| PWD P-200-24187-329156 | Nov. 8, 2024 (valid thru Nov. 7, 2025) | Valid; FEIN 84-3291047 — mismatch with PERM (B.1) |
| Résumé | undated | "Dr." title (D.1); R "intermediate" (C.1) |
| DataBridge experience letter | Apr. 10, 2025 | Solid; post-dated to filing (D.5); "team of 2" (C.3); "some use of R" (C.1) |
| Evalpoint experience letter | Mar. 28, 2025 | Solid; pre-master's, ancillary ML; uses "Ms." (D.1) |
| NC State transcript | Issued May 20, 2025 | Confirms M.S. (May 12, 2018) and RA appointment; no duties letter (C.2) |
| IAE credential evaluation | Feb. 15, 2025 | NACES; B.Tech = U.S. bachelor's; covers B.Tech only |
| Certifications compilation | June 2025 | Confirms no AWS ML – Specialty (A.1); AWS CCP expired; mislabeled (D.4) |
| HR-to-counsel email | Jun. 4, 2025 | Flags missing NC State RA letter (C.2); cap-gap question (separate advisory) |

---

*Prepared as attorney work product in anticipation of the I-140/I-129 filing and potential PERM audit. This memorandum reflects review of the documents listed in Section II as transmitted on June 4, 2025, and does not constitute a representation as to any document not reviewed.*