---
title: "Prism Data: CashScore — default risk, income and asset attributes from bank transaction data"
source: "https://www.prismdata.com/cashscore/"
type: articles
ingested: 2026-09-23
fetched: 2026-09-23
content_format: html
extraction_tool: web-fetch
tags: [vendor-documentation, cash-flow-underwriting, credit-scoring, transaction-data, prism-data, equifax]
summary: "Prism Data's CashScore ranks default risk and derives income, balance/asset, expense and behaviour attributes from multi-month transaction-level deposit data, with a vendor-stated average 30% KS lift over credit scores that is not independently validated."
---

# Prism Data: CashScore — default risk, income and asset attributes from bank transaction data

Inspected on 2026-09-23: the Prism Data CashScore product page (https://www.prismdata.com/cashscore/). Search results also surfaced an Equifax product sheet for the Equifax–Prism partnership (Prism CashScore & Attributes) and Prism's CashScore v4 announcement; these were not fetched and are not relied on here.

**Inputs and granularity.** CashScore takes transaction-level deposit-account data covering multiple months, sourced from open-banking aggregators or a lender's own core systems. The features it examines are described as "Income sources, Balances, Expenses, Bills, Behaviors, Counts, Patterns, Ratios" — i.e. both item-level categorisation and aggregate counts and ratios derived from it.

**Outputs.** The main output is a credit-risk score ranking the relative probability of default (described elsewhere by Equifax as a 1–999 FCRA-compliant score). Alongside it, Prism's Insights attribute library (vendor-stated as tens of thousands of trended attributes) describes income sources and consistency, balance trends and asset levels, expense and discretionary-spending patterns, and bill-payment behaviour; the company also offers income estimation and transaction categorisation via API.

**Vendor-stated claims and intended use.** The vendor states an average 30% predictive lift over traditional credit scores alone (KS statistic), 5–30% more approvals and 4–25% lower losses. These are vendor figures; the page does not cite an independent validation, and "lift" measures rank-ordering of default risk, not the accuracy of an income or asset estimate. Intended uses include consumer credit (auto, BNPL, cash advance, mortgage, personal loans, cards), SMB lending, tenant and utility screening, and portfolio risk management, with emphasis on thin-file ("credit invisible") consumers.

**What this establishes.** Transaction-derived features, including counts and ratios, are commercially used to estimate income and asset levels and to rank financial risk. It does not establish how accurate the income or asset estimates are for an individual, and the product relies on multi-month itemised deposit-account data (categories, timing, balances), so it does not show that annual per-asset totals and transaction counts, as in DAC8, would support comparable inferences.
