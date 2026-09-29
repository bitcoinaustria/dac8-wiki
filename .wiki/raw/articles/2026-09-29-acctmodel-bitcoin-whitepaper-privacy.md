---
title: "Nakamoto: Bitcoin whitepaper, section 10 (Privacy)"
source: "https://bitcoin.org/bitcoin.pdf"
type: articles
ingested: 2026-09-29
fetched: 2026-09-29
content_format: pdf
confidence: high
tags: [bitcoin, utxo, privacy, address-reuse, design-intent, non-peer-reviewed]
summary: "The 2008 Bitcoin whitepaper describes privacy as pseudonymous public keys on a public ledger, recommends a new key pair for each transaction, and warns that revealing one key owner can expose linked transactions."
---

# Bitcoin whitepaper, section 10 (Privacy)

Satoshi Nakamoto, *Bitcoin: A Peer-to-Peer Electronic Cash System* (2008). The bitcoin.org PDF was inspected; section 10 is on p. 6. This is a design document and was not peer reviewed. The Fifth Circuit cites it for the same proposition in *Van Loon v. Department of the Treasury* (2024), nn. 4–5.

Section 10 says the need to "announce all transactions publicly" rules out bank-style privacy. Instead, privacy "can still be maintained ... by keeping public keys anonymous", comparable to a stock-exchange tape that shows time and size without naming the parties. It then recommends: "As an additional firewall, a new key pair should be used for each transaction to keep them from being linked to a common owner." It acknowledges that "Some linking is still unavoidable with multi-input transactions" and that "if the owner of a key is revealed, linking could reveal other transactions that belonged to the same owner."

**Relevance and limits.** This is the baseline for the UTXO/account contrast. In the UTXO design, privacy depends on users taking fresh keys and avoiding linkage. The whitepaper itself concedes that pseudonymity is partial and that linkage can spread once a key owner is known. It therefore does not support a claim that UTXO chains are private. The Bitcoin clustering studies already in the wiki (Kappos et al. 2022, Möser/Narayanan 2022, Ghost Clusters 2025) measure how far that linkage goes in practice.
