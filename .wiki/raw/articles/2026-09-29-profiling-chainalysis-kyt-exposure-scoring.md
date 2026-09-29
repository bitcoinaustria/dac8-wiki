---
title: "Chainalysis KYT: attribution-based exposure scoring of customer crypto transactions (vendor description)"
source: "https://www.chainalysis.com/glossary/know-your-transaction/"
type: articles
ingested: 2026-09-29
fetched: 2026-09-29
content_format: html
extraction_tool: web-fetch
confidence: low
tags: [vendor, commercial-bias, blockchain-analytics, risk-scoring, profiling, gambling, casp-monitoring]
summary: "Chainalysis describes KYT as continuous screening of customers' incoming and outgoing transactions, attributing addresses to real-world entities and scoring direct and multi-hop indirect exposure to risk categories that include gambling services and crypto ATMs; accuracy is not disclosed."
---

# Chainalysis Know Your Transaction (KYT)

Two vendor pages were read through a text-extraction tool: the Chainalysis glossary entry "What Is Know Your Transaction (KYT)?" (undated) and the blog post "Chainalysis KYT Alerts" (Chainalysis Team, 22 August 2019, https://www.chainalysis.com/blog/chainalysis-kyt-alerts/).

**Vendor description.** KYT screens "incoming and outgoing cryptocurrency transactions continuously". It starts by "attributing wallet addresses to real-world entities". Each transaction receives a risk score based on "direct exposure" (funds sent to or received from a risky entity) and "indirect exposure" (funds connected "through intermediary hops … as many hops as needed until an identified service is reached"). The glossary adds that machine learning is used to detect patterns such as structuring, layering and peel chains. The 2019 post lists alert categories: darknet markets, terrorist financing, sanctioned addresses, stolen funds, scams, ransomware, "gambling services", mixers, "cryptocurrency ATMs", high-risk exchanges, and fundraising for illicit or violent activity. The post says Chainalysis labels an address with an entity name only when "100% sure", but gives neither database size nor error rates.

**Evidence class and DAC8 transfer.** This is commercial self-description with an evident interest in presenting the product as accurate and necessary, so confidence is low. It establishes that CASPs routinely run automated counterparty-category scoring on identified customers' transactions. Those categories include lawful but potentially sensitive activity (gambling). It does not establish accuracy; independent validation of clustering is covered by existing wiki sources on Kappos et al. and "ghost clusters". It concerns AML/CFT processing by providers, not DAC8 reporting. It shows that provider-held records already contain a derived behavioural layer, which falls under the WP29 definition of inferred personal data and, where sensitive, under C-252/21's Article 9 test.
