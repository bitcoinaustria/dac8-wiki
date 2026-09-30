---
title: "Bitcoin Core 31.0: origin privacy and private broadcasting"
source: "https://bitcoincore.org/en/releases/31.0/"
type: articles
ingested: 2026-09-30
fetched: 2026-09-30
version: "Bitcoin Core 31.0"
content_format: html
extraction_tool: web-html-text
extraction_status: selective-source-digest
tags: [bitcoin, network-observer, broadcast, tor, i2p, version-boundary]
summary: "Core 31.0 documents optional per-transaction Tor/I2P broadcasting for sendrawtransaction; origin exposure depends on version, configuration and observer capability."
quality: 4
credibility_score: 1
confidence: low
---

# Verified scope

**Locator:** release notes, “P2P and network changes”, first item; “Updated settings”, privatebroadcast item. Publication day is not stated on this page. Score: recent release +1, recognized project +1, first-party implementation account -1. Unique implemented-version evidence, not an independent anonymity measurement.

## Source digest

The release contrasts normal local transaction relay to connected peers with an optional mechanism for the `sendrawtransaction` RPC using Tor/I2P and a separate connection for each broadcast transaction. The stated goals are withholding the originator's IP from recipients and preventing connection-based linkage of otherwise unrelated broadcasts. The option is not evidence that every Core wallet operation, RPC client or third-party wallet uses this path. An external wallet's submission to a remote RPC operator remains a separate observation surface. A connected peer may receive a relayed transaction rather than one created by that peer; a blockchain record itself contains no originating IP. “First seen” therefore needs network coverage, timing and deployment assumptions. These notes do not establish resistance to a global observer, endpoint compromise, operator logs or identity linkage from other data. Do not transfer results of older network-origin attacks to all Core 31.0 configurations.
