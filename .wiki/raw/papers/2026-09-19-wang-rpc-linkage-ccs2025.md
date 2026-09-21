---
title: "Wang et al.: RPC traffic and public-ledger linkage"
source: "https://arxiv.org/pdf/2508.21440"
type: papers
ingested: 2026-09-19
fetched: 2026-09-19
content_format: pdf
page_count: 20
extraction_tool: "web PDF and HTML text extraction"
extraction_status: "selective full-text digest"
tags: [peer-reviewed, blockchain, linkage, timing, network-metadata, evidence-limits]
summary: "CCS 2025 research links observed RPC network traffic to blockchain pseudonyms in controlled experiments; precise timing and network visibility prevent transfer of its success rates to DAC8 annual aggregates."
---

# RPC traffic and public-ledger linkage

Shan Wang et al., *Time Tells All: Deanonymization of Blockchain RPC Users with Zero Transaction Fee*, ACM CCS 2025, pp. 3490–3504, [DOI 10.1145/3719027.3765082](https://doi.org/10.1145/3719027.3765082). The [university publication record](https://research.polyu.edu.hk/en/publications/time-tells-all-deanonymization-of-blockchain-rpc-users-with-zero-/) confirms peer review and venue.

The verified research text is the extended arXiv version 1 of 29 August 2025, not a checked copy of the final proceedings version. Locators refer to its PDF pages; [HTML equivalent](https://arxiv.org/html/2508.21440v1). No local binary hash is available.

## Findings and limits

- **Sections 8–9, PDF pp. 11–13:** 90 emulated users across three regions generated 1,099 Ethereum-testnet transactions; 100 further transactions tested Ethereum mainnet. The experiments used controlled devices and software routers.
- Reported experimental success reached 95.33% on Ethereum mainnet and 96.80% on its testnet under selected conditions. Bitcoin and Solana mainnet were not experimentally tested.
- Required inputs include observed network traffic and precise temporal linkage to ledger activity. Network visibility, dynamic IPs, shared IPs and timing variation constrain transfer.
- The endpoint is an IP-to-blockchain-pseudonym link, not proof of a person's identity, ownership or current wealth. These are experimental success rates, not population incidence or physical-attack probabilities.

No actual assaults, tax-report fields or annual DAC8 aggregate tuples were tested. The study supports a specific additional-data mechanism, not annual-aggregate deanonymisation.
