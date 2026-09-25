---
title: "Aiello, Baker, Balyuk, Di Maggio, Johnson & Kotter: Imputing household crypto wealth from bank transfers to exchanges"
source: "https://www.nber.org/papers/w31445"
type: papers
ingested: 2026-09-23
fetched: 2026-09-23
content_format: pdf
extraction_tool: web-fetch
tags: [working-paper, crypto-wealth, wealth-imputation, bank-transactions, exchange-flows, measurement-error, not-peer-reviewed]
summary: "An NBER working paper (not peer-reviewed) imputes US households' crypto portfolio values by rolling dated bank deposits to and withdrawals from exchanges forward at daily BTC/ETH prices; this shows that flow data can be converted into wealth estimates, but the imputation depends on per-transaction dates, is never validated against actual holdings, and assumes zero starting wealth."
---

# The Effects of Cryptocurrency Wealth on Household Consumption and Investment

Darren Aiello, Scott R. Baker, Tetyana Balyuk, Marco Di Maggio, Mark J. Johnson, Jason D. Kotter. NBER Working Paper No. 31445, July 2023 (revised October 2023). The cover states that NBER working papers "have not been peer-reviewed". Inspected: the full NBER PDF, in particular Sections 2.1–2.3 (data, validation, crypto identification and wealth imputation, Eq. 1, Table 1 summary statistics) and the MPC estimation notes.

**Data and granularity.** The data come from a financial-aggregation firm (Yodlee): bank, debit-card and credit-card transactions of more than 60 million US users, 2010–2022, used from 2014 onward. The household analysis uses 95,965 users drawn from the top-quality decile of the data, and the county analysis uses about 6 million households. The input is **item-level**. Each transaction has an exact date, amount, text description and category. Crypto users are identified by string-matching transfers to and from exchanges (about 90% of dollar flows go to Coinbase). Coin-level holdings are not observed.

**Wealth imputation.** Crypto wealth is rebuilt recursively (Eq. 1, p. 11). Each day, the previous day's value is multiplied by the return of a household-specific Bitcoin/Ether index, and that day's net deposits are added. The assumptions are: every deposit buys BTC/ETH on the same day at market-cap weights; withdrawals are pro-rata sales; initial crypto wealth is zero; and off-exchange (self-custody, mined) holdings are not captured. The authors say this necessarily underestimates retail crypto wealth. Result: a mean end-of-sample portfolio of about $21,797, a median of $1,024 and a 75th percentile of $6,225. **No accuracy figure exists** because the imputation is never compared with actual account balances. Validation is limited to showing that aggregate spending tracks Census retail sales (correlation ≈ 0.90) and that the wealth distribution resembles SCF equity holdings. The authors note that the imputation is more accurate in 2016–2017, when Bitcoin dominated, than later. They winsorise crypto gains "to alleviate concerns over measurement error in crypto wealth".

**Use and limits.** The imputed wealth is used in regressions (the marginal propensity to consume out of crypto gains, and county house prices), where individual errors average out. Individual portfolio values are not the object of the analysis.

**Relevance to annual aggregate reports.** This is the closest empirical analogue to inferring crypto holdings from fiat purchase and sale flows, and it shows that researchers treat such flow-based estimates as usable proxies for statistical analysis. It does **not** establish statistically reliable *individual* balance estimation. No validation against true holdings is reported. The method needs the **date** of each flow to price it, whereas DAC8 reports give annual totals in EUR and units without dates. It also rests on strong assumptions (zero starting wealth, no off-exchange holdings, a fixed coin basket). Annual EUR totals together with total units per asset would remove the need for price-timing assumptions for the reported units, but not the unobserved opening balance or off-platform holdings. Status: working paper, not peer-reviewed.
