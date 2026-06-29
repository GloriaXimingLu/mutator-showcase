# rollouts/_stats — TRAIN grade trend

**TRAIN only — the held-out val set is never here.** This is the cheap navigation layer: read
it first, then drill into the worst tasks' `transcript.jsonl`. One rollout per task, so single
swings are noisy; trust the persistent / cross-iteration signals.

Latest iter: **1** | tasks: 30

## Train mean by iteration
- iter0: 0.8283  _(bare baseline)_
- iter1: 0.8401

## Improved vs last edit
- corporate-governance/extract-compliance-requirements-from-municipal-cannabis-dispensary-permit-application  +0.132  (0.72 -> 0.85)
- corporate-governance/compare-state-paid-leave-requirements-across-seven-jurisdictions  +0.117  (0.75 -> 0.87)
- real-estate/draft-development-agreement  +0.115  (0.81 -> 0.92)
- capital-markets/draft-registration-statement-on-form-s  +0.089  (0.78 -> 0.87)
- arbitration-international-dispute-resolution/identify-issues-in-arbitrator-disclosure-statement  +0.079  (0.92 -> 1.00)
- international-trade-sanctions/draft-ofac-specific-license-application  +0.078  (0.89 -> 0.97)
- litigation-dispute-resolution/draft-motion-to-dismiss-brief  +0.067  (0.87 -> 0.93)
- environmental-esg/identify-issues-in-phase-one-environmental-site-assessment  +0.057  (0.09 -> 0.15)
- contracts/corporate-ma/joint-venture-agreement-term-negotiation/scenario-02  +0.036  (0.77 -> 0.80)
- immigration/identify-h1b-qualification-issues  +0.026  (0.77 -> 0.79)
- corporate-governance/assess-impact-of-sec-cybersecurity-disclosure-rule-on-incident-response-procedures  +0.022  (0.76 -> 0.78)
- trusts-estates-private-client/extract-key-exhibits-from-document-production  +0.017  (0.80 -> 0.82)

## Harmed vs last edit
- litigation-dispute-resolution/assess-reasonableness-of-staffing-levels-on-litigation-invoice  -0.102  (0.92 -> 0.82)
- arbitration-international-dispute-resolution/identify-arbitration-agreement-issues  -0.075  (0.90 -> 0.82)
- corporate-ma/analyze-cim-deal-teaser/scenario-02  -0.073  (0.93 -> 0.85)
- trusts-estates-private-client/analyze-counterparty-markup-of-postnuptial-agreement  -0.043  (0.96 -> 0.91)
- tax/review-iss-tax-transaction-structure  -0.036  (0.93 -> 0.89)
- intellectual-property/extract-key-terms-from-technology-licensing-term-sheet  -0.032  (0.97 -> 0.94)
- capital-markets/draft-underwriting-agreement  -0.024  (0.89 -> 0.87)
- contracts/commercial-vendor-customer/saas-api-subscription-term-negotiation/scenario-01  -0.020  (0.94 -> 0.92)
- data-privacy-cybersecurity/audit-privacy-policy-compliance/scenario-01  -0.020  (0.92 -> 0.90)
- litigation-dispute-resolution/draft-interrogatories  -0.020  (0.98 -> 0.96)
- employment-labor/draft-markup-of-settlement-agreement  -0.019  (0.65 -> 0.63)
- funds-asset-management/draft-fund-closing-certificate  -0.018  (0.89 -> 0.88)

## Improved vs bare
- corporate-governance/extract-compliance-requirements-from-municipal-cannabis-dispensary-permit-application  +0.132  (0.72 -> 0.85)
- corporate-governance/compare-state-paid-leave-requirements-across-seven-jurisdictions  +0.117  (0.75 -> 0.87)
- real-estate/draft-development-agreement  +0.115  (0.81 -> 0.92)
- capital-markets/draft-registration-statement-on-form-s  +0.089  (0.78 -> 0.87)
- arbitration-international-dispute-resolution/identify-issues-in-arbitrator-disclosure-statement  +0.079  (0.92 -> 1.00)
- international-trade-sanctions/draft-ofac-specific-license-application  +0.078  (0.89 -> 0.97)
- litigation-dispute-resolution/draft-motion-to-dismiss-brief  +0.067  (0.87 -> 0.93)
- environmental-esg/identify-issues-in-phase-one-environmental-site-assessment  +0.057  (0.09 -> 0.15)
- contracts/corporate-ma/joint-venture-agreement-term-negotiation/scenario-02  +0.036  (0.77 -> 0.80)
- immigration/identify-h1b-qualification-issues  +0.026  (0.77 -> 0.79)
- corporate-governance/assess-impact-of-sec-cybersecurity-disclosure-rule-on-incident-response-procedures  +0.022  (0.76 -> 0.78)
- trusts-estates-private-client/extract-key-exhibits-from-document-production  +0.017  (0.80 -> 0.82)

## Harmed vs bare — cumulative regressions — watch these
- litigation-dispute-resolution/assess-reasonableness-of-staffing-levels-on-litigation-invoice  -0.102  (0.92 -> 0.82)
- arbitration-international-dispute-resolution/identify-arbitration-agreement-issues  -0.075  (0.90 -> 0.82)
- corporate-ma/analyze-cim-deal-teaser/scenario-02  -0.073  (0.93 -> 0.85)
- trusts-estates-private-client/analyze-counterparty-markup-of-postnuptial-agreement  -0.043  (0.96 -> 0.91)
- tax/review-iss-tax-transaction-structure  -0.036  (0.93 -> 0.89)
- intellectual-property/extract-key-terms-from-technology-licensing-term-sheet  -0.032  (0.97 -> 0.94)
- capital-markets/draft-underwriting-agreement  -0.024  (0.89 -> 0.87)
- contracts/commercial-vendor-customer/saas-api-subscription-term-negotiation/scenario-01  -0.020  (0.94 -> 0.92)
- data-privacy-cybersecurity/audit-privacy-policy-compliance/scenario-01  -0.020  (0.92 -> 0.90)
- litigation-dispute-resolution/draft-interrogatories  -0.020  (0.98 -> 0.96)
- employment-labor/draft-markup-of-settlement-agreement  -0.019  (0.65 -> 0.63)
- funds-asset-management/draft-fund-closing-certificate  -0.018  (0.89 -> 0.88)

## Stuck (max < 0.5 across all iters)
- environmental-esg/identify-issues-in-phase-one-environmental-site-assessment  max 0.15  (0.09 -> 0.15)

## Volatile (span > 0.3 — likely 1-rollout noise)
- (none)

## By practice area (mean per iter)
- arbitration-international-dispute-resolution: 0.9105 -> 0.9125
- capital-markets: 0.8359 -> 0.8686
- contracts: 0.8449 -> 0.8502
- corporate-governance: 0.742 -> 0.8325
- corporate-ma: 0.8986 -> 0.862
- data-privacy-cybersecurity: 0.92 -> 0.9
- employment-labor: 0.6538 -> 0.6346
- environmental-esg: 0.0943 -> 0.1509
- funds-asset-management: 0.8947 -> 0.8772
- healthcare-life-sciences: 0.8936 -> 0.8936
- immigration: 0.7683 -> 0.7812
- intellectual-property: 0.918 -> 0.9021
- international-trade-sanctions: 0.8906 -> 0.9688
- litigation-dispute-resolution: 0.9212 -> 0.903
- real-estate: 0.8151 -> 0.8728
- tax: 0.9286 -> 0.8929
- trusts-estates-private-client: 0.8783 -> 0.8649
