---
title: "Buterin: A maximally simple L1 privacy roadmap (2025)"
source: "https://ethereum-magicians.org/t/a-maximally-simple-l1-privacy-roadmap/23459"
type: articles
ingested: 2026-09-29
fetched: 2026-09-29
content_format: html
confidence: high
tags: [ethereum, privacy-roadmap, address-reuse, shielded-balance, rpc-privacy, design-intent, non-peer-reviewed]
summary: "Buterin's April 2025 roadmap proposes wallet-integrated shielded balances, 'one address per application' by default, and RPC and network privacy. It implicitly concedes that default Ethereum usage publicly links a user's activity across applications."
---

# A maximally simple L1 privacy roadmap

Vitalik Buterin (forum user `vbuterin`), Fellowship of Ethereum Magicians, posted 11 April 2025 (UTC). The first post was read through the forum's JSON endpoint. It is a proposal by a protocol developer, not peer reviewed and not an adopted protocol specification. For context, [ethereum.org's privacy roadmap page](https://ethereum.org/roadmap/privacy/) (last updated 24 August 2026) states that privacy on Ethereum "is moving from an optional add-on to a network-level default". It describes privacy pools as "only available via privacy apps, wallets, and layer 2 networks today".

**Content.** The post covers four forms of privacy: on-chain payments, "partial anonymization of onchain activity inside applications", reads to the chain (RPC calls), and network-level anonymisation. Its proposals include: integrating Railgun and Privacy Pools into wallets with a "shielded balance" and a default "send from shielded balance" option; moving toward "one address per application" by default, which Buterin calls "the most practical way to remove public links between all of your activity across different applications" at "significant convenience sacrifices"; making send-to-self private by default; TEE-based and later PIR-based RPC privacy; and multiple RPC nodes, optionally via a mixnet. The intended end state is still that "Activity inside of each individual application is public", with only the links between applications made private.

**Direction and transfer.** **Supports** the claim that default account-model use links activity across contexts. Needing "one address per application" as a future default implies the present default is cross-application address reuse. **Nuances** "no privacy at all": the roadmap relies on tools that already exist (Railgun, Privacy Pools) and aims only at partial privacy. RPC privacy corresponds to the network-metadata leak measured by Wang et al. (CCS 2025), already in the wiki. The roadmap does not show how much has been implemented; current wallet defaults were not verified.
