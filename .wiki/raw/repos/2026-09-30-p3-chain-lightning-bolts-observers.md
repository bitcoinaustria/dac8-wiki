---
title: "Lightning BOLTs: gossip, local HTLC knowledge and onion limits"
source: "https://github.com/lightning/bolts"
type: repos
ingested: 2026-09-30
fetched: 2026-09-30
revision: "1aadb719b4007c4cea0ba6e36b08c4fb53788dee"
content_format: markdown
extraction_tool: web-raw-text-and-git-ls-remote
extraction_status: selected-specification-sections
tags: [lightning, bolt2, bolt4, bolt7, gossip, htlc, onion-routing, observer-model]
summary: "Public funding/gossip, local HTLC state and onion routing expose different facts; no public complete Lightning payment history follows from a funding anchor."
quality: 4
credibility_score: 1
confidence: low
---

# Verified scope

HEAD was resolved by read-only `git ls-remote`. BOLT [2](https://raw.githubusercontent.com/lightning/bolts/1aadb719b4007c4cea0ba6e36b08c4fb53788dee/02-peer-protocol.md) and [4](https://raw.githubusercontent.com/lightning/bolts/1aadb719b4007c4cea0ba6e36b08c4fb53788dee/04-onion-routing.md) were fetched at that revision. BOLT [7](https://raw.githubusercontent.com/lightning/bolts/master/07-routing-gossip.md) was verified from contemporaneous master; its pinned URL failed. No full repository import or implementation test. Score: recognized protocol project +1; commit publication date unverified. Unique normative evidence.

## Source digest

**Locators:** BOLT 7, short_channel_id definition, announcement_signatures, channel_announcement and node_announcement; BOLT 2, open_channel, adding/fulfilling HTLCs; BOLT 4, overview and route blinding.

For announced channels, gossip ties node keys to a specific funding output; node announcements may publish connection addresses. Channel capacity is not the user's unilateral spendable balance. Unannounced channels omit this public gossip relationship, not the underlying on-chain funding transaction or participants' knowledge. HTLC messages convey a local amount, expiry and payment hash; fulfillment reveals a preimage. Onion routing conceals the full path from an ordinary intermediate hop, while the specification expressly excludes a blanket guarantee against traffic analysis. Shared hashes and additional observations can aid correlation but do not automatically establish payer, payee or purchase purpose. Channel peers, routing nodes, custodial wallets and a passive blockchain reader have different knowledge. Public funding alone is not a public ledger of every off-chain payment. This source does not measure current deanonymization success or deployed support for every negotiated feature.
