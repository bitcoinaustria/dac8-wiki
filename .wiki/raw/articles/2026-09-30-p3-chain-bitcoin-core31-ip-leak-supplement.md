---
title: "Bitcoin Core 31.0 private-broadcast IP disclosure and 31.1 correction"
source: "https://bitcoincore.org/en/2026/06/06/privatebroadcast-ip-leak/"
type: articles
published: 2026-06-06
ingested: 2026-09-30
fetched: 2026-09-30
version: "Affected: Core 31.0; documented fix: Core 31.1, released 2026-07-08"
content_format: html
extraction_tool: web-html-text
extraction_status: selective-source-digest
tags: [bitcoin, network-observer, broadcast, implementation-defect, ip-disclosure, version-boundary]
summary: "Official disclosure qualifies Core 31.0's release-note privacy promise; Core 31.1 documents a specific proxy-reconnection fix, not universal anonymity."
quality: 4
credibility_score: 1
confidence: low
---

# Verified scope

**Locators:** disclosure, “Affected users”, “Impact” and “How this can happen”; [Core 31.1 release notes](https://bitcoincore.org/en/releases/31.1/), “PrivateBroadcast” and P2P PRs #35032/#35410; [31.1 release announcement](https://bitcoincore.org/en/2026/07/08/release-31.1/). Supplement to [the immutable 31.0 digest](2026-09-30-p3-chain-bitcoin-core31-broadcast.md). Score: recent +1, recognized project +1, first-party account -1. The disclosure establishes implementation risk; it does not measure exploitation prevalence.

## Source digest

The official June 6 disclosure states that Core 31.0 private broadcasting can expose the transaction originator's IP to the receiving peer. Its stated affected scope requires the enabled feature, sendrawtransaction, reachable Tor, permitted direct IPv4/IPv6 outbound connections without an applicable proxy, and enabled v2 transport. After a failed v2 handshake, the retry can use v1 directly instead of the intended Tor proxy. This explicitly contradicts the release notes' IP-hiding promise. Ordinary wallet RPCs do not use this feature; absence of this defect in them is not proof of equivalent origin privacy. Onion/I2P peers and initial v1 connections are outside the disclosed defect. Core 31.1, released July 8, documents a fix for clearnet connections replacing the enabled privacy network. Treat the earlier raw's privacy claims as design goals, qualified by this disclosure. Neither release establishes universal anonymity against operator logs, traffic analysis, endpoint compromise or auxiliary identity data. No real-world exploitation rate or affected-user count is established here.
