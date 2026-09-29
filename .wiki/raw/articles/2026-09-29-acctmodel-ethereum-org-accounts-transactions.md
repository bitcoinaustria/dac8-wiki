---
title: "ethereum.org: account and transaction data model"
source: "https://ethereum.org/en/developers/docs/accounts/"
type: articles
ingested: 2026-09-29
fetched: 2026-09-29
content_format: html
confidence: high
tags: [ethereum, account-model, nonce, balance, protocol-documentation, official-docs]
summary: "Official Ethereum developer documentation: an account holds a balance and a nonce, and each transaction names one sender and one recipient address with a sequential nonce. The protocol records a persistent per-address state, not discrete outputs."
---

# ethereum.org: account and transaction data model

Official developer documentation maintained by the Ethereum community on ethereum.org. Two pages were checked: [Accounts](https://ethereum.org/en/developers/docs/accounts/) (last updated 6 August 2026 per page metadata) and [Transactions](https://ethereum.org/en/developers/docs/transactions/) (last updated 24 September 2026). This is protocol documentation, not peer-reviewed privacy research. Neither page discusses privacy or compares Ethereum with Bitcoin's UTXO model.

**Accounts page.** Ethereum has externally-owned accounts, controlled by private keys, and contract accounts, controlled by code. Every account has four fields: `nonce` ("A counter that indicates the number of transactions sent from an externally-owned account or the number of contracts created by a contract account"), `balance` ("The number of wei owned by this address"), `codeHash` and `storageRoot`. The nonce prevents replay attacks.

**Transactions page.** A transaction is "an action initiated by an externally-owned account". Its fields include `from` (the sender's address), `to` (the receiving address), `signature`, `nonce` ("a sequentially incrementing counter which indicates the transaction number from the account"), `value`, `input data`, `gasLimit`, `maxPriorityFeePerGas` and `maxFeePerGas`.

**Relevance and limits.** The documentation shows how the protocol works. Value sits as a mutable balance on a persistent address, and each outgoing transaction from that address carries the next nonce. Once an address is linked to a person, its current native balance and the ordered sequence of its sent transactions can therefore be read directly from chain state. Token balances sit in token-contract storage rather than in the account's `balance` field. The documentation says nothing about how many addresses users actually hold or how they behave. Those are empirical questions, covered in the Victor (FC 2020) and Béres et al. (DAPPS 2021) digests. For DAC8, the annual report itself contains no address. The exposure described here depends on a separate anchor, such as a provider withdrawal record, that ties an identity to an address.
