---
title: "ERC-4626: share balance, asset estimate and redemption limits"
source: https://eips.ethereum.org/EIPS/eip-4626
source_url: https://eips.ethereum.org/EIPS/eip-4626
source_type: protocol-specification
type: articles
ingested: 2026-09-30
retrieved: 2026-09-30
published: 2021-12-22
publication_date_status: "Created date; Final ERC specification"
license: CC0
tags: [chain-data, ethereum, erc4626, vault, shares, valuation, liquidity]
credibility_score: 1
credibility: low
credibility_reason: "Recognized Ethereum specification +1; no recency or peer-review point. Unique normative interface reference, not measured solvency or actual deployment compliance."
summary: "Vault shares, ideal asset conversion, fee-adjusted preview and redemption limits are different quantities."
---

# Distinct observations

Created 2021-12-22, Final. Locators: Specification; convertToAssets; maxRedeem; previewRedeem; redeem; Security Considerations. balanceOf counts shares, not underlying tokens or native ETH. convertToAssets excludes fees/slippage and describes an ideal, caller-independent conversion. previewRedeem includes withdrawal fees but ignores redemption limits. maxRedeem accounts for owner/global limits, must be zero when redemption is disabled, and may conservatively underestimate. redeem can require prior requests and must revert if requested shares cannot be redeemed. Inference: positive shares or conversion estimates do not prove immediate liquidity; zero limits do not prove zero economic value. Historical code, block, units, authorization and actual limits require verification; interface conformance does not establish solvency.
