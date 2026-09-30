---
title: "Geth built-in tracers: call frames versus committed state"
source: https://geth.ethereum.org/docs/developers/evm-tracing/built-in-tracers
source_type: official-documentation
source_url: https://geth.ethereum.org/docs/developers/evm-tracing/built-in-tracers
type: articles
ingested: 2026-09-30
published: 2024-12-16
publication_date_status: "Last-edited date, not original publication"
retrieved: 2026-09-30
tags: [chain-data, ethereum, geth, evm, traces, reverts, evidence]
credibility_score: 2
credibility: medium
credibility_reason: "Recognized public reference-client documentation +1 and dated revision within three years +1; no peer-reviewed person-attribution result. Describes Geth, not every indexer."
summary: "callTracer reconstructs a nested execution tree; prestateTracer can show changed state but does not produce a cryptographic state proof."
related_sources: [https://geth.ethereum.org/docs/developers/evm-tracing]
---

# Reconstructed execution

Last edited 2024-12-16. Locators: callTracer, its Hints/options; prestateTracer and diff mode. The official tracing introduction, last edited 2023-02-07, explains local re-execution with required historical state. callTracer returns nested CALL/STATICCALL/DELEGATECALL/CREATE frames with input, value, errors and optional logs. DELEGATECALL's target is executed code, not automatically a separate asset recipient. onlyTopCall omits subcalls. prestateTracer's diff mode reports changed account/storage fields; omitted fields can be unchanged. It explicitly does not generate cryptographic proofs. Explorer “internal transactions” are thus derived call records, not separately signed outer transactions. Attempted subcalls and their value fields must not be equated with persistent asset movement: revert scope and ancestor failures matter. Record client/version, tracer settings, canonical block and historical-state availability. This source does not measure any person's ownership or any authority's deployment.
