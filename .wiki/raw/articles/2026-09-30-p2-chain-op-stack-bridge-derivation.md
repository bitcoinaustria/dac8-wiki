---
title: "OP Stack: bridge representations, derivation and distinct finality concepts"
source: https://docs.optimism.io/app-developers/guides/bridging/standard-bridge
source_type: official-documentation
source_url: https://docs.optimism.io/app-developers/guides/bridging/standard-bridge
type: articles
ingested: 2026-09-30
retrieved: 2026-09-30
publication_date_status: "Undated live guide/specifications; no pinned release or verified deployment version"
tags: [chain-data, ethereum, optimism, layer2, bridge, accounting, finality, evidence]
credibility_score: 0
credibility: low
credibility_reason: "Recognized project/institution +1; first-party product documentation -1, non-stacked. No verified date or independent implementation measurement. Unique primary protocol/accounting reference; not evidence every deployment matches current specifications."
summary: "Lock/mint and burn/unlock connect distinct token contracts. L2 input finality and withdrawal/output finalization are separate concepts."
related_sources: [https://specs.optimism.io/protocol/overview.html, https://specs.optimism.io/protocol/bridges.html, https://specs.optimism.io/protocol/derivation.html]
---

# Cross-chain observation boundaries

Retrieved 2026-09-30. Guide locators: Design/Bridged tokens, Bridging native tokens, Bridging non-native tokens; opening warning on unsupported rebasing/fee-on-transfer tokens. Native tokens are locked while representations are minted; return burns representations and unlocks originals. Multiple representations are independent contracts, with escrow tracked by local/remote token pair. Inference: adding aggregate backing escrow to users' representation holdings double-counts the underlying position; contract balance does not allocate all backing to one user. Unsupported rebasing tokens can invalidate simple bridge accounting assumptions. Followed official derivation specification: Block derivation and Engine Queue distinguish unsafe sequencer head, safe L1-derived input and finalized L1-derived input. About reorgs Post-Merge expressly separates this input finality from optimistic withdrawal/output finalization. Reconstruction needs applicable chain configuration, L1 batch/deposit information and L2 state; a single L1 address balance is insufficient. Neither current rendered specifications nor a token ticker proves a deployed bridge's exact version, redeemability, valuation or economic owner.
