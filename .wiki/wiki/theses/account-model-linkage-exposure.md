---
title: "Account-Model Chains and Exposure After an Identity Link"
type: thesis
status: completed
verdict: partially-supported
confidence: high
core_claim: "Account-based cryptoassets such as ETH provide no privacy at all; once an identity is linked to an account, its full history and balance are exposed."
key_variables: [ledger-model, address-reuse, identity-anchor, privacy-tooling, linkage-rate]
falsification: "Measured linkage on account-based chains is no higher than under UTXO fresh-address use, or privacy tools on account-based chains leave most users unlinked."
sources:
  - raw/articles/2026-09-29-acctmodel-ethereum-org-accounts-transactions.md
  - raw/articles/2026-09-29-acctmodel-bitcoin-whitepaper-privacy.md
  - raw/papers/2026-09-29-acctmodel-victor-ethereum-clustering-fc2020.md
  - raw/papers/2026-09-29-acctmodel-beres-ethereum-deanonymization-dapps2021.md
  - raw/papers/2026-09-29-acctmodel-torres-web3-wallet-leaks-usenix2023.md
  - raw/papers/2026-09-29-acctmodel-wang-zkp-mixers-www2023.md
  - raw/papers/2026-09-29-acctmodel-privacy-pools-bcra-2024.md
  - raw/articles/2026-09-29-acctmodel-stealth-addresses-buterin-erc5564.md
  - raw/articles/2026-09-29-acctmodel-buterin-l1-privacy-roadmap-2025.md
  - raw/articles/2026-09-29-acctmodel-stablecoin-issuer-freeze-terms.md
  - raw/papers/2026-09-29-acctmodel-stablecoin-sanction-evasion-preprint.md
  - raw/articles/2026-09-29-acctmodel-tornado-cash-us-legal-status.md
  - raw/papers/2026-09-04-kappos-bitcoin-cluster-validation-usenix-2022.md
  - raw/papers/2026-09-04-moeser-narayanan-bitcoin-clustering-fc-2022.md
  - raw/papers/2026-09-19-wang-rpc-linkage-ccs2025.md
  - raw/articles/2026-08-27-eu-amlr-regulation-2024-1624.md
  - raw/articles/2026-09-29-payrisk-us-v-storm-docket-status.md
created: 2026-09-29
updated: 2026-09-29
tags: [ethereum, account-model, utxo, linkage, address-reuse, privacy-tools, stablecoins, dac8]
aliases: [Ethereum privacy, account-based privacy, ETH no privacy, UTXO versus account model]
volatility: warm
verified: 2026-09-29
summary: "On Ethereum-style chains, default use concentrates a balance and ordered history at a few reused addresses, so one verified identity link exposes more than a single fresh-address UTXO output; privacy tools reduce but do not remove this, and 'no privacy at all' overstates the measured evidence."
---

# Account-Model Chains and Exposure After an Identity Link

## Verdict

**Partially supported, high confidence.** The structural part of the thesis holds: an account-based chain keeps value as one persistent balance per address, and default use reuses that address across transactions and applications. Once a single address is verifiably linked to a person, its visible history and current native and token balances can be read directly from chain state. With careful fresh-address use on a UTXO chain, one linked output typically exposes less.

"No privacy at all" is not supported. Account-model addresses remain pseudonymous until an anchor links them to an identity. Measured clustering on Ethereum covered a minority of accounts, and a widely used mixer left most users unlinked under published heuristics. UTXO chains are transparent too; the difference is in how much one link exposes and how easily linkage spreads, not in public visibility.

The formulation the evidence supports:

> On account-based chains such as Ethereum, default use concentrates a user's balance and transaction sequence at a few persistent, reused addresses. Once one address is verifiably linked to an identity, its full visible history and current balances can be read directly, usually more completely than for a single UTXO address used under fresh-address practice. Application-layer privacy tools reduce this exposure; measured use shows they are weakened by user behaviour and funding links, but not reduced to zero.

DAC8's annual report contains no wallet address. The exposure described here arises only where a separate anchor exists, such as a provider deposit or withdrawal record, a web-tracker leak or a public name.

## Mechanism

| Feature | Account model (Ethereum) | UTXO model (Bitcoin) |
|---|---|---|
| where value sits | a mutable `balance` on a persistent address; token balances in token-contract storage | discrete outputs; a wallet balance is the sum of outputs across addresses |
| change | stays at the sender account, so the next transaction reuses the address | returned to a change output, which may be a new address |
| ordering | each sent transaction carries the account's sequential `nonce` | no per-address counter |
| design guidance | protocol developers name "one address per application" as a future default (2025) | whitepaper section 10 recommends a new key pair per transaction |
| strongest clustering heuristic | none equivalent to multi-input; substitute heuristics rely on service patterns | multi-input and change heuristics |

Sources: ethereum.org account and transaction documentation; Bitcoin whitepaper section 10; Béres et al., p. 1; Victor, pp. 1–2.

Béres et al. argue that the account model "relies on address-reuse on the protocol level", making it "inferior to UTXO-based currencies from a privacy perspective". This is the authors' reasoning; they do not measure how many addresses users hold. The Bitcoin whitepaper itself concedes that "if the owner of a key is revealed, linking could reveal other transactions that belonged to the same owner", so UTXO pseudonymity is also partial.

## Evidence for

- **Persistent state.** ethereum.org documents a per-address balance and nonce. Once an address is known, balance and outgoing-transaction sequence are directly readable. Wu et al. (preprint) describe persistent state as "associated with accounts and updated directly by transactions".
- **Cross-context identifier.** Torres, Willi and Shinde (USENIX Security 2023) found 211 DApps and 13 of 100 wallets leaking the user's address to third parties such as RPC and analytics providers, alongside the user's IP address. They treat the address as a unique identifier and show that a 256-bit balance is itself a quasi-identifier. Counts are lower bounds from a 2022–2023 crawl.
- **Public names.** ENS names publish links between a name and an address. Béres et al. used ENS as ground truth and note that revealed names already expose activity such as gambling.
- **Developer concessions.** Buterin (2023): "By default, anything that goes onto a public blockchain is public", and using the application suite involves "making a significant portion of your life public". The 2025 roadmap proposes one address per application and shielded balances as future defaults. Even its target state leaves "Activity inside of each individual application" public.
- **Issuer control.** Circle and Tether terms reserve the right to block or freeze stablecoins at address level. Wu et al. count about USD 1.41 billion (USDT) and USD 108 million (USDC) frozen on Ethereum from November 2017 to August 2025, as lower bounds. A stablecoin balance is therefore both visible and centrally controllable per address.

## Evidence against

- **Limited clustering coverage.** Victor (FC 2020) states that no existing heuristic applies directly to the account model. Deposit-address reuse, airdrop consolidation and token self-authorisation clustered 17.9 percent of active externally owned accounts up to September 2019, mainly around exchange deposit addresses; 82.1 percent were not clustered. There was no ground truth.
- **Weak behavioural profiling.** Béres et al. found that time-of-day, gas-price and graph features yield 1.6 bits, reducing an anonymity set by a factor of about three. That is real but modest leakage.
- **Mixers left most users unlinked.** For Tornado Cash's first four months, Béres et al. linked 5.3 to 17.1 percent of withdrawals per pool. Wang et al. (WWW 2023, data to October 2022) reduced anonymity sets by 27.34 percent on average, with validation F1 of 0.55, and concluded that "most of the users can still stay anonymous".
- **Privacy constructions exist.** Stealth addresses are a final Ethereum standard (ERC-5564). Privacy Pools is a peer-reviewed design for zero-knowledge selective disclosure (abstract only read). Railgun and Privacy Pools are named for wallet integration in the 2025 roadmap.

## Nuances

- **Privacy depends on behaviour and tooling.** Wang et al. show that advertised anonymity sets overstate privacy and that careless use (address reuse, fee payment from the deposit address, direct transfers) collapses it. Béres et al. show a dust-amount balance fingerprint is feasible because 98.1 percent of transactions leave the last nine digits of a balance unchanged.
- **Tools are partial.** Stealth addresses hide the recipient, not the transfer. Funding a fresh stealth address with gas from a main wallet recreates the link; ERC-5564 lists funding as a known privacy issue.
- **Network metadata is separate.** RPC and network-layer leakage (Wang et al., CCS 2025, already in the wiki) is an additional route that the 2025 roadmap addresses separately.
- **Legal hazard of tools.** The US designated Tornado Cash in 2022. The Fifth Circuit held in *Van Loon* (26 November 2024) that immutable smart contracts are not blockable "property" under IEEPA, and Treasury delisted it on 21 March 2025. Roman Storm was convicted in August 2025 of conspiracy to operate an unlicensed money-transmitting business. The docket shows a Rule 29 acquittal motion still pending after argument on 9 April 2026, retrial of the open counts set for 26 April 2027, and a Speedy Trial Act dismissal motion denied on 10 September 2026. In the EU, AMLR Article 79 prohibits obliged entities, from 10 July 2027, from keeping anonymous crypto-asset accounts or accounts enabling anonymisation or obfuscation; it is not a ban on personal self-custody. Its exact scope was not re-read against the Official Journal text for this thesis. None of this is Austrian or CJEU authority.
- **Evidence age.** Most empirical work covers 2019–2022. No post-2022 peer-reviewed measurement of Railgun, Privacy Pools or stealth-address adoption was found.

## DAC8 transfer

- DAC8 annual aggregates contain no address. The account-model effect applies only after a separate anchor links an identity to an address.
- The most relevant anchors are provider records. Victor's strongest heuristic rests on exchange deposit addresses, the same infrastructure whose customer records identify users. A provider record naming a deposit or withdrawal address is therefore a stronger anchor than any annual aggregate. See [[krypto-mpfg-provider-record-architecture|Krypto-MPfG Provider Record Architecture]] ([Krypto-MPfG Provider Record Architecture](../references/krypto-mpfg-provider-record-architecture.md)).
- Where such an anchor exists, the harm analysis should be chain-specific. For an Ethereum address, one link can expose the balance and ordered history directly; for a Bitcoin output, exposure depends on clustering, which has its own validated error profile. See [[identity-to-public-ledger-linkage-evidence|Identity-to-Public-Ledger Linkage Evidence]] ([Identity-to-Public-Ledger Linkage Evidence](../references/identity-to-public-ledger-linkage-evidence.md)).
- An expert test for a concrete claimant should record which chains and assets are involved, whether a provider holds any address for the claimant, and whether the address was reused. See [[dac8-blockchain-linkage-expert-evidence-protocol|DAC8 Blockchain-Linkage Expert-Evidence Protocol]] ([DAC8 Blockchain-Linkage Expert-Evidence Protocol](../references/dac8-blockchain-linkage-expert-evidence-protocol.md)).

## Claims to exclude

- "Ethereum provides no privacy at all."
- "UTXO chains such as Bitcoin are private."
- "Bitcoin clustering coverage or error rates transfer to Ethereum."
- "DAC8 reports expose Ethereum addresses."
- "Tornado Cash use is traceable in general"; measured linkage is partial and heuristic.
- "A linked address shows the person's whole portfolio"; other addresses and custodial holdings may remain unlinked.

## Open questions

- No peer-reviewed measurement of how many addresses a typical Ethereum user controls.
- No validated person-level identification rate for Ethereum users.
- No chain-specific evidence for Tron, Solana or Ethereum layer-2 networks, although stablecoin use on Tron is significant.
- Whether current wallet defaults already follow the 2025 roadmap was not verified.

## See Also

- [[identity-to-public-ledger-linkage-evidence|Identity-to-Public-Ledger Linkage Evidence]] ([Identity-to-Public-Ledger Linkage Evidence](../references/identity-to-public-ledger-linkage-evidence.md)) — four-step linkage model and chain-specific limits.
- [[dac8-blockchain-linkage-expert-evidence-protocol|DAC8 Blockchain-Linkage Expert-Evidence Protocol]] ([DAC8 Blockchain-Linkage Expert-Evidence Protocol](../references/dac8-blockchain-linkage-expert-evidence-protocol.md)) — expert test to which account-model specifics apply.
- [[bitcoin-payment-profile-retention|Bitcoin payment profiles and retention]] ([Bitcoin payment profiles and retention](bitcoin-payment-profile-retention.md)) — UTXO-side counterpart for payment inference.
- [[breach-harm-and-linkage-empirics|Breach Harm and Blockchain-Linkage Empirics]] ([Breach Harm and Blockchain-Linkage Empirics](../references/breach-harm-and-linkage-empirics.md)) — auxiliary-data linkage and breach consequences.

## Sources

- [US v. Storm docket status](../../raw/articles/2026-09-29-payrisk-us-v-storm-docket-status.md)
- [ethereum.org accounts and transactions](../../raw/articles/2026-09-29-acctmodel-ethereum-org-accounts-transactions.md)
- [Bitcoin whitepaper, section 10](../../raw/articles/2026-09-29-acctmodel-bitcoin-whitepaper-privacy.md)
- [Victor, FC 2020](../../raw/papers/2026-09-29-acctmodel-victor-ethereum-clustering-fc2020.md)
- [Béres et al., DAPPS 2021](../../raw/papers/2026-09-29-acctmodel-beres-ethereum-deanonymization-dapps2021.md)
- [Torres, Willi and Shinde, USENIX Security 2023](../../raw/papers/2026-09-29-acctmodel-torres-web3-wallet-leaks-usenix2023.md)
- [Wang et al., WWW 2023](../../raw/papers/2026-09-29-acctmodel-wang-zkp-mixers-www2023.md)
- [Buterin et al., Privacy Pools](../../raw/papers/2026-09-29-acctmodel-privacy-pools-bcra-2024.md)
- [Stealth addresses and ERC-5564](../../raw/articles/2026-09-29-acctmodel-stealth-addresses-buterin-erc5564.md)
- [Buterin L1 privacy roadmap 2025](../../raw/articles/2026-09-29-acctmodel-buterin-l1-privacy-roadmap-2025.md)
- [Circle and Tether freeze terms](../../raw/articles/2026-09-29-acctmodel-stablecoin-issuer-freeze-terms.md)
- [Wu et al., stablecoin blacklisting (preprint)](../../raw/papers/2026-09-29-acctmodel-stablecoin-sanction-evasion-preprint.md)
- [Tornado Cash US legal status](../../raw/articles/2026-09-29-acctmodel-tornado-cash-us-legal-status.md)
- [Kappos et al., USENIX 2022](../../raw/papers/2026-09-04-kappos-bitcoin-cluster-validation-usenix-2022.md)
- [Möser and Narayanan, FC 2022](../../raw/papers/2026-09-04-moeser-narayanan-bitcoin-clustering-fc-2022.md)
- [Wang et al., RPC linkage, CCS 2025](../../raw/papers/2026-09-19-wang-rpc-linkage-ccs2025.md)
- [AMLR digest](../../raw/articles/2026-08-27-eu-amlr-regulation-2024-1624.md)
