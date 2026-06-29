### FILE: gap-analysis-memo.md
# PRIVILEGED & CONFIDENTIAL — ATTORNEY-CLIENT PRIVILEGE / ATTORNEY WORK PRODUCT

# MEMORANDUM

| | |
|---|---|
| **TO:** | Audit Committee of the Board of Directors; Marcus Ellsworth, Chief Executive Officer; Lauren Hessler, Chief Technology Officer; Derek Fong, Chief Information Security Officer |
| **FROM:** | Office of the General Counsel — Priya Raghavan, General Counsel & Corporate Secretary, in coordination with Hollister Marsh LLP (Jonathan Beckett), outside securities counsel |
| **DATE:** | December 6, 2024 |
| **RE:** | SEC Compliance Gap Analysis — Cybersecurity Incident INC-2024-0047 (LockStar 3.0 Ransomware and Data-Exfiltration Event of November 18, 2024) |
| **CLASSIFICATION:** | Privileged & Confidential — Prepared at the Direction of Counsel in Anticipation of Litigation and for the Purpose of Providing Legal Advice |

> **Privilege Notice.** This memorandum was prepared by and at the direction of the Office of the General Counsel of Vantage Industrial Technologies, Inc. (the "Company," "Vantage," "we," or "us") and outside counsel for the purpose of evaluating the Company's disclosure and compliance obligations in connection with the cybersecurity incident described herein. It is intended to be protected by the attorney-client privilege and the attorney work product doctrine. This memorandum contains preliminary legal analysis and should not be forwarded, copied, or distributed outside the recipients listed above without the express written consent of the General Counsel.

---

## I. Executive Summary

On November 18, 2024, the Company's Security Operations Center ("SOC") detected a ransomware and data-exfiltration incident (the "Incident," ServiceNow ticket INC-2024-0047) involving the LockStar 3.0 variant. The threat actor gained initial access through a compromised virtual private network ("VPN") credential belonging to a third-party maintenance contractor that was **not** protected by multi-factor authentication ("MFA"), exfiltrated approximately 83 GB of data (including customer banking information, procurement-contact personally identifiable information ("PII"), and contract pricing data for approximately 4,200 customer records), and then encrypted 347 of the Company's approximately 2,100 networked endpoints, including the finance, procurement, and order management modules of the Company's enterprise resource planning ("ERP") system. Operational technology ("OT") and SCADA systems were not affected.

As of the date of this memorandum — **seventeen (17) days after discovery** — the Company has not (i) conducted any formal materiality determination, (ii) filed any Form 8-K or other public disclosure with the U.S. Securities and Exchange Commission (the "SEC"), (iii) issued any customer notifications (notwithstanding that contractual notification deadlines under at least three top-customer agreements expired on or before November 20, 2024), (iv) filed any state attorney general or international data-protection notifications, or (v) notified the Company's independent auditor or the counterparty to the Company's pending $425 million acquisition of Kessler Precision Systems GmbH. The Audit Committee Chair received her first notice of the Incident on December 3, 2024 (Day 15), and no special meeting of the Audit Committee has been called.

This memorandum identifies **fifteen (15) discrete compliance gaps** across SEC disclosure, disclosure accuracy, governance and board oversight, incident-response planning, customer-contract notification, insurance coverage, state and international breach notification, internal control over financial reporting ("ICFR"), pending M&A, and insider-trading controls. The most urgent findings are summarized below; each is developed in Part IV.

**Most urgent gaps (immediate action required):**

1. **No materiality determination and no Form 8-K filed under Item 1.05.** The SEC's cybersecurity disclosure rules require a materiality determination to be made "without unreasonable delay after discovery" and, upon a determination of materiality, a Form 8-K within four business days. Seventeen days have elapsed with no documented determination and no filing. Based on the qualitative and quantitative factors analyzed in Part V, the Incident is **likely material**, and a formal, documented materiality determination should be completed immediately, followed (if material, as appears likely) by an Item 1.05 Form 8-K.

2. **Disclosure-accuracy exposure in the FY2023 Form 10-K (Item 1C).** The Company's Annual Report on Form 10-K for the fiscal year ended December 31, 2023 (filed February 28, 2024) states that the Company has implemented MFA "for access to critical information systems, remote access connections, and administrative accounts." Thorngate Forensic Solutions, Inc. ("Thorngate") has determined that the compromised third-party contractor VPN credential was **not** MFA-protected and that MFA was not "universally required for third-party contractor VPN access" until November 20, 2024. This creates a potential inaccuracy or overstatement in a filed SEC disclosure and a corresponding control deficiency, and it independently jeopardizes the Company's cyber-insurance coverage (see Gap 9).

3. **Governance "timely escalation" disclosure inconsistent with actual practice.** The FY2023 10-K represents that the Company's processes "provide for escalation to the Board of Directors and, as appropriate, the Audit Committee, to ensure that the Board is informed in a timely manner" of significant cybersecurity incidents. The Audit Committee Chair was not notified until Day 15, and no special meeting has been called. This is difficult to reconcile with the "timely manner" representation.

4. **Customer-contract notification breaches.** Three of the Company's top-ten customers (Harmon Defense Solutions, Crestfield Aerospace, and Nexagen Manufacturing) impose 48-hour notification obligations that expired no later than November 20, 2024. No notifications have been sent. These breaches expose the Company to liquidated damages ($500,000 per incident under the Harmon agreement), immediate and short-fuse termination rights, payment suspension, audit rights, indemnification, and exclusion from future business — and they are independently material to the SEC materiality analysis because the top-ten customers represent approximately 38% of revenue (~$710.6 million).

5. **Cyber-insurance coverage at material risk.** The Company notified Ridgeline Insurance Group approximately 73 hours after discovery, one hour beyond the policy's 72-hour notice requirement (Ridgeline has reserved rights). More seriously, the policy application warranted MFA "for all remote access to Computer Systems," and the policy contains a "Failure to Maintain Minimum Security Standards" exclusion; the absence of MFA on the contractor VPN materially contributed to the Incident. Coverage — including the ~$2.0 million expected above the $2.5 million self-insured retention — is at risk of denial.

The remaining gaps (CIRP structural deficiencies, Audit Committee charter, state/international breach notification, independent-auditor and ICFR notification, pending-M&A disclosure, and insider-trading/trading-window controls) are developed in Part IV and the recommendations in Part VI.

---

## II. Factual Background and Chronology

### A. The Company

Vantage Industrial Technologies, Inc. (NASDAQ: VTIQ) is a Delaware corporation headquartered in Columbus, Ohio, that designs, manufactures, and distributes industrial automation solutions through 14 facilities in the United States, Germany, and Mexico, with approximately 6,800 employees. The Company is an accelerated filer. Projected FY2024 revenue is approximately $1.87 billion; projected FY2024 EBITDA is approximately $310 million. The Company's independent auditor is Greystone & Associates LLP. The Company is in active negotiations to acquire Kessler Precision Systems GmbH for approximately $425 million, with Canfield Cromdale Consulting & Co. advising.

### B. The Incident (INC-2024-0047)

On November 18, 2024, at approximately 2:17 a.m. EST, the SOC detected anomalous network activity originating from a VPN session authenticated with a credential belonging to a third-party maintenance contractor. Thorngate's interim status report dated December 1, 2024 (the "Thorngate Interim Report") establishes the following with high confidence:

- **Attack vector.** A compromised third-party contractor VPN credential that was **not** protected by MFA. Anomalous logins from an Eastern-European IP address began on or about November 14, 2024, followed by three to four days of low-volume internal reconnaissance.
- **Phase 1 — Data exfiltration (approx. 1:30 a.m. – 2:15 a.m. EST, Nov. 18).** Approximately 83 GB of data was exfiltrated to an external IP address via outbound HTTPS *before* ransomware deployment (a deliberate "double-extortion" methodology). Exfiltrated data includes, with high confidence: customer master records for approximately 4,200 corporate accounts; procurement-contact PII (names, emails, phone numbers, titles); contract pricing data; and **customer banking information (ACH routing numbers and account numbers), stored unencrypted at rest**.
- **Phase 2 — Ransomware deployment (approx. 2:17 a.m. – 4:45 a.m. EST, Nov. 18).** LockStar 3.0 encrypted 347 of approximately 2,100 endpoints, including the ERP finance, procurement, and order management modules. A ransom demand of 45 Bitcoin (~$2,029,500) was made; the Company has not paid and does not intend to pay.
- **OT/SCADA unaffected.** The air-gapped IT/OT segmentation performed as designed; manufacturing operations were not impacted.
- **Geographic scope of exfiltrated data.** Affected customer records span at least 38 U.S. states plus Germany, Mexico, Canada, and the United Kingdom, across defense, aerospace, and general-manufacturing sectors, including several of the Company's largest accounts by revenue.

### C. Estimated Financial Impact (as of December 5, 2024)

| Category | Estimated Cost |
|---|---:|
| Incident response costs (Thorngate, emergency IT labor, hardware, overtime) | $1,400,000 |
| Business disruption (delayed order processing, manual workarounds, lost productivity) | $2,800,000 |
| Customer-notification preparation (vendor, call center, credit monitoring) | $300,000 |
| **Total estimated costs (as of Dec. 5, 2024)** | **$4,500,000** |

The $4.5 million estimate equals approximately 1.45% of projected FY2024 EBITDA. It does **not** include potential customer claims, liquidated damages, indemnification, litigation, regulatory penalties, reputational impact, or the effect of any insurance-coverage denial, all of which could materially increase net exposure.

### D. Notification Chronology

| Date (Day) | Event |
|---|---|
| Nov. 18, ~2:17 a.m. (Day 0) | SOC detects anomalous activity. |
| Nov. 18, ~4:45 a.m. (Day 0) | Ransomware deployment across 347 endpoints completed. |
| Nov. 18, 5:00 a.m. (Day 0) | IRT activated under Tier 3 classification. |
| Nov. 18, 11:00 a.m. (Day 0) | CTO Lauren Hessler verbally informed (~6 hours after IRT activation). |
| Nov. 19 (Day 1) | Thorngate retained; Associate GC Daniel Ito learns of Incident informally. General Counsel traveling internationally; **not** informed. |
| Nov. 20 (Day 2) | General Counsel Priya Raghavan learns of Incident upon return from travel; FBI IC3 contacted; Hollister Marsh LLP engaged. |
| Nov. 21 (Day 3) | Ridgeline Insurance Group notified (~73 hours post-discovery; policy requires 72 hours). |
| Nov. 25 (Day 7) | CEO Marcus Ellsworth briefed. |
| Dec. 1 (Day 13) | Thorngate Interim Report confirms customer banking data exfiltrated. |
| Dec. 3 (Day 15) | Audit Committee Chair Dr. Helen Ostrowski emailed — **first Board-level notification**. |
| Dec. 5 (Day 17) | Incident Status Report prepared; no 8-K filed; no materiality determination; no customer notifications. |
| Jan. 22, 2025 | Next regularly scheduled Audit Committee meeting (no special meeting called). |

### E. Notifications NOT Made (as of December 5, 2024)

- SEC: no Form 8-K or other filing; no formal materiality determination.
- Customers (Harmon, Crestfield, Nexagen, and others): no notifications sent.
- State attorneys general / state data-protection authorities: none.
- International regulators (EU/UK/Germany data-protection authorities): none.
- Independent auditor (Greystone & Associates LLP): not notified.
- M&A counterparty (Kessler Precision Systems GmbH) and advisor (Canfield Cromdale Consulting & Co.): not notified.
- Public/media: no press release; no media inquiries received.

---

## III. Applicable SEC Regulatory Framework

The SEC's final rules on "Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure" (Release No. 33-11221), effective September 5, 2023, impose two principal disclosure obligations relevant here:

**1. Item 106 of Regulation S-K (annual disclosure).** Requires annual disclosure (on Form 10-K) of (a) the registrant's processes for assessing, identifying, and managing material risks from cybersecurity threats; (b) whether any cybersecurity risks or incidents have materially affected, or are reasonably likely to materially affect, the registrant's business strategy, results of operations, or financial condition; and (c) board and management governance of cybersecurity risk. The Company's FY2023 Form 10-K, Item 1C, addresses these requirements.

**2. Item 1.05 of Form 8-K (current incident disclosure).** Requires a registrant to disclose on Form 8-K a cybersecurity incident that the registrant **determines to be material**, filed **within four business days after the registrant determines that a material cybersecurity incident has occurred**. The disclosure must describe the material aspects of the nature, scope, and timing of the incident, and the material impact or reasonably likely material impact on the registrant, including its financial condition and results of operations. The instruction to Item 1.05 requires the materiality determination to be made **"without unreasonable delay after discovery of the cybersecurity incident."** The four-business-day clock runs from the date of the materiality determination, not from the date of discovery. Disclosure may be delayed only where the U.S. Attorney General determines that disclosure would pose a substantial risk to national security or public safety (Item 1.05(c)) — a determination that has **not** been made or requested here.

**3. Materiality standard.** Materiality is assessed under the Supreme Court's standards (*TSC Industries, Inc. v. Northway, Inc.*; *Basic Inc. v. Levinson*), considering both quantitative and qualitative factors. The SEC's adopting release expressly identifies qualitative considerations relevant to cybersecurity incidents, including harm to the registrant's reputation, customer relationships, and competitiveness; the possibility of litigation or regulatory action; and the impact on the registrant's operations and financial condition.

**4. Compliance dates.** For accelerated filers, Item 1.05 of Form 8-K has been applicable since December 18, 2023. The Incident (November 18, 2024) falls squarely within the compliance period.

**5. Related federal regimes implicated.** (a) **Regulation FD** — selective disclosure of material non-public information to customers, the M&A counterparty, or other third parties before public disclosure raises Reg FD risk. (b) **Insider trading** — the Incident constitutes material non-public information known to numerous insiders; Section 10(b)/Rule 10b-5 and Section 16 exposure must be managed through trading-window controls. (c) **ICFR and disclosure controls and procedures ("DC&P")** — disruption of the ERP finance module and reliance on manual workarounds may affect ICFR and DC&P, with consequences for Sarbanes-Oxley Sections 302/404 certifications in the FY2024 Form 10-K. (d) **State breach-notification statutes** and (e) **GDPR / EU member-state data-protection law** for affected EU/UK customer records.

---

## IV. Gap Analysis

### Gap 1 — No Materiality Determination and No Form 8-K Filed (Item 1.05)

**Finding.** As of December 6, 2024 — seventeen days after discovery — the Company has conducted **no formal materiality determination** and filed **no Form 8-K**. The Incident Status Report of December 5, 2024 expressly states: "No formal materiality determination has been conducted." Outside securities counsel (Hollister Marsh LLP) was engaged on November 20, 2024 to advise on disclosure obligations, but no determination has been documented.

**Why this is a gap.** Item 1.05 requires the materiality determination to be made "without unreasonable delay after discovery." The SEC has emphasized that the forensic-investigation timeline is not, by itself, a basis to defer the materiality determination, and that registrants must assess materiality based on the information reasonably available. By December 1, 2024 (Day 13), the Thorngate Interim Report had confirmed with high confidence the exfiltration of customer banking data, PII, and contract pricing for approximately 4,200 customers — a set of facts that, on their face, implicates multiple qualitative materiality factors. The absence of any documented determination process — let alone a determination — by Day 17 is inconsistent with the "without unreasonable delay" standard and creates disclosure-timing risk.

**Risk.** If the Incident is determined to be material (as the analysis in Part V suggests is likely), the four-business-day filing clock will have effectively been running against the Company since the date a reasonable determination should have been made. Late or absent disclosure exposes the Company to SEC enforcement risk, shareholder litigation, and reputational harm. Even if the Company ultimately concludes the Incident is not material, that conclusion must be documented and defensible.

**Recommendation.** Convene the disclosure committee / materiality working group immediately (see Part VI). Complete and document a formal materiality determination without further delay. If material, file an Item 1.05 Form 8-K within four business days of the determination. If the determination cannot be completed promptly, consider whether the information then available nonetheless warrants disclosure, and document the basis for any continued evaluation.

### Gap 2 — Disclosure-Accuracy Exposure: MFA Representation in the FY2023 Form 10-K

**Finding.** The FY2023 Form 10-K, Item 1C, states that the Company "has implemented access management controls, including role-based access controls, privileged access management, and **multi-factor authentication for access to critical information systems, remote access connections, and administrative accounts**." The Thorngate Interim Report states that "the compromised credential was not protected by multi-factor authentication" and that "MFA was not universally required for third-party contractor VPN access" prior to November 20, 2024 (when MFA was enforced on all VPN connections *after* the Incident).

**Why this is a gap.** A third-party contractor VPN session is a "remote access connection." The filed disclosure therefore appears to overstate the actual MFA coverage as of the filing date (February 28, 2024) — or, at minimum, to omit a material qualification that MFA was not uniformly applied to third-party remote access. This raises two concerns: (i) a potential inaccuracy in a filed SEC disclosure, and (ii) a control deficiency in a control the Company publicly represented as implemented. The discrepancy also has direct insurance consequences (Gap 9).

**Risk.** Inaccurate or misleading statements in a filed SEC report can give rise to Section 10(b)/Rule 10b-5 liability, Section 18 liability, and SEC enforcement action. The discrepancy will need to be addressed and accurately characterized in the FY2024 Form 10-K (and, if material, may require correction via amendment or current report). The Company should not repeat the unqualified MFA representation in future filings without confirming the control's actual scope.

**Recommendation.** Confirm the precise state of MFA coverage as of February 28, 2024 and as of the Incident date. Coordinate with outside counsel and the independent auditor on whether a correction or clarification is required. Ensure the FY2024 Form 10-K Item 1C disclosure accurately describes the MFA control environment, including any limitations on third-party remote access, and the remediation undertaken.

### Gap 3 — Governance "Timely Escalation" Disclosure Inconsistent with Actual Practice

**Finding.** The FY2023 Form 10-K represents that "in the event of a significant cybersecurity incident, the Company's processes provide for escalation to the Board of Directors and, as appropriate, the Audit Committee, to ensure that the Board is informed **in a timely manner** of developments that may affect the Company's operations, financial condition, or public disclosure obligations." In fact, for a Tier 3 incident involving confirmed exfiltration of customer banking data, the Audit Committee Chair was not notified until Day 15 (December 3, 2024), no special Audit Committee meeting has been called, and the next regularly scheduled meeting is January 22, 2025 — more than two months after discovery.

**Why this is a gap.** A 15-day delay in first Board-level notice of a Tier 3 incident with confirmed customer banking-data exfiltration is difficult to reconcile with a "timely manner" representation. The gap is both a disclosure-accuracy issue (the disclosed process did not operate as described) and a governance-failure issue (the Board was deprived of timely information needed to discharge its oversight function, including oversight of the Company's public-disclosure obligations).

**Risk.** Inconsistency between disclosed governance processes and actual practice is a recurring theme in SEC enforcement actions and shareholder litigation concerning cybersecurity incidents. It also undermines the reliability of the Company's Item 106 governance disclosure generally.

**Recommendation.** Call a special meeting of the Audit Committee promptly to review the Incident, the materiality determination, and the disclosure plan. Reconcile the FY2024 Form 10-K governance disclosure with the actual escalation performance, and remediate the escalation process (see Gaps 4 and 14).

### Gap 4 — CIRP Escalation Matrix Stops at the CTO; No Mandatory Legal, CEO, or Board Escalation

**Finding.** The Cybersecurity Incident Response Plan (the "CIRP," Version 1.0, effective June 15, 2022; administrative update August 14, 2023) escalation matrix (Section 10.1) provides that Tier 3 incidents are escalated from the CISO to the CTO (Lauren Hessler) only. The CIRP states that "[a]ny such further escalation [beyond the CTO] is at the CTO's sole discretion, and this Plan does not prescribe specific triggers, recipients, or timelines for escalation beyond the CTO." The General Counsel is listed only as an **optional** contact in Appendix B, "at the discretion of the Incident Commander." There is no mandatory escalation to the General Counsel, the CEO, the Audit Committee, or the Board for any severity tier.

**Why this is a gap.** The CIRP's escalation architecture is the root cause of the notification delays observed here: the General Counsel was not informed until Day 2 (and only because she returned from international travel; the Associate General Counsel learned informally on Day 1); the CEO was not briefed until Day 7; and the Audit Committee was not notified until Day 15. A Tier 3 incident with confirmed data exfiltration should trigger mandatory, time-bound notification of the General Counsel (for disclosure and legal-risk assessment), the CEO, and the Audit Committee / Board. The absence of such a path is a structural deficiency that directly caused the Item 1.05 and governance gaps above.

**Additional finding — CIRP escalation-timeframe violation.** The CIRP requires that for Tier 3 incidents the CTO be notified "within 2 hours of IRT activation." The IRT was activated at 5:00 a.m. on November 18; the CTO was verbally informed at 11:00 a.m. — approximately **six hours** after activation, exceeding the CIRP's own two-hour requirement by roughly four hours. This is a documented deviation from the Company's stated incident-response procedures.

**Recommendation.** Revise the CIRP escalation matrix to include mandatory, time-bound notification of the General Counsel (immediately upon Tier 2/Tier 3 classification), the CEO, and the Audit Committee Chair / Board, with defined triggers tied to data exfiltration, customer-data compromise, and potential materiality. Document and investigate the November 18 escalation-timeframe deviation.

### Gap 5 — CIRP Excludes External Communications and Disclosure from Its Scope

**Finding.** CIRP Section 9.3 expressly provides that "[e]xternal communications regarding cybersecurity incidents — including communications to customers, regulators, media, or the public — are outside the scope of this Plan," and leaves involvement of the corporate-communications team to the "professional judgment" of the Incident Commander. There is no defined process, ownership, or timeline for SEC disclosure, customer notification, state-regulator notification, or breach-notification coordination.

**Why this is a gap.** The CIRP governs the technical detection-to-recovery lifecycle but contains no bridge to the Company's disclosure and notification obligations. This is the structural reason the Company finds itself, on Day 17, with no materiality determination, no 8-K, no customer notifications, and no state filings — the technical response proceeded while the disclosure and notification workstreams had no defined owner or process within the CIRP. The SEC's Item 106 framework expects incident-response processes to be integrated with disclosure processes.

**Recommendation.** Integrate a disclosure-and-notification workstream into the CIRP, owned by the General Counsel and coordinated with the disclosure committee, with defined triggers (including any confirmed data exfiltration, any customer-data compromise, and any Tier 2/Tier 3 classification) that automatically initiate a materiality assessment and a notification-readiness review.

### Gap 6 — CIRP Severity Classification Is Technical-Only, with No Materiality or Disclosure Linkage

**Finding.** The CIRP severity matrix (Section 3.2) classifies incidents solely on technical criteria (endpoint count, downtime, data exfiltration, privileged-credential compromise). The matrix contains no reference to materiality, no requirement to assess disclosure obligations, and no linkage between severity tier and the disclosure-committee process. The Incident was correctly classified Tier 3 on technical grounds, but that classification triggered no disclosure assessment.

**Why this is a gap.** Technical severity and SEC materiality are related but distinct concepts. A technically Tier 3 incident may or may not be material, and a technically lower-tier incident may nonetheless be material (e.g., exfiltration of a small volume of highly sensitive data). The CIRP provides no mechanism to translate incident severity into a materiality assessment, which is the precondition for Item 1.05 compliance.

**Recommendation.** Add a materiality-assessment trigger to the severity framework (at minimum, any confirmed data exfiltration or any customer-data compromise should automatically initiate a documented materiality review by the disclosure committee).

### Gap 7 — CIRP Has Never Been Tested; No Tabletop Exercises or Simulations

**Finding.** The CIRP expressly states (Sections 1.4 and 4.3) that "[n]o tabletop exercises or simulation-based tests of this Plan have been conducted" and that "[a]s of the date of this Plan, no tabletop exercises have been scheduled." The CIRP has been in effect since June 2022 — approximately 29 months — without any testing.

**Why this is a gap.** An untested incident-response plan is a materially weaker control than a tested one, and the deficiencies identified in Gaps 4–6 are precisely the kind of gaps that testing is designed to surface. The FY2023 Form 10-K describes the CIRP as a key element of the Company's risk-management program without disclosing that it has never been tested. Item 106 expects disclosure of the processes for assessing and managing cybersecurity risk; the untested status of the CIRP is a relevant limitation that should be reflected in the FY2024 disclosure.

**Recommendation.** Schedule and conduct a tabletop exercise promptly (informed by lessons from this Incident), and establish a recurring exercise cadence. Reflect the testing status accurately in the FY2024 Form 10-K Item 1C disclosure.

### Gap 8 — Customer-Contract Notification Breaches (48-Hour Deadlines Expired)

**Finding.** The Office of the General Counsel's extracted-contract memorandum dated December 5, 2024 identifies 48-hour cybersecurity-incident notification obligations in three top-customer agreements, all of which have expired:

| Customer | Notification Deadline | Key Remedies for Non-Compliance |
|---|---|---|
| Harmon Defense Solutions (MSA § 9.4–9.5) | 48 hours from discovery | **$500,000 liquidated damages per incident**; 30-day termination right; full defense & indemnification (incl. regulatory and credit-monitoring costs); 3-year survival |
| Crestfield Aerospace (GTCP § 12.2–12.3) | 48 hours from discovery | **Immediate** termination; **payment suspension** pending investigation; 12-month audit right at Vantage's expense; indemnification + credit-monitoring costs; **$10M minimum cyber-insurance requirement** |
| Nexagen Manufacturing (VISA § 7.8–7.9) | 48 hours from discovery or suspicion | 15-day termination (immediate if security-standards failure); indemnification + regulatory-compliance costs; **up to 24-month exclusion from future business** |

The contract memorandum states that "the forty-eight (48) hour notification deadline under each agreement expired no later than November 20, 2024" and that "[a]s of December 5, 2024, no notifications have been sent." The defined "Security Incident"/"Cybersecurity Event"/"Security Breach" triggers in these agreements are broad and, on the preparer's preliminary review, encompass the exfiltrated data categories (customer master records, procurement contacts, contract pricing, ACH banking information). The Nexagen definition expressly treats a ransomware event affecting systems storing Nexagen Data as a Security Breach "regardless of whether Nexagen Data is confirmed to have been accessed or exfiltrated."

**Why this is a gap.** The Company is in breach of the notification obligations under all three agreements. The top-ten customers represent approximately 38% of total revenue (~$710.6 million), and at least six of the top ten are believed to have records in the exfiltrated dataset. The exposure includes liquidated damages, termination of relationships representing a material fraction of revenue, payment suspension, audit rights, indemnification, and exclusion from future business.

**SEC materiality nexus.** These contractual breaches are independently material to the Item 1.05 materiality analysis: the reasonably likely impact on customer relationships and revenue (a qualitative factor the SEC expressly identifies) is significant.

**Recommendation.** Issue customer notifications immediately under the direction of the General Counsel, coordinated with the disclosure plan (to manage Reg FD risk — ideally the public 8-K precedes or is contemporaneous with broad customer notification). Assess liquidated-damages and termination exposure and develop a customer-retention strategy. Complete the ongoing review of the remaining top-twenty customer contracts for similar provisions.

### Gap 9 — Cyber-Insurance Coverage at Material Risk

**Finding.** Three distinct coverage risks have arisen under Ridgeline Insurance Group Policy No. CYB-2024-08871:

1. **Late notice.** The policy requires notice "in no event later than seventy-two (72) hours after Discovery." The Company notified Ridgeline on November 21, 2024 — approximately **73 hours** after discovery. Ridgeline has "reserved rights regarding the timeliness of notice." Under the policy's notice-prejudice framework, late notice is not automatically fatal unless Ridgeline demonstrates material prejudice, but the reservation preserves Ridgeline's defenses.

2. **Policy-application warranty breach (MFA).** The policy application (dated October 15, 2023) warranted that the Company "employs multi-factor authentication for all remote access to Computer Systems," and provides that "[m]aterial misrepresentations in the Policy Application may void coverage ab initio." Thorngate has determined that the compromised contractor VPN credential was not MFA-protected and that MFA was not universally required for third-party contractor VPN access. This is a potential misrepresentation in the application that, if material, could jeopardize coverage from inception.

3. **"Failure to Maintain Minimum Security Standards" exclusion.** Exclusion (i) excludes loss "arising from the Named Insured's failure to maintain security controls substantially consistent with those represented in the Policy Application, provided that such failure materially contributed to the Cyber Event." The absence of MFA on the contractor VPN materially contributed to the Incident (it was the initial access vector). This exclusion is therefore directly implicated.

4. **Contractual-liability exclusion (potential).** Exclusion (g) may exclude loss "arising solely from breach of contractual notification or indemnification clauses — where no independent tort liability exists." This could limit coverage for the Harmon liquidated damages and the customer-contract indemnification exposures identified in Gap 8.

**Why this is gap.** The Company's financial-impact estimate assumes approximately $2.0 million of recovery above the $2.5 million self-insured retention. If coverage is denied or limited on any of the above grounds, the net unreimbursed exposure could rise materially (potentially to the full $4.5 million plus subsequent costs), which both increases the financial impact and strengthens the SEC materiality conclusion.

**Recommendation.** Engage coverage counsel immediately to manage the Ridgeline reservation of rights, to develop the record on the MFA warranty and the minimum-security-standards exclusion, and to preserve coverage. Document the MFA control state carefully. Do not make admissions to Ridgeline without coverage-counsel review. Reassess the financial-impact estimate on a gross (unreinsured) basis for materiality purposes.

### Gap 10 — State and International Breach-Notification Obligations Not Assessed or Initiated

**Finding.** The exfiltrated data includes ACH banking information (routing and account numbers) and procurement-contact PII for approximately 4,200 customer records spanning at least 38 U.S. states plus Germany, Mexico, Canada, and the United Kingdom. The Incident Status Report states that "[n]o notifications have been filed with any state attorney general or state data protection authority" and that "[n]o determinations have been made regarding notification obligations under applicable state data breach notification statutes."

**Why this is a gap.** The combination of financial-account data (with access codes/numbers) and personal information triggers breach-notification statutes in a large number of states (e.g., Ohio, the Company's principal place of business, covers personal information including financial-account numbers in conjunction with access codes). The multi-state and international footprint (Germany/UK GDPR exposure; Mexico Federal Data Protection Law) creates a complex, multi-jurisdictional notification burden with varying deadlines, content requirements, and regulator-notification thresholds. No assessment has been commenced.

**Recommendation.** Immediately retain breach-notification counsel to map the notification obligations across all affected jurisdictions, prioritize by deadline, and coordinate with the customer-notification workstream. Note that some state statutes require regulator notification within short windows (e.g., 30–60 days, or "without unreasonable delay") and that GDPR Article 33 requires notification to the supervisory authority within 72 hours of becoming aware of a personal-data breach — a deadline that has already elapsed for any EU/UK personal data in the exfiltrated set.

### Gap 11 — Independent Auditor Not Notified; ICFR and DC&P Implications

**Finding.** The Incident Status Report states that Greystone & Associates LLP "has not been notified of the incident." The Incident encrypted the ERP **finance** module (supporting accounts payable, accounts receivable, general ledger, and financial reporting), and the Company has relied on manual workaround processes since November 18, 2024. Data-integrity validation of restored ERP data is ongoing.

**Why this is a gap.** Disruption of the primary financial-reporting system and reliance on manual workarounds can affect both ICFR (Sarbanes-Oxley Section 404) and DC&P (Sections 302/906 certifications). The independent auditor should be informed promptly so that it can plan audit procedures addressing the period of disruption, the integrity of restored data, and any control deficiencies. The Audit Committee charter (Section V.A.6) requires the Committee to review significant deficiencies or material weaknesses in DC&P and ICFR — a review that cannot meaningfully occur until the Audit Committee is fully briefed (see Gap 3).

**Recommendation.** Notify Greystone & Associates LLP under the direction of the General Counsel. Assess and document any ICFR/DC&P deficiencies arising from the ERP disruption and manual workarounds, and plan the FY2024 Section 404 assessment accordingly. Brief the Audit Committee on ICFR/DC&P implications.

### Gap 12 — Pending M&A: Counterparty and Advisor Not Notified; Disclosure Implications

**Finding.** The Company is in active negotiations for the $425 million acquisition of Kessler Precision Systems GmbH, with Canfield Cromdale Consulting & Co. advising. Neither Kessler nor Canfield Cromdale has been notified of the Incident, and "[t]he potential impact of this cybersecurity incident on the pending acquisition … has not been evaluated."

**Why this is a gap.** A material cybersecurity incident can affect a pending transaction in several ways: (i) it may constitute a material adverse effect ("MAE") or trigger reps-and-warranties / disclosure-schedule update obligations; (ii) it may require disclosure in any proxy statement, registration statement, or other SEC filing related to the transaction; (iii) it may affect counterparty confidence and deal timeline; and (iv) selective disclosure to the counterparty without prior public disclosure raises Reg FD concerns. The failure to evaluate these issues — and to notify the advisor — leaves the Company exposed on multiple fronts.

**Recommendation.** Evaluate the Incident's impact on the Kessler transaction with deal counsel and Canfield Cromdale. Determine the appropriate timing and form of counterparty notification (coordinated with the public-disclosure plan to manage Reg FD risk). Assess MAE and disclosure-schedule implications and any required updates to transaction documents.

### Gap 13 — Disclosure Controls & Procedures and SOX Certification Readiness

**Finding.** The CEO and CFO certifications required by Sarbanes-Oxley Sections 302 and 906 (and Rule 13a-14) for the Company's periodic reports require evaluation of the effectiveness of DC&P and disclosure of material changes in ICFR. The Incident disrupted the ERP finance module and required manual workarounds during the Company's fourth fiscal quarter. No assessment of the Incident's effect on DC&P or ICFR has been documented.

**Why this is a gap.** The FY2024 Form 10-K certifications (anticipated ~February 2025) will require the certifying officers to address the Incident's impact on DC&P and ICFR. The certifying officers must be in a position to make those certifications knowledgeably, which requires a timely, documented assessment. The Audit Committee's oversight role over DC&P/ICFR (charter Section V.A.6) is also implicated.

**Recommendation.** Initiate a documented DC&P and ICFR impact assessment now, coordinated with the independent auditor (Gap 11) and the disclosure committee. Ensure the CEO and CFO are briefed on certification implications.

### Gap 14 — Audit Committee Charter Does Not Address Cybersecurity Oversight

**Finding.** The Audit Committee charter was last amended and restated on March 15, 2021 — predating the SEC's 2023 cybersecurity rules. The charter's "Compliance and Risk Management" section (Section V.D) addresses financial risk, legal matters, SOX compliance, whistleblower procedures, the code of ethics, and related-party transactions, but contains **no explicit cybersecurity risk-oversight, incident-reporting, or escalation responsibilities**. The FY2023 Form 10-K represents that the Audit Committee oversees cybersecurity risk and "receives quarterly updates," but the charter does not memorialize this responsibility.

**Why this is a gap.** Item 106(c) requires disclosure of the board's oversight of cybersecurity risk and management's role. A charter that does not reflect the cybersecurity-oversight function the Company publicly attributes to the Audit Committee is an internal-governance inconsistency and a weakness in the documented oversight framework. The charter should be updated to reflect cybersecurity-oversight responsibilities, incident-escalation expectations, and reporting cadence.

**Recommendation.** Amend the Audit Committee charter to add explicit cybersecurity risk-oversight and incident-reporting responsibilities, consistent with the Item 106 governance disclosure and the remediated escalation process (Gap 4).

### Gap 15 — Insider-Trading and Trading-Window Controls

**Finding.** The Incident constitutes material non-public information. Numerous insiders are aware of it, including the CISO, CTO, General Counsel, Associate General Counsel, CEO, Audit Committee Chair, IRT members, Thorngate personnel, and outside counsel. The Incident Status Report and related materials contain no reference to closing the Company's insider trading window or imposing trading restrictions on aware insiders.

**Why this is a gap.** Until the Incident is publicly disclosed (via Item 1.05 Form 8-K or otherwise), any trading by an aware insider while in possession of this material non-public information creates Section 10(b)/Rule 10b-5 and potential Section 16 liability for the individual and the Company. The absence of documented trading-window controls is a control deficiency and a source of individual and entity risk.

**Recommendation.** Immediately close the insider trading window and impose trading restrictions on all insiders aware of the Incident, with written acknowledgment. Maintain the restrictions until the second full trading day after public disclosure. Confirm that no aware insider has traded since November 18, 2024.

---

## V. Preliminary Materiality Assessment

This preliminary assessment is provided to support an immediate, formal materiality determination by the disclosure committee. It is not itself the Company's materiality determination, which must be documented by the appropriate decision-makers with the advice of outside counsel.

### A. Quantitative Factors

- Direct estimated costs of $4.5 million equal approximately 1.45% of projected FY2024 EBITDA (~$310 million) and approximately 0.24% of projected FY2024 revenue (~$1.87 billion). On a pure quantitative basis, the direct costs are modest.
- However, the $4.5 million figure excludes numerous potentially material amounts: Harmon liquidated damages ($500,000 per incident); customer-contract indemnification and credit-monitoring costs; potential lost revenue from customer termination (up to ~38% of revenue at risk across the top-ten customer base); litigation; regulatory penalties; reputational impact; and the effect of any insurance-coverage denial (which could increase net unreimbursed exposure toward the full $4.5 million and beyond).

### B. Qualitative Factors

The SEC's adopting release identifies qualitative considerations that are often determinative in the cybersecurity context. Several are strongly present here:

1. **Customer relationships and revenue concentration.** Customer banking data, PII, and contract pricing for approximately 4,200 customers were exfiltrated, including several of the Company's largest accounts. The top-ten customers represent ~38% of revenue, and at least six of the top ten are believed affected. Contractual notification breaches give key customers termination, payment-suspension, and future-business-exclusion rights.
2. **Nature of the compromised data.** ACH routing and account numbers (stored unencrypted) are financially sensitive and immediately usable for unauthorized fund transfers; procurement-contact PII and competitively sensitive contract pricing data carry privacy and commercial-harm dimensions. The defense and aerospace customer base adds national-security sensitivity.
3. **Operational impact.** Encryption of the ERP finance, procurement, and order management modules disrupted core transactional and financial operations and required manual workarounds, with potential ICFR/DC&P consequences.
4. **Regulatory and litigation exposure.** Multi-state breach-notification obligations (38+ states), GDPR Article 33 exposure (72-hour deadline likely already elapsed for EU/UK personal data), and prospective customer, shareholder, and regulatory claims.
5. **Pending strategic transaction.** The $425 million Kessler acquisition may be affected (MAE, disclosure-schedule, counterparty-confidence, and deal-timeline considerations).
6. **Insurance-coverage uncertainty.** Coverage is at material risk (late notice, MFA warranty, minimum-security-standards exclusion), potentially increasing net exposure.
7. **Reputational harm.** A double-extortion ransomware event with confirmed customer banking-data exfiltration at an industrial-automation supplier to defense and aerospace customers carries significant reputational risk.

### C. Preliminary Conclusion

Considering both quantitative and qualitative factors under the *TSC Industries* / *Basic* standard, the Incident is **likely material**. The qualitative factors — particularly the exfiltration of customer banking data, the concentration of affected customers among the Company's largest accounts (representing ~38% of revenue), the contractual notification breaches with termination and liquidated-damages consequences, the pending $425 million acquisition, and the multi-jurisdictional regulatory exposure — are, individually and collectively, the kind of information that a reasonable investor would consider important. The Company should complete a formal, documented materiality determination immediately and, if material (as this analysis suggests), file an Item 1.05 Form 8-K within four business days of that determination. Even if the Company were to conclude the Incident is not material, that conclusion must be documented and defensible, and the determination must be shown to have been made without unreasonable delay.

---

## VI. Prioritized Recommendations

### A. Immediate (0–4 business days)

1. **Materiality determination.** Convene the disclosure committee / materiality working group (General Counsel, CFO, CTO, CISO, outside securities counsel, and, as appropriate, the CEO and Audit Committee Chair). Complete and document a formal materiality determination.
2. **Form 8-K (Item 1.05).** If material (as anticipated), prepare and file an Item 1.05 Form 8-K within four business days of the determination, describing the material aspects of the nature, scope, and timing of the Incident and its material or reasonably likely material impact.
3. **Insider trading controls.** Close the trading window and impose trading restrictions on all aware insiders; confirm no aware insider has traded since November 18, 2024.
4. **Audit Committee.** Call a special Audit Committee meeting to review the Incident, the materiality determination, the disclosure plan, and ICFR/DC&P implications.
5. **Customer notifications.** Begin issuing customer notifications under the direction of the General Counsel, sequenced to follow or coincide with the public 8-K to manage Reg FD risk. Prioritize Harmon, Crestfield, and Nexagen (deadlines already breached).
6. **State and international breach notification.** Retain breach-notification counsel; map obligations across all affected jurisdictions; initiate GDPR Article 33 and state-AG analyses immediately.
7. **Independent auditor.** Notify Greystone & Associates LLP; begin the ICFR/DC&P impact assessment.
8. **M&A.** Evaluate the Incident's impact on the Kessler transaction with deal counsel and Canfield Cromdale; determine counterparty-notification timing.

### B. Near-Term (1–4 weeks)

9. **Insurance coverage.** Engage coverage counsel; manage the Ridgeline reservation of rights; develop the record on the MFA warranty and minimum-security-standards exclusion; reassess the financial-impact estimate on a gross (unreinsured) basis.
10. **CIRP revision.** Revise the CIRP to (i) add mandatory, time-bound escalation to the General Counsel, CEO, and Audit Committee/Board for Tier 2/Tier 3 incidents; (ii) integrate a disclosure-and-notification workstream owned by the General Counsel; (iii) add a materiality-assessment trigger to the severity framework; and (iv) document and investigate the November 18 escalation-timeframe deviation.
11. **Audit Committee charter.** Amend the charter to add explicit cybersecurity-oversight and incident-reporting responsibilities.
12. **Disclosure-accuracy review.** Confirm the MFA control state as of February 28, 2024 and the Incident date; coordinate with outside counsel and the auditor on any required correction; ensure the FY2024 Form 10-K Item 1C disclosure is accurate.
13. **Customer-contract review.** Complete the review of the remaining top-twenty customer contracts for notification and remedies provisions; develop a customer-retention and exposure-mitigation strategy.

### C. Longer-Term (1–6 months)

14. **CIRP testing.** Schedule and conduct a tabletop exercise informed by this Incident; establish a recurring exercise cadence.
15. **Control remediation.** Complete and validate MFA enforcement on all remote access (including third-party); implement encryption at rest for sensitive customer data (prioritizing ACH banking data); conduct the third-party access-management review recommended by Thorngate.
16. **FY2024 Form 10-K planning.** Plan the FY2024 Item 1C (Item 106) disclosure to accurately reflect the Incident, its material impact, the remediated governance and escalation processes, the CIRP testing status, and the MFA control environment. Update Item 1A risk factors accordingly.
17. **Post-incident review.** Conduct the Phase 5 post-incident review required by the CIRP and track remediation action items to closure.

---

## VII. Conclusion

The LockStar 3.0 Incident has exposed multiple, overlapping SEC compliance gaps. The most urgent is the absence, seventeen days after discovery, of any formal materiality determination or Form 1.05 8-K — a gap that, given the qualitative materiality factors present (customer banking-data exfiltration, top-customer concentration and contractual breach exposure, pending $425 million acquisition, and multi-jurisdictional regulatory exposure), should be closed immediately. The disclosure-accuracy exposure in the FY2023 Form 10-K (MFA), the governance "timely escalation" inconsistency, the customer-contract notification breaches, and the cyber-insurance coverage risk each carry independent legal and financial consequences and require prompt action. The structural deficiencies in the CIRP and Audit Committee charter — none of which are unique to this Incident — should be remediated to ensure that the Company's incident-response and oversight frameworks are integrated with its disclosure obligations and consistent with its public disclosures.

This memorandum is preliminary and based on the documents available as of December 6, 2024. The Thorngate preliminary findings report (due December 20, 2024) and the ongoing forensic investigation may materially affect the analysis. We recommend that the actions in Part VI.A be initiated without further delay and that this memorandum be reviewed at the special Audit Committee meeting.

---

*Prepared by the Office of the General Counsel, Vantage Industrial Technologies, Inc., in coordination with Hollister Marsh LLP. This memorandum is privileged and confidential and is intended only for the named recipients. Do not distribute without the express written consent of the General Counsel.*