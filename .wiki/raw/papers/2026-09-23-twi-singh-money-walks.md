---
title: "Singh, Bozkaya & Pentland: Money Walks — implicit mobility behavior and financial well-being"
source: "https://doi.org/10.1371/journal.pone.0136628"
type: papers
ingested: 2026-09-23
fetched: 2026-09-23
content_format: html
extraction_tool: web-fetch
tags: [peer-reviewed, financial-well-being, card-transactions, behavioural-features, feature-granularity, credit-risk]
summary: "Spatio-temporal features (diversity, loyalty, regularity) built from time-stamped, geolocated credit-card purchases of ~9,000 bank customers predicted overspending, late payment and financial trouble with AUC 0.77–0.83, against about 0.59 for demographics; the features rely on where and when people spend, not on amount totals."
---

# Money Walks: Implicit Mobility Behavior and Financial Well-Being

Vivek K. Singh, Burcin Bozkaya, Alex Pentland. *PLOS ONE* 10(8): e0136628, 2015. DOI: 10.1371/journal.pone.0136628. Inspected: the open-access HTML article on journals.plos.org (methods, results, Fig. 4, discussion), read through a text-extraction tool rather than as the typeset PDF.

**Data and granularity.** The data are 15.7 million credit-card purchase transactions for about 405,000 customer accounts at a large financial institution in an unnamed OECD country, over a 3-month window in 2013 that excluded holiday periods. After cleaning, 7,855 users with complete features entered the feature analysis and 9,011 entered the classifiers. Each transaction carries a timestamp, amount, merchant address/coordinates and spending category. It is linked to the bank's demographic record (age, gender, marital status, education, home/work location) and to income "as estimated by the bank". The predictors are computed from **item-level, time-stamped and geolocated** records: *diversity* (normalised entropy of transactions across spatial or temporal bins), *loyalty* (share of transactions in a customer's top-3 bins) and *regularity* (distance between 1-month and 3-month patterns).

**Target and accuracy.** The paper has three binary targets: *overspending* (card spending in the period exceeds the bank's income estimate), *late payment* (beyond a 3-day grace period) and *financial trouble* (default, non-payment or legal/administrative action within a subsequent lag window). A bagging classifier with a 70/30 split and SMOTE rebalancing reached AUC **0.831** (overspending), **0.786** (late payment) and **0.773** (financial trouble). Comparable demographic-only models reached about 0.59 (0.589 for financial trouble), a relative improvement of 30–49% (Results, Fig. 4).

**Stated limits.** This is a single-institution, cross-sectional, 3-month study. The income denominator in "overspending" is itself a bank estimate, not observed income. Late payment can have non-financial causes. The authors highlight privacy concerns about mobility-derived features and argue that behavioural features may transfer across cultures better than norm-based constructs, but they do not test this.

**Relevance to annual aggregate reports.** This supports the general proposition that spending behaviour predicts financial *condition* (strain, overspending, default risk) better than demographics. It does **not** show that wealth, balances or income can be estimated. Income was an input to the overspending label, not a prediction target. Nor does it show predictive power from annual totals and counts. The informative features were derived from the spatial and temporal distribution of individual purchases, which annual per-category aggregates cannot reconstruct.
