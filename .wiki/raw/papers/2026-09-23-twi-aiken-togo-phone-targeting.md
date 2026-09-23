---
title: "Aiken, Bellue, Karlan, Udry, Blumenstock: Phone-data ML targeting in Togo leaves about half of the poor excluded"
source: "https://www.nber.org/system/files/working_papers/w29070/w29070.pdf"
type: papers
ingested: 2026-09-23
fetched: 2026-09-23
content_format: pdf
extraction_tool: web-fetch
tags: [adverse-evidence, mobile-phone-metadata, poverty-prediction, targeting-errors, model-drift, individual-level-accuracy]
summary: "Phone metadata with machine learning ranks individuals by poverty only moderately well (AUC 0.70-0.73, rho about 0.46 with consumption); about 50-53% of the true poor are still excluded, and accuracy decays when the model or data are 18 months old."
---

# Machine Learning and Mobile Phone Data Can Improve the Targeting of Humanitarian Assistance

Emily Aiken, Suzanne Bellue, Dean Karlan, Christopher R. Udry, Joshua Blumenstock. NBER Working Paper 29070 (July 2021, revised June 2022). The peer-reviewed version is in *Nature* 603, 864-870 (2022), doi:10.1038/s41586-022-04484-9. I inspected the full NBER PDF text (main text pp. 4-6, Methods sections "Model Training", "Temporal Stability of Results" and "Targeting Evaluations"). The paper is a flagship *pro* study (Togo's Novissi COVID cash transfers). It is included here because its own figures set upper bounds on individual-level accuracy.

Data: call-detail records (CDR, i.e. phone metadata) for millions of Togolese subscribers, including counts, timing and location of calls, airtime top-ups, mobile-money and data usage. These are linked to a 2020 phone survey (ground truth: a proxy-means-test (PMT) score and an asset index) and to the 2018-19 national household survey (ground truth: consumption). Method: gradient-boosting models trained on the matched subsample, then evaluated out of sample on reaching the poorest 29%.

Figures: the correlation between phone-based predictions and consumption is 0.46, and 0.41 against the PMT (Methods, "Model Training", Extended Data Table 6). Location-only features alone reach 0.42 and 0.35. Targeting AUC is 0.70 for rural Novissi and 0.73 for a hypothetical national programme (pp. 4-5, Table 1). Exclusion errors (1 - recall) remain **53%** (rural) and **50%** (national). The phone-based approach beats geographic targeting (59-78% exclusion). It is worse than a perfectly calibrated PMT (AUC 0.85) or a poverty probability index (AUC 0.81), and only "approximately as accurate" as an asset index (AUC 0.55-0.75) (p. 6). A parsimonious rule based on phone *spending* alone gives AUC 0.57 and 0.63, "substantially worse" (p. 5). When the model or CDR data are about 18 months out of date, accuracy falls by 4-6% and precision by 10-14%. The authors note that these losses are "nearly as large as the gains" over geographic targeting (p. 6; Extended Data Table 4). The authors also state that the gains are largest in homogeneous populations and depend on training with "current and representative" survey data.

Limits for the thesis: even with thousands of rich behavioural features and a fresh, locally calibrated ground truth, individual-level rank prediction of economic status explains only a modest share of the variance (rho about 0.4-0.5). Roughly one in two target individuals is misclassified at a 29% cutoff. A spending-only aggregate, which is closer to what DAC8 totals provide, performs markedly worse. The study does NOT show that such inference is useless. It improves coarse targeting relative to geography, so the evidence supports probabilistic ranking or prioritisation rather than reliable estimation of a given person's wealth or income level. It also concerns consumption poverty in a low-income country, not balances of crypto-asset holders.
