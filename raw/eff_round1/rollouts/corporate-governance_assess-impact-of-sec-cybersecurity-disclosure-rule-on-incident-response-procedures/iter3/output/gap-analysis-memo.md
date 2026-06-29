# PRIVILEGED AND CONFIDENTIAL — ATTORNEY-CLIENT PRIVILEGE / ATTORNEY WORK PRODUCT

# GAP ANALYSIS MEMORANDUM

**TO:** Priya Raghavan, General Counsel & Corporate Secretary; Dr. Helen Ostrowski, Chair, Audit Committee; Marcus Ellsworth, Chief Executive Officer; Lauren Hessler, Chief Technology Officer

**FROM:** Office of the General Counsel — Securities & Cybersecurity Disclosure Working Group

**DATE:** December 6, 2024

**RE:** SEC Cybersecurity Disclosure Compliance Gaps — Incident INC-2024-0047 (LockStar 3.0 Ransomware and Data Exfiltration Event of November 18, 2024)

---

## PRIVILEGE AND CONFIDENTIALITY LEGEND

This memorandum is prepared at the direction of, and for the purpose of providing legal advice to, the General Counsel of Vantage Industrial Technologies, Inc. ("Vantage" or the "Company"). It is intended to be protected by the attorney-client privilege and the attorney work product doctrine. It contains confidential and proprietary information and should not be distributed, copied, or forwarded outside the Office of the General Counsel and the named recipients without the express written consent of the General Counsel. This memorandum reflects the analysis of the documents made available to the working group as of December 5, 2024 and is subject to revision as the forensic investigation and legal analysis progress.

---

## I. EXECUTIVE SUMMARY

On November 18, 2024, the Company's Security Operations Center detected a ransomware and data-exfiltration incident (Incident INC-2024-0047) involving the LockStar 3.0 variant. The attack was executed through a compromised virtual private network ("VPN") credential belonging to a third-party maintenance contractor that, contrary to the Company's documented and disclosed control posture, was **not** protected by multi-factor authentication ("MFA"). The threat actor exfiltrated approximately 83 GB of data — including customer banking information (ACH routing and account numbers), procurement contact personally identifiable information ("PII"), and contract pricing data for approximately 4,200 customer records — before encrypting 347 of the Company's approximately 2,100 networked endpoints, including the enterprise resource planning ("ERP") finance, procurement, and order management modules.

As of the date of this memorandum — **seventeen (17) days after detection and twelve (12) business days after the Company's most senior legal officer was informed** — the Company has **not** conducted a formal materiality determination, **has not** filed any disclosure with the U.S. Securities and Exchange Commission (the "SEC"), **has not** issued customer notifications under three material customer contracts whose 48-hour notification deadlines expired on or before November 20, 2024, **has not** made any state attorney general or international data protection authority notifications, and **has not** notified the Audit Committee as a body (only the Audit Committee Chair, by email, on Day 15). The Company's independent auditor and the counterparty to a pending $425 million acquisition have likewise not been notified.

This memorandum identifies **thirteen (13) categories of SEC cybersecurity disclosure compliance gaps and related legal exposures**, the most significant of which are:

1. **Failure to conduct a timely materiality determination under Item 1.05 of Form 8-K.** The SEC's cybersecurity disclosure rules require registrants to determine whether a cybersecurity incident is material "without unreasonable delay" after discovery and, upon a determination of materiality, to file an Item 1.05 Form 8-K within four business days. The Company has not made any materiality determination despite strong quantitative and qualitative indicators of materiality, creating exposure to enforcement risk and private litigation.

2. **Strong indicators that the incident is, in fact, material.** The exfiltration of unencrypted customer banking data affecting the Company's largest customers (representing 38% of revenue), breached contractual notification obligations carrying liquidated damages and termination rights, a pending $425 million acquisition, and the contradiction of the Company's most recent 10-K cybersecurity disclosure collectively point toward materiality under *TSC Industries v. Northway*.

3. **A material discrepancy between the Company's disclosed control posture and its actual practices.** The FY2023 Form 10-K (Item 1C), the Cybersecurity Incident Response Plan (the "CIRP"), and the Company's October 15, 2023 cyber insurance application each represent that MFA is required for all remote access / VPN connections. The compromised contractor credential was not MFA-protected. This discrepancy creates (a) potential inaccuracy in the Company's SEC disclosures, (b) a potential material misrepresentation that could void cyber insurance coverage *ab initio*, and (c) exposure under the policy's "failure to maintain minimum security standards" exclusion.

4. **Governance and escalation failures.** The CIRP's escalation matrix terminates at the Chief Technology Officer and contains no mandatory escalation to the General Counsel, Chief Executive Officer, Audit Committee, or Board. The Audit Committee Chair was not informed until Day 15, and no special Audit Committee meeting has been called — inconsistent with the 10-K's representation that the Company's processes provide for timely Board escalation of significant incidents. The Audit Committee charter (last amended March 15, 2021) does not expressly address cybersecurity oversight.

5. **Breach of customer contractual notification obligations.** All three reviewed top-customer contracts impose 48-hour notification duties that have been missed, exposing the Company to $500,000 in liquidated damages (Harmon Defense Solutions), immediate and 15/30-day termination rights, payment suspension, audit rights, and exclusion from future business — with direct revenue and materiality consequences.

The memorandum concludes with a prioritized action plan. **The most urgent actions — convening a materiality determination, preparing an Item 1.05 Form 8-K, and curing the customer notification defaults — should be initiated immediately.**

---

## II. FACTUAL BACKGROUND AND INCIDENT SUMMARY

The following factual summary is drawn from the Company's incident status report dated December 5, 2024 (Incident INC-2024-0047), the Thorngate Forensic Solutions, Inc. interim status report dated December 1, 2024, the General Counsel's December 3, 2024 email to the Audit Committee Chair, the customer contract excerpts prepared by the Office of the General Counsel, the Ridgeline Insurance Group policy summary, the CIRP, the Audit Committee charter, and the Company's FY2023 Form 10-K (Item 1C).

### A. The Incident

- **Detection.** On November 18, 2024, at approximately 2:17 a.m. EST, the SOC detected anomalous network activity originating from a VPN session authenticated with a credential belonging to a third-party maintenance contractor.
- **Attack vector.** Thorngate confirmed the initial access vector as the compromised contractor VPN credential and identified, as a preliminary root cause, that **the credential was not protected by MFA**, permitting authentication without a secondary verification factor.
- **Reconnaissance and dwell time.** Anomalous logins from an IP geolocated to Eastern Europe began on or about November 14, 2024, with an estimated three-to-four-day reconnaissance/dwell period (November 14–17) during which the threat actor enumerated network shares, Active Directory objects, and database servers.
- **Data exfiltration (Phase 1).** Between approximately 1:30 a.m. and 2:15 a.m. EST on November 18, 2024, the threat actor exfiltrated approximately 83 GB of data to an external IP address via outbound HTTPS, **prior to** ransomware deployment — a deliberate double-extortion methodology.
- **Ransomware deployment (Phase 2).** Between approximately 2:17 a.m. and 4:45 a.m. EST, the LockStar 3.0 variant encrypted 347 of approximately 2,100 networked endpoints, including the ERP finance, procurement, and order management modules. A ransom demand of 45 Bitcoin (approximately $2,029,500) was issued with a 72-hour deadline and a threat to publish exfiltrated data. The Company has not paid and does not intend to pay.
- **Operational technology.** Manufacturing operations and OT/SCADA systems were not affected; the air-gapped IT/OT architecture performed as designed.
- **Exfiltrated data (high confidence per Thorngate, December 1, 2024).** Customer master records for approximately 4,200 corporate client accounts; procurement contact PII (names, emails, phone numbers, titles); contract pricing data; and **customer banking information (ACH routing numbers and account numbers), stored unencrypted (plaintext) at rest** in the ERP accounts receivable module. Affected records span at least 38 U.S. states plus Germany, Mexico, Canada, and the United Kingdom, and include several of the Company's largest accounts (including Harmon Defense Solutions, Crestfield Aerospace, and Nexagen Manufacturing).

### B. Financial Impact (Preliminary)

| Category | Estimated Cost |
|---|---|
| Incident response costs | $1,400,000 |
| Business disruption costs | $2,800,000 |
| Customer notification preparation costs | $300,000 |
| **Total estimated costs (as of Dec. 5, 2024)** | **$4,500,000** |

The $4.5 million estimate represents approximately 1.45% of projected FY2024 EBITDA (~$310 million) and excludes the ransom (~$2.03M, not paid), potential customer claims, regulatory penalties, litigation, and reputational impact. Cyber insurance (Ridgeline, Policy No. CYB-2024-08871) carries a $15 million aggregate limit and a $2.5 million self-insured retention, implying approximately $2.0 million of potential recovery — which is at risk due to late notice and a potential application-warranty breach (see Section IV.I).

### C. Notification Chronology

| Date (Day) | Event |
|---|---|
| Nov. 18, 2024 (Day 0) | SOC detection (~2:17 a.m.); IRT activated Tier 3 (~5:00 a.m.); CTO verbally informed (~11:00 a.m.) |
| Nov. 19 (Day 1) | Thorngate retained; Associate GC learned informally from IT; **GC not informed (traveling)** |
| Nov. 20 (Day 2) | GC informed upon return; FBI IC3 contacted; Hollister Marsh LLP (outside securities counsel) engaged |
| Nov. 21 (Day 3) | Ridgeline Insurance notified (~73 hours post-discovery; **policy requires 72 hours — late by ~1 hour**); Ridgeline reserved rights |
| Nov. 25 (Day 7) | CEO briefed |
| Dec. 1 (Day 13) | Thorngate interim report confirming customer banking data exfiltration |
| Dec. 3 (Day 15) | **Audit Committee Chair emailed by GC — first Board-level notification** |
| Dec. 5 (Day 17) | Status report prepared; **no Form 8-K filed; no materiality determination; no customer notices; no state AG notices** |
| Jan. 22, 2025 | Next regularly scheduled Audit Committee meeting (no special meeting called) |

---

## III. APPLICABLE SEC REGULATORY FRAMEWORK

The Company's cybersecurity disclosure obligations arise principally from two SEC rules adopted on July 26, 2023 (effective September 5, 2023) in the final rule "Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure":

1. **Item 1.05 of Form 8-K (current incident disclosure).** A registrant must disclose a cybersecurity incident that the registrant determines to be material on a Form 8-K under Item 1.05 **within four (4) business days** after the registrant **determines** that the incident is material. The disclosure must describe the material aspects of the nature, scope, and timing of the incident, and the material impact or reasonably likely material impact on the registrant, including its financial condition and results of operations. The four-business-day clock runs from the date of the **materiality determination**, not the date of discovery. However, the SEC's adopting release and subsequent staff guidance (including the June 2024 Division of Corporation Finance compliance & disclosure interpretations) make clear that registrants must make the materiality determination **"without unreasonable delay"** after discovery of the incident and may not use the four-business-day period as a basis to defer the determination. Item 1.05 applies to incidents determined to be material on or after December 18, 2023.

2. **Item 106 of Regulation S-K (annual disclosure).** A registrant must describe in its annual report (Form 10-K) its (a) processes for assessing, identifying, and managing material risks from cybersecurity threats; (b) whether and how any cybersecurity risks have materially affected, or are reasonably likely to materially affect, the registrant; (c) the board of directors' oversight of cybersecurity risks; and (d) management's role in assessing and managing material cybersecurity risks. Item 106 applies to annual reports for fiscal years ending on or after December 15, 2023.

3. **Materiality standard.** Materiality is assessed under the standard articulated in *TSC Industries, Inc. v. Northway, Inc.*, 426 U.S. 438 (1976): information is material if there is a "substantial likelihood that a reasonable investor would consider it important" or if it would "significantly alter the total mix of information available." Materiality is a facts-and-circumstances determination that considers **both quantitative and qualitative factors**, and the SEC has expressly cautioned against an unduly narrow, purely quantitative analysis for cybersecurity incidents.

4. **Law enforcement delay exception.** Item 1.05 permits a registrant to delay disclosure only where the **U.S. Attorney General** determines that disclosure would pose a substantial risk to national security or public safety and notifies the SEC. A report to, or contact with, the FBI or other law enforcement — including the FBI Internet Crime Complaint Center ("IC3") — **does not** trigger or justify any delay absent a formal Attorney General determination.

5. **Antifraud and ongoing disclosure obligations.** Independent of Items 1.05 and 106, the Company remains subject to the antifraud provisions of the federal securities laws (Section 17(a) of the Securities Act; Section 10(b) and Rule 10b-5 of the Exchange Act) and to the duty to correct prior disclosures that become materially inaccurate and the duty to update where necessary to prevent prior statements from becoming misleading — particularly relevant where the Company is engaged in a registered securities offering or active M&A communications.

---

## IV. GAP ANALYSIS

### A. No Materiality Determination Has Been Conducted (Item 1.05 — Primary Gap)

**The gap.** As of December 5, 2024 — seventeen days after detection and twelve business days after the General Counsel was informed and outside securities counsel (Hollister Marsh LLP) was engaged — the Company has conducted **no formal materiality determination**. The incident status report expressly states: "No formal materiality determination has been conducted."

**Why it matters.** Item 1.05's four-business-day disclosure clock does not begin to run until the registrant determines materiality. The SEC has repeatedly emphasized that the materiality determination must be made "without unreasonable delay" and that the rule is not a license to defer the determination. A prolonged period of awareness of a severe incident without a contemporaneous, documented materiality analysis is itself the central compliance deficiency: it both delays any required disclosure and creates an evidentiary record suggesting that the Company may have avoided, rather than undertaken, the determination. The SEC has signaled active enforcement focus on cybersecurity disclosure failures (including actions premised on inaccurate or delayed cyber disclosures and on internal-control failures surrounding cyber incidents).

**Severity: Critical.** This is the single most significant SEC compliance gap and the predicate for several of the gaps that follow.

### B. Strong Indicators That the Incident Is Material

Even absent a formal determination, the available facts contain substantial indicators of materiality under the *TSC Industries* standard. The working group's preliminary assessment is that a robust, good-faith materiality analysis would be likely to conclude — or at minimum to conclude that materiality is reasonably likely — based on the following **qualitative** factors, which the SEC has stressed must be weighed alongside quantitative measures:

1. **Nature and sensitivity of exfiltrated data.** Unencrypted customer banking information (ACH routing and account numbers) for approximately 4,200 customer records, plus procurement contact PII and competitively sensitive contract pricing data. The unencrypted-at-rest finding means the data is immediately usable for fraud, materially elevating harm potential.
2. **Customer concentration and revenue exposure.** The Company's top 10 customers represent approximately 38% of total revenue (~$710.6 million of ~$1.87 billion). At least six of the top 10 are believed to be among the affected records. Affected customers include defense and aerospace accounts whose own regulatory and contractual regimes may amplify consequences.
3. **Breached contractual notification obligations.** Three top-customer contracts impose 48-hour notification duties that have been missed (see Section IV.J), triggering liquidated damages, termination rights, payment suspension, and future-business exclusion — each with direct revenue and relationship consequences.
4. **Pending $425 million acquisition.** The Kessler Precision Systems GmbH transaction may be affected as to representations and warranties, material adverse change analysis, counterparty confidence, financing, and timeline (see Section IV.L).
5. **Contradiction of prior SEC disclosure.** The FY2023 10-K (Item 1C) states that, as of the filing date, the Company "has not experienced any cybersecurity incidents that have materially affected, or are reasonably likely to materially affect, the Company's business strategy, results of operations, or financial condition." This incident, and its aftermath, may render related forward-looking and risk disclosures stale or potentially misleading, implicating the duty to correct/update.
6. **Regulatory exposure.** Potential obligations under the data breach notification laws of 38+ U.S. states and under the EU GDPR (German customers), each carrying notification duties and, in some cases, penalties.
7. **Double-extortion / reputational risk.** The threat of public disclosure of exfiltrated data on a dark-web leak site creates ongoing reputational and customer-trust risk that is not captured by the $4.5 million cost estimate.

**Quantitative counterweight.** The $4.5 million estimated cost (~1.45% of projected EBITDA) is, in isolation, modest. However, the SEC has cautioned that a purely quantitative threshold is inappropriate for cybersecurity incidents, and the figure excludes the categories above (customer claims, regulatory penalties, litigation, reputational harm, acquisition impact, and the at-risk insurance recovery). The quantitative figure should not be treated as dispositive.

**Severity: Critical.** The weight of qualitative indicators strongly supports proceeding to a documented materiality determination on an expedited basis.

### C. The Law Enforcement Delay Exception Is Not Available

**The gap.** The Company contacted the FBI IC3 on November 20, 2024. The incident status report confirms that "no request has been made by law enforcement to delay any public disclosure related to this incident."

**Why it matters.** Item 1.05's only disclosure-delay mechanism requires a determination by the U.S. Attorney General (notifying the SEC) that disclosure poses a substantial risk to national security or public safety. Mere contact with, or a report to, the FBI or IC3 does not satisfy this standard and provides no basis to defer an Item 1.05 filing. The Company must not treat the FBI contact as a basis for delay, and any internal or external communications implying that law-enforcement coordination justifies non-disclosure would be inaccurate and create additional risk.

**Severity: High** (as a risk-management and communications matter; it forecloses the only lawful basis for delay).

### D. Item 106 / 10-K Disclosure Accuracy and Required Updates

**The gap.** The FY2023 Form 10-K (filed February 28, 2024) Item 1C disclosure contains statements that are now in tension with, or contradicted by, the incident and the forensic findings, and that will require careful attention in the FY2024 10-K:

1. **"No material incidents" statement.** The 10-K states the Company "has not experienced any cybersecurity incidents that have materially affected, or are reasonably likely to materially affect, the Company's business strategy, results of operations, or financial condition." This was accurate as of February 28, 2024, but the FY2024 10-K (Item 1C / Item 106) must address this incident, the materiality determination process, and any material impact. The Company should also evaluate whether a duty to correct or update arises before the FY2024 10-K is filed (e.g., in any current offering or M&A communications).
2. **Disclosed controls vs. actual practice (MFA).** The 10-K represents that the Company has implemented "multi-factor authentication for access to critical information systems, remote access connections, and administrative accounts." The compromised third-party contractor VPN credential was **not** MFA-protected, and MFA was only enforced on all VPN connections on November 20, 2024 (after the incident). This is a factual discrepancy between a disclosed control and the Company's actual practice as of the incident. The FY2024 10-K must accurately describe the Company's controls, and the Company should assess whether the FY2023 statement was accurate when made and whether correction is warranted.
3. **Governance representations.** The 10-K represents that "the Company's processes provide for escalation to the Board of Directors and, as appropriate, the Audit Committee, to ensure that the Board is informed in a timely manner." The Audit Committee Chair was not informed until Day 15, and the Audit Committee as a body has not been informed. The FY2024 10-K's governance disclosure should accurately reflect the escalation process as actually implemented (see Section IV.F).
4. **CIRP recency.** The 10-K states the CIRP "was initially developed in June 2022 and was most recently reviewed in August 2023." The August 2023 review was administrative only (vendor contacts); no substantive review or testing has occurred since June 2022. The FY2024 disclosure should accurately characterize the review and testing cadence.

**Severity: High.** Inaccurate or stale Item 106 disclosures create both Item 106 noncompliance and antifraud exposure.

### E. Discrepancy Between Disclosed/Documented Controls and Actual Practice (MFA)

**The gap.** Three separate Company representations state that MFA is required for all remote access / VPN connections, yet the compromised contractor credential was not MFA-protected:

1. **FY2023 Form 10-K, Item 1C:** "multi-factor authentication for access to critical information systems, remote access connections, and administrative accounts."
2. **CIRP, Section 4.1(d):** "Multi-factor authentication (MFA) is required for all VPN connections. VPN access is provisioned through a formal request and approval process, and VPN credentials are reviewed quarterly."
3. **Ridgeline Insurance Policy Application (October 15, 2023), warranty (b):** the Company "employs multi-factor authentication for all remote access to Computer Systems." The policy summary states that "[t]he accuracy of these representations is a condition of coverage" and that "[m]aterial misrepresentations in the Policy Application may void coverage *ab initio*."

**Why it matters.** This single control failure has three distinct legal consequences:

- **SEC disclosure accuracy.** A disclosed control that was not, in fact, uniformly enforced is a potential inaccuracy in the Company's Item 1C/Item 106 disclosure (see Section IV.D).
- **Insurance coverage.** The application warranty is a condition of coverage. If the absence of MFA on third-party contractor VPN access is deemed a material misrepresentation, Ridgeline may seek to void the policy *ab initio*, eliminating the ~$2.0 million expected recovery and exposing the Company to the full (and growing) cost of the incident. Separately, the policy's "Failure to Maintain Minimum Security Standards" exclusion (Section 6(i)) may apply where the failure "materially contributed to the Cyber Event" — which, on these facts, it plainly did (the absence of MFA was the root-cause enabler of the intrusion).
- **Litigation/enforcement exposure.** The gap between disclosed and actual controls is precisely the type of inconsistency that has featured in SEC cybersecurity enforcement actions and that plaintiffs may cite in securities class actions.

**Severity: Critical** (for insurance exposure) / **High** (for disclosure exposure).

### F. Governance and Board Oversight Gaps

**The gaps.**

1. **Untimely Board/Audit Committee escalation.** The 10-K represents that the Company's processes provide for timely Board escalation of significant incidents. The Audit Committee Chair was not informed until Day 15 (December 3), and only by email from the General Counsel; the Audit Committee as a body has not been informed; no special meeting has been called; and the next regularly scheduled meeting is January 22, 2025 — more than two months after detection. For a Tier 3 (highest-severity) incident with clear disclosure implications, this is not timely.
2. **CIRP escalation matrix terminates at the CTO.** The CIRP's mandatory escalation matrix (Section 10) requires notification only up to the Chief Technology Officer. There is **no mandatory escalation** to the General Counsel, the Chief Executive Officer, the Audit Committee, or the Board. The General Counsel, outside counsel, the CEO, the cyber insurer, and the independent auditor appear only as **optional** contacts in Appendix B, at the discretion of the Incident Commander or CTO. This structure is the proximate cause of the delayed legal and Board involvement: the General Counsel was not informed until Day 2 (and only because she returned from travel; the Associate General Counsel learned informally on Day 1 but did not formally escalate), and the CEO was not briefed until Day 7.
3. **Audit Committee charter does not address cybersecurity.** The Audit Committee charter (last amended March 15, 2021) addresses financial reporting oversight, independent-auditor oversight, internal-audit oversight, compliance and (financial) risk management, related-party transactions, and other responsibilities. It does **not** expressly assign cybersecurity risk oversight to the Audit Committee, does not reference Item 106 of Regulation S-K, and predates the SEC's 2023 cybersecurity rules. The 10-K nonetheless states that the Board "acting primarily through its Audit Committee, oversees the Company's cybersecurity risk management program." The charter should be updated to align with the disclosed governance structure and the SEC's Item 106 governance requirements.
4. **No cybersecurity expertise disclosure.** Item 106 calls for disclosure of board oversight of cybersecurity risks, including whether any board members or committee members have cybersecurity expertise. The current charter and 10-K do not address cybersecurity expertise at the committee level; this should be evaluated for the FY2024 10-K.

**Severity: High.** These gaps undermine the accuracy of the Company's Item 106 governance disclosure and create disclosure-controls weaknesses (see Section IV.H).

### G. CIRP Deficiencies

**The gaps.**

1. **No testing.** The CIRP expressly states that "[n]o tabletop exercises or simulation-based tests of this Plan have been conducted" and that the CISO "will develop an exercise schedule following initial Plan deployment." As of the incident, more than two years after adoption, the Plan had never been tested. Untested plans are a recognized contributor to response failures.
2. **Stale substantive review.** The last substantive review was June 2022; the August 2023 review was administrative only (vendor contacts). The CIRP's own governance section (Section 1.4) requires annual review by the CISO.
3. **No disclosure/legal integration.** The CIRP's Incident Response Team (Section 2.3) does not include Legal/General Counsel as a standing member; the General Counsel is an optional contact. Section 9.3 expressly excludes customer, regulator, and public communications from the Plan's scope, leaving the disclosure and notification workflow ungoverned by the Plan. The CIRP contains no process for SEC materiality determination or Item 1.05 disclosure, no process for customer-contract notification tracking, and no process for state/international breach-notification triage.
4. **Severity classification is purely technical.** The CIRP's severity matrix (Section 3.2) is based solely on technical criteria (endpoint count, downtime, exfiltration). It does not incorporate legal, disclosure, or materiality dimensions, and the escalation matrix is keyed only to the technical tier — not to disclosure triggers. A technically "Tier 3" incident and a "material" incident are not the same concept, and conflating or omitting the latter is a structural weakness.
5. **OT scope exclusion.** The CIRP excludes OT/SCADA from its scope (Section 1.2). While the air-gap performed as designed here, the exclusion means the Plan provides no integrated response framework for an incident that crosses the IT/OT boundary — a meaningful residual risk for an industrial manufacturer.

**Severity: High.** These deficiencies both contributed to the response and disclosure delays and will require correction for accurate Item 106 disclosure.

### H. Disclosure Controls and Procedures Weaknesses

**The gap.** The sequence and timing of internal notifications reveal weaknesses in the Company's disclosure controls and procedures (as contemplated by Exchange Act Rule 13a-15):

- The General Counsel — the officer principally responsible for assessing disclosure obligations — was not informed until Day 2, and only upon her return from international travel. The Associate General Counsel learned of the incident informally from an IT colleague on Day 1 but did not formally escalate to the General Counsel or trigger a disclosure analysis.
- The CEO was not briefed until Day 7.
- The Audit Committee Chair was not informed until Day 15; the Audit Committee as a body remains uninformed.
- No disclosure committee or equivalent was convened; no materiality determination process was initiated until outside counsel was engaged on Day 2, and even then no determination has been completed as of Day 17.

**Why it matters.** Disclosure controls and procedures must ensure that information important to disclosure decisions is recorded, processed, summarized, and reported to management and the Board on a timely basis. The delays here suggest that the Company's controls did not ensure timely escalation of a material event to the appropriate disclosure decision-makers. This may constitute a disclosure-controls deficiency that must be evaluated for the FY2024 10-K (Item 9A) and that bears on the accuracy of management's disclosure-controls conclusions. The ERP finance module's involvement also raises internal-control-over-financial-reporting ("ICFR") considerations (see Section IV.M).

**Severity: High.**

### I. Insurance Coverage at Risk (Affecting Financial Impact and Materiality)

**The gaps.**

1. **Late notice.** Ridgeline was notified at approximately 73 hours post-discovery; the policy requires notice "in no event later than seventy-two (72) hours after Discovery." Ridgeline has reserved rights on timeliness. Under the policy's notice provisions (Section 5.3), late notice does not void coverage unless the insurer is materially prejudiced, but in jurisdictions applying strict compliance the late notice is a ground for denial. The ~$2.0 million expected recovery above the $2.5 million SIR is at risk.
2. **Application warranty breach (MFA).** As detailed in Section IV.E, the October 15, 2023 application warranted MFA for all remote access, which was not true for third-party contractor VPN access. A material misrepresentation may void coverage *ab initio*.
3. **Minimum-security-standards exclusion.** Section 6(i) excludes loss arising from the Company's failure to maintain security controls substantially consistent with those represented in the application, where the failure materially contributed to the Cyber Event. The MFA failure is the root-cause enabler.
4. **Consent-to-incur-costs.** Section 7.2 requires the insurer's prior written consent for first-party losses exceeding $50,000 individually or $150,000 in aggregate (with a 48-hour emergency ratification window). The Company incurred $1.4 million in incident response costs; it should confirm whether the consent/ratification requirements were satisfied, particularly as to non-panel vendors.
5. **Contractual-liability exclusion.** Section 6(g) may exclude liability arising solely from breach of contractual notification or indemnification clauses (e.g., the Harmon liquidated damages) where no independent tort liability exists — potentially limiting coverage for the customer-contract exposures in Section IV.J.

**Why it matters for SEC compliance.** Insurance recovery is a component of the financial-impact assessment that feeds the materiality determination. If the ~$2.0 million recovery is lost, the net financial impact rises and the materiality calculus shifts. The Company's materiality analysis must reflect a realistic, conservative view of recoverable insurance, not the gross $2.0 million figure.

**Severity: High.**

### J. Breach of Customer Contractual Notification Obligations (Affecting Materiality)

**The gap.** The Office of the General Counsel's December 5, 2024 contract-extracts memorandum identifies three top-customer contracts, each imposing a **48-hour notification** duty from discovery of a security incident/breach affecting customer data. The 48-hour deadlines expired no later than November 20, 2024. **As of December 5, 2024, no notifications have been sent to any of the three customers.** The affected data categories (customer master records, procurement contact PII, contract pricing, and ACH banking information) fall within the broad defined-data scopes of all three agreements.

| Customer | Notification Deadline | Key Remedies for Non-Compliance |
|---|---|---|
| Harmon Defense Solutions (MSA §9.4–9.5) | 48 hours from discovery | **$500,000 liquidated damages per incident**; 30-day termination right; full defense & indemnity (incl. regulatory, notification, credit-monitoring costs); 3-year survival |
| Crestfield Aerospace (GTCP §12.2–12.3) | 48 hours from discovery | Immediate termination; **payment suspension** pending investigation; 12-month audit right at Vantage's expense; indemnity + credit-monitoring costs; **$10M minimum cyber insurance per occurrence**; forensic report within 30 days |
| Nexagen Manufacturing (VISA §7.8–7.9) | 48 hours from discovery or suspicion | 15-day termination (immediate if security-standards failure); full indemnity + regulatory costs; **24-month future-business exclusion**; preliminary report within 5 business days; final report within 60 days |

**Why it matters for SEC compliance.** These breaches are not merely commercial exposures; they are materiality inputs:

- **Revenue concentration.** The top 10 customers represent ~38% of revenue (~$710.6M); at least six of the top 10 are believed affected. Termination, payment-suspension, or future-business-exclusion remedies threaten a material revenue stream.
- **Quantifiable damages.** The Harmon $500,000 liquidated damages alone are a concrete, near-certain cost; indemnity and credit-monitoring obligations across all three contracts add further exposure.
- **Crestfield insurance requirement.** Crestfield requires $10 million minimum cyber insurance per occurrence. The Company's policy provides a $15 million aggregate/per-occurrence limit, which facially satisfies the requirement, but if coverage is voided or eroded (Section IV.I), the Company may be in breach of this covenant as well — compounding termination risk.
- **Defense/aerospace amplification.** Harmon (defense) and Crestfield (aerospace) customers may themselves be subject to federal contracting and export-control regimes that magnify the consequences of a supplier breach.

**Severity: Critical** (commercially) and **High** (as a materiality factor).

### K. State and International Data Breach Notification Obligations

**The gap.** The exfiltrated data includes PII (procurement contact names, emails, phone numbers) and financial-account data (ACH routing and account numbers) for individuals and entities across at least 38 U.S. states and four foreign jurisdictions (Germany, Mexico, Canada, United Kingdom). As of December 5, 2024, **no notifications have been filed with any state attorney general or state data protection authority**, and no determinations have been made regarding such obligations.

**Why it matters.**

- **U.S. state laws.** All 50 states have breach-notification statutes; most require notice to affected individuals "without unreasonable delay" and to state attorneys general above defined thresholds, often within 30–60 days. ACH routing and account numbers, combined with identifying information, are commonly within the scope of "personal information." The Company's home state (Ohio) and the states of affected customers each impose distinct duties.
- **GDPR (Germany/EU).** If the Company processes EU personal data as a controller or processor, Article 33 of the GDPR requires notification to the competent supervisory authority within 72 hours of becoming aware of a personal-data breach, and Article 34 requires notification to data subjects where high risk exists. The 72-hour controller-notification deadline has likely already passed. The Ridgeline policy's Endorsement No. 5 extends regulatory coverage to GDPR proceedings, subject to the Regulatory Defense and Penalties sub-limit ($7.5M).
- **SEC materiality interaction.** The existence and magnitude of these regulatory obligations (and any penalties) are themselves materiality factors and must be reflected in the Item 1.05 disclosure (if material) and the Item 106 disclosure.

**Severity: High.**

### L. Pending Acquisition Disclosure Implications (Kessler Precision Systems GmbH)

**The gap.** The Company is in active negotiations for the $425 million acquisition of Kessler Precision Systems GmbH, with Canfield Cromdale Consulting & Co. advising. As of December 5, 2024, **neither the transaction counterparty nor the Company's financial advisor has been notified** of the incident, and "the potential impact of this cybersecurity incident on the pending acquisition ... has not been evaluated."

**Why it matters for SEC compliance.**

- **Material adverse change / reps & warranties.** The incident may constitute or contribute to a material adverse effect on the Company, with implications for deal representations, warranties, closing conditions, and the accuracy of any disclosure schedules or bring-down certificates.
- **Offering-period disclosure duties.** If the transaction or related financing involves a registered securities offering or proxy solicitation, the Company's antifraud and ongoing-disclosure duties are heightened during the offering period; material information must not be omitted, and prior statements must not become misleading.
- **Materiality.** The intersection of a material cyber incident and a pending $425 million acquisition is itself a materiality factor: the incident could affect the Company's ability to complete the transaction, the transaction's economics, or the Company's post-transaction financial condition.
- **Counterparty and advisor notification.** Failing to inform the financial advisor and counterparty may breach engagement or transaction agreements and may deprive the Company of timely deal-structuring advice.

**Severity: High.**

### M. Independent Auditor and ICFR Implications

**The gap.** The Company's independent auditor, Greystone & Associates LLP, has **not been notified** of the incident. The FY2024 audit cycle has not commenced. The incident directly affected the ERP **finance module** (accounts payable, accounts receivable, general ledger, and financial reporting functions), which was unavailable and operated via manual workarounds from November 18, 2024 through the report date.

**Why it matters.**

- **ICFR.** The encryption of the finance module and reliance on manual workarounds may indicate a significant deficiency or material weakness in internal control over financial reporting, particularly as it affects the Company's ability to record, process, and report financial transactions during the affected period. This must be assessed for the FY2024 10-K (Item 9A and the Section 404 management/auditor ICFR reports).
- **Auditor communication.** Auditing standards (and the Audit Committee charter) contemplate timely communication of matters affecting the audit, financial systems, and internal controls. Early notification enables the auditor to plan appropriate audit procedures and supports the integrity of the FY2024 audit.
- **Disclosure controls.** The ICFR and disclosure-controls implications (Sections IV.H and IV.M) should be evaluated and documented contemporaneously.

**Severity: Medium-High.**

---

## V. PRIORITIZED RECOMMENDATIONS AND ACTION PLAN

The following actions are prioritized by urgency. Items marked **IMMEDIATE** should be initiated within 24–48 hours.

### Tier 1 — Immediate (24–48 hours)

1. **Convene a materiality determination.** The General Counsel, with Hollister Marsh LLP and senior management (CEO, CFO, CTO, CISO), should convene a documented materiality-determination session applying the *TSC Industries* standard, weighing the quantitative and qualitative factors in Section IV.B. The determination, its basis, and the date of determination must be documented in a contemporaneous written record (e.g., a disclosure-committee memorandum). **Do not defer the determination pending the December 20 Thorngate preliminary report**; the SEC requires determination "without unreasonable delay," and sufficient information already exists to assess materiality (with refinement as facts develop).

2. **Prepare and file an Item 1.05 Form 8-K if material (or reasonably likely material).** If the determination is that the incident is material, file within four business days of the determination. The disclosure should address the material aspects of the nature, scope, and timing of the incident and the material or reasonably likely material impact on the Company, including financial condition and results of operations. If materiality is not yet determinable but reasonably likely, consider whether a disclosure is nonetheless required and whether interim disclosure (e.g., in offering or M&A communications) is warranted. Coordinate with the disclosure committee and confirm the absence of any Attorney General delay request before filing.

3. **Cure customer notification defaults.** Immediately issue notifications to Harmon Defense Solutions, Crestfield Aerospace, and Nexagen Manufacturing (and any other affected customers whose contracts impose notification duties), and complete the ongoing contract review (expected December 10, 2024). Document the notifications and assess liquidated-damages and termination exposure. Engage outside counsel on mitigation strategy for the missed deadlines.

4. **Notify the Audit Committee as a body and call a special meeting.** The full Audit Committee should be briefed immediately (not deferred to January 22, 2025), and a special meeting should be called to review the incident, the materiality determination, the disclosure decision, and the remediation and governance gaps. The Board should be informed consistent with the 10-K's stated escalation process.

5. **Notify the independent auditor (Greystone & Associates LLP).** Inform the auditor of the incident, the finance-module impact, and the manual-workaround period; begin the ICFR and disclosure-controls assessment.

6. **Notify the M&A advisor and assess acquisition impact.** Inform Canfield Cromdale Consulting & Co.; assess material adverse change, reps & warranties, and disclosure-schedule implications; determine whether and when to notify Kessler Precision Systems GmbH.

### Tier 2 — Near-Term (within 1–2 weeks)

7. **Initiate state and international breach-notification triage.** Engage privacy counsel to map notification obligations across the 38+ U.S. states and the EU/Germany, Mexico, Canada, and UK jurisdictions; prepare and file required regulator and data-subject notifications. Assess GDPR Article 33/34 exposure given the likely elapsed 72-hour controller deadline.

8. **Stabilize insurance position.** (a) Document the late-notice facts and prepare a material-prejudice analysis; (b) assess the MFA application-warranty exposure and develop a coverage-preservation strategy (consider whether the warranty can be reconciled with the Company's actual practices and whether any cure or negotiation is available); (c) confirm consent-to-incur-costs compliance for the $1.4 million in incident-response costs and any non-panel vendors; (d) evaluate the contractual-liability exclusion's effect on customer-contract exposures.

9. **Correct the MFA control and document the remediation.** Complete and validate MFA enforcement on all VPN connections (including third-party contractors), and document the remediation for both the FY2024 10-K disclosure and the insurance file. Conduct a broader third-party access management review per Thorngate's recommendation.

10. **Implement encryption at rest for sensitive data.** Per Thorngate's immediate recommendation, prioritize encryption at rest for ACH/banking and other sensitive ERP data fields.

### Tier 3 — Structural (within 30–90 days, ahead of FY2024 10-K)

11. **Revise the CIRP.** (a) Add mandatory escalation to the General Counsel, CEO, Audit Committee, and Board for Tier 2/Tier 3 and for any incident with potential disclosure or materiality implications; (b) add Legal as a standing IRT member; (c) incorporate a SEC materiality-determination and Item 1.05 disclosure workflow; (d) incorporate customer-contract notification tracking and state/international breach-notification triage; (e) add a legal/disclosure dimension to the severity matrix; (f) establish a tabletop-exercise schedule and conduct the first exercise; (g) conduct the overdue substantive annual review.

12. **Update the Audit Committee charter.** Expressly assign cybersecurity risk oversight to the Audit Committee (or appropriate committee), reference Item 106 of Regulation S-K, address cybersecurity-expertise considerations, and align the charter with the 10-K's stated governance structure. Obtain Board approval of the amended charter.

13. **Strengthen disclosure controls and procedures.** Establish or reinvigorate a disclosure committee with defined cyber-incident escalation triggers; ensure that the General Counsel and disclosure decision-makers are notified within hours (not days) of any Tier 2/Tier 3 incident; document the controls for the FY2024 10-K Item 9A assessment.

14. **Prepare the FY2024 10-K Item 1C / Item 106 disclosure.** Draft disclosure that accurately addresses: the incident and its material impact (if any); the materiality-determination process; the MFA control and its remediation; the (corrected) governance and escalation structure; the CIRP review and testing cadence; and board/committee cybersecurity oversight and expertise. Evaluate the duty to correct/update the FY2023 "no material incidents" statement.

15. **Preserve the privileged record.** Maintain the attorney-client privilege and work-product protections over the forensic investigation and materiality analysis (dual-track privileged/non-privileged documentation as appropriate); ensure Thorngate remains engaged at the direction of counsel; and manage communications to avoid inadvertent waiver.

---

## VI. CONCLUSION

The Company is facing a significant SEC cybersecurity disclosure compliance exposure arising principally from the **absence of a timely materiality determination** for an incident that bears multiple strong indicators of materiality, compounded by **governance and escalation failures**, a **discrepancy between disclosed and actual security controls (MFA)** that also jeopardizes insurance recovery, and **breached customer contractual notification obligations** with direct revenue and materiality consequences. The law-enforcement delay exception is unavailable, and the Company cannot rely on the pending Thorngate investigation or the FBI contact to defer its disclosure obligations.

The most urgent priority is to **convene and document a materiality determination immediately**, and to **prepare an Item 1.05 Form 8-K** on a stand-by basis, while concurrently curing the customer notification defaults, notifying the Audit Committee and independent auditor, and stabilizing the insurance position. The structural recommendations (CIRP revision, charter update, disclosure-controls strengthening, and FY2024 10-K preparation) should proceed in parallel and be substantially complete before the FY2024 10-K is filed.

This memorandum will be updated as the forensic investigation and legal analysis develop. The working group is available to assist with the materiality-determination session, the Form 8-K drafting, and the customer and regulator notification workstreams on an expedited basis.

---

## APPENDIX A: INCIDENT CHRONOLOGY (CONSOLIDATED)

| Date | Day | Event |
|---|---|---|
| ~Nov. 14–17, 2024 | (pre) | Threat actor reconnaissance/dwell via compromised contractor VPN credential (Eastern Europe IP); no MFA |
| Nov. 18, ~1:30–2:15 a.m. | 0 | ~83 GB data exfiltration (customer banking, PII, pricing) |
| Nov. 18, ~2:17 a.m. | 0 | SOC detection |
| Nov. 18, ~4:45 a.m. | 0 | LockStar 3.0 ransomware deployed; 347 endpoints encrypted; ERP finance/procurement/order mgmt down |
| Nov. 18, ~5:00 a.m. | 0 | IRT activated (Tier 3) |
| Nov. 18, ~11:00 a.m. | 0 | CTO verbally informed |
| Nov. 19 | 1 | Thorngate retained; Assoc. GC learns informally; **GC not informed (traveling)** |
| Nov. 20 | 2 | GC informed; FBI IC3 contacted; Hollister Marsh LLP engaged |
| Nov. 21 | 3 | Ridgeline notified (~73 hrs; **late vs. 72-hr requirement**); reserved rights |
| Nov. 25 | 7 | CEO briefed |
| Dec. 1 | 13 | Thorngate interim report: customer banking data exfiltration confirmed (high confidence) |
| Dec. 3 | 15 | **Audit Committee Chair emailed (first Board-level notice)** |
| Dec. 5 | 17 | Status report; **no 8-K; no materiality determination; no customer notices; no state AG notices** |
| Dec. 18 | (target) | Estimated full endpoint restoration |
| Dec. 20 | (target) | Thorngate preliminary findings report due |
| Jan. 22, 2025 | (scheduled) | Next regular Audit Committee meeting (no special meeting called as of Dec. 5) |

---

## APPENDIX B: SUMMARY OF IDENTIFIED GAPS AND SEVERITY

| # | Gap | Primary Authority | Severity |
|---|---|---|---|
| A | No materiality determination conducted | Item 1.05 Form 8-K | Critical |
| B | Strong indicators of materiality (qualitative) | *TSC Industries*; Item 1.05 | Critical |
| C | Law enforcement delay exception unavailable | Item 1.05 | High |
| D | 10-K Item 1C/Item 106 accuracy and updates | Item 106 Reg. S-K | High |
| E | Disclosed vs. actual controls (MFA) discrepancy | Item 106; insurance warranty | Critical / High |
| F | Governance and Board oversight gaps | Item 106; charter | High |
| G | CIRP deficiencies (no testing, no legal/disclosure integration) | Item 106 | High |
| H | Disclosure controls and procedures weaknesses | Rule 13a-15; Item 9A | High |
| I | Insurance coverage at risk (late notice, warranty, exclusions) | Policy CYB-2024-08871 | High |
| J | Breached customer notification obligations (48-hr) | Customer contracts | Critical / High |
| K | State/international breach-notification obligations not initiated | State laws; GDPR Art. 33/34 | High |
| L | Pending acquisition disclosure implications | Antifraud; offering-period duties | High |
| M | Independent auditor / ICFR implications | SOX §404; Item 9A | Medium-High |

---

*Prepared by the Office of the General Counsel, Securities & Cybersecurity Disclosure Working Group, Vantage Industrial Technologies, Inc. This memorandum is privileged and confidential. December 6, 2024.*