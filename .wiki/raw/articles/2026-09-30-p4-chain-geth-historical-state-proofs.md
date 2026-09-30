---
title: "Geth archive mode: historical state versus historical proofs"
source_type: official-documentation
source_url: https://geth.ethereum.org/docs/fundamentals/archive
source: https://geth.ethereum.org/docs/fundamentals/archive
type: articles
ingested: 2026-09-30
published: 2026-02-24
retrieved: 2026-09-30
tags: [chain-data, ethereum, archive-node, state, proofs, retention]
credibility_score: 2
credibility: medium
credibility_reason: "Official client documentation +1 and current dated revision +1. Describes implementation capabilities; no empirical person-attribution result."
summary: "Historical balances and historical Merkle proofs require different archive configuration and version support."
---

# Historical capabilities

Official Geth page, last edited February 24, 2026; Path-Based Archive Node and Historical Trie Node Retention. Path-based archive introduced in v1.16.0 retains configurable state history; historical proof support is absent in v1.16.x and supported from v1.17.x when required trie-node history is retained. State indexing must finish before historical queries are available. An archive label alone therefore does not guarantee proof capability or complete queried history. This digest does not endorse changing a real node or generalise Geth's options to every client. A missing historical response is not proof that the historical balance was zero.
