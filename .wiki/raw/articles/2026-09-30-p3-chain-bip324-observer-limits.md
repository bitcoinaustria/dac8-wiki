---
title: "BIP 324: encrypted P2P transport and residual observation"
source: "https://bips.dev/324/"
type: articles
ingested: 2026-09-30
fetched: 2026-09-30
assigned: 2019-03-08
version: "1.0.2; status Deployed"
content_format: html
extraction_tool: web-html-text
extraction_status: selective-source-digest
tags: [bitcoin, bip324, transport-encryption, network-observer, traffic-analysis]
summary: "BIP 324 separates public consensus data from sensitive network metadata and distinguishes passive confidentiality from active-peer and traffic-analysis attacks."
quality: 4
credibility_score: 1
confidence: low
---

# Verified scope

**Locators:** header; “Motivation”; “Why encrypt without authentication?”; “Why have a pseudorandom bytestream when traffic analysis is still possible?”; “Goals”. Canonical text linked from the [Bitcoin BIPs repository](https://github.com/bitcoin/bips/blob/master/bip-0324.mediawiki). Score: recognized authors +1; assigned date is not a recent publication date. Unique normative specification; no population incidence measurement.

## Source digest

Bitcoin consensus data can be public while connection metadata remains privacy-sensitive. The specification contrasts plaintext v1 observations with v2 opportunistic transport encryption. Passive capture of a v2 byte stream without timing or fragmentation information must not reveal plaintext. This does not conceal a peer's network endpoint from its connection partner, authenticate that partner's expected identity, or prevent a malicious peer from receiving relayed transactions. The text expressly preserves active interception, downgrade or attacker-operated-node possibilities, and traffic analysis using lengths and timing. Consequently, passive chain access, passive network access and active peer participation are different capabilities. The global plaintext-v1 attacker in the motivation is not a demonstrated current attack rate for ordinary observers. Status “Deployed” does not prove every peer or connection uses v2. Transport confidentiality must not be equated with transaction-origin anonymity or hiding blockchain amounts and scripts.
