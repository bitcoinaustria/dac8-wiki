---
title: "Ghost Clusters denominator and coverage supplement"
source: "https://www.usenix.org/system/files/usenixsecurity25-lubbertsen.pdf"
type: papers
ingested: 2026-09-30
fetched: 2026-09-30
content_format: pdf
tags: [blockchain-analysis, ground-truth, false-discovery-rate, recall, correction]
confidence: high
credibility_score: 4
summary: "Figure 1 supports service-specific label precision and varying recall, but lacks a population-negative denominator for classical FPR."
---

# Ghost Clusters denominator supplement

Supplement to the preserved 4 September digest; USENIX Security 2025, printed pp. 1360–1363 and 1370, Figure 1.

For BestMixer/Hansa/Wall Street, true positives are 44,821/913,171/525,236 and false labels 19/1,695/611. Ground-truth address totals are 182,612/1,157,519/553,777; recall is 24.54%/78.89%/94.85%.

Published FP percentages divide by ground-truth addresses, not all genuine negatives. Own calculation FP/(TP+FP), the false discovery share among labels, gives 0.0424%/0.1853%/0.1162%. No population FPR can be calculated without the negative denominator. High label precision can coexist with low coverage.

These are three service-address sets in a commercial snapshot, not validated natural-person identity or total wealth. Historical raw text remains unchanged.

Scoring: peer-reviewed +2, recent +1, recognised researchers +1.
