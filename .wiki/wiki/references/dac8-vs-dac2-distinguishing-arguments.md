---
title: "DAC8 versus DAC2: Distinguishing Arguments"
category: reference
sources:
  - raw/articles/2026-08-27-dac2-directive-2014-107.md
  - raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md
  - raw/articles/2026-08-27-dac8-impact-assessment-swd-2022-401.md
  - raw/articles/2026-08-27-vfgh-e-2097-2021-dac2.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-section-18.md
  - raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md
  - raw/articles/2026-08-30-eu-implementing-regulation-2025-2263-xml-granularity.md
  - raw/articles/2026-08-30-oecd-carf-xml-schema-2025.md
  - raw/articles/2026-08-27-cjeu-c175-20-sia-ss-tax-data.md
  - raw/articles/2026-08-27-cjeu-c-623-22-dac6.md
  - raw/articles/2026-09-04-eu-delegated-regulation-2025-1140-mica-records.md
  - raw/articles/2026-09-04-cjeu-c340-21-tax-authority-breach-security.md
  - raw/articles/2026-09-04-austria-gmsg-section-5-processing-retention.md
  - raw/articles/2026-09-04-austria-gmsg-retention-rationale-and-records.md
  - raw/articles/2026-10-20-dac8-domestic-scope-versus-gmsg.md
  - raw/articles/2026-10-20-austria-kapitalabfluss-meldegesetz-expiry.md
created: 2026-08-30
updated: 2026-10-20
tags: [dac8, dac2, crs, proportionality, data-minimisation, litigation-strategy]
aliases: [DAC8 DAC2 comparison, DAC8 distinguishing case]
confidence: high
volatility: warm
verified: 2026-09-04
summary: "Field-level comparison showing which DAC8 features materially distinguish the adverse Austrian DAC2 precedent, with counterarguments and evidence gates."
---

# DAC8 versus DAC2: Distinguishing Arguments

> DAC8 uses DAC2's automatic-exchange architecture, but it does not merely substitute a crypto account for a bank account. Its asset-by-asset activity profile materially differs from the limited account, balance and interest facts on which VfGH E 2097/2021 relied in the claimant's deposit-account case. That distinction requires a fresh proportionality analysis; it does not predetermine the result.

## Controlling field comparison

| Dimension | DAC2 / facts in E 2097/2021 | DAC8 | Legal significance |
|---|---|---|---|
| Identity and account reference | Name, address, TIN, birth data, institution and account number or functional equivalent | Comparable biographical and provider identity, but no DAC8 user-account-number field | Identity matching is comparable; DAC2 additionally carries the account identifier. |
| Residents of the reporting state | Not reported: GMSG § 91 Z 1 limits participating states to *other* Member States, so an account holder resident only in Austria is not a reportable person | Reported: DAC8 Annex VI IV(D)(8) covers residents of *any* Member State; Krypto-MPfG § 14(1) Z 1 includes Austria | EU-mandated difference, not Austrian gold-plating; recital 13 gives effectiveness, level-playing-field and non-discrimination reasons (checked 20 October 2026). |
| Holdings | Year-end account balance or value, or closure | No year-end crypto-asset balance is reported | DAC8 is not a complete holdings or wealth register. |
| Income and proceeds | Broad annual interest, dividend, income and sale/redemption totals, depending on account type | Annual values organized by crypto asset and activity category | DAC8 exposes more structured economic activity, but remains aggregated. |
| Asset detail | No asset-by-asset unit and transaction-count profile in the fields considered by the VfGH | Asset name, values, units and counts for acquisitions and disposals | Supports a materially richer inference case. |
| Payments and transfers | No comparable transfer-direction or retail-payment fields | Annual aggregate value, units and count of retail-payment transactions, each exceeding USD 50,000; incoming and outgoing transfers; transfer type where known | Extends beyond balance and income totals into use and movement categories. |
| External-address signal | None | Aggregate value and units sent to DLT addresses not known by the provider to be associated with a VASP or financial institution | Records the provider's knowledge state and outward movement; it does not reveal the address or prove that no intermediary exists. |
| Time resolution | Annual reporting | Annual reporting | DAC8 does not supply transaction dates or a daily chronology. |
| Transaction identifiers and counterparties | Not part of the DAC2 comparison | Not reported by DAC8 | Blockchain linkage and relationship mapping cannot be presumed from the DAC8 report alone. |
| Adjacent provider records | The VfGH addressed the reported DAC2 data and an abstract claim of hacker access | MiCA Delegated Regulation 2025/1140 can require covered provider records that link identified buyer/seller data to on-chain hashes and wallet addresses | A new factual linkage environment is relevant only if the particular records, join and legal access path are proved; it does not change the DAC8 payload. |
| Austrian deletion rule for transmitted information | Five years under the GMSG provision quoted in E 2097/2021 | Ten years under section 20(4) Krypto-MPfG | A separate national proportionality issue; it is not necessary to invalidate DAC8 to challenge this choice. |
| Provider compliance records | Seven years under current section 7a GMSG | Ten years under section 39 Krypto-MPfG | Austria chose 10/10 rather than GMSG's 5/7 structure. Different data and audit needs may justify this, but the Krypto-MPfG materials do not address the divergence. |

The Commission's impact assessment confirms that this difference was deliberate. It rejected balance-only reporting as insufficient for frequently traded crypto-assets, selected a transaction-derived annual category-aggregate model for more precise risk assessment, and expected that model to have a stronger deterrent and tax-collection effect than balance reporting. Those statements explain the legislative objective; they are not independent proof that every adopted field is strictly necessary.

“Transaction-based” must not be confused with itemised transmission. Every in-scope exchange and transfer feeds the report and the provider's processing duty, while the routine section 18 payload contains annual asset-and-category totals, units and counts rather than one record per underlying transaction.

VfGH E 2097/2021 rejected an abstract security argument. CJEU C-340/21 does not overrule that result; it is a GDPR security-and-damages judgment. It does, however, supply a disciplined factual method: assess the nature, implementation and practical effects of the actual controls against the concrete processing risks, while recognising that a breach alone proves neither inadequacy nor invalidity. Combined with the enacted MiCA Table 3/Table 4 join, this supports targeted evidence requests rather than a generic assertion that crypto data are inherently insecure.

## Domestic residents: checked 20 October 2026

DAC8 recital 13 says the reporting obligation „sollte sich sowohl auf grenzüberschreitende als auch auf innerstaatliche Transaktionen erstrecken“. The recital speaks of transactions; the operative extension to the provider's own-state residents comes from Annex VI's "Member State Person" definition and, in Austria, Krypto-MPfG § 14(1) Z 1. Under the GMSG, by contrast, a person resident only in Austria is outside CRS/DAC2 reporting ([primary-text record](../../raw/articles/2026-10-20-dac8-domestic-scope-versus-gmsg.md)).

This supports an accurate comparison: an Austrian resident's domestic bank account generates no automatic-exchange report, while the same person's account at an Austrian crypto-asset service provider does. Three limits keep it accurate:

- Other domestic bank layers exist: the Kontenregister records account existence (not balances), banks withhold KESt, and AML records are kept. From March 2015 to December 2022 the [Kapitalabfluss-Meldegesetz](../../raw/articles/2026-10-20-austria-kapitalabfluss-meldegesetz-expiry.md) made banks report outflows of EUR 50,000 or more, including cash withdrawals, to the Finance Ministry. "Banks have never reported domestic withdrawals" would be wrong.
- The difference is set by DAC8. It can be argued as a proportionality point against the EU baseline, or politically for EU-level change, but not as a national excess.
- The State will cite recital 13's non-discrimination rationale: without domestic coverage, residents using foreign providers would be reported while those using domestic providers would not.

## Ranked arguments

| Weight | Argument | Why E 2097/2021 does not dispose of it | Likely State response | Evidence gate |
|---|---|---|---|---|
| Strongest factual distinction | **The inference premise has changed.** DAC8 permits asset exposure, activity counts, gross flow direction, approximate average transaction values, high-value payment use and outward transfers meeting the provider-knowledge test for VASP/financial-institution association to be derived from one annual report. | The VfGH expressly relied on the DAC2 data revealing only an account, balance/value and interest and not permitting further conclusions about essential private life. It did not assess DAC8's fields. | The data remain annual aggregates collected for taxation, without dates, counterparties, addresses or a movement chronology. | Obtain the actual Austrian report schema and demonstrate only the inferences reproducible from its fields. |
| Arguable | **The marginal necessity of additional field groups should be tested.** Transfer types, the external-address aggregate, counts and units may reveal activity that does not itself establish a taxable event. EU law does not require a separately published justification for every field. | DAC2's broad account totals did not require the same structured activity data. The DAC8 impact assessment partly justifies detail by better risk selection and fewer follow-up requests but does not measure every final subfield separately. | CJEU C-623/22 upheld the DAC6 information package collectively. Transfers can reconcile provider activity and hidden disposals; counts and units can detect implausible values. | Map each contested field to the tax task and prove that a narrower value, threshold or risk-triggered follow-up would be equally effective. |
| Strong national point | **Austria selected a ten-year deletion horizon for transmitted information.** | The GMSG rule before the VfGH required deletion after five years. DAC8 requires received exchange records to be kept at least five years but no longer than necessary; its separate five-to-ten-year corridor applies to provider reporting and due-diligence records. It does not itself prescribe Austria's ten-year rule for transmitted information. | Ten years may track tax limitation, audit and correction needs and can still satisfy the EU necessity limit. | Establish actual recipient retention, access frequency, audit timelines, backups and why five or seven years would be insufficient. |
| Claimant-dependent | **Full-profile processing of a genuinely non-reportable user may exceed what reportability due diligence requires.** | DAC2 also had an all-customer processing rule, so all-customer coverage alone is not new. The possible distinction is the greater breadth of the section 18 activity profile and its continued creation or retention after non-reportable status is settled. | Universal self-certification, status checks and some data processing are required by DAC8; early collection may be operationally necessary. | A non-reportable claimant, identified provider, access response, data flow and proof that the full section 18 profile is created or retained despite settled status. |
| Fact-dependent | **Combined provider and authority data may make the annual report more identifying than its face suggests.** | E 2097/2021 assessed the transmitted DAC2 fields, not linkage with provider-held DLT addresses, transfer records or blockchain analytics. | DAC8 does not transmit addresses, transaction IDs or counterparties; hypothetical linkage is not a defect in the directive. | Provider retention map, recipient access powers and a reproducible expert linkage demonstration. |
| Remedy-focused | **Valuation and classification errors require effective correction and review.** Fiat acquisitions and disposals report amounts paid or received; crypto-to-crypto transactions, retail payments and transfers use fair-market value under a consistently applied provider method. | The DAC2 case did not resolve the consequences of crypto-specific valuation and category errors propagated through annual profiles. | Data-quality, access, rectification and appeal safeguards can cure errors without invalidating reporting. | Real inaccurate record, correction attempt, response time and downstream use. |
| Secondary | **Expression, association, religion or physical-security effects may strengthen a concrete case.** | DAC8 categories can become revealing when linked to a claimant's proved conduct or provider records. | Generic chilling or security fears are speculative, and the report contains no counterparty or address. | Claimant-specific activity and a documented causal disclosure or threat pathway. |

## Arguments to retire or subordinate

- suspicionless reporting is invalid by itself;
- every account or user needs a de minimis threshold;
- all-customer processing is new to DAC8;
- generic hacking risk establishes invalidity;
- DAC8 directly reports wallet addresses, counterparties, transaction IDs or dates;
- DAC8 is a complete crypto wealth register;
- annual crypto aggregates are equivalent to telecommunications traffic and location data.

These points were rejected in the Austrian DAC2 litigation, are factually inaccurate, or require evidence not contained in the reporting schema.

## Procedural fit

- A challenge to DAC8-mandated fields raises EU-act validity. An Austrian court may reject that argument but cannot invalidate DAC8; a genuine validity doubt must be referred to the CJEU under Article 267 TFEU.
- A challenge to Austria's ten-year rule, implementation safeguards or a proven national excess can be decided as national law and may support partial annulment or a data-protection remedy without directive-wide invalidity.
- For an individual, the DSB and BVwG route remains the established Austrian vehicle. The field distinction strengthens the merits argument; it does not remove the subsidiarity obstacle to an immediate Article 140 application.

## See Also

- [[dac2-crs-austrian-litigation|Austrian DAC2/CRS Litigation]] ([Austrian DAC2/CRS Litigation](../topics/dac2-crs-austrian-litigation.md))
- [[dac8-charter-proportionality|DAC8 Charter Proportionality]] ([DAC8 Charter Proportionality](../topics/dac8-charter-proportionality.md))
- [[austrian-gold-plating-and-claimant-audit|Austrian Gold-Plating and Claimant Audit]] ([Austrian Gold-Plating and Claimant Audit](austrian-gold-plating-and-claimant-audit.md))
- [[austria-eu-precedent-matrix|Austria and EU Precedent Matrix]] ([Austria and EU Precedent Matrix](austria-eu-precedent-matrix.md))
- [[dac8-field-necessity-and-alternatives|DAC8 Field Necessity and Less-Intrusive Alternatives]] ([DAC8 Field Necessity and Less-Intrusive Alternatives](dac8-field-necessity-and-alternatives.md))
- [[dac8-inference-linkage-and-error-evidence|DAC8 Inference, Linkage and Error Evidence]] ([DAC8 Inference, Linkage and Error Evidence](dac8-inference-linkage-and-error-evidence.md))
- [[dac8-data-lifecycle-access-retention-remedies|DAC8 Data Lifecycle: Access, Retention and Remedies]] ([DAC8 Data Lifecycle: Access, Retention and Remedies](dac8-data-lifecycle-access-retention-remedies.md))
- [[dac8-transaction-granularity-and-reporting-layers|DAC8 Transaction Granularity and Reporting Layers]] ([DAC8 Transaction Granularity and Reporting Layers](dac8-transaction-granularity-and-reporting-layers.md))
- [[krypto-mpfg-provider-record-architecture|Krypto-MPfG Provider Record Architecture]] ([Krypto-MPfG Provider Record Architecture](krypto-mpfg-provider-record-architecture.md))
- [[financial-data-breach-and-security-authorities|Financial-Data Breach and Security Authorities]] ([Financial-Data Breach and Security Authorities](financial-data-breach-and-security-authorities.md))
- [[dac8-equality-and-technology-neutrality|DAC8 Equality and Technology-Neutrality Arguments]] ([DAC8 Equality and Technology-Neutrality Arguments](dac8-equality-and-technology-neutrality.md))

## Sources

- [Directive 2014/107/EU (DAC2)](../../../legal-docs/core/eu-dac2-directive-2014-107.pdf)
- [Directive (EU) 2023/2226 (DAC8)](../../../legal-docs/core/eu-dac8-directive-2023-2226.pdf)
- [Commission impact assessment SWD(2022) 401](../../../legal-docs/supporting/eu-swd-2022-401-dac8-impact-assessment.pdf)
- [VfGH E 2097/2021-13](../../../legal-docs/core/at-vfgh-e-2097-2021-13.pdf)
- [Krypto-MPfG, BGBl I 96/2025](../../../legal-docs/core/at-bgbl-i-96-2025-krypto-mpfg.pdf)
- [CJEU C-175/20, Valsts ieņēmumu dienests](../../../legal-docs/supporting/eu-cjeu-c175-20-valsts-ienemumu-dienests.pdf)
- [CJEU C-623/22, Belgian Association of Tax Lawyers](../../../legal-docs/core/eu-cjeu-c623-22-belgian-tax-lawyers.pdf)
- [Commission Delegated Regulation (EU) 2025/1140](https://eur-lex.europa.eu/eli/reg_del/2025/1140/oj/eng)
- [CJEU C-340/21, Natsionalna agentsia za prihodite](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0340)
- [GMSG section 5](../../raw/articles/2026-09-04-austria-gmsg-section-5-processing-retention.md)
- [GMSG retention rationale and section 7a](../../raw/articles/2026-09-04-austria-gmsg-retention-rationale-and-records.md)
- [DAC8 domestic scope versus GMSG](../../raw/articles/2026-10-20-dac8-domestic-scope-versus-gmsg.md)
- [Kapitalabfluss-Meldegesetz scope and expiry](../../raw/articles/2026-10-20-austria-kapitalabfluss-meldegesetz-expiry.md)
