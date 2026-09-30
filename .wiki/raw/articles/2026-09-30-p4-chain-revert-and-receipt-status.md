---
title: "EIP-140 and EIP-658: execution revert scope and receipt status"
source: https://eips.ethereum.org/EIPS/eip-140
additional_sources: [https://eips.ethereum.org/EIPS/eip-658]
type: articles
ingested: 2026-09-30
retrieved: 2026-09-30
created_dates: [2017-02-06, 2017-06-30]
version: "Final specifications; respective Created dates, not implementation audit"
license: CC0
tags: [chain-data, ethereum, revert, receipts, execution, evidence]
credibility_score: 1
confidence: low
credibility_reason: "Recognized specification authors +1; no recency/peer-review points. Unique normative scope and status definitions, not empirical attribution."
summary: "Execution rollback and top-level receipt status are distinct from broader transaction pre-processing such as EIP-7702 authorization."
---

# Execution boundary

EIP-140 Specification defines REVERT's rollback of execution state changes and distinguishes its remaining-gas behaviour from out-of-gas. Reverted LOGs are discarded. EIP-658 Specification defines receipt status 0/1 for top-level failure/success after Byzantium. A successful parent may handle a failed subcall; top-level success is therefore not a guarantee every attempted subcall persisted. Modern preprocessing requires separate consideration: EIP-7702 expressly preserves processed delegations despite later execution failure. No EVM or live account was tested in this source work.
