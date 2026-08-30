---
title: "DAC8 Inference, Linkage and Error Evidence"
category: reference
sources:
  - raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-section-18.md
  - raw/articles/2026-08-27-commission-implementing-regulation-2025-2263.md
  - raw/articles/2026-08-29-oecd-carf-2022.md
  - raw/articles/2026-08-30-eu-implementing-regulation-2025-2263-xml-granularity.md
  - raw/articles/2026-08-30-oecd-carf-xml-schema-2025.md
  - raw/articles/2026-08-30-dac8-impact-assessment-evidence-and-options.md
  - raw/articles/2026-08-28-cjeu-c487-21-access-copy.md
  - raw/articles/2026-08-27-eu-tfr-regulation-2023-1113.md
  - raw/articles/2026-08-27-eu-mica-regulation-2023-1114.md
created: 2026-08-30
updated: 2026-08-30
tags: [dac8, inference, linkage, valuation, classification, data-quality, evidence]
aliases: [DAC8 inference matrix, DAC8 technical evidence]
confidence: high
volatility: hot
verified: 2026-08-30
summary: "Technical truth table for what DAC8 annual fields reveal directly, what requires other datasets, and which valuation, classification and correction facts need proof."
---

# DAC8 Inference, Linkage and Error Evidence

> Every in-scope transaction is captured in the provider's compliance process, but the routine DAC8 payload is an identity-linked annual crypto-activity profile rather than an itemised transaction or current-wealth register. Strong legal arguments must reproduce the inference from the transmitted fields and identify every additional dataset used.

## Inference truth table

| Reported field | Directly supportable inference | Not supportable from DAC8 alone | Additional data needed |
|---|---|---|---|
| Identity, residence, TIN and provider | A named reportable user or entity had reportable activity; TIN supports matching across reports. A controlling person is linked to that entity and reported role, not necessarily a user or transactor. | Current custody location, key control or current holdings. | Current KYC, custody and account records. |
| Asset name | Asset-specific annual activity and multi-year change in use. | Contract address, chain, token version or current balance. | Canonical asset identifier and provider metadata. |
| Fiat acquisitions: total amount, units and count | Annual volume, mean reported transaction size and implied weighted unit value. | Individual prices, dates or remaining tax basis. | Transaction ledger, timestamps, fees and lot history. |
| Fiat disposals: total amount, units and count | Annual gross proceeds and mean reported transaction size. | Gain, tax liability or evasion. | Acquisition lots, opening holdings, fees and applicable tax treatment. |
| Crypto-to-crypto acquisitions and disposals | Annual activity on both sides by asset; the implementing schema may include an optional exchange-type code. | Reliable pairing of an acquisition to a disposal. | Trade ID, pair, timestamp and provider ledger. |
| Retail payments over USD 50,000 | Annual aggregate value, units and count of retail-payment transactions, each exceeding USD 50,000. | Individual value, merchant, goods, location, date or economic purpose. | Payment and counterparty records. |
| Incoming/outgoing transfers: value, units, count and transfer subtype | Annual flow direction and a mandatory schema subtype, using `Unknown` where the provider lacks a more specific code. | Taxable income, disposal, gift, loan, collateral or self-transfer as a legal conclusion. | Transfer record, counterparty, contract and tax classification. |
| Transfers to DLT addresses not known by the provider to be associated with a VASP or financial institution: value and units | Annual value and units meeting that provider-knowledge test. | Address, transaction count, wallet count, self-custody, ownership or tax flight. | Provider-held address/transaction data, ownership evidence and lawful linkage authority. |

## Calculation limits

- Total value divided by count is a mean, not a chronology or distribution.
- Total value divided by units is an implied weighted value, not a price series.
- Crypto-to-crypto acquisitions and disposals represent two sides of activity; summing them can double-count.
- The external-address aggregate can overlap with general outgoing transfers and is not an independent asset or revenue block.
- Gross flows do not produce a closing balance without opening holdings, off-provider activity, lost access and complete transfer history.
- High transfer counts can reflect wrapping, bridges, collateral, loans or own-account movement rather than a large economic change.

## Linkage layers

| Added dataset | What it could add | Legal and technical boundary |
|---|---|---|
| Other DAC8 reports with the same TIN | Cross-provider annual profiles and transfer candidates | No exact reconciliation without a shared transaction key. |
| Tax returns, DAC2 or bank data | Mismatch and risk-selection signals | A mismatch is not proof of underpayment. |
| Provider transaction records | Dates, order IDs, pairs, fees and often destination information | Provider possession does not establish tax-authority access or routine fusion. |
| TFR or AML records | Originator, beneficiary or self-hosted-address evidence in covered transfers | Separate purpose, competence, access and proportionality rules apply. |
| Address or transaction ID plus public ledger | Hypothetical paths and heuristic address clusters | Requires separate technical evidence; internal provider ledgers remain invisible and attribution or clustering can be wrong. |

Article 16(1) DAC permits exchanged information to be used for covered taxes, VAT and other indirect taxes, customs, AML/CFT, recovery, compulsory social-security contributions and tax-law penalty proceedings. Article 16(2) separately governs other purposes, including its approval and communicated-list mechanisms. Neither provision establishes the reverse proposition that every AML, TFR or MiCA record is automatically available for every tax use.

## Valuation and classification error paths

Krypto-MPfG section 18 permits several valuation routes, including provider trading pairs, book values, third-party prices, the latest available value and a reasonable estimate. Different providers can therefore reach different but facially lawful values because of market, time, spread, fee, liquidity and fallback choices.

Transfer classification depends on provider knowledge. Within an incoming or outgoing transfer category, the same economic act may receive a loan, collateral, payment, other or `Unknown` subtype from different providers. The schema also permits optional alternative-valuation information for incoming, outgoing and external-address aggregates. Whether a destination is “not known” as associated with a VASP or financial institution depends on the provider's current data and method; it is not a finding that the user owns a self-hosted wallet.

The implementing schema permits corrections. That proves correction is technically contemplated, not that the correction replaces the value in every recipient copy, risk model, audit file and backup.

## Evidence protocol

1. Obtain the exact provider record and the exact transmitted or planned XML, not a generic privacy notice.
2. Preserve valuation source, timestamp, method, currency conversion and fee treatment for disputed fields.
3. Test identical assets and cross-provider transfers across providers for value and category dispersion.
4. Measure known-VASP, third-party-wallet and own-wallet classification error for the external-address field.
5. Reproduce any asserted tax or behavioural inference from DAC8 alone, then add each external dataset one at a time.
6. Record legal basis, controller, access log and purpose for every linkage step.
7. Submit a controlled correction and trace it provider → Austrian authority → recipient state → downstream system.

## Claims to exclude

- DAC8 transmits wallet addresses, transaction IDs, dates, counterparties or current balances.
- The external-address field includes a transaction or wallet count.
- “Not known as VASP/FI” proves self-custody, ownership or tax evasion.
- High gross flows prove gains or tax liability.
- DAC8 alone performs exact cross-provider reconciliation.
- Different valuations are necessarily inaccurate.
- Provider retention under another regime proves routine tax-authority access.

## See Also

- [[dac8-transaction-granularity-and-reporting-layers|DAC8 Transaction Granularity and Reporting Layers]] ([DAC8 Transaction Granularity and Reporting Layers](dac8-transaction-granularity-and-reporting-layers.md))
- [[dac8-field-necessity-and-alternatives|DAC8 Field Necessity and Less-Intrusive Alternatives]] ([DAC8 Field Necessity and Less-Intrusive Alternatives](dac8-field-necessity-and-alternatives.md))
- [[dac8-data-lifecycle-access-retention-remedies|DAC8 Data Lifecycle: Access, Retention and Remedies]] ([DAC8 Data Lifecycle: Access, Retention and Remedies](dac8-data-lifecycle-access-retention-remedies.md))
- [[dac8-vs-dac2-distinguishing-arguments|DAC8 versus DAC2: Distinguishing Arguments]] ([DAC8 versus DAC2: Distinguishing Arguments](dac8-vs-dac2-distinguishing-arguments.md))

## Sources

- [Directive (EU) 2023/2226 (DAC8)](../../../legal-docs/core/eu-dac8-directive-2023-2226.pdf)
- [Krypto-MPfG consolidated text](../../../legal-docs/core/at-krypto-mpfg-consolidated-2026.html)
- [Commission Implementing Regulation (EU) 2025/2263](https://eur-lex.europa.eu/eli/reg_impl/2025/2263/oj)
- [OECD CARF XML Schema User Guide, July 2025](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/07/crypto-asset-reporting-framework-xml-schema-july-2025_d1f81247/6e60235b-en.pdf)
- [Transfer of Funds Regulation (EU) 2023/1113](https://eur-lex.europa.eu/eli/reg/2023/1113/oj)
- [MiCA Regulation (EU) 2023/1114](https://eur-lex.europa.eu/eli/reg/2023/1114/oj)
