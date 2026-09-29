---
title: "IMF WP/25/141 (Reuter): geolocating self-custodial wallets from time-of-day activity and on-chain behaviour"
source: "https://www.imf.org/-/media/Files/Publications/WP/2025/English/wpiea2025141-source-pdf.ashx"
type: papers
ingested: 2026-09-29
fetched: 2026-09-29
content_format: pdf
extraction_tool: pdftotext
confidence: medium
tags: [imf, working-paper, crypto, stablecoins, geolocation, time-of-day, behavioural-profiling, ens, llm-labelling, not-peer-reviewed]
summary: "An IMF working paper trains a model on on-chain features, including hour-of-day activity, to assign self-custodial wallets to one of five world regions (65% accuracy vs 20% chance; 79% for China vs rest of Asia-Pacific); timestamps visibly shift with daylight saving time, but resolution is regional, not personal."
---

# Decrypting Crypto: How to Estimate International Stablecoin Flows

Marco Reuter, IMF Working Paper WP/25/141, July 2025 (Research Department). Working papers "describe research in progress" and do not necessarily represent IMF views. The full PDF was read.

**Method.** Training labels come from two sources. About 6 million ENS domain names were classified by region by a large language model, and wallets interacting with regionally focused centralised exchanges were labelled too. Together these labelled 346,201 wallets; 260,655 (about 4.4% of names) came from ENS. The labels were checked against hour-of-day activity profiles. With timestamps shifted to a regional time zone (e.g., UTC−6 North America, UTC+8 Asia-Pacific), activity peaks in local daytime. The North American profile shifts by roughly one hour between daylight-saving and standard time; Asia-Pacific shows no such shift (section 5.1, Fig. 4). A gradient-boosted tree model then used time-of-day features, exchange interactions and token and contract usage, applied to wallets with at least 50 transactions.

**Accuracy and limits.** Overall accuracy across five regions is 65%, against 20% for random guessing. A separate China vs Asia-Pacific model reaches 79%. The author lists several limitations. Users may pick names tied to another culture. The LLM may default German names to Germany rather than Austria or Switzerland. The key assumption is that labelled and unlabelled wallets behave alike. The paper also contrasts its method with Chainalysis' commercial geography data, which allocates exchange flows by web-traffic shares. It finds that assumption violated for China, where Binance is reachable only via VPN.

**Evidence class and DAC8 transfer.** This is an official-institution working paper, not peer-reviewed, and the data cover Ethereum-family/stablecoin wallets. It shows that timestamps and behaviour on public ledgers support location inference by an institutional analyst. The inference is coarse, though: continental regions at 65% accuracy, not a person's country or city. It is adverse to claims that timing analysis pinpoints individuals' locations. DAC8 reports carry no timestamps. A provider's records combined with on-chain timestamps would, however, allow such time-of-day profiling of identified customers.
