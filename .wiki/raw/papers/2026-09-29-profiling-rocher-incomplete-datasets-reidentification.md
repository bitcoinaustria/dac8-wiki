---
title: "Rocher, Hendrickx & de Montjoye: Estimating the success of re-identifications in incomplete datasets"
source: "https://doi.org/10.1038/s41467-019-10933-3"
type: papers
ingested: 2026-09-29
fetched: 2026-09-29
content_format: html
extraction_tool: web-fetch
confidence: medium
tags: [peer-reviewed, reidentification, anonymisation, sampling, gdpr-anonymisation, demographic-attributes]
summary: "A generative model estimates that 99.98% of Americans would be correctly re-identified in any dataset from 15 demographic attributes, and the authors reject the argument that releasing only a sample provides plausible deniability; the attributes are demographic, not transactional."
---

# Estimating the success of re-identifications in incomplete datasets using generative models

Luc Rocher, Julien M. Hendrickx, Yves-Alexandre de Montjoye, *Nature Communications* 10: 3069 (2019), open access (PMC6650473). The PMC full text was read through a text-extraction tool; figures below come from that reading.

**Findings.** Using a copula-based generative model, the authors estimate that "99.98% of Americans would be correctly re-identified in any dataset using 15 demographic attributes". The model predicts individual uniqueness with mean AUC from about 0.89 (trained on a 1% sample) to 0.93. The authors state that their results "reject the claims" that sampling or releasing partial datasets provides plausible deniability. They add that even heavily sampled anonymised datasets are unlikely to meet the GDPR's anonymisation standard.

**Relevance and limits.** This is the empirical answer to the sample-versus-population uniqueness objection that Sánchez et al. raised against the 2015 card-metadata study ([Record](2026-09-29-profiling-demontjoye-shopping-mall-reidentification.md)). Confidence is medium for this path because the attributes are demographic (age, sex, ZIP code, etc.), not transactions, and the paper is by the same group whose earlier work was criticised. For DAC8 it supports only the general point: pseudonymised or sampled extracts of provider records should not be presumed anonymous. The DAC8 report itself is not anonymised, since it carries name, address and TIN.
