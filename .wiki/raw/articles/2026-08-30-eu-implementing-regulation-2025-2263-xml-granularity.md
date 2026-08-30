---
title: "EU DAC8 implementing XSD: transaction granularity"
source: "https://eur-lex.europa.eu/eli/reg_impl/2025/2263/oj"
type: articles
ingested: 2026-08-30
fetched: 2026-08-30
content_format: pdf
tags: [eu, dac8, implementing-regulation, xml, reporting, transaction-granularity, aggregates]
summary: "Annex XVIII to Regulation 2025/2263 implements annual crypto-asset category records containing aggregate amounts, units and counts, without item-level transaction fields."
---

# EU DAC8 implementing XSD: transaction granularity

Annex XVIII to Commission Implementing Regulation (EU) 2025/2263 contains the computerised format for DAC8 crypto-asset information exchange.

Within a crypto-user record, `RelevantTransactions` is repeatable and identifies a `CryptoAsset`. The available category elements include `CryptoToCryptoIn`, `CryptoToCryptoOut`, `CryptoFiatIn`, `CryptoFiatOut`, `CryptoTransferIn`, `CryptoTransferOut`, `TransferWallet` and `RRPT`.

The ordinary category elements contain `NumberofTransactions`, `Amount` and `NumberofUnits`, with optional exchange, transfer or valuation classifiers where applicable. `TransferWallet` contains amount and units but no transaction count. The XSD contains no field for an underlying transaction date, blockchain transaction ID, order ID, counterparty or individual wallet address.

The schema therefore implements the aggregate fields enacted in Article 8ad(3)(c) and Annex VI Section II.B.3 of Directive 2023/2226. Repetition supports different crypto-assets, categories, types and currencies; it does not by itself convert the prescribed amount, unit and count fields into an itemised transaction ledger.

This regulation governs the standard inter-authority format. It is strong evidence of the EU exchange payload but does not by itself prove the exact fields accepted by every national provider-to-authority portal.
