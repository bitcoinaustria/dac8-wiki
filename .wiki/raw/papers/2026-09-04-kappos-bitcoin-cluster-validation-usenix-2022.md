---
title: "How to Peel a Million: Validating and Expanding Bitcoin Clusters"
source: "https://www.usenix.org/conference/usenixsecurity22/presentation/kappos"
type: papers
ingested: 2026-09-04
fetched: 2026-09-04
content_format: html
tags: [bitcoin, clustering, attribution, ground-truth, false-positive, peer-reviewed]
summary: "Peer-reviewed validation of Bitcoin clustering and peel-chain methods, with explicit ground-truth, exchange-ledger and generalisation limits."
---

# How to Peel a Million

Kappos and co-authors, USENIX Security 2022, develop and validate methods for expanding Bitcoin clusters using a ground-truth dataset. The work confirms that public transaction structure can support longitudinal flow analysis after an address or entity seed is available.

The authors also identify material limits: private exchange ledgers are not visible on-chain, wallet behaviour can defeat heuristics, ground truth is limited and heuristic output should not be treated as definitive proof. The paper therefore supports both the feasibility of linkage and the need to disclose assumptions, error rates and validation.
