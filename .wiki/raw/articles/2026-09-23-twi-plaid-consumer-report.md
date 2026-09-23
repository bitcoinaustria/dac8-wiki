---
title: "Plaid: Consumer Report (Plaid Check) — income, average balances and default risk from bank transactions"
source: "https://plaid.com/docs/check/"
type: articles
ingested: 2026-09-23
fetched: 2026-09-23
content_format: html
extraction_tool: web-fetch
tags: [vendor-documentation, open-banking, income-verification, cash-flow-underwriting, transaction-data, plaid]
summary: "Plaid Check's Consumer Report derives modelled historical and forecast income, average balances and a 12-month default score from up to 24 months of item-level, categorised bank transactions; the docs state no accuracy figures."
---

# Plaid: Consumer Report (Plaid Check) — income, average balances and default risk from bank transactions

Inspected on 2026-09-23: the Plaid Docs product introduction (https://plaid.com/docs/check/) and the API reference (https://plaid.com/docs/api/products/check/).

**Inputs and granularity.** Consumer Report is produced by Plaid Check, which Plaid positions as a consumer reporting agency (FCRA context). Input is up to 24 months of consumer-permissioned bank account data from one or several linked accounts: account-holder identity, item-level transactions and categorised inflows and outflows, plus observed account balances. The analysis therefore starts from itemised transactions and balance observations, not from annual aggregates.

**Outputs.** The Base Report returns account-level attributes including `average_balance` over the report period, `average_monthly_balances` and `most_recent_thirty_day_average_balance`, along with aggregated cash-flow metrics (inflow and outflow totals and transaction counts over 30/60/90-day windows, NSF-fee counts). The Income Insights module returns "over a dozen" categorised income streams with employer name, frequency and predicted next payment date, and modelled fields such as `historical_average_monthly_income`, `historical_average_annual_income` (gross and net) and `forecasted_average_monthly_income`. Beta modules add LendScore (1–99, likelihood of default over the next 12 months, with reason codes), Cash Flow Insights (volatility across income and expenditure categories) and Network Insights (signals from rent, BNPL, cash-advance and earned-wage-access activity). Home-lending asset verification is offered for GSE submission.

**Accuracy and intended use.** The inspected documentation states no quantified accuracy, error rate or validation study for the income or balance estimates; income fields are described by the vendor as "modeled estimates". Intended uses are income and employment verification, debt-to-income calculation, credit decisioning (personal loans, BNPL, second-look underwriting), mortgage underwriting and post-decision servicing, all on a consumer-permissioned basis.

**What this establishes.** A mainstream commercial API infers income (historical and forecast) and balance levels from bank transaction data, and exposes counts and totals per time window as features, so the commercial practice exists. It does not establish independent accuracy of those estimates, and it does not show that comparable inferences are possible from annual per-asset totals and transaction counts alone: the product relies on item-level transactions with descriptions, dates and categories, and directly observes balances, none of which a DAC8 report contains.
