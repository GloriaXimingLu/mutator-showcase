# PRIVILEGED & CONFIDENTIAL --- ATTORNEY-CLIENT PRIVILEGED / ATTORNEY WORK PRODUCT

**Prepared at the direction of counsel in anticipation of litigation and
for the purpose of providing legal advice. Do not distribute outside the
Office of the General Counsel without prior authorization.**

# MEMORANDUM

  ----------------------------------- -----------------------------------
  **TO:**                             Audit Committee of the Board of
                                      Directors; Marcus Ellsworth, Chief
                                      Executive Officer; Priya Raghavan,
                                      General Counsel & Corporate
                                      Secretary

  **FROM:**                           Hollister Marsh LLP --- Securities
                                      Law & Disclosure Counsel (Jonathan
                                      Beckett, Lead Partner)

  **DATE:**                           December 6, 2024

  **RE:**                             SEC Cybersecurity Disclosure
                                      Compliance Gap Analysis ---
                                      Incident INC-2024-0047 (Ransomware
                                      and Data Exfiltration Event of
                                      November 18, 2024)

  **PRIVILEGE:**                      Attorney-Client Privileged /
                                      Attorney Work Product
  ----------------------------------- -----------------------------------

## I. Executive Summary

This memorandum presents a comprehensive gap analysis of the
cybersecurity disclosure and incident-response posture of Vantage
Industrial Technologies, Inc. ("Vantage" or the "Company") in light of
the ransomware and data-exfiltration incident detected on November 18,
2024 (Incident INC-2024-0047, the "Incident"). The analysis is based on
our review of the Company's Form 10-K Item 1C disclosure for fiscal year
2023, the Audit Committee Charter, the Cybersecurity Incident Response
Plan ("CIRP"), the Thorngate Forensic Solutions interim status report
dated December 1, 2024, the CISO incident status report dated December
5, 2024, the cyber-insurance policy summary, the General Counsel's
December 3, 2024 email to the Audit Committee Chair, and the Office of
the General Counsel's extract of customer-contract notification
provisions.

**The central finding is that, as of December 5, 2024 --- seventeen (17)
days after discovery of the Incident --- the Company has not conducted a
formal materiality determination and has not filed any disclosure with
the Securities and Exchange Commission (the "SEC").** The SEC's
cybersecurity incident disclosure rule (Item 1.05 of Form 8-K) requires
a registrant to determine whether a cybersecurity incident is material
"without unreasonable delay" after discovery and, upon a materiality
determination, to file a Current Report on Form 8-K within four (4)
business days. The Company's delay in initiating a documented
materiality assessment --- particularly after the December 1, 2024
forensic confirmation that customer banking data (ACH routing and
account numbers) was exfiltrated --- creates material risk of an SEC
disclosure violation and enforcement exposure.

Our preliminary assessment, set forth in Part V, is that the Incident is
**likely material** under the federal securities laws based on
qualitative factors that substantially outweigh the modest quantitative
impact (\~1.45% of projected FY2024 EBITDA). Those qualitative factors
include: (i) exfiltration of unencrypted banking information and
personally identifiable information ("PII") for approximately 4,200
customer accounts, including at least six (6) of the Company's top ten
customers (representing \~38% of revenue); (ii) breach of 48-hour
customer-contract notification deadlines with three top customers,
exposing the Company to liquidated damages, termination, payment
suspension, and exclusion from future business; (iii) a pending \$425
million acquisition (Kessler Precision Systems GmbH) whose counterparty
and financial advisor have not been notified; (iv) potential inaccuracy
of the Company's prior Item 1C disclosure regarding multi-factor
authentication ("MFA"); and (v) potential impairment of cyber-insurance
coverage.

The analysis identifies **twenty-three (23) discrete compliance gaps**
across eleven (11) subject areas, summarized in the consolidated table
in Part VI and detailed in Part IV. The most urgent are:

1.  **No materiality determination and no Form 8-K filed** (CRITICAL);
2.  **Customer-contract notification deadlines missed** with three
    top-ten customers, with material contractual and
    revenue-concentration consequences (CRITICAL);
3.  **Potential inaccuracy of the FY2023 10-K Item 1C MFA disclosure**
    and a corresponding **cyber-insurance application warranty breach**
    that could void coverage (CRITICAL);
4.  **No insider trading blackout** implemented despite a class of
    insiders holding material nonpublic information (CRITICAL);
5.  **Audit Committee Charter does not address cybersecurity
    oversight**, inconsistent with the governance disclosure in Item 1C
    (HIGH);
6.  **CIRP escalation tops out at the CTO** with no mandatory triggers
    to the General Counsel, CEO, Audit Committee, or Board, and
    expressly excludes external (customer/regulator/public)
    communications from its scope (HIGH);
7.  **No state or international data-breach notifications** commenced
    despite affected records in 38+ U.S. states and the EU (HIGH); and
8.  **Independent auditor not notified** of an Incident that encrypted
    the ERP finance, procurement, and order-management modules (HIGH).

Part VII sets out a prioritized remediation roadmap. The Company should,
without further delay, (a) convene a documented materiality
determination with management and counsel, (b) implement an insider
trading blackout, (c) notify the independent auditor and the Kessler
transaction counterparty, (d) issue the overdue customer notifications,
and (e) call a special meeting of the Audit Committee rather than
waiting for the January 22, 2025 regularly scheduled meeting.

## II. Factual Background and Incident Summary

The following factual summary is drawn from the documents identified
above and is stated for the purpose of framing the legal analysis. All
times are Eastern Standard Time.

### A. The Company

Vantage is a Delaware corporation headquartered in Columbus, Ohio, with
common stock listed on Nasdaq (ticker: VTIQ). The Company operates 14
manufacturing facilities across the United States, Germany, and Mexico,
employs approximately 6,800 personnel, and manages approximately 2,100
networked endpoints. Projected FY2024 revenue is approximately \$1.87
billion and projected FY2024 EBITDA is approximately \$310 million. The
Company's top ten customers represent approximately 38% of total revenue
(\~\$710.6 million). The Company is in active negotiations to acquire
Kessler Precision Systems GmbH for approximately \$425 million, with
Canfield Cromdale Consulting & Co. serving as financial advisor.

### B. The Incident

On November 18, 2024, at approximately 2:17 a.m., the Company's Security
Operations Center ("SOC") detected anomalous network activity
originating from a VPN session authenticated with a credential belonging
to a third-party maintenance contractor. Forensic analysis by Thorngate
Forensic Solutions, Inc. ("Thorngate") subsequently established a
two-phase attack:

-   **Phase 1 --- Data exfiltration (approx. 1:30 a.m. -- 2:15 a.m.,
    November 18):** Approximately 83 GB of data was exfiltrated to an
    external IP address *before* ransomware deployment, consistent with
    a double-extortion methodology.
-   **Phase 2 --- Ransomware deployment (approx. 2:17 a.m. -- 4:45 a.m.,
    November 18):** The LockStar 3.0 ransomware variant encrypted 347 of
    approximately 2,100 endpoints, including the ERP finance,
    procurement, and order-management modules.

A ransom demand of 45 Bitcoin (\~\$2,029,500) was issued. The Company
has not paid and does not intend to pay. Manufacturing operations and
OT/SCADA systems were not affected; the IT/OT air-gap performed as
designed.

### C. Exfiltrated Data (Thorngate, "High Confidence," December 1, 2024)

Thorngate confirmed with high confidence that the exfiltrated data
includes:

-   Customer master records for approximately 4,200 corporate accounts;
-   Procurement-contact PII (names, email addresses, telephone numbers,
    job titles);
-   Contract pricing data and terms; and
-   **Customer banking information --- ACH routing numbers and account
    numbers --- stored unencrypted (plaintext) at rest** in the ERP
    accounts-receivable module.

Affected records span at least 38 U.S. states and customers in Germany,
Mexico, Canada, and the United Kingdom, and include several of the
Company's largest accounts, including Harmon Defense Solutions,
Crestfield Aerospace, and Nexagen Manufacturing.

### D. Root Cause

Thorngate's preliminary root-cause finding is that the compromised
third-party contractor VPN credential **was not protected by
multi-factor authentication ("MFA")**, permitting the threat actor to
authenticate without a secondary factor. The threat actor's dwell time
(reconnaissance) is estimated at three to four days (approx. November
14--17).

### E. Key Chronology

  -----------------------------------------------------------------------
  Date                                Event
  ----------------------------------- -----------------------------------
  Nov. 18, \~2:17 a.m.                SOC detects anomalous activity;
                                      data exfiltration already
                                      underway/completed.

  Nov. 18, \~4:45 a.m.                Ransomware deployment across 347
                                      endpoints complete.

  Nov. 18, 5:00 a.m.                  CISO activates IRT under Tier 3
                                      classification.

  Nov. 18, 11:00 a.m.                 CTO Lauren Hessler verbally
                                      informed.

  Nov. 19                             Thorngate retained (60-day
                                      engagement; preliminary findings
                                      due Dec. 20). Associate GC Daniel
                                      Ito learns of Incident via informal
                                      IT communication. **General Counsel
                                      Priya Raghavan (traveling) not
                                      informed.**

  Nov. 20                             GC Raghavan learns of Incident upon
                                      return; Hollister Marsh LLP
                                      engaged; FBI IC3 contacted.

  Nov. 21                             Ridgeline Insurance Group notified
                                      (\~73 hours post-discovery; policy
                                      requires 72 hours).

  Nov. 25                             CEO Marcus Ellsworth briefed.

  Dec. 1                              Thorngate interim report confirms
                                      customer banking data exfiltrated.

  Dec. 3                              Audit Committee Chair Dr. Helen
                                      Ostrowski notified by email (first
                                      Board-level notice; Day 15).

  Dec. 5                              CISO status report prepared. **No
                                      Form 8-K filed; no formal
                                      materiality determination
                                      conducted; no customer
                                      notifications sent.**

  Jan. 22, 2025                       Next regularly scheduled Audit
                                      Committee meeting (no special
                                      meeting called).
  -----------------------------------------------------------------------

### F. Estimated Financial Impact (as of December 5, 2024)

  -----------------------------------------------------------------------
  Category                            Estimated Cost
  ----------------------------------- -----------------------------------
  Incident response costs             \$1,400,000

  Business disruption costs           \$2,800,000

  Customer-notification preparation   \$300,000
  costs                               

  **Total estimated costs**           **\$4,500,000**
  -----------------------------------------------------------------------

The \$4.5 million total represents approximately 1.45% of projected
FY2024 EBITDA. These figures do not include potential customer claims,
liquidated damages, regulatory penalties, litigation, or reputational
impact, all of which could materially increase total exposure.

## III. Applicable SEC Regulatory Framework

The following SEC rules and requirements are principally implicated:

1.  **Item 1.05 of Form 8-K** (17 C.F.R. § 249.308) --- requires a
    registrant that determines a cybersecurity incident to be material
    to file a Current Report on Form 8-K within **four (4) business
    days** after the materiality determination, disclosing (a) the
    material aspects of the nature, scope, and timing of the
    incident; (b) the material or reasonably likely material impact on
    the registrant, including financial condition and results of
    operations; (c) whether the incident has been remediated and, if
    not, what is being done; and (d) whether law enforcement has
    requested a delay in disclosure. The instruction to Item 1.05
    requires the registrant to determine materiality **"without
    unreasonable delay"** after discovery of the incident.

2.  **Item 106 of Regulation S-K** (17 C.F.R. § 229.106) / **Item 1C of
    Form 10-K** --- governs annual disclosure of cybersecurity risk
    management, strategy, and governance, including (a) the Company's
    processes for assessing, identifying, and managing material
    cybersecurity risks; (b) whether and how cybersecurity risks have
    materially affected, or are reasonably likely to materially affect,
    the Company; and (c) the Board's oversight of cybersecurity risks
    and management's role in assessing and managing such risks.

3.  **Rule 13a-15** under the Securities Exchange Act of 1934 (the
    "Exchange Act") --- requires disclosure controls and procedures
    reasonably designed to ensure that information required to be
    disclosed is recorded, processed, summarized, and reported within
    required time periods, and internal control over financial reporting
    ("ICFR").

4.  **Section 13(a)** of the Exchange Act and **Rules 13a-11 and
    13a-13** --- periodic and current reporting obligations.

5.  **Regulation FD** (Rules 100--103) --- prohibition on selective
    disclosure of material nonpublic information to certain outside
    parties without broad public disclosure.

6.  **Rule 10b-5** under the Exchange Act and **Section 17(a)** of the
    Securities Act --- anti-fraud prohibitions on material misstatements
    and omissions.

7.  **Sections 302 and 404** of the Sarbanes-Oxley Act of 2002 and the
    related certifications --- CEO/CFO certifications regarding
    disclosure controls and ICFR.

8.  **Materiality standard** --- *TSC Industries, Inc. v. Northway,
    Inc.*, 426 U.S. 438 (1976), and *Basic Inc. v. Levinson*, 485 U.S.
    224 (1988): information is material if there is a substantial
    likelihood that a reasonable investor would consider it important,
    or if it would significantly alter the "total mix" of available
    information. The SEC's adopting release (Release No. 33-11221)
    confirms that cybersecurity-incident materiality is assessed under
    this standard and may turn on qualitative as well as quantitative
    factors.

## IV. Gap Analysis

### A. Materiality Determination and Form 8-K Item 1.05 Disclosure --- **CRITICAL**

**Gap A-1. No formal materiality determination has been conducted.** The
CISO status report (Dec. 5, 2024) expressly states: "No formal
materiality determination has been conducted." Item 1.05's instruction
requires the Company to determine materiality "without unreasonable
delay" after discovery. Discovery occurred on November 18, 2024.
Seventeen days have elapsed. Although the SEC rule does not prescribe a
fixed deadline for the materiality determination itself, the
determination must be made promptly, and the four-business-day filing
clock cannot begin to run until it is. The absence of any documented
determination process --- despite the engagement of outside securities
counsel on November 20, the CEO briefing on November 25, the December 1
forensic confirmation of banking-data exfiltration, and the December 3
notice to the Audit Committee Chair --- is inconsistent with the
"without unreasonable delay" standard and creates enforcement exposure.

**Gap A-2. No Form 8-K has been filed.** No Current Report on Form 8-K
(Item 1.05 or otherwise) has been filed regarding the Incident. If the
Incident is determined to be material (see Part V), the Company must
file within four business days of that determination. The longer the
determination is deferred, the greater the risk that the SEC will view
the delay as itself a violation of the disclosure-controls requirements
and the "without unreasonable delay" standard.

**Gap A-3. No law-enforcement delay basis exists.** Item 1.05 permits
delayed disclosure only where the U.S. Attorney General (or designee)
notifies the SEC that disclosure would pose a substantial risk to
national security or public safety. The Company contacted the FBI IC3 on
November 20, 2024, but the status report confirms that **no
law-enforcement request to delay disclosure has been received**. IC3
reporting is a complaint-intake mechanism, not a basis for delaying Item
1.05 disclosure. There is accordingly no lawful basis to defer the 8-K
on law-enforcement grounds.

**Gap A-4. No interim disclosure under Item 7.01/8.01 considered.** Even
where materiality has not yet been determined, many issuers make a
voluntary interim disclosure under Item 7.01 (Regulation FD) or Item
8.01 (Other Events) of Form 8-K to (i) manage Regulation FD and
insider-trading risk arising from the possession of material nonpublic
information by insiders, and (ii) satisfy any "duty to update" arising
from prior cybersecurity disclosures. The Company has not done so. Given
that the Company's FY2023 10-K Item 1C expressly addressed cybersecurity
and stated that no material incident had occurred, the Company should
evaluate whether its continued silence renders its prior disclosure and
any subsequent investor communications misleading.

### B. Accuracy of Prior 10-K Item 1C Disclosure --- **CRITICAL**

**Gap B-1. Potential inaccuracy of the MFA disclosure.** The FY2023 Form
10-K Item 1C (filed February 28, 2024) states that the Company has
implemented "multi-factor authentication for access to critical
information systems, remote access connections, and administrative
accounts." The CIRP (Section 4.1(d)) likewise states that
"\[m\]ulti-factor authentication (MFA) is required for all VPN
connections." However, Thorngate's root-cause finding and the CISO
status report establish that **MFA was not universally required for
third-party contractor VPN access** prior to November 20, 2024. If MFA
was not in fact required for all remote-access connections (including
third-party contractor VPN) as of the February 28, 2024 filing date, the
Item 1C description of this control was inaccurate or materially
incomplete, raising Rule 10b-5 and Section 17(a) concerns and
undermining the reliability of the Company's Item 106 risk-management
disclosure. The Company should assess whether a corrective disclosure is
required and whether the FY2024 10-K Item 1C must be revised to
accurately describe the control environment.

**Gap B-2. The "no material incidents" statement remains accurate as of
the prior filing but requires updating.** The FY2023 10-K's statement
that the Company "has not experienced any cybersecurity incidents that
have materially affected, or are reasonably likely to materially affect"
the Company was accurate as of the February 28, 2024 filing date and
does not, by itself, require amendment. However, the Company now has a
material incident (see Part V) and must disclose it timely via Form 8-K
and in its FY2024 10-K (Item 1C, MD&A, and risk factors). The Company
should also evaluate whether any statements made in investor
communications, earnings calls, or the Kessler transaction materials
since November 18, 2024 are rendered misleading by the nondisclosure.

**Gap B-3. CIRP "review" characterization may be misleading.** Item 1C
states the CIRP "was most recently reviewed in August 2023." The CIRP
itself discloses that the August 14, 2023 review was **administrative
only** (vendor-contact updates), with no substantive changes since the
June 2022 original release, and that **no tabletop exercises or
simulations have ever been conducted**. The Item 1C description of an
"adaptive" program that is "periodically reviewed and updated"
overstates the actual maintenance and testing of the CIRP. The FY2024
10-K should accurately characterize the CIRP's review history and
testing status.

### C. Disclosure Controls and Procedures / Internal Control Over Financial Reporting --- **HIGH**

**Gap C-1. Disclosure-controls breakdown in escalation.** The chronology
reveals multiple disclosure-controls failures: (i) the General Counsel
--- the Company's principal disclosure officer --- was not informed of
the Incident until November 20 (Day 2) because she was traveling; (ii)
the Associate General Counsel learned of the Incident on November 19 via
"informal communication from an IT colleague" rather than through a
formal escalation channel; and (iii) the Audit Committee Chair was not
informed until December 3 (Day 15). The CIRP's escalation matrix
(Section 10) tops out at the CTO and treats the General Counsel, CEO,
and Board as "optional" contacts (Appendix B) at the Incident
Commander's discretion. This structure does not ensure that material
information reaches the Company's disclosure decision-makers "within the
time periods specified in the Commission's rules and forms," as required
by Rule 13a-15(a).

**Gap C-2. ICFR impact not assessed.** The Incident encrypted the ERP
finance, procurement, and order-management modules --- the systems that
support the Company's core transaction processing, accounts payable and
receivable, general ledger, and financial reporting. Thorngate reports
that "certain ERP functions may produce results that require manual
verification" and that data-integrity validation is ongoing. The Company
has not assessed whether the Incident created a material weakness or
significant deficiency in ICFR. Given that the Company's fiscal year
ends December 31, 2024, and the FY2024 10-K will require Section 302/404
certifications, this assessment is time-critical.

**Gap C-3. No disclosure-controls certification analysis initiated.**
The CEO and CFO certifications in the FY2024 10-K will require
conclusions about the effectiveness of disclosure controls and
procedures. The delays and escalation failures identified above may
require disclosure of a material weakness or significant deficiency in
Item 9A of the FY2024 10-K. The Company should begin this analysis now.

### D. Board and Audit Committee Governance --- Charter and Oversight --- **HIGH**

**Gap D-1. Audit Committee Charter does not address cybersecurity.** The
Audit Committee Charter (last amended and restated March 15, 2021) does
not mention cybersecurity anywhere. Section V.D ("Compliance and Risk
Management") addresses "major financial risk exposures" but is silent on
cybersecurity risk. The Charter predates the SEC's cybersecurity
disclosure rules (effective September 5, 2023) and has not been updated.
This is inconsistent with the Item 1C governance disclosure, which
states that "the Board, acting primarily through its Audit Committee,
oversees the Company's cybersecurity risk management program" and that
the Audit Committee "receives quarterly updates on the Company's
cybersecurity posture." The absence of an express charter mandate
creates a gap between disclosed governance and documented authority and
weakens the Company's ability to demonstrate Board-level oversight to
the SEC, auditors, and plaintiffs.

**Gap D-2. No special Audit Committee meeting called.** The Audit
Committee Chair was first notified on December 3, 2024 (Day 15). The
next regularly scheduled meeting is January 22, 2025 --- more than two
months after discovery. The General Counsel's December 3 email suggests
the matter be discussed "at the next scheduled Audit Committee meeting
on January 22, 2025, or sooner if you believe a special session is
warranted." For an incident of this magnitude, deferring Board-level
oversight to a routine quarterly meeting is inconsistent with the Item
1C representation that the Board is informed "in a timely manner" of
significant incidents. A special meeting should be convened promptly.

**Gap D-3. CISO lacks direct reporting access to the Board/Audit
Committee.** The CISO reports to the CTO, who reports to the CEO; Audit
Committee visibility is limited to the CTO's quarterly technology
updates. The Item 1C disclosure describes this structure, but the
Incident demonstrates that it contributed to the 15-day delay in Board
notification. Item 106(c) governance disclosure and emerging best
practices favor direct CISO access to the Audit Committee (or a
designated cybersecurity-oversight body) for significant incidents. The
Company should consider establishing a direct reporting line or a
mandatory escalation trigger for Tier 3 incidents.

### E. Cybersecurity Incident Response Plan (CIRP) Deficiencies --- **HIGH**

**Gap E-1. Escalation matrix does not mandate notice to the General
Counsel, CEO, Audit Committee, or Board.** The CIRP escalation matrix
(Section 10.1) requires escalation only from the CISO to the CTO. The
General Counsel, CEO, and Board are listed in Appendix B as "optional
contacts" at the Incident Commander's discretion, with the note that the
Incident Commander "should consult the CTO before engaging optional
contacts." This design is the proximate cause of the disclosure-controls
breakdown: the Company's principal disclosure officer (the General
Counsel) was not in the mandatory notification chain. The CIRP must be
revised to mandate prompt notification of the General Counsel (as
disclosure officer), the CEO, and the Audit Committee/Board for all Tier
2 and Tier 3 incidents, with defined timeframes.

**Gap E-2. External communications expressly excluded from CIRP scope.**
CIRP Section 9.3 states that "\[e\]xternal communications regarding
cybersecurity incidents --- including communications to customers,
regulators, media, or the public --- are outside the scope of this
Plan." This is a structural deficiency: the CIRP governs the technical
response but provides no framework, triggers, or coordination protocol
for the customer, regulatory, and public disclosures that a material
incident requires. The Plan should be integrated with a
disclosure-decision protocol that links severity classification to
materiality assessment and external-notification workflows (customer
contracts, state breach laws, GDPR, SEC 8-K).

**Gap E-3. No tabletop exercises or simulations conducted.** The CIRP
(Sections 1.4 and 4.3) expressly acknowledges that "no tabletop
exercises or simulation-based tests of this Plan have been conducted."
The Item 1C disclosure describes an "adaptive" program, but an untested
plan cannot credibly be represented as such. The absence of testing also
means the escalation and disclosure gaps identified here were never
surfaced internally. The Company should implement a regular exercise
schedule and document results for the Audit Committee.

**Gap E-4. CIRP not substantively updated since June 2022.** The CIRP
has had no substantive revision since its June 15, 2022 original
release; the August 2023 "review" was administrative only. The threat
landscape, the Company's environment, and the regulatory framework
(including the SEC's September 2023 rules) have all changed materially.
The CIRP should be substantively reviewed and updated, with CTO
re-approval, and the Item 1C description should accurately reflect the
review cadence.

**Gap E-5. Severity classification is purely technical and does not
incorporate materiality or disclosure triggers.** The CIRP severity
matrix (Section 3.2) classifies incidents solely on technical criteria
(endpoint count, downtime, data exfiltration, privileged-credential
compromise). It contains no bridge from technical severity to
materiality assessment or disclosure obligations. A Tier 3 technical
classification does not automatically trigger a materiality analysis.
The Plan should incorporate a materiality-assessment step and a
disclosure-decision checkpoint for Tier 2/Tier 3 incidents.

### F. Regulation FD, Selective Disclosure, and Insider Trading --- **CRITICAL**

**Gap F-1. No insider trading blackout implemented.** As of December 5,
2024, a defined class of insiders --- including the CEO, CTO, CISO,
General Counsel, Associate General Counsel, and the Audit Committee
Chair --- has possessed material nonpublic information about the
Incident since on or before November 25, 2024 (and earlier for certain
officers). The documents reviewed contain no indication that the Company
has imposed a trading blackout, closed any window, or issued
insider-trading reminders. If any insider has traded, or trades, in
Vantage securities while aware of this information, the Company and the
individual face Rule 10b-5 and Section 16 liability risk. A blackout
should be implemented immediately and retroactively documented.

**Gap F-2. Selective disclosure risk.** Material nonpublic information
regarding the Incident has been selectively communicated to the Audit
Committee Chair (December 3) and to members of management without any
broad public disclosure. While internal communications to directors and
officers in their fiduciary capacities are generally outside Regulation
FD, the Company should be alert to any communication of this information
to outside parties (e.g., lenders, significant shareholders, analysts,
or the Kessler counterparty) that would trigger Regulation FD's
simultaneous or prompt-disclosure requirement. The Company should
restrict internal circulation on a need-to-know basis and prepare a
public disclosure to cure any selective-disclosure exposure.

**Gap F-3. No Regulation FD / "duty to update" analysis documented.**
Because the Company has made public cybersecurity disclosures (Item 1C)
and is engaged in a material acquisition, it should analyze whether its
continued silence creates a "duty to update" risk and whether a
voluntary disclosure under Item 7.01/8.01 is advisable to manage Reg FD
and insider-trading exposure pending the materiality determination.

### G. Customer Contract Notification Obligations --- **CRITICAL**

**Gap G-1. 48-hour notification deadlines missed with three top-ten
customers.** The Office of the General Counsel's contract extract
(December 5, 2024) confirms that Harmon Defense Solutions, Crestfield
Aerospace, and Nexagen Manufacturing each impose a **48-hour
notification obligation** from discovery of a security incident/breach
affecting their data. Discovery occurred November 18, 2024; the
deadlines expired no later than November 20, 2024. **As of December 5,
2024, no notifications have been sent to any of these customers** ---
approximately 15 days late. These three customers are among the
Company's top ten (collectively \~38% of revenue).

**Gap G-2. Material contractual consequences have accrued.** The missed
deadlines trigger significant contractual remedies:

  -------------------------------------------------------------------------------------------
  Customer          Liquidated        Termination Right    Other Remedies
                    Damages                                
  ----------------- ----------------- -------------------- ----------------------------------
  Harmon Defense    **\$500,000 per   30 days' notice      Full indemnity
  Solutions         incident** for                         (incl. regulatory-investigation,
                    late notification                      notification, and
                                                           credit-monitoring costs); 3-year
                                                           survival

  Crestfield        None specified    **Immediate**        Payment suspension pending
  Aerospace                                                investigation; 12-month audit
                                                           right at Vantage's expense; full
                                                           indemnity + credit monitoring;
                                                           \$10M insurance requirement

  Nexagen           None specified    15 days (immediate   Full indemnity +
  Manufacturing                       if                   regulatory-compliance costs; **up
                                      security-standards   to 24-month exclusion from future
                                      failure)             business**
  -------------------------------------------------------------------------------------------

**Gap G-3. Revenue-concentration risk.** At least six (6) of the top ten
customers (representing a substantial portion of the \~\$710.6 million
in concentrated revenue) are believed to have records in the exfiltrated
dataset. The combination of breached notification deadlines, termination
rights, payment-suspension rights, and future-business exclusion creates
a material risk to revenue that significantly elevates the materiality
of the Incident (see Part V) and must be quantified for the materiality
determination and for any 8-K disclosure of reasonably likely material
impact.

**Gap G-4. Additional customer contracts not yet reviewed.** The
contract extract notes that only three of the top-twenty customer
contracts have been reviewed and that the full review is expected by
December 10, 2024. Additional notification obligations and remedies may
exist. The Company should expedite the full contract review and triage
notification obligations by deadline.

**Gap G-5. Forensic-report-sharing obligations.** Crestfield requires
delivery of the forensic investigator's findings within 30 days of the
investigation's conclusion; Nexagen requires a preliminary report within
5 business days and a final report within 60 days of initial
notification. The Company should plan to satisfy these obligations
(subject to privilege protections) and coordinate with Thorngate and
counsel on deliverable scope and timing.

### H. State and International Data-Breach Notification Obligations --- **HIGH**

**Gap H-1. No state notifications commenced.** Affected records span at
least 38 U.S. states. The exfiltrated data includes financial-account
information (ACH routing and account numbers) and PII, which trigger
notification obligations under numerous state data-breach notification
statutes (typically requiring notice to affected individuals "without
unreasonable delay" or within 30--60 days, and notice to state attorneys
general above defined resident thresholds; several states require notice
to credit-reporting agencies where financial-account data of more than a
specified number of residents is implicated). **No state notifications
have been filed as of December 5, 2024.** The Company should immediately
map affected residents by state, determine applicable deadlines, and
commence notifications.

**Gap H-2. GDPR / EU and other international obligations.** Affected
customers include entities in Germany and the United Kingdom. Under the
EU General Data Protection Regulation ("GDPR"), Article 33 requires
notification of a personal-data breach to the competent supervisory
authority within **72 hours** of becoming aware, and Article 34 requires
notification of data subjects without undue delay where the breach is
likely to result in a high risk to their rights and freedoms. Mexico's
LFPDPPP and Canadian requirements may also apply. The Company became
aware of EU-customer data exposure no later than December 1, 2024
(Thorngate interim report), and arguably earlier. The 72-hour GDPR
supervisory-authority deadline may have already lapsed or be imminent.
**No EU or other international notifications have been made.** The
Company should engage EU privacy counsel immediately.

**Gap H-3. No breach-notification workflow integrated with the CIRP.**
As noted in Gap E-2, the CIRP excludes external/regulatory
communications from its scope. There is no documented workflow
connecting the forensic determination of affected data categories and
jurisdictions to the applicable breach-notification deadlines. This is a
process gap that should be remediated.

### I. Cyber-Insurance Coverage Risks --- **CRITICAL**

**Gap I-1. Late notice to the insurer.** Ridgeline Insurance Group was
notified on November 21, 2024, approximately **73 hours** after
discovery. Policy CYB-2024-08871 (Section 5.1) requires notice "in no
event later than seventy-two (72) hours after Discovery." "Discovery" is
defined as the point at which the CISO, CIO, CTO, General Counsel, CFO,
or any VP-level-or-above officer first becomes aware of facts indicating
a Cyber Event. The CISO became aware on November 18, 2024. Notice was
therefore late by approximately one hour. Ridgeline has **reserved
rights on the timeliness of notice**. While the policy contains a
notice-prejudice framework in some jurisdictions, in jurisdictions
applying strict compliance the late notice is a ground for denial. The
Company should document the basis for the timing and prepare a prejudice
analysis.

**Gap I-2. Potential application-warranty breach (MFA).** The Policy
Application (October 15, 2023) warranted that the Company "employs
multi-factor authentication for all remote access to Computer Systems."
Thorngate's root-cause finding establishes that the compromised
third-party contractor VPN credential was **not** MFA-protected, and the
CISO status report confirms that "MFA was not universally required for
third-party contractor VPN access" prior to November 20, 2024. If MFA
was not in fact employed for all remote access as of the application
date and policy inception (January 1, 2024), the warranty was
inaccurate, and the policy states that "\[m\]aterial misrepresentations
in the Policy Application may void coverage ab initio." This is a
**material coverage risk** that could eliminate the \~\$2.0 million of
recoverable loss above the \$2.5 million SIR and the full \$15 million
aggregate limit.

**Gap I-3. Potential "failure to maintain minimum security standards"
exclusion.** Exclusion (i) excludes loss arising from the Company's
failure to maintain security controls substantially consistent with
those represented in the application, where the failure materially
contributed to the Cyber Event. The MFA failure was the root cause of
the Incident and therefore materially contributed to it. Ridgeline may
invoke this exclusion independently of the warranty analysis. The
Company should develop the factual record (e.g., evidence of MFA
deployment scope, any partial MFA implementation) to defend against this
exclusion.

**Gap I-4. Contractual-liability exclusion may bar customer-claim
coverage.** Exclusion (g) excludes loss "arising solely from breach of
contractual notification or indemnification clauses --- where no
independent tort liability exists." The Harmon liquidated damages
(\$500,000), the Crestfield payment-suspension and audit-cost
obligations, and the Nexagen indemnification and
future-business-exclusion remedies arise principally from breached
contractual notification clauses. To the extent these claims rest solely
on contract (without independent tort liability), they may be
**uninsured**. The Company should not assume the \$15 million aggregate
will absorb customer-contract exposure.

**Gap I-5. Consent-to-incur-costs compliance.** Section 7.2 requires the
insurer's prior written consent for first-party losses exceeding
\$50,000 individually or \$150,000 in the aggregate (with an emergency
exception requiring notice within 48 hours of incurring costs). The
Company has incurred \~\$1.4 million in incident-response costs. The
Company should confirm that the emergency-exception notice was timely
given and that vendor selections (Thorngate is on the pre-approved
panel, which is favorable) comply with the consent provisions to
preserve coverage.

### J. Pending Kessler Acquisition --- **HIGH**

**Gap J-1. Transaction counterparty and financial advisor not
notified.** The Company is negotiating the \$425 million acquisition of
Kessler Precision Systems GmbH. As of December 5, 2024, **neither
Kessler nor the Company's financial advisor (Canfield Cromdale
Consulting & Co.) has been notified** of the Incident, and "the
potential impact of this cybersecurity incident on the pending
acquisition ... has not been evaluated." The Incident may affect (i)
representations and warranties in the acquisition agreement (including
any cyber-incident, data-breach, or compliance reps), (ii)
material-adverse-change provisions, (iii) counterparty confidence and
deal timeline, and (iv) any financing arrangements. Failure to disclose
a material cyber incident to a transaction counterparty creates
litigation and indemnity risk and may itself be a breach of any existing
agreement.

**Gap J-2. SEC disclosure implications for the transaction.** If the
Company prepares any SEC disclosure in connection with the acquisition
(e.g., a proxy statement, Form S-4, or Form 8-K under Item
1.01/2.01/9.01), the cybersecurity incident is a material fact that must
be disclosed. The Company should ensure that transaction disclosure
documents address the Incident and its reasonably likely material
impact. The General Counsel has appropriately flagged the need to
coordinate with outside counsel (Hollister Marsh) on the intersection of
the Incident and the transaction; this analysis should be expedited.

**Gap J-3. No assessment of MAC/financing impact.** The Company has not
assessed whether the Incident constitutes or could be argued to
constitute a material adverse change under any financing or transaction
document, or whether lenders or other financing sources must be
notified. This assessment should be undertaken promptly.

### K. Independent Auditor Notification --- **HIGH**

**Gap K-1. Independent auditor not notified.** Greystone & Associates
LLP, the Company's independent auditor, has not been notified of the
Incident. The FY2024 audit cycle has not commenced, but the Incident
directly implicates the audit because: (i) the ERP finance, procurement,
and order-management modules were encrypted and remain subject to
data-integrity validation; (ii) the Incident may have created a material
weakness or significant deficiency in ICFR; (iii) the Incident may give
rise to loss contingencies requiring evaluation under ASC 450 and
disclosure in the financial statements; and (iv) subsequent-event
considerations apply. Under PCAOB standards and the auditor's
professional responsibilities, the auditor should be informed of the
Incident promptly so that it can plan the FY2024 audit, evaluate ICFR,
and consider disclosure and contingent-liability implications. The
Company should notify Greystone without further delay.

**Gap K-2. No loss-contingency analysis initiated.** The Company has not
commenced an analysis of whether the Incident gives rise to accrued or
disclosed loss contingencies under ASC 450-20 (including the Harmon
liquidated damages, customer indemnification claims, regulatory
exposure, and litigation risk). This analysis is necessary for both the
8-K (if material) and the FY2024 financial statements and should be
undertaken with the auditor and counsel.

## V. Preliminary Materiality Assessment

The formal materiality determination is the responsibility of
management, with the advice of counsel and the oversight of the Audit
Committee. The following preliminary assessment is provided to frame the
urgency of that determination and is based on the information available
as of December 5, 2024.

**Quantitative factors (favoring immateriality, but not dispositive):**

-   Estimated direct costs of \~\$4.5 million represent \~1.45% of
    projected FY2024 EBITDA and a smaller fraction of projected revenue
    (\~\$1.87 billion). On cost alone, the Incident may not meet a
    purely quantitative materiality threshold.
-   The ransom (\~\$2.03 million) has not been and will not be paid.

**Qualitative factors (strongly favoring materiality):**

1.  **Nature and sensitivity of exfiltrated data.** Unencrypted ACH
    routing and account numbers and procurement-contact PII for \~4,200
    customer accounts. Banking data is especially sensitive and creates
    a heightened risk of fraudulent fund transfers and downstream harm
    to customers.
2.  **Customer concentration and contractual breach.** At least six of
    the top ten customers (\~38% of revenue) are affected; 48-hour
    notification deadlines with three top customers have been breached,
    exposing the Company to a \$500,000 liquidated-damages claim
    (Harmon), immediate termination rights (Crestfield), payment
    suspension, a 12-month audit right at the Company's expense, and up
    to 24-month exclusion from future business (Nexagen). The reasonably
    likely impact on revenue and customer relationships is material.
3.  **Pending \$425 million acquisition.** The Incident may affect
    representations, the deal timeline, counterparty confidence, and
    financing. A material cyber incident during a pending acquisition of
    this size is the type of development a reasonable investor would
    consider important.
4.  **Control-environment and disclosure-accuracy implications.** The
    MFA root cause calls into question the accuracy of the Company's
    prior Item 1C disclosure and its insurance-application warranty,
    which in turn affects the reliability of the Company's public
    cybersecurity disclosures and its insurance recovery.
5.  **Regulatory and litigation exposure.** Breach-notification
    obligations across 38+ states and the EU (GDPR), potential SEC
    disclosure-violation exposure, and likely customer and possibly
    class-action litigation.
6.  **Reputational harm.** The Company serves defense and aerospace
    customers (Harmon Defense Solutions, Crestfield Aerospace); a breach
    involving defense-sector customer data may carry heightened
    reputational and possibly regulatory (e.g., CFIUS,
    defense-industrial-base) consequences.
7.  **Insurance recovery uncertainty.** Late notice and the potential
    warranty/exclusion issues place \~\$2.0 million of expected recovery
    (and the full \$15 million aggregate) at risk, increasing net
    exposure.

**Preliminary conclusion.** Based on the qualitative factors, which the
SEC's adopting release confirms are properly considered in the
cybersecurity-incident materiality analysis, **the Incident is likely
material** under the *TSC Industries* / *Basic* standard. The reasonably
likely material impact on the Company's customer relationships, revenue
concentration, the pending acquisition, and the reliability of its prior
disclosures --- independent of the modest direct cost --- supports a
materiality conclusion. The Company should not rely on the
1.45%-of-EBITDA figure alone. We recommend that management, with
counsel, convene a documented materiality determination promptly and, if
material (as we expect), file a Form 8-K under Item 1.05 within four
business days of that determination.

## VI. Consolidated Gap Summary

  ---------------------------------------------------------------------------------------
  \#             Gap                       Subject Area   Severity       Primary
                                                                         SEC/Regulatory
                                                                         Hook
  -------------- ------------------------- -------------- -------------- ----------------
  A-1            No formal materiality     8-K disclosure CRITICAL       Item 1.05
                 determination conducted                                 instruction;
                 (Day 17)                                                Rule 13a-15

  A-2            No Form 8-K filed         8-K disclosure CRITICAL       Item 1.05 of
                                                                         Form 8-K

  A-3            No law-enforcement delay  8-K disclosure CRITICAL       Item 1.05(d)
                 basis                                                   

  A-4            No interim Item 7.01/8.01 8-K disclosure HIGH           Reg FD; duty to
                 disclosure considered                                   update

  B-1            MFA disclosure in Item 1C Prior          CRITICAL       Item 106; Rule
                 potentially inaccurate    disclosure                    10b-5
                                           accuracy                      

  B-2            Prior "no material        Prior          HIGH           Item 106;
                 incidents" statement      disclosure                    Section 13(a)
                 requires updating         accuracy                      

  B-3            CIRP "review"/"adaptive"  Prior          MEDIUM         Item 106
                 characterization          disclosure                    
                 overstated                accuracy                      

  C-1            Disclosure-controls       Controls       HIGH           Rule 13a-15(a)
                 escalation breakdown                                    

  C-2            ICFR impact not assessed  Controls       HIGH           Rules 13a-15(f),
                                                                         13a-15(a); SOX
                                                                         404

  C-3            No disclosure-controls    Controls       HIGH           SOX 302; Item 9A
                 certification analysis                                  

  D-1            Audit Committee Charter   Governance     HIGH           Item 106(c)
                 silent on cybersecurity                                 

  D-2            No special Audit          Governance     HIGH           Item 106(c)
                 Committee meeting called                                

  D-3            CISO lacks direct         Governance     MEDIUM         Item 106(c)
                 Board/Audit Committee                                   
                 access                                                  

  E-1            CIRP escalation does not  Incident       HIGH           Rule 13a-15;
                 mandate GC/CEO/Board      response                      Item 106(a)
                 notice                                                  

  E-2            External communications   Incident       HIGH           Item 106(a)
                 excluded from CIRP scope  response                      

  E-3            No tabletop               Incident       MEDIUM         Item 106(a)
                 exercises/simulations     response                      
                 ever conducted                                          

  E-4            CIRP not substantively    Incident       MEDIUM         Item 106(a)
                 updated since June 2022   response                      

  E-5            Severity matrix lacks     Incident       MEDIUM         Item 106(a)
                 materiality/disclosure    response                      
                 bridge                                                  

  F-1            No insider trading        Insider        CRITICAL       Rule 10b-5;
                 blackout implemented      trading                       Section 16

  F-2            Selective disclosure risk Reg FD         HIGH           Regulation FD
                 to outside parties                                      

  F-3            No Reg FD /               Reg FD         MEDIUM         Regulation FD
                 duty-to-update analysis                                 
                 documented                                              

  G-1            48-hour customer          Customer       CRITICAL       (Contractual;
                 notification deadlines    contracts                     materiality
                 missed (3 top customers)                                input)

  G-2            Contractual remedies      Customer       CRITICAL       (Contractual;
                 accrued (LDs,             contracts                     materiality
                 termination, suspension,                                input)
                 exclusion)                                              

  G-3            Revenue-concentration     Customer       CRITICAL       (Materiality
                 risk (top-10 customers)   contracts                     input)

  G-4            Additional customer       Customer       HIGH           (Contractual)
                 contracts not yet         contracts                     
                 reviewed                                                

  G-5            Forensic-report-sharing   Customer       MEDIUM         (Contractual)
                 obligations not planned   contracts                     

  H-1            No state data-breach      Breach         HIGH           State breach
                 notifications commenced   notification                  statutes

  H-2            No GDPR/EU/international  Breach         HIGH           GDPR Arts.
                 notifications; 72-hour    notification                  33--34; LFPDPPP
                 clock at risk                                           

  H-3            No breach-notification    Breach         MEDIUM         State/EU law
                 workflow integrated with  notification                  
                 CIRP                                                    

  I-1            Late notice to cyber      Insurance      CRITICAL       Policy terms
                 insurer (\~73 hrs                                       
                 vs. 72-hr requirement)                                  

  I-2            Potential MFA             Insurance      CRITICAL       Policy terms
                 application-warranty                                    
                 breach (voiding risk)                                   

  I-3            Potential "failure to     Insurance      CRITICAL       Policy Exclusion
                 maintain security                                       (i)
                 standards" exclusion                                    

  I-4            Contractual-liability     Insurance      HIGH           Policy Exclusion
                 exclusion may bar                                       (g)
                 customer-claim coverage                                 

  I-5            Consent-to-incur-costs    Insurance      MEDIUM         Policy Section
                 compliance unconfirmed                                  7.2

  J-1            Kessler counterparty and  M&A            HIGH           (Contractual;
                 financial advisor not                                   disclosure)
                 notified                                                

  J-2            SEC disclosure for        M&A            HIGH           Item 1.01/9.01;
                 transaction not addressed                               proxy/S-4

  J-3            No MAC/financing-impact   M&A            MEDIUM         (Contractual)
                 assessment                                              

  K-1            Independent auditor not   Financial      HIGH           PCAOB; ASC 450;
                 notified                  reporting                     SOX 404

  K-2            No loss-contingency       Financial      HIGH           ASC 450-20
                 analysis initiated        reporting                     
  ---------------------------------------------------------------------------------------

## VII. Recommended Remediation Actions

The following actions are prioritized by urgency. "Immediate" actions
should be undertaken within the next one to four business days.

### Tier 1 --- Immediate (0--4 business days)

1.  **Convene a documented materiality determination.** Management, with
    disclosure counsel, should conduct and document a formal materiality
    analysis (quantitative and qualitative) immediately. Document the
    participants, the analysis, the conclusion, and the date/time of the
    determination. (Addresses A-1; Part V.)
2.  **Prepare and file Form 8-K Item 1.05 if material.** If the
    determination is material (as we preliminarily conclude), draft and
    file the 8-K within four business days of the determination,
    addressing the nature, scope, and timing of the Incident; the
    material or reasonably likely material impact; remediation status;
    and the absence of any law-enforcement delay request. (Addresses
    A-2, A-3.)
3.  **Implement an insider trading blackout.** Close all trading windows
    for directors, officers, and other insiders aware of the Incident;
    issue written reminders; and document the blackout effective date
    (retroactive to the date material nonpublic information arose).
    (Addresses F-1.)
4.  **Notify the independent auditor (Greystone & Associates LLP).**
    Provide a briefing on the Incident, its impact on the ERP financial
    systems, and the ICFR/disclosure-controls implications. (Addresses
    K-1, C-2.)
5.  **Notify the Kessler transaction counterparty and financial
    advisor.** Coordinate with transaction counsel on the timing, scope,
    and form of notice, and assess MAC, reps-and-warranties, and
    financing implications. (Addresses J-1, J-3.)
6.  **Issue overdue customer notifications.** Send notifications to
    Harmon, Crestfield, and Nexagen (and other affected customers as
    identified) without further delay to mitigate liquidated-damages,
    termination, and exclusion exposure, even though the 48-hour
    deadlines have passed. Coordinate content with counsel to preserve
    privilege and satisfy contractual content requirements. (Addresses
    G-1, G-2.)
7.  **Commence state and international breach-notification analysis.**
    Map affected residents by jurisdiction; engage EU privacy counsel
    for GDPR Arts. 33--34 compliance; determine state AG and
    individual-notification deadlines; and begin filings. (Addresses
    H-1, H-2.)
8.  **Call a special Audit Committee meeting.** Do not defer Board-level
    oversight to the January 22, 2025 routine meeting. Provide the Audit
    Committee with the materiality analysis, the 8-K draft, and the
    remediation plan. (Addresses D-2.)
9.  **Engage Ridgeline on coverage.** Provide a detailed claim
    submission; address the late-notice issue with a prejudice analysis;
    and develop the factual record on MFA deployment to defend against
    the warranty and exclusion positions. (Addresses I-1, I-2, I-3,
    I-5.)

### Tier 2 --- Near-term (1--4 weeks)

10. **Update the Audit Committee Charter** to expressly address
    cybersecurity-risk oversight, including the Committee's
    responsibility for oversight of cybersecurity risk management,
    materiality-determination processes, and incident-reporting
    protocols. Obtain Board approval. (Addresses D-1.)
11. **Revise the CIRP** to (i) mandate prompt notification of the
    General Counsel, CEO, and Audit Committee/Board for all Tier 2 and
    Tier 3 incidents with defined timeframes; (ii) incorporate a
    materiality-assessment and disclosure-decision checkpoint; (iii)
    bring external communications (customer, regulator, public) within
    scope or integrate a companion disclosure protocol; and (iv) require
    periodic tabletop exercises. Obtain CTO re-approval. (Addresses E-1,
    E-2, E-5.)
12. **Assess disclosure controls and ICFR.** Evaluate whether the
    escalation failures constitute a material weakness or significant
    deficiency; document the assessment for the FY2024 10-K Item 9A and
    Section 302/404 certifications. (Addresses C-1, C-2, C-3.)
13. **Complete the customer-contract review** (top-twenty and beyond)
    and triage all notification obligations and remedies. (Addresses
    G-4, G-5.)
14. **Implement MFA universally** for all remote access (internal and
    third-party) and implement encryption at rest for sensitive data
    (per Thorngate's recommendation), prioritizing ACH/banking fields.
    (Addresses B-1 control remediation; I-2/I-3 mitigation.)
15. **Establish a direct CISO reporting line or escalation trigger** to
    the Audit Committee for significant incidents. (Addresses D-3.)
16. **Evaluate a corrective/interim disclosure** regarding the MFA
    control description and any investor communications made since
    November 18, 2024. (Addresses B-1, B-2, A-4, F-3.)

### Tier 3 --- Ongoing

17. **Prepare FY2024 10-K disclosures** --- Item 1C (accurate
    risk-management, strategy, and governance description, including the
    Incident and the MFA correction), MD&A (impact and known
    trends/uncertainties), risk factors, and Item 9A (controls).
    (Addresses B-1, B-2, B-3, C-3.)
18. **Conduct and document tabletop exercises** and report results to
    the Audit Committee. (Addresses E-3, E-4.)
19. **Complete the CIRP Phase 5 post-incident review** and track
    remediation actions to closure in ServiceNow. (Addresses E-4.)
20. **Monitor dark web** for exfiltrated data and maintain enhanced
    detection for LockStar 3.0 IOCs. (Operational; supports loss
    mitigation and disclosure accuracy.)
21. **Initiate loss-contingency analysis** under ASC 450-20 with the
    auditor and counsel for the FY2024 financial statements. (Addresses
    K-2.)
22. **Restrict internal circulation** of Incident information to a
    need-to-know basis and prepare a public-disclosure plan to cure any
    selective-disclosure exposure. (Addresses F-2.)
23. **Coordinate transaction disclosure** for the Kessler acquisition to
    address the Incident in any proxy, S-4, or 8-K. (Addresses J-2.)

## VIII. Conclusion

The November 18, 2024 ransomware and data-exfiltration Incident presents
a serious and time-sensitive SEC cybersecurity-disclosure compliance
challenge. The most significant gap --- the absence of a formal
materiality determination and any SEC filing seventeen days after
discovery --- should be closed immediately. Our preliminary assessment
is that the Incident is likely material based on qualitative factors,
particularly the exfiltration of unencrypted customer banking data, the
breach of 48-hour notification deadlines with top customers representing
a substantial portion of concentrated revenue, the potential inaccuracy
of the Company's prior MFA disclosure, and the implications for the
pending \$425 million acquisition. The Company should convene a
documented materiality determination without further delay, implement an
insider trading blackout, notify the independent auditor and the Kessler
counterparty, issue the overdue customer notifications, commence state
and international breach notifications, and call a special Audit
Committee meeting. Concurrently, the Company should remediate the
structural governance and incident-response gaps --- including the Audit
Committee Charter, the CIRP escalation and external-communications
scope, and the disclosure-controls breakdown --- that this Incident has
exposed, and should prepare accurate FY2024 10-K disclosures.

We are available to assist with the materiality determination, the Form
8-K drafting, the customer and regulatory notification strategy, the
insurance-coverage analysis, and the CIRP and charter revisions. This
memorandum is privileged and confidential and should not be distributed
outside the Office of the General Counsel without prior authorization.

**Hollister Marsh LLP**

Jonathan Beckett, Lead Partner Securities Law & Disclosure Counsel 700 K
Street NW, Washington, D.C. 20001

*This memorandum constitutes legal advice and is protected by the
attorney-client privilege and the attorney work-product doctrine. It was
prepared at the direction of Priya Raghavan, General Counsel & Corporate
Secretary of Vantage Industrial Technologies, Inc., in connection with
the cybersecurity incident disclosed herein.*
