---
title: "Ethereum ZK rollups: public state data versus historical retrieval"
source: https://ethereum.org/developers/docs/scaling/zk-rollups/
source_url: https://ethereum.org/developers/docs/scaling/zk-rollups/
source_type: official-documentation
type: articles
ingested: 2026-09-30
retrieved: 2026-09-30
published: 2026-09-08
publication_date_status: "Page-last-update date, not original publication"
tags: [chain-data, ethereum, zk-rollup, data-availability, blobs, privacy, history]
credibility_score: 2
credibility: medium
credibility_reason: "Recognized noncommercial Ethereum documentation +1; verified page update within three years +1. General architecture, not a deployment audit or empirical privacy measurement."
summary: "Validity proofs do not inherently hide published rollup state data; availability is not indefinite historical retrievability."
related_sources: [https://ethereum.org/developers/docs/data-availability/, https://eips.ethereum.org/EIPS/eip-4844]
---

# Proof and data boundaries

ZK-rollups page updated 2026-09-08; Transactions and Data availability. Published compressed transactions or state differences are public and permit state reconstruction; validity proof alone is not privacy. Data-availability page updated 2026-02-23, Data availability vs. data retrievability, separates timely access from historical retrieval. EIP-4844 Security Considerations specifies approximately 18 days of minimum blob retention; this is not universal deletion by all holders. Inference: L1 proof/root/commitment alone supplies neither complete historical L2 data nor every execution detail. Required historical batches/state and chain-specific formats must remain retrievable. Short protocol retention establishes neither anonymity nor actual permanent loss: archives, providers or other observers may retain copies. No deployment completeness was tested.
