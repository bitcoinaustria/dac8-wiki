---
title: "Krypto-MPfG Provider Record Architecture"
category: reference
sources:
  - raw/articles/2026-08-27-austria-krypto-mpfg-section-18.md
  - raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md
  - raw/articles/2026-08-30-austria-krypto-mpfg-section-39-records.md
  - raw/articles/2026-09-04-krypto-mpfg-section-39-timing-correction.md
  - raw/articles/2026-09-04-oecd-carf-external-wallet-address-retention.md
  - raw/articles/2026-08-27-eu-tfr-regulation-2023-1113.md
  - raw/articles/2026-09-04-eu-delegated-regulation-2025-1140-mica-records.md
  - raw/articles/2026-09-04-austria-dac8-controller-and-authority-retention-precision.md
created: 2026-09-04
updated: 2026-09-04
tags: [krypto-mpfg, dac8, mica, tfr, records, wallet-address, transaction-hash, retention]
aliases: [Krypto-MPfG record layers, CASP address records]
confidence: high
volatility: hot
verified: 2026-09-04
summary: "Separates the address-free DAC8 report from the inputs and separate MiCA, TFR and CARF record layers that may contain linkable wallet and transaction data."
---

# Krypto-MPfG Provider Record Architecture

> The routine DAC8 report does not contain a wallet address or transaction hash. A provider may nevertheless hold address-bearing and identity-linked records under separate rules. Each record, purpose, retention period, controller and access path must be proved rather than collapsed into a single database.

## Record layers

| Layer | What is legally established | Address or transaction identifier | Retention and access boundary |
|---|---|---|---|
| Krypto-MPfG section 18 report | Annual identity-linked aggregates by asset and transaction category | No wallet address, transaction hash, transaction timestamp or counterparty | Provider submits to the competent Austrian tax authority; exchange is routed under DAC8 |
| Krypto-MPfG section 20(1) processing | Provider must determine, collect, store and process the section 18 information for all customers, transactions and crypto-assets | Producing the external-address aggregate necessarily uses a destination address and a VASP/FI attribution decision, but section 20 does not expressly make the address a reported field or prescribe its storage period | Exact staging fields, source records and deletion logic are factual questions |
| Krypto-MPfG section 39 documentation | Provider documents steps taken under Chapters 3–7 and retains those documents for ten years after the end of the relevant reporting period | The provision does not expressly name wallet addresses or raw transaction records | Whether an address or attribution record forms part of the documented step is unresolved and provider-specific |
| OECD CARF commentary | Standard expects external-wallet addresses to be retained for follow-up requests | Yes, as provider-held records; not in the routine report | Soft-law standard, not by itself an Austrian storage power |
| TFR Articles 14–16 and 26 | Covered CASP transfers carry originator, beneficiary and account or DLT-address information | Yes, for covered transfers | AML/CFT purpose; normally five years; no automatic tax-purpose fusion |
| MiCA Article 68(9) and Delegated Regulation 2025/1140 | Covered service, order and transaction records identify buyer and seller; where relevant, a transaction hash appears in the off-chain record | Annex Table 4 contains hash, wallet addresses, timestamp and other on-chain fields, linked to the off-chain transaction record by the firm's transaction-record number | MiCA supervisory record. Scope depends on the service and transaction; competent-authority access under MiCA is not tax-authority receipt under DAC8 |

## The important linkage seam

Delegated Regulation 2025/1140 supplies the clearest enacted identity-to-ledger seam located in this research. Table 3 can hold a natural-person buyer or seller identifier, name and birth date and, where relevant, a transaction hash. Table 4 separately specifies wallet addresses and other on-chain data and uses the same transaction-record number to link the on-chain and off-chain records.

This does not change the DAC8 field map. It changes the factual inquiry at the provider:

1. Which Table 3 and Table 4 records exist for the relevant service and transaction?
2. Are identity, tax aggregation and on-chain records physically or logically separated?
3. Which roles, processors and authorities can join them?
4. What legal basis and purpose govern each join?
5. Which record survives for five, seven or ten years, and which deletion rule is actually applied?

## External-address aggregation

The section 18 external-address field contains only aggregate fair-market value and aggregate units. It has no transaction count and no address. Its production is nevertheless address-predicated: the provider must examine the destination and decide whether it is known to be associated with a VASP or financial institution.

The OECD commentary treats the aggregate as a possible trigger for later information requests and expects the provider to keep the underlying external address for at least five years. DAC8 did not reproduce that CARF address-retention clause verbatim. The question for Austria is therefore not whether the routine payload contains an address; it does not. The questions are which binding rule supports provider retention of the address, how long it is retained, and which authority may obtain it for which purpose.

## Section 39 correction

Section 39 measures its ten-year period from the end of the `Meldezeitraum`. The earlier raw record described the starting point as the end of the later year in which the report was due. The correction record supersedes that timing sentence. The broader uncertainty remains: the provision retains documented compliance steps but does not expressly define every input record covered.

Section 20(4) is also actor-specific. It orders the reporting provider to delete transmitted information after ten years; it does not set the retention period for the BMF's originating copy. The authority-copy period must be derived from the rule applicable to that controller and copy, subject to DAC Article 25(5). It must not be inferred from the provider rule.

## Evidence requests

- the provider's data dictionary for Krypto-MPfG, MiCA, TFR and AML records;
- a field-level map from source transaction to section 18 aggregate;
- the current Austrian portal XSD, WSDL and validation rules;
- the provider's Table 3/Table 4 applicability analysis under Regulation 2025/1140;
- role, processor and authority-access matrices for every record layer;
- retention schedules for active systems, archives and backups, including deletion triggers;
- logs or policies showing whether tax, compliance and supervisory records are joined;
- the legal basis and approval path for any follow-up request for an address or transaction identifier.

## Claims to exclude

- DAC8 or section 18 routinely transmits wallet addresses or transaction hashes.
- Section 39 expressly requires ten-year retention of every destination address.
- Provider possession gives the tax authority automatic access.
- Every CASP transaction produces every field in Tables 3 and 4 of Regulation 2025/1140.
- TFR's AML/CFT purpose limitation disappears because the same provider performs DAC8 reporting.

## See Also

- [[dac8-transaction-granularity-and-reporting-layers|DAC8 Transaction Granularity and Reporting Layers]] ([DAC8 Transaction Granularity and Reporting Layers](dac8-transaction-granularity-and-reporting-layers.md))
- [[dac8-data-lifecycle-access-retention-remedies|DAC8 Data Lifecycle: Access, Retention and Remedies]] ([DAC8 Data Lifecycle: Access, Retention and Remedies](dac8-data-lifecycle-access-retention-remedies.md))
- [[mica-tfr-krypto-mpfg-nexus|MiCA, TFR, and the Krypto-MPfG Nexus]] ([MiCA, TFR, and the Krypto-MPfG Nexus](../topics/mica-tfr-krypto-mpfg-nexus.md))
- [[identity-to-public-ledger-linkage-evidence|Identity-to-Public-Ledger Linkage Evidence]] ([Identity-to-Public-Ledger Linkage Evidence](identity-to-public-ledger-linkage-evidence.md))

## Sources

- [Krypto-MPfG consolidated text](../../../legal-docs/core/at-krypto-mpfg-consolidated-2026.html)
- [OECD CARF and commentary](https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/international-standards-for-automatic-exchange-of-information-in-tax-matters_ab3a23bc/896d79d1-en.pdf)
- [TFR](https://eur-lex.europa.eu/eli/reg/2023/1113/oj)
- [Commission Delegated Regulation (EU) 2025/1140](https://eur-lex.europa.eu/eli/reg_del/2025/1140/oj/eng)
