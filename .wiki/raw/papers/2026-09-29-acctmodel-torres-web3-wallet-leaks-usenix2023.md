---
title: "Torres, Willi and Shinde: Web3 wallet-address leakage"
source: "https://www.usenix.org/system/files/usenixsecurity23-torres.pdf"
type: papers
ingested: 2026-09-29
fetched: 2026-09-29
content_format: pdf
extraction_tool: pdftotext
confidence: high
tags: [ethereum, account-model, wallets, web-tracking, address-leakage, balance-fingerprint, peer-reviewed]
summary: "USENIX Security 2023: 211 DApps and 13 of 100 wallets leaked users' Ethereum addresses to third parties. Because an account address is a stable identifier and its balance has high resolution, web trackers can tie off-chain browsing data to on-chain accounts."
---

# Is Your Wallet Snitching On You? An Analysis on the Privacy Implications of Web3

Christof Ferreira Torres, Fiona Willi and Shweta Shinde (ETH Zurich), 32nd USENIX Security Symposium, 2023. The open-access proceedings PDF was inspected (proceedings pp. 769–786).

**Account-model framing (s. 2.1–2.3, p. 770–771).** The authors compare Ethereum to bank accounts: addresses "act as a unique identifier that can be used to link transactions back to users". "All transactions from and to a given account can easily be linked to a user's account address, but not necessarily to its real-world identity." Third-party scripts in a connected DApp can read the address and balance and also see the user's IP address.

**Findings (s. 1, p. 770; s. 4).** Of the top 100K websites, 1,325 probe for installed wallets. Of the DApps analysed, 211 leak the user's wallet address to third parties such as RPC providers and analytics platforms. The denominator is 616 in the abstract and 1,572 in the results paragraph. Of 100 wallets, 13 leak the address, and wallets involve more than 137 unique third parties. The best single ad-blocking list blocked 39% of the relevant third parties; all lists combined blocked 51% (s. 5.2, p. 780). Section 5.2 also says a proxy-address countermeasure fails because the real balance, with 256-bit resolution, can be matched on-chain: "the likelihood that two users having the exact same balance is very low."

**Evidence class and limits.** Peer-reviewed measurement, and the authors treat the counts as a lower bound (s. 5.1). It measures leakage of address to third party and does not test identification of named persons. The 2022–2023 crawl may not match current wallet behaviour. Direction: **supports** the claim that an account-model address works as a persistent cross-context identifier and that a balance can itself act as a quasi-identifier. It shows mechanisms by which non-tax actors can create an identity-to-address anchor. DAC8 transfer: DAC8 does not create these web anchors. If one exists, a single linked account reveals more than a single UTXO address used once.
