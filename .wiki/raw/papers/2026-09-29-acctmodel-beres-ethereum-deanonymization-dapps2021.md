---
title: "Béres et al.: Profiling and deanonymizing Ethereum users"
source: "https://arxiv.org/abs/2005.14051"
type: papers
ingested: 2026-09-29
fetched: 2026-09-29
content_format: pdf
extraction_tool: pdftotext
confidence: medium
tags: [ethereum, account-model, address-reuse, tornado-cash, ens, quasi-identifiers, peer-reviewed]
summary: "The authors argue the account model relies on address reuse at protocol level. Time-of-day, gas-price and graph profiles link same-user addresses better than chance but modestly. In early Tornado Cash, 5.3% to 17.1% of withdrawals per pool were linked by simple heuristics."
---

# Blockchain is Watching You: Profiling and Deanonymizing Ethereum Users

Ferenc Béres, István A. Seres, András A. Benczúr and Mikerah Quintyne-Collins. The arXiv v2 of 13 October 2020 was inspected (PDF pp. 1–19). The search-index record gives publication at IEEE DAPPS 2021, DOI 10.1109/DAPPS52256.2021.00013. The version of record was not checked.

**Mechanism claim (p. 1).** The authors argue that in an account model "the change remains at the sender account", so a later transaction "necessarily uses the same address again". The model "essentially relies on address-reuse on the protocol level", which "practically renders the account-based cryptocurrencies inferior to UTXO-based currencies from a privacy perspective". They add that users "tend to use only a handful of addresses". This is the authors' reasoning; the paper does not measure address counts per user.

**Profiling findings (s. 6, pp. 6–7).** Ground truth: 129 ENS names with exactly two addresses, collected from Twitter, with 3,321 candidate addresses. Time-of-day and gas-price profiles, plus graph embeddings (Diff2Vec and Role2Vec combined), linked same-user addresses "significantly better than random guessing". The best combination yields 1.6 bits of information, which reduces an address's anonymity set by a factor of about 3.03. That is real but modest leakage. Section 4 (p. 4) also observes that publicly revealed ENS names already expose sensitive activity such as gambling.

**Tornado Cash findings (s. 7, pp. 9–12; Table 2, p. 11).** Data run to 4 April 2020. Three heuristics were used: same deposit and withdrawal address, unique manually set gas price, and a direct transaction between deposit and withdrawal addresses. Linked withdrawals per pool: 218 of 1,272 (17.1%) at 0.1 ETH, 110 of 833 (13.2%) at 1 ETH, 60 of 738 (8.1%) at 10 ETH and 7 of 132 (5.3%) at 100 ETH. Most linked users withdrew within a day. For the 0.1 ETH pool, assuming the deposit fell within one day of the withdrawal reduces the average anonymity set "of 400 ... to almost 12" (p. 12). Section 8 (p. 12) shows that 98.1% of transactions leave the last nine digits of a balance unchanged, so a crafted dust amount can fingerprint an account.

**Evidence class and limits.** Peer-reviewed workshop/conference paper. Ground truth is small and self-constructed, and the Tornado ground truth comes from the heuristics themselves (p. 10). The data cover Tornado Cash's first four months. Section 9.4 (p. 15) says the same quasi-identifiers "also" apply to UTXO chains and that Bitcoin mixers likely provide less privacy than expected. Direction: **supports** the claim that the account model's structure worsens linkability. It **opposes** "no privacy at all": most early Tornado withdrawals were not linked, and behavioural profiling alone was weak. DAC8 transfer: these methods need an address or transaction anchor. DAC8 annual aggregates supply neither.
