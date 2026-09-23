---
title: "Equifax (IXI): WealthComplete Premier — household investable-asset estimates from pooled institutional asset data"
source: "https://assets.equifax.com/marketing/US/assets/wealth-complete-ps.pdf"
type: articles
ingested: 2026-09-23
fetched: 2026-09-23
content_format: pdf
extraction_tool: web-fetch
tags: [vendor-documentation, wealth-estimation, equifax-ixi, marketing-data, share-of-wallet, household-assets]
summary: "Equifax WealthComplete Premier estimates each US household's total liquid financial assets and product-level holdings by modelling from anonymised, directly measured asset balances pooled by IXI member institutions; no error metrics are published and the input is balances, not transactions."
---

# Equifax (IXI): WealthComplete Premier — household investable-asset estimates from pooled institutional asset data

Inspected on 2026-09-23: the Equifax WealthComplete Premier product sheet (PDF, text extracted locally with pdftotext), found via the Equifax product page https://www.equifax.com/business/product/wealthcomplete-premier/.

**Inputs and granularity.** The foundation is Equifax's "direct-measured Financial Assets Database": anonymous asset data contributed by IXI Network member financial institutions, stated as over $30 trillion of invested retail assets, about 45% of US consumer invested assets. Equifax then applies proprietary modelling to "project" this measured data to all US households (about $75.3 trillion in liquid financial assets). The sheet does not disclose model features or the geographic level at which contributed data is pooled. It states that the Premier model uses no protected-class variables, no demographics such as age, and no income. The inputs are asset balances held at institutions, not transaction flows.

**Outputs.** For "nearly every U.S. household", continuous dollar estimates of Total Assets (deposits plus investments, capped at $25 million+), Total Investments split into stocks, bonds, mutual funds, annuities and other, and Total Deposits split into six deposit-account types. Retirement plans such as 401(k), business accounts, life insurance and home value are excluded.

**Vendor-stated claims and intended use.** Equifax claims "superior performance" over survey-based wealth segmentations (which it says may rest on about 1% of households) and "zero share-of-wallet failure", without publishing error metrics or an independent validation. The product is sold exclusively to IXI members for marketing: appending estimated total assets to client and prospect files, computing share of wallet, finding "high-asset prospects" and prioritising call-centre contacts.

**What this establishes.** Commercial household-level wealth estimation for marketing is an established product, and it is built by extrapolating from pooled, aggregated financial data rather than from a person's own complete records. It does not establish individual-level accuracy (no error bands are published), and it is not a transaction-based inference: its primary signal is measured balances from a large share of the market, which is a different and stronger input than annual transaction totals and counts per crypto-asset.
