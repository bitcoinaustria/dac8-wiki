---
title: "Ethereum JSON-RPC: state, transactions, receipts and logs"
source: https://ethereum.org/developers/docs/apis/json-rpc/
source_type: official-documentation
source_url: https://ethereum.org/developers/docs/apis/json-rpc/
type: articles
ingested: 2026-09-30
retrieved: 2026-09-30
publication_date_status: "Undated live page; no verified revision date"
tags: [chain-data, ethereum, rpc, state, receipts, tokens, evidence]
credibility_score: 1
credibility: low
credibility_reason: "Recognized noncommercial public Ethereum documentation +1; no verified publication date, peer review or independent empirical corroboration. Unique primary interface reference; tier is not a measurement of protocol correctness."
summary: "State queries are block-specific; native balance, transaction intent, execution status and emitted logs are different observations."
related_sources: [https://ethereum.github.io/execution-apis/]
---

# Interface boundaries

Retrieved 2026-09-30. Locators: The block parameter; eth_getBalance; eth_call; eth_getTransactionByHash; eth_getTransactionReceipt; eth_getFilterChanges/log fields. getBalance returns native wei at a selected block, not all token balances. eth_call evaluates a message against selected state without publishing a transaction. Transaction value/input/nonce record submitted fields; receipts add actual gasUsed, effectiveGasPrice, success/failure and logs. Logs identify emitter, topics, data and possible removal after reorganisation. These interfaces do not establish human identity, economic ownership, token legitimacy or complete historical availability. An input selector is not a uniquely verified economic purpose. The page's illustrative transaction-type list is not a complete current catalogue: EIP-7702 separately defines type 0x04. Execution fee multiplication alone need not cover blob or L2 data fees. No live account was queried.
