---
title: "EU DAC8 XML: correction and deletion message types"
source: "https://eur-lex.europa.eu/eli/reg_impl/2025/2263/oj"
type: articles
ingested: 2026-09-04
fetched: 2026-09-04
content_format: pdf
tags: [eu, dac8, xml, correction, deletion, implementing-regulation, primary-law]
summary: "The binding DAC8 exchange schema includes typed correction and deletion records and references to the earlier message and document."
---

# EU DAC8 XML: correction and deletion message types

Annex XVIII to Commission Implementing Regulation (EU) 2025/2263 defines the DAC8 computerised exchange format.

The `DocTypeIndic` enumeration distinguishes new data (`OECD1`), corrected data (`OECD2`) and deletion of data (`OECD3`). A correction or deletion message uses `CorrMessageRefId` and `CorrDocRefId` to identify the earlier message and record. The schema documentation states that a `CARF702` message may contain corrections, deletions or both, but not new data.

This establishes that corrections and deletions are technically supported in the inter-authority exchange. It does not by itself establish the substantive grounds on which a data subject can demand either operation, a pre-filing hearing, or deletion of every downstream copy. Those questions remain controller-, purpose- and copy-specific.

