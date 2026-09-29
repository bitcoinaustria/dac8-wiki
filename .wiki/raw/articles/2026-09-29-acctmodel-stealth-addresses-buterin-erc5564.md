---
title: "Stealth addresses: Buterin (2023) and ERC-5564"
source: "https://vitalik.eth.limo/general/2023/01/20/stealth.html"
type: articles
ingested: 2026-09-29
fetched: 2026-09-29
content_format: html
confidence: high
tags: [ethereum, stealth-addresses, erc-5564, recipient-privacy, design-intent, non-peer-reviewed]
summary: "Ethereum's co-founder says that by default everything on a public chain is public and that using Ethereum apps makes much of one's life public. Stealth addresses, standardised as final ERC-5564, hide only the recipient, and funding their gas can recreate the link."
---

# Stealth addresses: Buterin (2023) and ERC-5564

Two primary developer documents, not peer reviewed but authoritative on design intent. (1) Vitalik Buterin, "An incomplete guide to stealth addresses", 20 January 2023. (2) [ERC-5564: Stealth Addresses](https://eips.ethereum.org/EIPS/eip-5564) by Toni Wahrstätter, Matt Solomon, Ben DiFrancesco and Vitalik Buterin, created 13 August 2022; the repository text was checked with `status: Final`.

**Problem statement (post, introduction).** "One of the largest remaining challenges in the Ethereum ecosystem is privacy. By default, anything that goes onto a public blockchain is public." This covers ENS names, POAPs, NFTs and soulbound tokens as well as payments; "using the entire suite of Ethereum applications involves making a significant portion of your life public for anyone to see and analyze."

**Scope and limits of the tool.** The post says "Hiding the fact that a transfer happened is impossible, especially if it's an NFT", but "hiding who is the recipient may be much more viable". It distinguishes this from Tornado Cash-style transfer hiding. Gas funding is an unsolved leak: a fresh stealth address "has 0 ETH in it", and "you can't send ETH into it from your main wallet, because then you're creating a publicly visible link." ERC-5564's Security Considerations likewise state that funding "represents a known issue that might breach privacy". The wallet that funds the stealth address "MUST NOT have any physical connection to the stealth address owner". Its `Announcement` event publishes `msg.sender` and optional metadata that can include the amount.

**Direction and transfer.** **Supports** the claim that account-based Ethereum is transparent by default and that linkage across applications is the norm. **Opposes** "no privacy at all" by showing that recipient-unlinkability tools are standardised, though partial. Adoption rates were not verified. DAC8 transfer: a withdrawal from a reporting provider to a stealth address still creates a provider-side record of that address.
