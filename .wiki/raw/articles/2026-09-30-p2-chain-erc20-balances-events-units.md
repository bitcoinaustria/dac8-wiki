---
title: "ERC-20: balances, optional units and event limitations"
source: https://eips.ethereum.org/EIPS/eip-20
source_type: protocol-specification
source_url: https://eips.ethereum.org/EIPS/eip-20
type: articles
ingested: 2026-09-30
published: 2015-11-19
publication_date_status: "Created date; Final ERC specification"
retrieved: 2026-09-30
license: CC0
tags: [chain-data, ethereum, erc20, balances, events, units, evidence]
credibility_score: 1
credibility: low
credibility_reason: "Recognized Ethereum standard/authors +1; no recency point. Foundational token-interface standard exempted from the over-ten-year age penalty. Unique normative interface, not empirical prevalence evidence."
summary: "balanceOf returns a contract-defined integer; optional decimals determine display units. Events do not independently authenticate economic value."
related_sources: [https://docs.soliditylang.org/en/latest/abi-spec.html]
---

# Token observation

Created 2015-11-19, Final. Locators: Methods/NOTES, decimals, balanceOf, transfer/transferFrom, approve/allowance, Events/Transfer. name, symbol and decimals are optional; display quantity is raw quantity divided by 10**decimals when reliably known. Zero-value transfers must emit Transfer. Mint-from-zero Transfer is only SHOULD; no universal burn-event rule is specified. Callers must handle false returns. Approval is a spending authorization, not itself a transfer. Query token balances with eth_call against the correct chain, contract, account and historical block. The followed Solidity ABI specification, rendered as 0.8.38-develop, Events/Errors, distinguishes intrinsic emitter from arbitrary event parameters and warns that error data can be fabricated. Inference: an event-shaped log, familiar symbol or unsolicited token entry alone proves neither legitimate value nor the recipient's participation. Contract semantics and persistent state must be checked; this digest asserts no measured spam rate.
