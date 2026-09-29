---
title: "de Montjoye et al.: Unique in the shopping mall — reidentifiability of credit card metadata (with Sánchez et al. comment and reply)"
source: "https://doi.org/10.1126/science.1256297"
type: papers
ingested: 2026-09-29
fetched: 2026-09-29
content_format: pdf
extraction_tool: pdftotext
confidence: high
tags: [peer-reviewed, reidentification, anonymisation, card-transactions, unicity, adverse-evidence, item-level-data]
summary: "In 3 months of card records for 1.1 million people, four spatiotemporal points uniquely identify 90% of individuals; approximate price raises unicity by 22% on average; coarsening helps only slowly. A Science technical comment argues the risk is overstated (sample uniqueness, naive coarsening) and that k-anonymity works; the authors reply that the counter-example does not generalise to high-dimensional data."
---

# Unique in the shopping mall: On the reidentifiability of credit card metadata

Yves-Alexandre de Montjoye, Laura Radaelli, Vivek K. Singh, Alex "Sandy" Pentland, *Science* 347(6221): 536–539, 30 January 2015. The full report text was read in an author-hosted PDF copy. The debate appears in *Science* 351(6279): 1274, 18 March 2016. For the Sánchez, Martínez and Domingo-Ferrer comment (doi:10.1126/science.aad9295), the arXiv manuscript (arXiv:1808.01113, supplement arXiv:1511.05957) and the PubMed abstract were read. For the reply by de Montjoye and Pentland (doi:10.1126/science.aaf1578), only the PubMed abstract was accessible.

**Data and findings.** The dataset held 3 months of credit card transactions for 1.1 million users in 10,000 shops in an unnamed OECD country. It was "simply anonymized": no names, account numbers or obvious identifiers. Each transaction carried a date (1-day resolution), a shop and a price. Knowing four random spatiotemporal points (shop and day) makes 90% of individuals unique (ε4 > 0.9, Fig. 2), which exposes all their other records. Adding approximate price raises unicity by 22% on average (a = 0.50). Coarsening lowers unicity only slowly. At h = 15 days, v = 350 shops and a = 0.50, four points give ε4 < 0.15, but ten points give ε10 > 0.8 (Fig. 3). Women are more reidentifiable than men (ε4 0.93 vs 0.89; odds 1.214×). High-income people are more reidentifiable than low-income people (0.93 vs 0.88; odds 1.746×; Fig. 4). The authors conclude that such data "can probably not be anonymized by simply coarsening". Raw data were not released.

**Critique and reply.** Sánchez et al. make four points. First, the figures are probably overstated because 1.1 million people are only a sample of the country, and sample uniqueness does not imply population uniqueness. Second, reidentification still requires linking to an identified external source. Third, fixed-range, attribute-by-attribute coarsening is naive. Fourth, k-anonymity yields zero unequivocal reidentifications, with a random-guess success rate of 1/k. Their demonstration used a synthetic version of a Californian hospital discharge dataset (about 4 million patients), not the card data. In the published abstract, de Montjoye and Pentland reply that this "textbook" example "bears no resemblance to modern high-dimensional data sets" and that deidentification "should not be considered a useful basis for policy". The sampling objection is addressed empirically, for demographic attributes, by Rocher et al. 2019 ([Record](2026-09-29-profiling-rocher-incomplete-datasets-reidentification.md)).

**Evidence class and DAC8 transfer.** This is a peer-reviewed, frequently cited measurement of reidentification risk in item-level card metadata; the critique is also peer-reviewed. What it establishes: item-level records with shop, date and price are highly unique, so removing names does not anonymise them. What it does not establish: that actual attackers reidentify people, or that properly k-anonymised releases fail. The finding transfers to provider-held transaction logs with timestamps, counterparties and amounts. It does not transfer directly to the DAC8 report, which already names the person and contains annual aggregates per crypto-asset and transaction type rather than item-level shop/time/price tuples. For DAC8 the point is less reidentification than the richness of the underlying provider records.
