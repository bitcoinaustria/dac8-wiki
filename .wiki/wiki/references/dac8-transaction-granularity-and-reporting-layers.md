---
title: "DAC8 Transaction Granularity and Reporting Layers"
category: reference
sources:
  - raw/articles/2026-08-27-austrian-bmf-dac8-overview.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-section-18.md
  - raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md
  - raw/articles/2026-08-27-krypto-mpfg-dv-attackable-regulation.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-materials-rv306.md
  - raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md
  - raw/articles/2026-08-27-commission-implementing-regulation-2025-2263.md
  - raw/articles/2026-08-30-eu-implementing-regulation-2025-2263-xml-granularity.md
  - raw/articles/2026-08-29-oecd-carf-2022.md
  - raw/articles/2026-08-30-oecd-carf-xml-schema-2025.md
  - raw/articles/2026-08-30-dac8-impact-assessment-evidence-and-options.md
  - raw/articles/2026-09-04-eu-delegated-regulation-2025-1140-mica-records.md
  - raw/articles/2026-09-04-oecd-carf-external-wallet-address-retention.md
created: 2026-08-30
updated: 2026-09-04
tags: [dac8, austria, krypto-mpfg, reporting, transaction-granularity, xml, carf]
aliases: [DAC8 every transaction, DAC8 transaction reporting]
confidence: high
volatility: hot
verified: 2026-09-04
summary: "Separates the all-transaction scope and provider processing duty from the annual asset-and-category aggregates routinely reported to tax authorities."
---

# DAC8 Transaction Granularity and Reporting Layers

> Every in-scope exchange and transfer is a reportable transaction and must feed the provider's compliance process. The routine annual DAC8 report is nevertheless an identity-linked set of aggregates by crypto asset and transaction category, not an itemised transaction ledger.

## Four distinct propositions

| Layer | Primary-text result | What it does not establish |
|---|---|---|
| Transaction scope | Section 6 Krypto-MPfG defines every exchange transaction and every transfer of a reportable crypto-asset as a `meldepflichtige Transaktion`. | That every transaction is a separate row in the report sent to the authority. |
| Provider processing | Section 20(1) requires the provider to determine, record, store and process reportable information for all customers, transactions and crypto-assets, irrespective of reportable-user status. | That the Austrian authority routinely receives all provider-held transaction details. |
| Annual provider report | Sections 18 and 19 require an annual report. For each reportable crypto-asset and relevant category it contains aggregate amount or fair-market value, total units and usually the number of reportable transactions. | Transaction date, transaction identifier, counterparty, wallet address, order ID, fee or a chronological ledger. |
| Automatic exchange | Section 21 sends the section 18 information to the relevant participating jurisdiction. Article 8ad(3) DAC uses the same aggregate fields. | A broader automatic exchange of the provider's underlying transaction ledger. |

## Why “transaction-based” is accurate but incomplete

The Austrian BMF contrasts DAC8's `transaktionsbasierte Meldung` with DAC2's static balance report. That description is accurate because each underlying exchange or transfer is classified, valued at the time of the transaction and incorporated into transaction-category totals. It does not resolve payload granularity by itself.

The operative provisions do. Section 18 repeatedly requires a total or aggregate amount, total units and a transaction count for the reporting period. Section 19 defines that period as the calendar year. The explanatory materials describe section 18 as the content of the annual report and use the same total-and-count structure.

## XML confirmation

The Commission's implementing XSD groups `RelevantTransactions` by crypto-asset and then uses category elements such as crypto-to-fiat acquisitions, crypto-to-crypto disposals and inbound or outbound transfers. Those elements contain `NumberofTransactions`, `Amount` and `NumberofUnits`; the external-wallet category contains aggregate amount and units. There is no element for an underlying transaction date, transaction identifier, counterparty or wallet address.

The OECD CARF XML Schema User Guide is explicit that the repeatable `RelevantTransactions` element is repeated for each relevant crypto-asset type. Within each category, `Amount` is an aggregate amount or aggregate fair-market value and `NumberofTransactions` is the count during the reporting period. The schema is designed for inter-authority exchange and may also be used domestically if a jurisdiction chooses.

The XSD allows category elements to repeat and does not itself impose a uniqueness key. This does not create a duty to report individual transactions: the directive defines the material values as aggregates and the schema lacks item-level fields. It does mean that the actual Austrian business rules and a real submission example remain relevant to exclude technical over-segmentation.

The Commission impact assessment independently distinguishes three models: highly aggregated reporting, transaction-by-transaction reporting and the selected hybrid. It describes the selected model as predominantly aggregated and says providers would not be obliged to report each item of transactional data. This legislative history cannot override the enacted text, but it confirms the same reading.

## Austrian technical-specification boundary

Section 4 Krypto-MPfG-DV requires the provider to transmit **the information named in section 18** through the FinanzOnline crypto-provider portal and says the XML/WSDL specifications are available on the BMF website and in the portal. No public Austrian crypto-provider XSD or WSDL was located in the BMF software-vendor pages during the 30 August 2026 review.

The statutory wording therefore supports annual aggregate transmission. A different factual conclusion would require the current Austrian portal XSD, WSDL or a real submission example showing additional item-level fields. Even then, the legal basis for any field beyond section 18 would need separate analysis.

## Residual detail inside an aggregate

Aggregation does not make every report coarse. If a user has only one transaction in an asset-and-category group, a count of one together with its amount and units effectively reveals those quantitative facts for that transaction, although not its date, identifier, counterparty or address. Rare assets, narrow transfer types and correction records can also increase inferential detail. These are consequences of the enacted aggregate fields, not evidence that a full itemised ledger is routinely transmitted.

## Separate provider records

The absence of addresses and hashes from the DAC8 report does not mean they are absent from the provider. For covered MiCA services and transactions, Delegated Regulation (EU) 2025/1140 can link identified buyer/seller records to on-chain records containing hashes, wallet addresses and timestamps through the provider's transaction-record number. TFR separately requires identity and address-related records for covered transfers. OECD CARF commentary expects external wallet addresses to be retained for follow-up requests, but DAC8 does not reproduce that exact commentary clause as a reported field or express Austrian retention rule.

These layers make provider discovery important. They do not establish routine transmission, tax-authority access or lawful fusion. Each address-bearing record needs its own binding basis, purpose, period, controller and access path.

## Litigation consequence

The accurate privacy premise is broader than the transmitted XML but narrower than a claim of routine itemised reporting:

- every in-scope transaction is captured and processed by the provider;
- the authority routinely receives an identity-linked annual activity profile derived from those transactions;
- item-level provider records may be obtainable through a separate information, audit or enforcement power, but that access and its use require their own legal basis and facts; and
- the routine DAC8 payload itself is not an itemised transaction history on the currently verified sources.

The strongest proportionality analysis should therefore examine both mandatory all-transaction processing under section 20 and the inferential content of the section 18 aggregates. It should not depend on the unsupported proposition that dates, transaction IDs, counterparties or addresses are automatically transmitted under DAC8.

## See Also

- [[dac8-inference-linkage-and-error-evidence|DAC8 Inference, Linkage and Error Evidence]] ([DAC8 Inference, Linkage and Error Evidence](dac8-inference-linkage-and-error-evidence.md))
- [[dac8-vs-dac2-distinguishing-arguments|DAC8 versus DAC2: Distinguishing Arguments]] ([DAC8 versus DAC2: Distinguishing Arguments](dac8-vs-dac2-distinguishing-arguments.md))
- [[dac8-data-lifecycle-access-retention-remedies|DAC8 Data Lifecycle: Access, Retention and Remedies]] ([DAC8 Data Lifecycle: Access, Retention and Remedies](dac8-data-lifecycle-access-retention-remedies.md))
- [[krypto-mpfg-provider-record-architecture|Krypto-MPfG Provider Record Architecture]] ([Krypto-MPfG Provider Record Architecture](krypto-mpfg-provider-record-architecture.md))

## Sources

- [Krypto-MPfG, sections 6 and 18-21](../../../legal-docs/core/at-bgbl-i-96-2025-krypto-mpfg.pdf)
- [Krypto-MPfG explanatory materials, RV 306](../../../legal-docs/supporting/at-krypto-mpfg-erlaeuterungen-rv-306.pdf)
- [Krypto-MPfG-DV, section 4](../../../legal-docs/core/at-bgbl-ii-331-2025-krypto-mpfg-dv.pdf)
- [BMF automatic and international exchange overview](https://www.bmf.gv.at/themen/betrugsbekaempfung/automatischer-informationsaustausch.html)
- [Directive (EU) 2023/2226, Article 8ad and Annex VI](../../../legal-docs/core/eu-dac8-directive-2023-2226.pdf)
- [Commission Implementing Regulation (EU) 2025/2263](../../../legal-docs/supporting/eu-implementing-regulation-2025-2263.pdf)
- [OECD CARF XML Schema User Guide, July 2025](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/07/crypto-asset-reporting-framework-xml-schema-july-2025_d1f81247/6e60235b-en.pdf)
- [Commission impact assessment SWD(2022) 401](../../../legal-docs/supporting/eu-swd-2022-401-dac8-impact-assessment.pdf)
- [Commission Delegated Regulation (EU) 2025/1140](https://eur-lex.europa.eu/eli/reg_del/2025/1140/oj/eng)
