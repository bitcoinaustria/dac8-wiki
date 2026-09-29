---
title: "Wu et al.: USDT/USDC blacklisting and sanction-evasion races (preprint)"
source: "https://arxiv.org/abs/2603.27739"
type: papers
ingested: 2026-09-29
fetched: 2026-09-29
content_format: pdf
extraction_tool: pdftotext
confidence: medium
tags: [stablecoins, usdt, usdc, blacklisting, freeze, ethereum, account-model, preprint]
summary: "Preprint dataset of Ethereum USDT and USDC freezes from November 2017 to August 2025, covering more than $1.5 billion frozen. Some sanctioned addresses had been drained before the freeze executed. Shows address-level issuer control on account-model token ledgers."
---

# Ordering Power is Sanctioning Power: Sanction Evasion-MEV and the Limits of On-Chain Enforcement

Di Wu, Yuman Bai, Shoupeng Ren, Xinyu Zhang, Yiyue Cao, Xuechao Wang, Wu Wen and Jian Liu. arXiv 2603.27739, submitted 29 March 2026 and revised 3 May 2026. **Not peer reviewed.** The arXiv PDF was inspected (14 pp.).

**Findings.** The paper builds a dataset of contract-layer blacklist actions for Ethereum-based USDT and USDC from November 2017 to August 2025 (abstract; s. 1, p. 1). The balance frozen at the moment of enforcement was $1,411,842,932.22 for USDT and $108,250,166.32 for USDC, which the authors call lower bounds (s. 5.1, p. 7). After filtering, 146 USDT addresses (7.34%) and 23 USDC addresses (18.7%) held zero balance when the freeze executed, even though each had received stablecoin inflows before. The authors read this as suggesting targeted on-chain evasion. Only 26 USDT and 15 USDC addresses in the analysed set could be linked directly to OFAC SDN designations (s. 5.1, p. 7). The paper describes Ethereum's account model as one where "persistent state is associated with accounts and updated directly by transactions" (s. 2, p. 2).

**Evidence class and limits.** Preprint; labels come from a hierarchical fusion of sources (s. 4, p. 6), and the authors call the measurements conservative lower bounds. Direction: **supports** the claim that, on account-based token ledgers, balances and flows per address are publicly readable and centrally freezable, which adds an issuer-control dimension beyond visibility. It does not measure the identification of natural persons. The freeze mechanics are recorded in issuer terms (Circle, Tether); see the stablecoin issuer-terms digest.
