---
title: "Profiling and Sensitive Inference from Transaction Records"
category: reference
sources:
  - raw/papers/2026-09-29-profiling-demontjoye-shopping-mall-reidentification.md
  - raw/papers/2026-09-29-profiling-rocher-incomplete-datasets-reidentification.md
  - raw/papers/2026-09-29-profiling-gladstone-psychological-traits-spending.md
  - raw/papers/2026-09-29-profiling-muggleton-gambling-bank-transactions.md
  - raw/papers/2026-09-29-profiling-brewer-clocs-purchase-health-inference.md
  - raw/papers/2026-09-29-profiling-imf-wallet-geolocation-time-of-day.md
  - raw/articles/2026-09-29-profiling-chainalysis-kyt-exposure-scoring.md
  - raw/articles/2026-09-29-profiling-cjeu-c252-21-meta-sensitive-inference.md
  - raw/articles/2026-09-29-profiling-cjeu-c634-21-schufa-scoring.md
  - raw/papers/2026-09-29-profiling-wp29-wp251-profiling-guidelines.md
  - raw/papers/2026-09-29-profiling-edpb-edps-digital-euro-joint-opinion.md
  - raw/articles/2026-09-20-cjeu-c184-20-indirect-sensitive-data.md
  - raw/articles/2026-09-23-twi-edpb-psd2-transaction-inference.md
  - raw/papers/2026-09-29-acctmodel-beres-ethereum-deanonymization-dapps2021.md
  - raw/articles/2026-09-29-atrisk-bmf-pacc-risk-scoring-self-description.md
created: 2026-09-29
updated: 2026-09-29
tags: [profiling, inference, special-categories, article-9-gdpr, reidentification, transaction-data, cjeu, dac8]
aliases: [Transaction profiling, sensitive inference from payments, Article 9 inference test]
confidence: medium
volatility: warm
verified: 2026-09-29
summary: "Item-level transaction records are highly re-identifiable and support statistical inference of traits, gambling and health signals and coarse location; CJEU C-252/21 applies Article 9 wherever processing allows sensitive information to be revealed; every empirical finding depends on merchant, time or item fields that the DAC8 annual report lacks but provider records may hold."
---

# Profiling and Sensitive Inference from Transaction Records

Transaction records can reveal more than wealth. This reference collects evidence on re-identification, trait and health inference, crypto timing analysis and the legal treatment of inferred data. It complements [[transaction-data-wealth-inference|Vermögensschätzung aus Transaktionsdaten als Analogie für DAC8]] ([Vermögensschätzung aus Transaktionsdaten als Analogie für DAC8](../theses/transaction-data-wealth-inference.md)), which covers wealth and income.

## Legal framework

| Authority | Holding or statement | Limit |
|---|---|---|
| GDPR Article 4(4); WP29 WP251rev.01 (endorsed by the EDPB) | profiling is automated evaluation of personal aspects; it creates "derived or inferred data", which is "new" personal data (pp. 6–9) | aggregate statistics without conclusions about individuals are not necessarily profiling |
| WP251rev.01, Chapter III.C (p. 15) | special-category data inferred from non-sensitive data need an Article 9(2) condition; example: health inferred from food shopping | non-binding guidance; the examples are item-level |
| CJEU C-184/20 (already in the wiki) | indirectly revealed sensitive data can fall under Article 9 | concerned publication of declarations of interest |
| CJEU C-252/21 *Meta Platforms v Bundeskartellamt*, Grand Chamber, 4 July 2023, paras 68–73 | Article 9(1) applies where processed data "allow" sensitive information to be revealed, whether or not the information is correct and whatever the controller's purpose; this covers data from website visits and online orders | whether particular data actually reveal sensitive information is for the national court; private controller relying on consent or contract, not a statutory tax duty |
| C-252/21, para 89 | a dataset collected en bloc, where sensitive and non-sensitive items cannot be separated at collection, is prohibited as a whole if it contains one sensitive item and no Article 9(2) derogation applies | the derogations available to a statutory public-law obligation were not in issue |
| CJEU C-634/21 *SCHUFA*, 7 December 2023, paras 43–50 and 73 | an automated probability score that a third party draws on "strongly" is itself an Article 22 decision and is profiling; national authorising law must respect Articles 5 and 6 (paras 65–68) | relevant to DAC8 only if a tax administration or provider actually scores reported persons in a way that strongly determines measures; Austria scores about 6.6 million cases a year, but DAC8 inputs and score-determined outcomes are undocumented |
| EDPB Guidelines 06/2020 on PSD2 (already in the wiki) | payment data can reveal special categories (donations, union fees, medical payments, sexual orientation) | concerns account-level payment data |
| EDPB-EDPS Joint Opinion 02/2023 on the digital euro | opposes recording all online transactions "regardless of their amount" (para 23); recalls the EDPB view that central-bank access to transaction data for "enforcement of tax rules should be avoided" (para 5); centralisation increases breach scale (para 53) | advisory; concerns a CBDC proposal, not tax-information exchange |

The C-252/21 test matters most for this repository. It moves the question from "was sensitive information sought or correct?" to "does the processing allow it to be revealed?". Applied to provider-held crypto records with counterparties, merchants or timestamps, that test can be met without any intent to profile. Applied to the DAC8 annual report, which contains no counterparty or merchant data, the showing is harder and must be made on the actual fields.

## Empirical evidence by granularity

| Study | Data | Finding | Limit |
|---|---|---|---|
| de Montjoye et al., *Science* 2015 | 3 months of card transactions, 1.1 million people, 10,000 shops; shop, day, price | four shop-day points make 90 percent unique; price adds 22 percent on average; coarsening helps slowly (ten coarse points still give over 80 percent); women and high-income people more re-identifiable | sample, not population, uniqueness; re-identification also needs an identified external source |
| Sánchez et al., *Science* 2016 comment | synthetic hospital data | argues the risk is overstated and that k-anonymisation yields zero unequivocal re-identifications | demonstration not on card data; the authors' reply (abstract only read) rejects it for high-dimensional data |
| Rocher et al., *Nature Communications* 2019 | modelled demographic attributes | 15 demographic attributes would correctly re-identify 99.98 percent of Americans; rejects the sampling-protects objection | demographic, not transaction attributes; same research group |
| Gladstone, Matz and Lemaire, *Psychological Science* 2019 | about two million transactions of 2,193 consenting UK app users; merchant categories | predicted and self-reported traits correlate at r = .15 for the Big Five and r = .33 for materialism; age and gender alone give r = .11 | modest accuracy; far from reliable individual labels; a corroborating 2021 study (abstract only) calls inference "a challenging task" |
| Muggleton et al., *Nature Human Behaviour* 2021 | Lloyds Banking Group data, up to 6.5 million customers; merchant categories and timestamps | gambling share associated with night-time spending (+11.5 percent "nights awake" per 10 points), later unemployment and disability-benefit receipt, and about one-third higher 5-year mortality | population associations, not individual predictions; bank-funded; cash and intermediated gambling missed |
| Brewer et al., *JMIR Public Health and Surveillance* 2023 | loyalty-card baskets, 153 ovarian-cancer cases and 120 controls | pain and indigestion medication purchases rise before diagnosis (OR 2.9 at 8 months); maximum AUC 0.65 | small; product-level baskets, far richer than payment records |
| IMF WP/25/141 (Reuter 2025) | Ethereum-family wallets with at least 50 transactions; hour-of-day activity, exchange and token use | wallets assigned to one of five world regions with 65 percent accuracy (random 20 percent); activity shifts with daylight saving time | working paper, not peer-reviewed; continental resolution only |
| Béres et al., DAPPS 2021 (account-model path) | Ethereum time-of-day, gas price and graph features | 1.6 bits of linking information between a user's addresses | modest; see [[account-model-linkage-exposure|Account-Model Chains and Exposure After an Identity Link]] ([Account-Model Chains and Exposure After an Identity Link](../theses/account-model-linkage-exposure.md)) |

**What the evidence supports.** Item-level records with shop, time and amount are highly unique, so removing names does not anonymise them. Spending categories and timestamps support statistical inference of traits, gambling behaviour, health-relevant signals and coarse location. For public-ledger activity, timestamps alone support region-level location inference.

**What it does not support.** Accurate labelling of individuals: the trait and health effect sizes are modest, and the gambling study reports associations. Nor does it support pinpointing a person's country or city from ledger timing. No peer-reviewed study inferring religion or sexual orientation from payment data was found; WP251's figures come from Facebook Likes.

## Provider-side derived layer

Chainalysis describes its KYT product as continuous, attribution-based risk scoring of customers' incoming and outgoing transactions. Scores rest on direct and multi-hop exposure to categories that include "gambling services" and cryptocurrency ATMs, and no error rates are published. This is vendor self-description with low confidence on accuracy. It does establish that provider-held records can already carry a derived behavioural layer about identified customers. Under WP251 that layer is inferred personal data. Where it reveals sensitive information, it falls under the C-252/21 test.

## Transfer to DAC8

- Every empirical finding above depends on merchant, counterparty, timestamp or item fields. The DAC8 annual report carries annual aggregates per crypto-asset and transaction type and none of those fields. See [[dac8-transaction-granularity-and-reporting-layers|DAC8 Transaction Granularity and Reporting Layers]] ([DAC8 Transaction Granularity and Reporting Layers](dac8-transaction-granularity-and-reporting-layers.md)).
- The findings transfer to provider-held MiCA, TFR and AML records, where those contain the relevant fields. See [[krypto-mpfg-provider-record-architecture|Krypto-MPfG Provider Record Architecture]] ([Krypto-MPfG Provider Record Architecture](krypto-mpfg-provider-record-architecture.md)).
- Re-identification is not the DAC8 issue: the report already names the person. The relevant point is how much the underlying provider records reveal, and whether any authority can join them to the report.
- An Article 9 argument against the DAC8 report itself requires showing that its actual fields allow sensitive information to be revealed. No study showing sensitive inference from annual per-asset totals was found.
- A SCHUFA argument requires evidence that DAC8 data feed automated scores that strongly determine measures against a person. Austria's PACC does score identified taxpayers at scale under § 114(4) BAO, but no source states that DAC8 or CRS data are model inputs, and officials rather than models set tax. See [[austrian-tax-risk-scoring-and-financial-data-use|Austrian Tax Risk Scoring and Actual Use of Financial Data]] ([Austrian Tax Risk Scoring and Actual Use of Financial Data](austrian-tax-risk-scoring-and-financial-data-use.md)).

## Claims to exclude

- "DAC8 reports reveal health, religion or sexual orientation."
- "Four transactions identify 90 percent of people" applied to DAC8 annual reports.
- "Spending data reliably reveal personality."
- "Blockchain timing reveals where a user lives."
- "C-252/21 makes all financial data special-category data."
- "Chainalysis risk scores are accurate."

## Open questions

- Whether DAC8 or provider data are inputs to PACC scoring models, and whether audit selection is strongly determined by the score.
- Whether the DAC8 annual fields for a concrete claimant (for example, transfers to a gambling service or a single named asset) allow sensitive information to be revealed.
- Legislative status of the digital euro proposal in 2026 (not verified).

## See Also

- [[austrian-tax-risk-scoring-and-financial-data-use|Austrian Tax Risk Scoring and Actual Use of Financial Data]] ([Austrian Tax Risk Scoring and Actual Use of Financial Data](austrian-tax-risk-scoring-and-financial-data-use.md)) — Austrian automated scoring (PACC) and the SCHUFA question.
- [[transaction-data-wealth-inference|Vermögensschätzung aus Transaktionsdaten als Analogie für DAC8]] ([Vermögensschätzung aus Transaktionsdaten als Analogie für DAC8](../theses/transaction-data-wealth-inference.md)) — wealth and income inference; same granularity boundary.
- [[bitcoin-payment-profile-retention|Bitcoin payment profiles and retention]] ([Bitcoin payment profiles and retention](../theses/bitcoin-payment-profile-retention.md)) — payment inference from stored identity links and the C-184/20 point.
- [[dac8-inference-linkage-and-error-evidence|DAC8 Inference, Linkage and Error Evidence]] ([DAC8 Inference, Linkage and Error Evidence](dac8-inference-linkage-and-error-evidence.md)) — linkage layers and inference truth table.
- [[account-model-linkage-exposure|Account-Model Chains and Exposure After an Identity Link]] ([Account-Model Chains and Exposure After an Identity Link](../theses/account-model-linkage-exposure.md)) — Ethereum behavioural linking.

## Sources

- [de Montjoye et al. 2015, with comment and reply](../../raw/papers/2026-09-29-profiling-demontjoye-shopping-mall-reidentification.md)
- [Rocher et al. 2019](../../raw/papers/2026-09-29-profiling-rocher-incomplete-datasets-reidentification.md)
- [Gladstone, Matz and Lemaire 2019](../../raw/papers/2026-09-29-profiling-gladstone-psychological-traits-spending.md)
- [Muggleton et al. 2021](../../raw/papers/2026-09-29-profiling-muggleton-gambling-bank-transactions.md)
- [Brewer et al. 2023](../../raw/papers/2026-09-29-profiling-brewer-clocs-purchase-health-inference.md)
- [IMF WP/25/141](../../raw/papers/2026-09-29-profiling-imf-wallet-geolocation-time-of-day.md)
- [Chainalysis KYT](../../raw/articles/2026-09-29-profiling-chainalysis-kyt-exposure-scoring.md)
- [CJEU C-252/21](../../raw/articles/2026-09-29-profiling-cjeu-c252-21-meta-sensitive-inference.md)
- [CJEU C-634/21](../../raw/articles/2026-09-29-profiling-cjeu-c634-21-schufa-scoring.md)
- [WP29 WP251rev.01](../../raw/papers/2026-09-29-profiling-wp29-wp251-profiling-guidelines.md)
- [EDPB-EDPS Joint Opinion 02/2023](../../raw/papers/2026-09-29-profiling-edpb-edps-digital-euro-joint-opinion.md)
- [CJEU C-184/20](../../raw/articles/2026-09-20-cjeu-c184-20-indirect-sensitive-data.md)
- [EDPB PSD2 guidelines digest](../../raw/articles/2026-09-23-twi-edpb-psd2-transaction-inference.md)
- [Béres et al. 2021](../../raw/papers/2026-09-29-acctmodel-beres-ethereum-deanonymization-dapps2021.md)
