---
title: "Bitcoin whitepaper: abstract, transfer model and section 10 recheck"
source: "https://bitcoin.org/bitcoin.pdf"
type: articles
ingested: 2026-10-20
fetched: 2026-10-20
content_format: pdf
tags: [bitcoin, design-intent, electronic-cash, digital-signatures, privacy, non-peer-reviewed, supplement]
summary: "Supplement to the existing section 10 record: the abstract frames bitcoin as peer-to-peer electronic cash without a financial institution, section 2 defines transfer by owner signature, and the section 10 quotations were rechecked."
---

# Bitcoin whitepaper: abstract and transfer model

Satoshi Nakamoto, *Bitcoin: A Peer-to-Peer Electronic Cash System* (2008). bitcoin.org PDF retrieved 20 October 2026, SHA-256 `b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553`, nine pages. Supplements the [section 10 record](2026-09-29-acctmodel-bitcoin-whitepaper-privacy.md), which remains controlling for privacy.

## Exact quotations

Abstract, p. 1: "A purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution."

Section 2, p. 2: "We define an electronic coin as a chain of digital signatures. Each owner transfers the coin to the next by digitally signing a hash of the previous transaction and the public key of the next owner and adding these to the end of the coin."

## Section 10 recheck (p. 6)

The three quotations in the earlier record match the PDF verbatim: "a new key pair should be used for each transaction to keep them from being linked to a common owner"; "Some linking is still unavoidable with multi-input transactions, which necessarily reveal that their inputs were owned by the same owner"; "The risk is that if the owner of a key is revealed, linking could reveal other transactions that belonged to the same owner."

## Limits

A design document, not peer reviewed and not evidence of how bitcoin is used today. "Electronic cash" describes the design goal; it does not establish legal equivalence to cash, anonymity or a particular custody risk. The transfer model shows that control of signing keys suffices for a valid transfer; it says nothing about legal ownership, regulation of intermediaries or the security of self-custody.
