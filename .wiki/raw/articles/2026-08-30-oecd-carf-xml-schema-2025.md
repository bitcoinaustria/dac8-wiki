---
title: "OECD CARF XML Schema: transaction granularity"
source: "https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/07/crypto-asset-reporting-framework-xml-schema-july-2025_d1f81247/6e60235b-en.pdf"
type: articles
ingested: 2026-08-30
fetched: 2026-08-30
content_format: pdf
tags: [oecd, carf, xml, reporting, transaction-granularity, aggregates]
summary: "The July 2025 CARF XML guide groups annual report data by user, crypto-asset and category, using aggregate amounts, units and transaction counts rather than itemised transaction records."
---

# OECD CARF XML Schema: transaction granularity

The July 2025 User Guide is version 2.0 for CARF XML Schema version 1.5. It is primarily designed for exchange between tax administrations but may also be used for domestic provider reporting where national law permits.

The repeatable `RelevantTransactions` element contains a user's relevant transactions during the reporting period for each relevant crypto-asset type. The guide says that this element is repeated for each crypto-asset type, then subdivides it into transaction categories.

The category elements include crypto-to-crypto and crypto-to-fiat acquisitions and disposals, inbound and outbound transfers, reportable retail-payment transactions and transfers to wallet addresses not known to be associated with a VASP or financial institution. The ordinary category record contains:

- `NumberofTransactions` for the number of underlying transactions during the reporting period;
- `Amount`, described as an aggregate amount or aggregate fair-market value; and
- `NumberofUnits`, reflecting the total relevant units.

The external-wallet category contains aggregate amount and units but no transaction count. The schema does not contain an underlying transaction date, blockchain transaction ID, order ID, counterparty or individual wallet address. `ReportingPeriod` and the message timestamp belong to the message header; `DocRefID` identifies a correctable report record rather than an underlying transaction.

Accordingly, all relevant transactions feed classification, valuation and counting, while the standard output is an annual asset-and-category aggregate. A category containing only one transaction may still reveal that transaction's aggregate value and units. The XSD also allows repeated category elements, so a real national submission example remains useful to test whether a jurisdiction permits over-segmentation.
