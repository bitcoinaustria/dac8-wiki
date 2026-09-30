---
title: "Bitcoin Core: serialized UTXO records, contextual time and dust policy"
source: "https://github.com/bitcoin/bitcoin/blob/4b612c6bf8cfa319a9df130d4b3d0523fddb6579/src/primitives/transaction.h"
type: repos
ingested: 2026-09-30
fetched: 2026-09-30
revision: "4b612c6bf8cfa319a9df130d4b3d0523fddb6579"
revision_date: "2026-09-30T14:30:40Z"
sha256: "329c0f009edcda9dc2d3ff00e16066b1ff0f47d349a74c5cfb933aec4492c3fa"
content_format: cpp
extraction_tool: curl-pinned-source
extraction_status: selective-source-digest
tags: [bitcoin, utxo, serialization, outpoint, mempool, timestamp, dust]
summary: "The serialized transaction records spent outpoints and created values/scripts, not civil identities, input amounts, fees, or transaction execution timestamps."
quality: 4
credibility_score: 1
confidence: low
normative_authority: canonical-implementation-source
locators: "transaction.h lines 29-43, 62-68, 125, 140-153, 184-269, 297-306, 347-350; rawtransaction.cpp lines 84-108, 240-268; mempool.cpp lines 497, 572-589; policy.cpp lines 27-68, 158-160"
---

## Source digest

An input serializes a previous transaction identifier plus output index, scriptSig and sequence; its value must be joined from the referenced output. Outputs serialize integer values and locking scripts. Ordinary fees are derived from previous-input values minus output values. Coinbase instead has one special null-outpoint input. The transaction serialization contains no actual execution timestamp; lock-time fields impose eligibility conditions. RPC block time is contextual metadata; mempool time explicitly means local pool entry. Addresses are not mandatory serialized fields. The record establishes spend/create edges, not an allocation of each input's value to particular outputs or human ownership. Dust thresholds depend on output size and relay fee policy; they are not ownership classifications.

Auxiliary files at the same revision: [rawtransaction.cpp](https://github.com/bitcoin/bitcoin/blob/4b612c6bf8cfa319a9df130d4b3d0523fddb6579/src/rpc/rawtransaction.cpp), [mempool.cpp](https://github.com/bitcoin/bitcoin/blob/4b612c6bf8cfa319a9df130d4b3d0523fddb6579/src/rpc/mempool.cpp), [policy.cpp](https://github.com/bitcoin/bitcoin/blob/4b612c6bf8cfa319a9df130d4b3d0523fddb6579/src/policy/policy.cpp).

Mechanical score 1: recognized project +1; no empirical peer-review or publication-recency points. Unique implementation authority; this development snapshot does not establish deployed fleet versions or population error rates.
