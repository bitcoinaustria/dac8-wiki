---
title: "Zcash protocol: shielded notes, nullifiers and viewing authority"
source: "https://zips.z.cash/protocol/protocol.pdf"
type: papers
ingested: 2026-09-30
fetched: 2026-09-30
version: "v2026.7.0-234-geaccf9 [NU6.2]"
page_count: 236
content_format: pdf
extraction_tool: web-pdf-text
extraction_status: selected-specification-sections-no-local-binary-hash
tags: [zcash, sapling, orchard, commitments, nullifiers, viewing-keys, observer-model]
summary: "Current fetched specification distinguishes hidden note contents from public verification data and incoming/full viewing keys from spending authority."
quality: 4
credibility_score: 2
confidence: medium
---

# Verified scope

**Locators, printed pages:** §§ 3.1–3.2.3, pp. 14–18; § 4.15, pp. 59–60; § 4.16, p. 60; § 4.20, pp. 70–73; § 5.6.3–5.6.4, pp. 119–123. Authors' protocol specification; score recent version +1, recognized authors/project +1. Not an independent privacy-implementation audit. The PDF version does not itself establish NU6.2 mainnet activation.

## Source digest

The examined Sapling/Orchard sections describe encrypted note contents, commitments and public nullifiers used to prevent double spending. Public verification does not require disclosure of each note's recipient or amount. Under the specified security requirement, nullifiers of initially unknown notes must not reveal their note correspondence beyond chance even to an incoming-viewing-key holder without the full viewing key. Incoming and full viewing authority are consequently different. Full viewing components can reveal spent-note associations and outgoing information unavailable to the ordinary public reader; they do not automatically provide independent spend authorization. Transparent inputs/outputs and public pool-balance fields remain separate visible components; a mixed transaction cannot be treated as wholly opaque. Disclosure of wallet keys, decrypted memos or provider records can change the information available without breaking the proof system. Historical Sprout attacks, or failures involving particular implementations, are not automatically results about Sapling/Orchard. No population deanonymization rate, Austrian provider key collection or complete wealth reconstruction is established.
