# Redline Review Memorandum — Summary of Work

**Deliverable:** `output/redline-review-memorandum.docx` (validated against ECMA-376; ~7,300 words; 9 sections + 6 tables)

## What I did

I reviewed Husband's counsel's redlined postnuptial agreement against the original draft and four supporting documents (client intake memo, Linden & Fosse financial disclosure schedules, Strand practice valuation report, and Baxter's transmittal email), then prepared a detailed internal memorandum with change analysis and negotiation strategy for the January 27, 2025 four-way conference.

## Key findings driving the memo

**The transmittal email materially understates the changes.** Baxter flags only benign items (severability, notarization, a spelling fix, a recital, sunset, venue) while the redline contains six first-order adverse changes.

**Six critical (must-fix) issues:**
1. **Deletion of Wife's $1.2M premarital savings reimbursement** — the client's stated #1, "non-negotiable" objective; ~$600,000 transfer to Husband.
2. **Reversal of the commingling/transmutation rule** — protects Husband's $3.8M Inheritance; amplified by the fact the Inheritance brokerage sits at the same custodian (Northbridge) as the joint account.
3. **Unilateral modification by notice (Section 14.2)** — the most dangerous provision; contradicts the client's mutual-consent requirement.
4. **Voidability tightened + disclosure weakened** — $100K threshold, clear-and-convincing, intentional-concealment, 2-year SOL, "substantially" softening, deletion of ongoing duties; directly contradicts Objective #2 given Husband's $68K concealment history.
5. **"Earned Income" definition as a Trojan horse** — excludes bonuses/equity/RSUs and, read with the redefined Marital Property, risks reclassifying Husband's ~$90K bonus outside marital property.
6. **Coverture fraction on RSUs** — reduces Wife's share of post-dissolution-vesting tranches.

**Favorable items to preserve:** active/passive Practice appreciation (supported by Strand's 60/40 attribution) and the $200K maintenance waiver (likely eliminates Husband's maintenance). I recommend a fixed 60/40 Practice split to avoid future forensic battles.

**Factual discrepancies reconciled against the verified schedules:** both drafts misidentify the Inheritance brokerage custodian (Hartleigh/Tidewater vs. actual Northbridge 8837); the redline also gets the 403(b) custodian/value, pension value, 401(k) custodian, joint-account bank, Door County appraiser, credit-card balance, and account numbers wrong; the mother's death date conflicts across all three sources (Aug 12 / Sept 3 / "October 2024"); children's birth dates differ and need birth-certificate verification.

**Net effect:** a lopsided trade — certain ~$600K property loss plus open-ended Inheritance protection weighed against uncertain, smaller maintenance savings and speculative Practice protection. The memo recommends not accepting the redline as a baseline, with a prioritized disposition matrix, leverage points, sequencing, and counter-drafting instructions.

## Method

Built the .docx with python-docx (firm letterhead, memo header block, numbered sections, six formatted tables) and validated it with the docx skill's `validate.py` (passed). Confirmed rendering via pandoc and fixed a typo and a list-numbering continuation issue.