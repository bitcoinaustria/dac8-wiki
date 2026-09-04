---
title: "Resurrecting Address Clustering in Bitcoin"
source: "https://arxiv.org/abs/2107.05749"
type: papers
ingested: 2026-09-04
fetched: 2026-09-04
content_format: html
tags: [bitcoin, clustering, heuristics, false-positive, coinjoin, payjoin, peer-reviewed]
summary: "Peer-reviewed analysis showing that Bitcoin address-clustering effectiveness varies over time and can produce severe errors when heuristics are naively combined."
---

# Resurrecting Address Clustering in Bitcoin

Möser and Narayanan, Financial Cryptography 2022, examine change-address and multi-input clustering. They show that heuristic performance changes with protocol and wallet-use patterns, that CoinJoin and PayJoin can disrupt common assumptions, and that naive cluster combination can create very large erroneous clusters.

The paper also improves clustering performance. It therefore does not prove that attribution is impossible. Its proper use is to require method disclosure, current validation, ground truth and false-positive analysis before an attributed cluster is treated as a fact.
