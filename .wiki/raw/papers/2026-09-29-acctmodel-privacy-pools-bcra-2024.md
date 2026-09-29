---
title: "Buterin et al.: Privacy Pools and regulatory compliance"
source: "https://doi.org/10.1016/j.bcra.2023.100176"
type: papers
ingested: 2026-09-29
fetched: 2026-09-29
content_format: html
extraction_status: "abstract and bibliographic metadata only; full text not accessible (SSRN and ScienceDirect blocked)"
confidence: medium
tags: [ethereum, privacy-pools, zero-knowledge, compliance, association-sets, peer-reviewed, abstract-only]
summary: "Proposal for smart-contract Privacy Pools in which users prove with zero-knowledge proofs that funds come from, or not from, defined association sets, without revealing their whole transaction graph. Design proposal, not a measurement of privacy in use."
---

# Blockchain privacy and regulatory compliance: Towards a practical equilibrium

Vitalik Buterin, Jacob Illum, Matthias Nadler, Fabian Schär and Ameen Soleimani, *Blockchain: Research and Applications* 5(1), 100176 (March 2024), DOI 10.1016/j.bcra.2023.100176. The SSRN working paper dated 6 September 2023 has [DOI 10.2139/ssrn.4563364](https://doi.org/10.2139/ssrn.4563364). Only the abstract and Crossref metadata were read; the full text was not accessible.

The abstract describes Privacy Pools as "a novel smart contract-based privacy-enhancing protocol". Users "publish a zero-knowledge proof, demonstrating that their funds (do not) originate from known (un-)lawful sources, without publicly revealing their entire transaction graph", by "proving membership in custom association sets". The authors present it as "a first step" towards proving compliance "without having to reveal their entire transaction history".

**Evidence class and limits.** Peer-reviewed journal article; one co-author designed Ethereum. It is a design and incentive analysis, not an empirical measurement of anonymity sets or linkage in deployment. No figures were extracted. Direction: **opposes** the claim that account-based chains are inherently incapable of privacy, since selective-disclosure privacy can be built at the application layer. It also shows that protocol developers treat the default ledger as exposing the "entire transaction graph". Deployment status and uptake were not verified here. The 2025 Buterin roadmap names Privacy Pools and Railgun as tools to integrate into wallets.
