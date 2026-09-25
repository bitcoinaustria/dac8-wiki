---
title: "Tobback & Martens: Retail credit scoring using fine-grained payment data"
source: "https://doi.org/10.1111/rssa.12469"
type: papers
ingested: 2026-09-23
fetched: 2026-09-23
content_format: pdf
extraction_tool: web-fetch
tags: [peer-reviewed, credit-scoring, payment-data, feature-granularity, aggregation, bank-transactions]
summary: "Using 183 million checking-account payments of 2.6 million bank clients, counterparty-level payment networks added significant predictive power for loan default over the bank's own rating. The authors locate the signal in who was paid, not in amounts or frequency, and contrast their approach with the monthly aggregates used in earlier studies."
---

# Retail credit scoring using fine-grained payment data

Ellen Tobback, David Martens. *Journal of the Royal Statistical Society Series A* 182(4):1227–1246, 2019. DOI: 10.1111/rssa.12469. Inspected: the author manuscript PDF from the University of Antwerp repository (repository.uantwerpen.be, version dated 2020-05-25), full text including Tables 1–2 and Figs. 5–12.

**Data and granularity.** The data are checking-account transactions (debit-card point-of-sale payments and electronic transfers; no credit cards) from a major European commercial bank. They cover August–December 2014: 182.6 million transactions by 2,585,227 clients holding a consumer loan, with about 5.9 million distinct counterparties (Table 1). The input is **item-level and counterparty-identified**. It is used as a sparse client × counterparty matrix, as a "direct" network (clients who paid each other) and as an "implied" network (clients who paid the same entities). The authors explicitly contrast this with earlier credit-scoring studies that reduce payment data to monthly aggregates such as transaction counts, average balance and total in/outflow (p. 4). They argue that aggregation discards important information.

**Target and accuracy.** The target is loan default in 2015 (base rate 0.77% in the test set). This is a credit-risk outcome, not wealth or income. The benchmark is the bank's internal 12-notch rating, built from sociodemographic and aggregated behavioural variables. The network models, and especially ensembles of network scores with the rating, achieve significantly higher out-of-sample AUC than the rating alone (ten-fold cross-validation; one-sided paired t-tests, all p < 1e-07; Table 2). AUC values are reported only graphically. In Fig. 5b the ensemble models lie in roughly the 0.86–0.94 band, above the benchmark rating, and single network models lie roughly between 0.80 and 0.85 (Fig. 11). Among the 1% riskiest clients, the direct-network model's lift is 115% higher than the rating model's (p. 14). Of test clients linked to at least one known defaulter, 51.98% defaulted.

**Key finding on granularity and stated limits.** Weighting network edges by the number of transactions rather than by months with a transaction made no significant difference once four or more months were included (p > 0.31). The authors conclude that the predictive value "seems to lie in the fact that a payment to a certain counterparty has been made, not in the amount or frequency" (p. 19). Transfers were more predictive than point-of-sale payments. Stated limits: testing was out-of-sample but not out-of-time; the data came from one bank and one prediction task; the rating model is confidential; and model explanations are hard with millions of sparse features.

**Relevance to annual aggregate reports.** This is strong evidence that item-level payment data identifying counterparties improves individual risk prediction, and it supports the broader claim that transaction data reveal personal financial condition. It does **not** support inferring wealth, balances or income from annual totals and counts per category. The target is default, not wealth. The information-bearing element was counterparty identity, which DAC8 reports do not contain. The paper itself reports that amount and frequency added little to that relational signal. It also frames aggregates (monthly counts and totals) as the weaker, information-losing representation.
