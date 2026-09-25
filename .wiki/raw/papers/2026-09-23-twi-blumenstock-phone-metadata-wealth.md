---
title: "Blumenstock, Cadamuro & On: Predicting poverty and wealth from mobile phone metadata"
source: "https://doi.org/10.1126/science.aac4420"
type: papers
ingested: 2026-09-23
fetched: 2026-09-23
content_format: pdf
extraction_tool: web-fetch
tags: [peer-reviewed, wealth-inference, behavioural-metadata, machine-learning, feature-granularity, mobile-phone-data]
summary: "Several thousand features engineered from individual call-detail logs predicted a survey wealth index for 856 Rwandan subscribers with cross-validated r = 0.68, and far better (r ≈ 0.92) once predictions were averaged by district; individual-level error remains substantial and the inputs are item-level logs, not annual totals."
---

# Predicting poverty and wealth from mobile phone metadata

Joshua Blumenstock, Gabriel Cadamuro, Robert On. *Science* 350(6264):1073–1076, 27 November 2015. DOI: 10.1126/science.aac4420. Inspected: the full article PDF (author copy, jblumenstock.com), including Figs. 1–3 and Table 1. The supplementary materials (feature list, table S1, robustness checks) were not inspected.

**Data and granularity.** The input was an anonymised database of "billions of interactions" (calls and text messages) from Rwanda's largest mobile operator, covering about 1.5 million subscribers. For training, the operator's records were linked, with consent, to a phone survey of a geographically stratified random sample of 856 subscribers (~75 questions on assets, housing and welfare). The input is **item-level**: each subscriber's own transaction log (timing, direction, counterparty, cell tower location). An automated combinatorial procedure turned each log into several thousand metrics: total volume, intensity, timing and direction of communication, contact-network structure, and mobility/migration patterns from geospatial markers (p. 1074). Elastic-net regularisation then kept a sparse model.

**Target and accuracy.** The target was a composite wealth index: the first principal component of survey asset and housing answers. It is not income or monetary balances. Individual level: cross-validated correlation between predicted and survey wealth **r = 0.68** (p. 1074, Fig. 1A). Binary asset ownership: AUC 0.85 (electricity), 0.67 (motorcycle), 0.84 (television), 0.88 (fridge). Across all survey questions, AUCs ranged from 0.50 to 0.88. Identifying the relatively poor: AUC 0.72 at the 5th percentile and 0.81 at the 25th percentile (Fig. 1B–C). Aggregate level: district means of out-of-sample predictions correlated with a 12,792-household government survey (DHS 2010) at **r = 0.917** (phone-owning households) and r = 0.916 (all households) over 30 districts. At the level of 492 DHS clusters (village-sized) the correlation was r = 0.79 (Fig. 3, p. 1075–1076). The authors say the geographic correlations are "partially driven" by stark urban–rural differences, but they persist within urban and rural strata.

**Stated limits.** The model was trained on a small sample and cross-validated to limit overfitting. The authors report that the automated high-dimensional feature approach performed significantly better than a small set of hand-crafted metrics (table S1, not inspected). Micro-regional estimates below district level could not be checked against ground truth. Privacy and operator commercial concerns are named as the main obstacle to wider use. The setting is a low-income country where phone use tracks wealth closely, and the target is a relative asset index.

**Relevance to annual aggregate reports.** This establishes that behavioural transaction records can rank individuals by relative wealth better than chance, with moderate individual-level accuracy (r = 0.68, i.e. roughly 46% of variance). Accuracy becomes high only after averaging over many people. It does **not** establish that a few annual totals per category (sum, units, count) allow reliable estimation of an individual's wealth, balance or income. The model depended on thousands of features derived from timestamps, counterparties and locations. The authors themselves report that a small set of simple hand-made metrics did worse. The target was also a relative asset index rather than a monetary amount.
