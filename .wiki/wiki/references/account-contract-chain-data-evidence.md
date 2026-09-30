---
title: "Account and contract chain-data evidence"
category: reference
sources:
  - raw/articles/2026-09-30-p2-chain-ethereum-rpc-state-receipts.md
  - raw/articles/2026-09-30-p2-chain-geth-call-state-tracers.md
  - raw/articles/2026-09-30-p2-chain-erc20-balances-events-units.md
  - raw/articles/2026-09-30-p2-chain-erc1967-proxy-state-history.md
  - raw/articles/2026-09-30-p2-chain-erc1271-signature-scope.md
  - raw/articles/2026-09-30-p2-chain-eip7702-delegation-reverts.md
  - raw/articles/2026-09-30-p2-chain-op-stack-bridge-derivation.md
  - raw/articles/2026-09-30-p2-chain-erc4626-vault-redeemability.md
  - raw/articles/2026-09-30-p2-chain-zk-rollups-public-da-history.md
  - raw/articles/2026-09-30-p4-chain-eip1898-canonical-snapshots.md
  - raw/articles/2026-09-30-p4-chain-geth-historical-state-proofs.md
  - raw/articles/2026-09-30-p4-chain-revert-and-receipt-status.md
created: 2026-09-30
updated: 2026-09-30
verified: 2026-09-30
volatility: hot
confidence: medium
tags: [ethereum, chain-data, contracts, receipts, tokens, bridges, layer2, technical-evidence]
summary: "Submitted intent, execution, emitted logs, historical state and economic claims are separate evidence endpoints."
---

# Account and contract chain-data evidence

An address anchor can expose persistent public account activity, but observations must use the correct chain and historical state. These normative/interface sources do not measure current Austrian implementation or human-ownership accuracy.

## Execution and authority

Transaction value/input describe submitted fields, not guaranteed committed transfers. Receipts add top-level status and gas information. Reconstructed call trees include attempted subcalls; ancestor failure and handled subcall failure differ. DELEGATECALL targets code, not automatically an economic recipient. Trace/diff output is not a cryptographic state proof.

EIP-7702 breaks two blanket assumptions on implementing forks: nonempty code does not uniquely identify a classic contract account; processed delegations can survive later execution failure. Fee payer and authorizing account can differ. Ordinary reverted call effects still roll back. Old code/nonce/gas-price classifiers require revalidation.

ERC-1271 acceptance is contextual authorization of a particular challenge, not economic sole ownership or every asset's control. Record the historical code, permissions, challenge scope and block.

## Position reconstruction

Native balance is not all tokens. A token needs chain/contract identity, units and validated semantics. Familiar symbols and event parameters do not independently authenticate value or participation. ERC-20 metadata are optional; mint/burn logs cannot universally substitute for state. Allowance is not transfer.

Proxy code can change while storage remains. Current ABI/code is insufficient for old-year analysis; upgrade logs are recommended, not mandatory. Verify historical implementation/beacon/storage. Vault shares, ideal asset conversion, fee-adjusted preview and permitted redemption are separate quantities; interface conformity does not prove solvency.

Bridge escrow and its representation must not be counted as two independent user assets under a 1:1 claim model. Escrow totals do not allocate every user's entitlement. OP input finality differs from optimistic withdrawal finalization; actual chain configuration and L2 data are necessary.

ZK validity does not imply privacy of published state data. Data availability during validation does not establish indefinite historical retrieval. Short blob retention is not deletion by all archives. Missing historical data are not proof of zero holdings.

## Consistent state evidence

EIP-1898 supplies hash-specific state queries with optional canonical membership checks on supported endpoints. Historical state and historical Merkle-proof capability differ by client/version/configuration; Geth archive mode is not a universal historical-proof guarantee. A validated root binds data, not a person's external identity.

## See Also

- [Account-model exposure thesis](../theses/account-model-linkage-exposure.md)
- [Identity-to-ledger evidence](identity-to-public-ledger-linkage-evidence.md)
- [Bitcoin UTXO evidence](bitcoin-utxo-observation-and-attribution.md)
- [Off-chain/private observers](offchain-private-ledger-observation-limits.md)
- [Concentration proof and alternatives](financial-data-concentration-proof-and-alternatives.md)

## Sources

Source records preserve versions, exact sections and mechanical low/medium scores. Unique normative authority is not promoted to empirical attribution accuracy or deployed fleet evidence.
