---
title: "CARF baseline: due diligence for all users covers identity, reporting covers reportable users"
source: "https://www.gov.je/TaxesMoney/InternationalTaxAgreements/IGAs/pages/cryptoassetreporting.aspx"
type: articles
ingested: 2026-09-10
fetched: 2026-09-10
tags: [carf, oecd, due-diligence, krypto-mpfg, section-20, gold-plating, data-minimisation]
summary: "The CARF standard requires collection of tax identification and residence from all users but reporting only for reportable users; the Austrian addition operates on the transaction axis, not the identity axis."
---

# CARF baseline: identity versus transaction

## Rule captured

The Government of Jersey states the baseline plainly: reporting providers "must collect due diligence information, including Taxpayer Information Numbers (TINs) and jurisdiction(s) of tax residence for all users. However, information must only be reported in respect of users who are identified as Reportable Users".

The OECD CARF XML Schema User Guide of July 2025 carries the same structure on the reporting side. The CARF Body is built around a Reportable User with User ID, optional Controlling Person and RelevantTransactions. There is no element for a user determined not to be reportable. Message type indicator CARF703 provides for domestic nil reporting, in which the CARF Body is populated only with information on the reporting provider itself.

The OECD CARF FAQs of December 2025 address nexus, retail payment transactions, third-party reliance, entity residence, non-custodial services, wrapping, collateralised loans, NFTs and e-money. None addresses processing or retention for non-reportable users.

## Research use

This locates the Austrian excess precisely. Collecting something from every customer is the international standard, so an argument that universal collection is per se unlawful will fail. What the standard requires universally is identity and residence data for the purpose of sorting users. § 20 Abs. 1 Krypto-MPfG extends the universal duty to "alle Transaktionen und Kryptowerte".

The pleading axis is therefore transaction data, not self-certification. A complaint that attacks the self-certification requirement attacks the part of the regime that is genuinely standard-mandated.
