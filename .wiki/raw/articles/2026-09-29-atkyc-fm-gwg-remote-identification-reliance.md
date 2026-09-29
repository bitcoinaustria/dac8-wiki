---
title: "FM-GwG identification, remote-identification, third-party reliance and penalty provisions (consolidated 29 September 2026)"
source: "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009769"
type: articles
ingested: 2026-09-29
fetched: 2026-09-29
content_format: html
confidence: high
tags: [austria, fm-gwg, cdd, remote-identification, qualified-electronic-signature, reference-payment, third-party-reliance, casp, penalties, enacted-law]
summary: "FM-GwG sections 1, 6(1)-(4), 7(6)-(7), 13, 15, 34, 37 and Annex III as in force on 29 September 2026: the closed list of remote-identification substitutes, reliance on third parties, and penalty caps. Complements the existing 2026-08-27 FM-GwG digest; it does not measure compliance."
---

# FM-GwG: remote identification, reliance and penalties

RIS consolidated FM-GwG (BGBl. I 118/2016 as amended), version of 29 September 2026. This digest covers only the provisions on how identity is established remotely and who may be relied on. Section 11a and the reporting duties are covered in the existing `2026-08-27-austria-fm-gwg-current-crypto.md`.

**Scope and identification standard.**
- **Who is covered (§ 1 Abs. 1):** credit and financial institutions and "Anbieter von Kryptowerte-Dienstleistungen" (CASPs).
- **Basic identification duty (§ 6 Abs. 1 Z 1):** identify the customer and verify identity using documents, data or information from a credible and independent source. This includes electronic identification means, eIDAS trust services, and other secure remote or electronic procedures "nach Maßgabe des Abs. 4".
- **Default for natural persons (§ 6 Abs. 2 Z 1):** in-person presentation of an official photo ID issued by a state authority.

**Remote-identification substitutes (§ 6 Abs. 4).** Where there is no personal contact, in-person presentation may be replaced by safeguards. The obliged entity must always know the customer's name, date of birth and address. The permitted safeguards are:
- **Z 1:** video-based online identification (details in the Online-IDV);
- **Z 2:** a statutory electronic ID procedure providing the same information as a photo ID;
- **Z 3:** the customer's declaration signed with a QES (Art. 3 Z 12 eIDAS), or registered-mail delivery to the stated residence, subject to three conditions:
  - lit. a: for a legal person, a declaration that its registered seat is also its seat of central administration;
  - lit. b: a copy of the ID before contract conclusion, **unless the contract is concluded electronically by QES**;
  - lit. c: for customers resident in a third country, written confirmation from another credit institution that it identified the customer;
- **Z 4:** the first payment runs through an account in the customer's name at a credit institution within § 13, plus copies of documents that make the customer's details credible. Instead of copies, written confirmation from that credit institution that it identified the customer is enough.

The final sentence of § 6 Abs. 4 empowers the FMA to set online-identification safeguards by regulation, in particular on data security, forgery resistance and staff.

**Risk classification and consequences.**
- **Annex III Z 2 lit. c:** lists non-face-to-face relationships *without* such safeguards as a factor of potentially higher risk.
- **§ 7 Abs. 6:** CDD must be reapplied to existing customers on a risk basis, including where the obliged entity has a duty under Directive 2011/16/EU (DAC).
- **§ 7 Abs. 7:** if CDD cannot be completed, no transaction may be carried out, no relationship may be opened, and an existing relationship must be ended. An STR must be considered.

**Reliance and outsourcing.**
- **Reliance on third parties (§ 13 Abs. 1–2):** obliged entities may rely on third parties for § 6 Abs. 1 Z 1–5 and 7 unless there are indications that equivalent performance is doubtful. Final responsibility stays with the obliged entity. It must promptly obtain the CDD information and be able to get copies on request, including for eIDAS and § 6 Abs. 4 remote procedures.
- **Who counts as a third party (§ 13 Abs. 3–4):**
  - domestic credit and financial institutions, excluding pure bureaux de change;
  - certain professions;
  - domestic insurance intermediaries;
  - EU and equivalent third-country institutions that are subject to equivalent CDD rules and supervision.
  The text read does not expressly list CASPs as qualified third parties. This is noted, not confirmed as intended.
- **Outsourcing (§ 15):** the third-party section does not apply where, by contract, the outsourcing provider counts as part of the obliged entity.

**Penalties (§ 34, § 35, § 37).**
- **§ 34 Abs. 1:** breaches of §§ 5–12, of the § 6 Abs. 4 regulation (Online-IDV) and of §§ 13–15 are administrative offences, with fines up to EUR 150,000 for the responsible person.
- **§ 34 Abs. 4:** for serious, repeated or systematic CDD breaches, the cap is EUR 5,000,000 or twice the benefit gained.
- **§ 35:** allows fines on legal persons.
- **§ 37 Abs. 1–2:** allows naming on the FMA website, and requires publication of final fines.

Evidence class: enacted statute (primary legal source). For DAC8, the key structural points are these:
- The QES route (Z 3) lets an Austrian obliged entity onboard a domestic or EU customer without an ID copy. It therefore relies on the identity proofing done by the QES trust-service provider.
- The reference-account route (Z 4) relies on a prior credit institution's identification.

Both routes can therefore chain one earlier identification into later accounts. That is an inference from the text; the A-FIU and NRA 2025 describe this chaining in practice. The provisions show safeguards and sanctions exist. They do not show error rates.
