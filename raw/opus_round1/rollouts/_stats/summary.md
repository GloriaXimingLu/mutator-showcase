# rollouts/_stats — TRAIN grade trend

**TRAIN only — the held-out val set is never here.** This is the cheap navigation layer: read
it first, then drill into the worst tasks' `transcript.jsonl`. One rollout per task, so single
swings are noisy; trust the persistent / cross-iteration signals.

Latest iter: **1** | tasks: 30

## Train mean by iteration
- iter0: 0.8423  _(bare baseline)_
- iter1: 0.8231

## Improved vs last edit
- litigation-dispute-resolution/assess-reasonableness-of-staffing-levels-on-litigation-invoice  +0.061  (0.84 -> 0.90)
- funds-asset-management/draft-fund-closing-certificate  +0.053  (0.89 -> 0.95)
- capital-markets/draft-registration-statement-on-form-s  +0.044  (0.79 -> 0.83)
- intellectual-property/rnw-ip-license-renewal  +0.044  (0.85 -> 0.90)
- trusts-estates-private-client/analyze-counterparty-markup-of-postnuptial-agreement  +0.043  (0.91 -> 0.96)
- data-privacy-cybersecurity/audit-privacy-policy-compliance/scenario-01  +0.040  (0.86 -> 0.90)
- employment-labor/draft-markup-of-settlement-agreement  +0.038  (0.60 -> 0.63)
- international-trade-sanctions/draft-ofac-specific-license-application  +0.031  (0.92 -> 0.95)
- contracts/commercial-vendor-customer/saas-api-subscription-term-negotiation/scenario-01  +0.020  (0.92 -> 0.94)
- real-estate/draft-settlement-statement  +0.016  (0.81 -> 0.82)

## Harmed vs last edit
- corporate-governance/compare-state-paid-leave-requirements-across-seven-jurisdictions  -0.250  (0.97 -> 0.72)
- corporate-ma/review-governance-diligence/scenario-01  -0.148  (0.96 -> 0.81)
- corporate-ma/analyze-cim-deal-teaser/scenario-02  -0.098  (0.85 -> 0.76)
- healthcare-life-sciences/identify-issues-in-fda-pre  -0.085  (0.89 -> 0.81)
- corporate-governance/extract-compliance-requirements-from-municipal-cannabis-dispensary-permit-application  -0.073  (0.82 -> 0.75)
- tax/review-iss-tax-transaction-structure  -0.071  (0.93 -> 0.86)
- contracts/corporate-ma/joint-venture-agreement-term-negotiation/scenario-02  -0.054  (0.77 -> 0.71)
- trusts-estates-private-client/extract-key-exhibits-from-document-production  -0.050  (0.77 -> 0.72)
- environmental-esg/identify-issues-in-phase-one-environmental-site-assessment  -0.038  (0.17 -> 0.13)
- arbitration-international-dispute-resolution/identify-issues-in-arbitrator-disclosure-statement  -0.026  (0.97 -> 0.95)
- capital-markets/draft-underwriting-agreement  -0.024  (0.91 -> 0.88)
- immigration/compare-immigration  -0.023  (0.81 -> 0.79)

## Improved vs bare
- litigation-dispute-resolution/assess-reasonableness-of-staffing-levels-on-litigation-invoice  +0.061  (0.84 -> 0.90)
- funds-asset-management/draft-fund-closing-certificate  +0.053  (0.89 -> 0.95)
- capital-markets/draft-registration-statement-on-form-s  +0.044  (0.79 -> 0.83)
- intellectual-property/rnw-ip-license-renewal  +0.044  (0.85 -> 0.90)
- trusts-estates-private-client/analyze-counterparty-markup-of-postnuptial-agreement  +0.043  (0.91 -> 0.96)
- data-privacy-cybersecurity/audit-privacy-policy-compliance/scenario-01  +0.040  (0.86 -> 0.90)
- employment-labor/draft-markup-of-settlement-agreement  +0.038  (0.60 -> 0.63)
- international-trade-sanctions/draft-ofac-specific-license-application  +0.031  (0.92 -> 0.95)
- contracts/commercial-vendor-customer/saas-api-subscription-term-negotiation/scenario-01  +0.020  (0.92 -> 0.94)
- real-estate/draft-settlement-statement  +0.016  (0.81 -> 0.82)

## Harmed vs bare — cumulative regressions — watch these
- corporate-governance/compare-state-paid-leave-requirements-across-seven-jurisdictions  -0.250  (0.97 -> 0.72)
- corporate-ma/review-governance-diligence/scenario-01  -0.148  (0.96 -> 0.81)
- corporate-ma/analyze-cim-deal-teaser/scenario-02  -0.098  (0.85 -> 0.76)
- healthcare-life-sciences/identify-issues-in-fda-pre  -0.085  (0.89 -> 0.81)
- corporate-governance/extract-compliance-requirements-from-municipal-cannabis-dispensary-permit-application  -0.073  (0.82 -> 0.75)
- tax/review-iss-tax-transaction-structure  -0.071  (0.93 -> 0.86)
- contracts/corporate-ma/joint-venture-agreement-term-negotiation/scenario-02  -0.054  (0.77 -> 0.71)
- trusts-estates-private-client/extract-key-exhibits-from-document-production  -0.050  (0.77 -> 0.72)
- environmental-esg/identify-issues-in-phase-one-environmental-site-assessment  -0.038  (0.17 -> 0.13)
- arbitration-international-dispute-resolution/identify-issues-in-arbitrator-disclosure-statement  -0.026  (0.97 -> 0.95)
- capital-markets/draft-underwriting-agreement  -0.024  (0.91 -> 0.88)
- immigration/compare-immigration  -0.023  (0.81 -> 0.79)

## Stuck (max < 0.5 across all iters)
- environmental-esg/identify-issues-in-phase-one-environmental-site-assessment  max 0.17  (0.17 -> 0.13)

## Volatile (span > 0.3 — likely 1-rollout noise)
- (none)

## By practice area (mean per iter)
- arbitration-international-dispute-resolution: 0.9368 -> 0.9237
- capital-markets: 0.8474 -> 0.8578
- contracts: 0.8383 -> 0.8207
- corporate-governance: 0.8782 -> 0.7704
- corporate-ma: 0.9083 -> 0.7855
- data-privacy-cybersecurity: 0.86 -> 0.9
- employment-labor: 0.5962 -> 0.6346
- environmental-esg: 0.1698 -> 0.1321
- funds-asset-management: 0.8947 -> 0.9474
- healthcare-life-sciences: 0.8936 -> 0.8085
- immigration: 0.7788 -> 0.7671
- intellectual-property: 0.9185 -> 0.9406
- international-trade-sanctions: 0.9219 -> 0.9531
- litigation-dispute-resolution: 0.8919 -> 0.9123
- real-estate: 0.86 -> 0.8632
- tax: 0.9286 -> 0.8571
- trusts-estates-private-client: 0.8399 -> 0.8366
