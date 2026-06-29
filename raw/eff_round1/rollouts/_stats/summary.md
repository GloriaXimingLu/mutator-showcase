# rollouts/_stats — TRAIN grade trend

**TRAIN only — the held-out val set is never here.** This is the cheap navigation layer: read
it first, then drill into the worst tasks' `transcript.jsonl`. One rollout per task, so single
swings are noisy; trust the persistent / cross-iteration signals.

Latest iter: **4** | tasks: 30

## Train mean by iteration
- iter0: 0.8423  _(bare baseline)_
- iter1: 0.8158
- iter2: 0.8261
- iter3: 0.8349
- iter4: 0.8376

## Improved vs last edit
- corporate-governance/compare-state-paid-leave-requirements-across-seven-jurisdictions  +0.217  (0.97 -> 0.93 -> 0.92 -> 0.73 -> 0.95)
- funds-asset-management/draft-fund-closing-certificate  +0.070  (0.89 -> 0.84 -> 0.91 -> 0.88 -> 0.95)
- real-estate/draft-settlement-statement  +0.065  (0.81 -> 0.81 -> 0.79 -> 0.77 -> 0.84)
- contracts/commercial-vendor-customer/saas-api-subscription-term-negotiation/scenario-01  +0.060  (0.92 -> 0.92 -> 0.90 -> 0.88 -> 0.94)
- capital-markets/draft-underwriting-agreement  +0.059  (0.91 -> 0.86 -> 0.88 -> 0.84 -> 0.89)
- employment-labor/draft-markup-of-settlement-agreement  +0.058  (0.60 -> 0.56 -> 0.60 -> 0.48 -> 0.54)
- capital-markets/draft-registration-statement-on-form-s  +0.056  (0.79 -> 0.83 -> 0.87 -> 0.84 -> 0.90)
- litigation-dispute-resolution/draft-motion-to-dismiss-brief  +0.045  (0.90 -> 0.87 -> 0.94 -> 0.91 -> 0.96)
- litigation-dispute-resolution/draft-interrogatories  +0.040  (0.94 -> 0.90 -> 0.88 -> 0.92 -> 0.96)
- trusts-estates-private-client/extract-key-exhibits-from-document-production  +0.033  (0.77 -> 0.75 -> 0.75 -> 0.73 -> 0.77)
- healthcare-life-sciences/identify-issues-in-fda-pre  +0.021  (0.89 -> 0.87 -> 0.87 -> 0.85 -> 0.87)
- contracts/banking/intercreditor-agreement-term-negotiation  +0.019  (0.83 -> 0.85 -> 0.85 -> 0.81 -> 0.83)

## Harmed vs last edit
- environmental-esg/identify-issues-in-phase-one-environmental-site-assessment  -0.358  (0.17 -> 0.11 -> 0.09 -> 0.49 -> 0.13)
- trusts-estates-private-client/analyze-counterparty-markup-of-postnuptial-agreement  -0.087  (0.91 -> 0.91 -> 0.91 -> 0.96 -> 0.87)
- corporate-ma/review-governance-diligence/scenario-01  -0.074  (0.96 -> 0.94 -> 0.87 -> 0.94 -> 0.87)
- immigration/identify-h1b-qualification-issues  -0.051  (0.74 -> 0.85 -> 0.87 -> 0.90 -> 0.85)
- immigration/compare-immigration  -0.046  (0.81 -> 0.77 -> 0.77 -> 0.84 -> 0.79)
- data-privacy-cybersecurity/audit-privacy-policy-compliance/scenario-01  -0.040  (0.86 -> 0.86 -> 0.88 -> 0.90 -> 0.86)
- tax/review-iss-tax-transaction-structure  -0.036  (0.93 -> 0.79 -> 0.86 -> 0.86 -> 0.82)
- arbitration-international-dispute-resolution/identify-issues-in-arbitrator-disclosure-statement  -0.026  (0.97 -> 0.89 -> 0.92 -> 0.89 -> 0.87)
- litigation-dispute-resolution/assess-reasonableness-of-staffing-levels-on-litigation-invoice  -0.020  (0.84 -> 0.90 -> 0.90 -> 0.84 -> 0.82)

## Improved vs bare
- capital-markets/draft-registration-statement-on-form-s  +0.111  (0.79 -> 0.83 -> 0.87 -> 0.84 -> 0.90)
- immigration/identify-h1b-qualification-issues  +0.103  (0.74 -> 0.85 -> 0.87 -> 0.90 -> 0.85)
- litigation-dispute-resolution/draft-motion-to-dismiss-brief  +0.056  (0.90 -> 0.87 -> 0.94 -> 0.91 -> 0.96)
- contracts/corporate-ma/joint-venture-agreement-term-negotiation/scenario-02  +0.054  (0.77 -> 0.73 -> 0.80 -> 0.80 -> 0.82)
- funds-asset-management/draft-fund-closing-certificate  +0.053  (0.89 -> 0.84 -> 0.91 -> 0.88 -> 0.95)
- real-estate/draft-settlement-statement  +0.032  (0.81 -> 0.81 -> 0.79 -> 0.77 -> 0.84)
- contracts/commercial-vendor-customer/saas-api-subscription-term-negotiation/scenario-01  +0.020  (0.92 -> 0.92 -> 0.90 -> 0.88 -> 0.94)
- litigation-dispute-resolution/draft-interrogatories  +0.020  (0.94 -> 0.90 -> 0.88 -> 0.92 -> 0.96)
- intellectual-property/extract-key-terms-from-technology-licensing-term-sheet  +0.016  (0.98 -> 0.95 -> 0.97 -> 0.98 -> 1.00)
- intellectual-property/rnw-ip-license-renewal  +0.015  (0.85 -> 0.84 -> 0.88 -> 0.85 -> 0.87)

## Harmed vs bare — cumulative regressions — watch these
- tax/review-iss-tax-transaction-structure  -0.107  (0.93 -> 0.79 -> 0.86 -> 0.86 -> 0.82)
- arbitration-international-dispute-resolution/identify-issues-in-arbitrator-disclosure-statement  -0.105  (0.97 -> 0.89 -> 0.92 -> 0.89 -> 0.87)
- corporate-ma/review-governance-diligence/scenario-01  -0.093  (0.96 -> 0.94 -> 0.87 -> 0.94 -> 0.87)
- employment-labor/draft-markup-of-settlement-agreement  -0.058  (0.60 -> 0.56 -> 0.60 -> 0.48 -> 0.54)
- corporate-governance/assess-impact-of-sec-cybersecurity-disclosure-rule-on-incident-response-procedures  -0.044  (0.84 -> 0.82 -> 0.76 -> 0.80 -> 0.80)
- trusts-estates-private-client/analyze-counterparty-markup-of-postnuptial-agreement  -0.043  (0.91 -> 0.91 -> 0.91 -> 0.96 -> 0.87)
- environmental-esg/identify-issues-in-phase-one-environmental-site-assessment  -0.038  (0.17 -> 0.11 -> 0.09 -> 0.49 -> 0.13)
- corporate-governance/extract-compliance-requirements-from-municipal-cannabis-dispensary-permit-application  -0.029  (0.82 -> 0.74 -> 0.75 -> 0.78 -> 0.79)
- immigration/compare-immigration  -0.023  (0.81 -> 0.77 -> 0.77 -> 0.84 -> 0.79)
- healthcare-life-sciences/identify-issues-in-fda-pre  -0.021  (0.89 -> 0.87 -> 0.87 -> 0.85 -> 0.87)
- litigation-dispute-resolution/assess-reasonableness-of-staffing-levels-on-litigation-invoice  -0.020  (0.84 -> 0.90 -> 0.90 -> 0.84 -> 0.82)
- corporate-governance/compare-state-paid-leave-requirements-across-seven-jurisdictions  -0.017  (0.97 -> 0.93 -> 0.92 -> 0.73 -> 0.95)

## ⚠ Cost THRASH (latest harvested iter vs bare — turns/tokens blown up)
- watch   intellectual-property_extract-key-terms-from-technology-licensing-term-sheet  turns x1.93  tokens x2.74  (iter4 vs bare)
- watch   contracts_banking_intercreditor-agreement-term-negotiation  turns x1.17  tokens x1.81  (iter4 vs bare)
- watch   corporate-governance_compare-state-paid-leave-requirements-across-seven-jurisdictions  turns x1.48  tokens x1.59  (iter4 vs bare)
  (an efficiency edit must NOT thrash: a good mean cut HIDES these per-task blowups. turns AND tokens both up = a re-fetch LOOP (fix it, e.g. pin recently re-fetched content); tokens up with turns ~flat = a one-time re-read (a cost regression to weigh, not a loop).)

## Per-task cost — bare (pick experiments cost/time-aware)
_input_tokens = where the savings live (aim your edit at the giants); wall-clock = the TIME each
costs to RUN (don't re-run the giants on every micro-variant — explore broadly on a cheap/fast
mix, prove out on a few giants); money is ~$1/task flat, so breadth costs money + the giants cost time._
-    5.6M in_tok    34m  39 turns  litigation-dispute-resolution_draft-motion-to-dismiss-brief
-    3.5M in_tok     7m  32 turns  contracts_corporate-ma_joint-venture-agreement-term-negotiation_scenario-02
-    3.3M in_tok    18m  40 turns  employment-labor_draft-markup-of-settlement-agreement
-    3.3M in_tok    29m  34 turns  corporate-ma_analyze-cim-deal-teaser_scenario-02
-    3.1M in_tok     9m  20 turns  contracts_commercial-vendor-customer_saas-api-subscription-term-negotiation_scenario-01
-    2.8M in_tok    16m  29 turns  contracts_banking_intercreditor-agreement-term-negotiation
-    2.6M in_tok    16m  22 turns  corporate-governance_extract-compliance-requirements-from-municipal-cannabis-dispensary-permit-application
-    2.4M in_tok    12m  26 turns  capital-markets_draft-underwriting-agreement
-    2.4M in_tok    10m  21 turns  capital-markets_draft-registration-statement-on-form-s
-    2.3M in_tok     9m  25 turns  real-estate_draft-settlement-statement
-    2.0M in_tok    11m  23 turns  funds-asset-management_draft-fund-closing-certificate
-    1.9M in_tok    11m  22 turns  real-estate_draft-development-agreement

## Stuck (max < 0.5 across all iters)
- environmental-esg/identify-issues-in-phase-one-environmental-site-assessment  max 0.49  (0.17 -> 0.11 -> 0.09 -> 0.49 -> 0.13)

## Volatile (span > 0.3 — likely 1-rollout noise)
- environmental-esg/identify-issues-in-phase-one-environmental-site-assessment  span 0.40  (0.17 -> 0.11 -> 0.09 -> 0.49 -> 0.13)

## By practice area (mean per iter)
- arbitration-international-dispute-resolution: 0.9368 -> 0.8599 -> 0.873 -> 0.8974 -> 0.8842
- capital-markets: 0.8474 -> 0.8461 -> 0.8745 -> 0.8399 -> 0.8971
- contracts: 0.8383 -> 0.8328 -> 0.8499 -> 0.8304 -> 0.8628
- corporate-governance: 0.8782 -> 0.8303 -> 0.8074 -> 0.7709 -> 0.848
- corporate-ma: 0.9083 -> 0.8747 -> 0.8376 -> 0.8991 -> 0.862
- data-privacy-cybersecurity: 0.86 -> 0.86 -> 0.88 -> 0.9 -> 0.86
- employment-labor: 0.5962 -> 0.5577 -> 0.5962 -> 0.4808 -> 0.5385
- environmental-esg: 0.1698 -> 0.1132 -> 0.0943 -> 0.4906 -> 0.1321
- funds-asset-management: 0.8947 -> 0.8421 -> 0.9123 -> 0.8772 -> 0.9474
- healthcare-life-sciences: 0.8936 -> 0.8723 -> 0.8723 -> 0.8511 -> 0.8723
- immigration: 0.7788 -> 0.8068 -> 0.8196 -> 0.8673 -> 0.8184
- intellectual-property: 0.9185 -> 0.8953 -> 0.9253 -> 0.9185 -> 0.9338
- international-trade-sanctions: 0.9219 -> 0.8906 -> 0.8594 -> 0.9062 -> 0.9219
- litigation-dispute-resolution: 0.8919 -> 0.8877 -> 0.9073 -> 0.8889 -> 0.9105
- real-estate: 0.86 -> 0.8359 -> 0.8471 -> 0.839 -> 0.8713
- tax: 0.9286 -> 0.7857 -> 0.8571 -> 0.8571 -> 0.8214
- trusts-estates-private-client: 0.8399 -> 0.8315 -> 0.8315 -> 0.8449 -> 0.8181
