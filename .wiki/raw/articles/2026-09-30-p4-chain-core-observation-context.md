---
title: "Bitcoin Core 30.0: block and unspent-output observation context"
source_type: official-documentation
source_url: https://bitcoincore.org/en/doc/30.0.0/rpc/blockchain/gettxout/
source: https://bitcoincore.org/en/doc/30.0.0/rpc/blockchain/gettxout/
type: articles
ingested: 2026-09-30
additional_urls:
  - https://bitcoincore.org/en/doc/30.0.0/rpc/blockchain/getblockheader/
published: 2025-10-02
retrieved: 2026-09-30
tags: [chain-data, bitcoin, rpc, evidence, reorg, mempool]
credibility_score: 2
credibility: medium
credibility_reason: "Official implementation documentation +1; release within three years +1. Normative interface evidence, not empirical attribution accuracy."
summary: "Versioned RPC fields distinguish confirmed chain state, block identity and optional mempool observations."
---

# Versioned observation context

Official RPC documentation exported from Bitcoin Core 30.0. `getblockheader`, Result: hash, height, confirmation count (-1 outside the main chain), time and median time. `gettxout`, Arguments and Result: txid plus output index; optional mempool inclusion can hide an output spent by a mempool transaction; result includes bestblock, confirmations, value, script and optional address. A null result is not independently a historical spending proof. Version 30.0 is deliberately specified, not represented as the current newest Core release. The published date denotes the release, not an asserted edit date of these individual pages.

Technical application: preserve snapshot and observation configuration before interpreting an output as confirmed and unspent. The methods provide no civil-ownership evidence.
