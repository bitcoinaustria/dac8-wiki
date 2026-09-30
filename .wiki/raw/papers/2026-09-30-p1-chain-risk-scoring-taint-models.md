---
title: "Towards Risk Scoring of Bitcoin Transactions: taint rules and an uncalibrated historic pilot"
source: "https://maltemoeser.de/paper/risk-scoring.pdf"
type: papers
ingested: 2026-09-30
fetched: 2026-09-30
published: 2014
authors: [Malte Möser, Rainer Böhme, Dominic Breuker]
institution: University of Münster
venue: "Financial Cryptography and Data Security 2014 workshops; Bitcoin Research"
doi: "10.1007/978-3-662-44774-1_2"
version: "Author-hosted PDF, 17 PDF pages; not asserted identical to publisher pagination"
sha256: "2c5bbcebf7f9e7fcfe0b9705268da3e2d90dc261765a2ae4d75612fb1e2d9381"
content_format: pdf
extraction_tool: pdftotext-layout
extraction_status: selective-source-digest
tags: [bitcoin, taint, poison, haircut, fifo, risk-scoring, sampling]
summary: "Different taint-propagation policies assign different consequences to the same transaction graph; the theft pilot was too small and heterogeneous to calibrate a predictor."
quality: 4
credibility_score: 2
confidence: medium
locators: "Author PDF section 3.1/pages 6-7/Figure 2; section 4.1/page 9; section 4.3/pages 11-12/Table 2; Conclusion/page 15"
---

## Source digest

Poison marks descendants invalid after any tainted ancestor; haircut propagates a proportional amount; FIFO is another allocation policy. These are analytical/normative choices, not uniquely serialized paths of particular input value into particular outputs. Figure 2 contrasts consequences under different rules on one graph. The empirical pilot selected community-listed major thefts from 2011–2013: nine had transaction hashes, six timestamps and only three usable transactions before the assumed disclosure time. Table 2 compares small incident samples of 7, 8 and 82 transactions with 112 controls each. The authors report that their data could not establish acceptable predictors or calibrate the risk model. Neither civil-identity precision nor wealth-estimation accuracy was tested.

[Institutional publication record](https://www.wi.uni-muenster.de/research/publications/93356) confirms the peer-reviewed 2014 workshop publication. Mechanical score 2: peer-reviewed +2, recognized institution +1, age over ten years −1. Historic non-representative sampling limits empirical transfer; the paper remains useful for distinguishing graph facts from propagation assumptions.
