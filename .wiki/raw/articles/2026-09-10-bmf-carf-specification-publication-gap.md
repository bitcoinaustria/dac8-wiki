---
title: "BMF CARF reporting specification: the referenced technical rules are not public, unlike every comparable regime"
source: "https://www.bmf.gv.at/services/finanzonline/informationen-fuer-softwarehersteller/softwarehersteller-erklarungen-und-antraege.html"
type: articles
ingested: 2026-09-10
fetched: 2026-09-10
tags: [krypto-mpfg-dv, article-18-b-vg, publication, legalitaetsprinzip, bmf, finanzonline, dac7, gmsg]
summary: "Section 2(2) and section 4 Krypto-MPfG-DV both refer to technical specifications on the BMF website; no CARF specification is publicly retrievable, while DAC7, GMSG, CbC, GIR and Kontenregister packages are freely downloadable."
---

# The CARF specification publication gap

## Fact captured

The Krypto-MPfG-Durchführungsverordnung, BGBl. II Nr. 331/2025, uses the same dynamic reference twice, not once. § 4 (transmission of the report) and § 2 Abs. 2 (exemption notification under § 16) both state that the required organisational and technical specifications, "z. B. XML-Struktur; WSDL", are available on the BMF website and in the provider portal. The regulation contains no annex, no data-set description and no field list.

As at 10 September 2026 no CARF specification is publicly retrievable. It is absent from the software-developer page for other declarations, the banks page carrying GMSG and Kontenregister, the FinanzOnline "Sonstige Funktionen" webservice list, the `art` code list of the general File-Upload-Webservice (Stand 4 March 2026), the BMF's own automatic-exchange overview page, Findok and RIS.

Every comparable regime publishes a complete package without authentication:

- DAC7 / DPMG: general specification with a Stand date, a schema bundle, an error-code catalogue and a document-version file.
- DAC2 / GMSG: the same set for CRS 2.0, and already for CRS 3.0 from January 2027, including a field-level `GMSG_Datensatzaufbau_v2.xlsx`.
- Kontenregister, CbC and the Pillar 2 GIR: likewise.

The registration side of the crypto regime is public: § 3 DV names the web form IIN-CAO, and form IIN-CAO1 exists in the BMF form index. Only the reporting specification is missing.

The BMF told the WKO on 14 August 2025, in relation to the CRS limb of DAC8, that "Eine Veröffentlichung der angepassten österreichischen Meldevorgaben ist für Anfang Februar 2027 geplant" for a reporting period that began on 1 January 2026.

Findok returns zero documents for "Krypto-MPfG", "Krypto-Meldepflichtgesetz" and "CARF". By contrast GMSG has a Richtlinie and an annually refreshed BMF-Info on participating states, most recently 21 April 2026, resting on the published Verordnung BGBl. II Nr. 64/2026. DPMG has a BMF-Info FAQ.

## Research use

The drafting technique is not an outlier. § 3 DPMG-Durchführungsverordnung, BGBl. II Nr. 490/2022, uses materially the same formula. The argument should therefore not be that website references are per se unlawful, which invites the adverse authority on recognised technical standards.

The argument that fits the evidence is narrower: a dynamic reference whose referent is neither kundgemacht nor publicly accessible fails the determinacy and publicity requirements of Article 18 B-VG, and the BMF's uniform practice across six neighbouring regimes shows that publication was both possible and expected.

## Open point

Whether the specification exists behind the authenticated provider portal is unestablished. Both "gated but present" and "not yet produced" remain live. A written Auskunftsbegehren to the BMF asking whether, where and when the § 4 specifications were published would settle it, and an absent answer is itself evidence.
