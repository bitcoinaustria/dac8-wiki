---
title: "Victor: Address clustering heuristics for Ethereum"
source: "https://www.ifca.ai/fc20/preproceedings/31.pdf"
type: papers
ingested: 2026-09-29
fetched: 2026-09-29
content_format: pdf
extraction_tool: pdftotext
confidence: high
tags: [ethereum, account-model, clustering, deposit-address, airdrop, peer-reviewed]
summary: "FC 2020: three account-model heuristics cluster 17.9% of active Ethereum EOAs through block 8,500,000. Exchange deposit-address reuse does most of the work. Bitcoin's multi-input heuristic does not apply, and error rates were not validated."
---

# Address clustering heuristics for Ethereum

Friedhelm Victor (TU Berlin), Financial Cryptography and Data Security 2020, LNCS 12059, pp. 617–633, [DOI 10.1007/978-3-030-51280-4_33](https://doi.org/10.1007/978-3-030-51280-4_33). The full text of the FC 2020 pre-proceedings PDF was inspected. It may differ from the Springer version of record, which was paywalled. Data: Ethereum up to block 8,500,000 (7 September 2019), roughly the first four years.

**Mechanism (pp. 1–2).** "Currently, there are no heuristics that can directly be applied to Ethereum's account balance model." Bitcoin's multi-input and change heuristics need several inputs and outputs, and a regular Ethereum transaction "has one source and one destination account address". The paper proposes three substitutes: (1) exchange deposit-address reuse, where addresses sending to the same per-customer exchange deposit address are clustered; (2) airdrop multi-participation, where tokens received on many addresses are collected into one; (3) ERC-20 self-authorisation through `approve`.

**Findings.** Deposit-address heuristic (s. 5.1, p. 8): 6,670,392 deposit addresses were linked to 186 exchange addresses. Of 3,261,091 addresses that used a deposit address, 1,446,715 (44.3%) shared a deposit address with another account, giving 333,107 multi-address entities. Airdrop heuristic (s. 5.2, p. 11): 675,512 addresses in 20,453 entities, with clusters capped at 1,000 addresses. Self-authorisation "only provided very few results". All heuristics combined (s. 6, p. 13): 10,561,143 addresses in 343,467 entities, mostly exchange entities. That is 9,562,153 EOAs, or 17.9% of active EOAs.

**Evidence class and limits.** Peer-reviewed measurement. There was no ground truth: "it is very difficult to assess the quality of the clustering heuristics" (s. 7, p. 15). The heuristics need parameters and external exchange labels. The author shows that an adversary could inject a false positive by forwarding funds to an exchange (p. 8). Implausibly large clusters were excluded by hand. The data are from 2019. The study is **nuancing** evidence. It shows that account-model linkage depends on user and service patterns, above all custodial deposit addresses, rather than following from the protocol, and that the strongest Bitcoin heuristic has no Ethereum equivalent. Most active EOAs (82.1%) were not clustered. DAC8 transfer: the deposit-address heuristic depends on the same exchange infrastructure whose customer records identify users. A provider record naming a deposit or withdrawal address is therefore a stronger anchor than any annual aggregate.
