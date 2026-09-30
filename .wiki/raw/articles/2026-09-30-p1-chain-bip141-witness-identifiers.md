---
title: "BIP 141: txid, wtxid and public witness disclosure"
source: "https://github.com/bitcoin/bips/blob/3a10b5b5f0a7586df8928d580a3009744ebb2079/bip-0141.mediawiki"
type: articles
ingested: 2026-09-30
fetched: 2026-09-30
assigned: 2015-12-21
authors: [Eric Lombrozo, Johnson Lau, Pieter Wuille]
version: "Status Deployed; repository revision 3a10b5b5f0a7586df8928d580a3009744ebb2079"
sha256: "d72409335872a32494f75e7547589abf4b3b23b6beebe6bc6999c7a84b135e2c"
content_format: mediawiki
extraction_tool: curl-pinned-source
extraction_status: selective-source-digest
tags: [bitcoin, segwit, txid, wtxid, witness, script]
summary: "SegWit separates witness-inclusive and traditional transaction hashes; witness separation does not encrypt transaction values, graph edges or disclosed spending conditions."
quality: 4
credibility_score: 1
confidence: low
normative_authority: canonical-protocol-specification
locators: "Transaction ID lines 39-59; Witness program lines 82-109; Transaction size lines 140-142"
---

## Source digest

The txid hashes traditional transaction serialization without witness; the wtxid hashes the witness-inclusive serialization. They coincide when there is no witness. Each input has a witness stack in the extended serialization. A native P2WPKH spend discloses signature and public key; a P2WSH spend discloses the executed witness script and its arguments. Witness separation addresses transaction malleability and resource accounting, not confidentiality of the blockchain graph or output amounts. Evidence pipelines must distinguish txid from wtxid rather than interchange superficially similar hash strings. The coinbase witness-root rule has a special zero-hash convention and must not be generalized to ordinary transaction identifiers. Virtual size is derived from transaction weight, not simply the byte length of full witness serialization.

Mechanical score 1: recognized authors +1; foundational specification exempted from the age penalty; no empirical peer-review points. Unique normative authority. Status “Deployed” is not an adoption measurement or identity-linkage benchmark.
