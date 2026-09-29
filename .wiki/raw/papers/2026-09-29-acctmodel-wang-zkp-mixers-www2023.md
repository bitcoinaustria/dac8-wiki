---
title: "Wang et al.: ZKP mixers improve and worsen user privacy"
source: "https://arxiv.org/abs/2201.09035"
type: papers
ingested: 2026-09-29
fetched: 2026-09-29
content_format: pdf
extraction_tool: pdftotext
confidence: high
tags: [ethereum, bsc, tornado-cash, mixers, anonymity-set, heuristics, peer-reviewed]
summary: "WWW 2023: five on-chain heuristics cut Tornado Cash's advertised anonymity sets on Ethereum by 27.34% on average (46.02% for a BSC mixer). The authors conclude that most users can still stay anonymous. Validation against weak side-channel ground truth gives an average F1 of 0.55."
---

# On How Zero-Knowledge Proof Blockchain Mixers Improve, and Worsen User Privacy

Zhipeng Wang, Stefanos Chaliasos, Kaihua Qin, Liyi Zhou, Lifeng Gao, Pascal Berrang, Benjamin Livshits and Arthur Gervais. ACM Web Conference 2023 (WWW '23), [DOI 10.1145/3543507.3583217](https://doi.org/10.1145/3543507.3583217). The arXiv v2 of 6 March 2023 was inspected (PDF pp. 1–14). It states acceptance at WWW '23 (p. 1). Data: Tornado Cash (TC) on Ethereum and Typhoon.Network (TN) on BSC, before 1 October 2022.

**Findings.** TC reported an anonymity set of 51,286 for its 1 ETH pool on 8 August 2022, "simply derived from the count of equal user deposits" (p. 1). Five heuristics were applied: address reuse; a deposit address paying the withdrawal fee; a direct transfer between deposit and withdrawal addresses; intermediary deposit addresses; and matching multi-pool deposit and withdrawal amounts. Combined, they reduce the observed anonymity set on average by 27.34% for TC and 46.02% for TN. That raises an adversary's chance of linking a withdrawal to the correct depositor by 37.63% for TC and 85.26% for TN (s. 7.1.6, pp. 8–9, Table 4). The per-pool TC reductions range from 24.98% (1 ETH) to 30.68% (0.1 ETH). Heuristics 2–5 link 18,705 TC address pairs into 8,164 clusters. Separately, TC daily deposits fell by more than 80% (83% in the contributions and conclusion) after the OFAC sanctions.

**Validation and limits (s. 7.2, pp. 9–11).** The authors call their heuristics "best-effort methods" that "may yield false positives and negatives". Against candidate ground truth drawn from airdrop and ENS side channels, the average F1 is 0.55. The strongest heuristic (direct transfer) has precision of 0.37 to 0.40 and recall of 0.94 to 1.00 (Table 5). Under a Debank-following assumption, 34 of 150 linked pairs (23%) would be false positives. Section 8 (p. 11): "although users may reveal their transaction history because they are not familiar with the workflow of mixers ... most of the users can still stay anonymous."

**Direction and transfer.** Peer-reviewed measurement. It **opposes** "no privacy at all" on account-based chains: a widely used ZKP mixer left most users unlinked under these heuristics. It **nuances** the claim by showing that advertised anonymity sets overstate privacy and that careless use collapses it. The US designation of Tornado Cash was later lifted; see the Tornado Cash legal-status digest. EU AMLR Article 79, which applies from 10 July 2027, addresses obliged entities' handling of anonymisation tools; see the existing AMLR digest. For DAC8 purposes, the paper measures linkage between on-chain addresses. It does not measure identification from tax reports.
