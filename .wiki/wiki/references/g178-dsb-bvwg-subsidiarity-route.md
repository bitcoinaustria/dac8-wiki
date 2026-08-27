---
title: "G 178/2024 and the DAC8 Citizen Remedy Chain"
category: reference
sources:
  - raw/articles/2026-08-27-vfgh-g178-2024-eimpfpass.md
  - raw/articles/2026-08-27-vfgh-g385-2018-elga.md
  - raw/articles/2026-08-27-vfgh-g-17-2024-admissibility.md
  - raw/articles/2026-08-27-austria-dsg-24-27-remedy-chain.md
  - raw/articles/2026-08-27-austria-vwgvg-appeal-and-delay.md
  - raw/articles/2026-08-27-austrian-dsb-complaint-guidance.md
  - raw/articles/2026-08-27-cjeu-c768-21-land-hessen.md
  - raw/articles/2026-08-27-bvwg-w211-2232955-dac2.md
  - raw/articles/2026-08-27-vfgh-e-2097-2021-dac2.md
  - raw/articles/2026-08-27-cjeu-foto-frost-c-314-85.md
  - raw/articles/2026-08-27-cjeu-kubera-c-144-23.md
created: 2026-08-27
updated: 2026-08-27
tags: [dac8, austria, vfgh, individualantrag, dsb, bvwg, subsidiarity, article-267]
aliases: [G 178 DAC8 route, DSB BVwG citizen route]
confidence: high
volatility: hot
verified: 2026-08-27
summary: "G 178/2024 makes a direct citizen Article 140 application against DAC8 processing highly vulnerable and shifts the primary route to a concrete DSB complaint, BVwG review, and judicial Article 267 or Article 140 escalation."
---

# G 178/2024 and the DAC8 Citizen Remedy Chain

> Bottom line: G 178/2024 is not a minor procedural risk. It is the closest current authority and makes a direct Article 140 application by an ordinary affected crypto-asset user highly likely to fail on subsidiarity. The stronger citizen route starts with actual provider processing before the first report, proceeds through the DSB to the BVwG, and can reach both the CJEU and the VfGH from that live case.

## Terminology

This article uses the Krypto-MPfG terms precisely. A **Kryptowert-Nutzer** under section 7(1) is a natural person or entity that is the customer of a reporting crypto-asset service provider and for whom reportable transactions are carried out. A **meldepflichtiger Nutzer** under section 7(4) is such a user who is a reportable person resident in a participating jurisdiction. A **non-reportable user** is only a working description for a user who does not meet section 7(4) for the relevant reporting period; it is not a separate statutory term. Citizenship alone does not decide this status, and self-custody alone does not create it.

“CASP” is used as readable shorthand. In a concrete proceeding, the entity's status as a reporting provider under sections 5 and 15 Krypto-MPfG, the relevant GDPR controller, and the correct respondent must be established separately.

## What G 178/2024 decided

The VfGH decided G 178/2024 on 28 April 2026. The applicant directly attacked mandatory eImpfpass processing and the statutory restriction of objection and erasure rights. He alleged current processing, section 1 DSG, Article 8 ECHR, informational self-determination, and GDPR violations.

The Court rejected the application without reaching the merits:

1. An Individualantrag is a subsidiary remedy. The statute must itself affect the applicant currently and directly, and no other reasonable route may exist.
2. Under section 24(1) DSG, a data subject can complain to the DSB about processing that allegedly violates the GDPR, section 1 DSG, or the first chapter of Article 2 DSG.
3. In that proceeding—possibly after a prior erasure request—the DSB must apply the statutory processing rules, including the challenged exclusions or restrictions of objection and erasure.
4. The DSB decision can be appealed under section 27 DSG to the BVwG.
5. The BVwG result can be challenged under Article 144 B-VG before the VfGH with the allegation that the prejudicial statutory provisions are unconstitutional.
6. The applicant's immediate prospects before the DSB are irrelevant to whether that route is reasonable.

The Court expressly left other defects undecided: challenge perimeter, adequate statement of constitutional concerns, and whether the direct applicability of the GDPR itself might independently preclude the Individualantrag. G 178/2024 therefore removes no other admissibility risk; it simply held that the alternative route was already dispositive.

## Why it maps closely to section 20 Krypto-MPfG

The analogy is unusually strong:

| G 178/2024 | DAC8/Krypto-MPfG user |
|---|---|
| Statute mandates personal-data processing | Section 20(1) mandates determination, collection, storage, and processing of reportable information for all customers, transactions, and crypto-assets |
| Data subject invokes section 1 DSG and GDPR | DAC8 claimant invokes the same rights plus Charter Articles 7, 8, and 52(1) |
| Objection or erasure is restricted by the statutory duty | A CASP will normally rely on Article 6(1)(c) GDPR and Krypto-MPfG duties to refuse erasure or continued restriction |
| DSB must apply the challenged processing law | DSB must apply sections 18–20 and the relevant due-diligence and retention provisions |
| DSB → BVwG → Article 144 VfGH | The identical domestic review chain is available |

The DAC2 litigation removes any suggestion that this is only a theoretical route for tax information. An Austrian individual used a DSB complaint against actual BMF processing, obtained BVwG review, and continued to the VfGH and VwGH. The claim failed on the merits and on the requested references, not because the route was unavailable.

## Red-team audit of proposed distinctions

| Attempted distinction | Assessment |
|---|---|
| The DSB cannot repeal a statute or invalidate DAC8 | Weak. G 178/2024 treated later BVwG and Article 144 review as sufficient. The DSB supplies the reviewable decision; it need not be the final norm-review court. |
| The DSB will reject processing expressly required by law | Expressly defeated. G 178/2024 says immediate DSB prospects do not matter. |
| The case raises EU-act validity, not only national constitutionality | Weak as an admissibility distinction. The BVwG is already a court able to refer under Article 267. Under Foto-Frost, it may reject an unfounded invalidity argument but cannot itself declare DAC8 invalid. |
| The CASP is a private company rather than a public e-health controller | Weak. Section 24 DSG applies to processing by private-sector controllers, and section 24(5) expressly provides remedial orders against them. |
| Reporting is cross-border and irreversible | Potentially relevant but not self-proving. A claimant must show an imminent transfer, why timely DSB/BVwG protection cannot prevent it, and why Article 58 corrective powers cannot supply effective protection. Starting in 2026 before the first 2027 report undercuts a self-created urgency argument. |
| The user has several CASPs | Usually weak. Known controllers can be identified separately. Mere multiplicity is not equivalent to the practically unknown and distributed provider set in the 2012 retention case. |
| The user does not know which authority will receive the data | Weak for section 20(1) source processing because the CASP is known. It may matter for later access and onward-transfer evidence, not for the availability of the first complaint. |
| The process will be slow and expensive | Weak. G 17/2024 requires special, extraordinary circumstances; ordinary time, cost, and process risk do not suffice. |
| Data-security and physical-security harm could occur before judgment | Relevant to the merits and to a request for timely protection, but normally insufficient by itself to erase the statutory review chain. The risk must be claimant-specific, technically supported, and linked to the actual dataset and recipients. |
| The user can rely on the exceptional retention-case route | Usually weak. DAC8 users normally know their CASP, records have a long horizon, and the ordinary route has already operated in DAC2. |

The best possible direct-application distinction is therefore not predicted failure. It is proof that the alternative route cannot provide effective protection before a concrete, irreversible injury. On the present statutory timeline, that is difficult: processing began on 1 January 2026, the first provider report for 2026 is due by 31 July 2027, and the BMF exchange follows within nine months after the reporting year.

## The primary citizen route

### 1. Select the right claimant and controller

Use an actual user whose data are already processed under the Krypto-MPfG and identify the exact controller. An Austria-home CASP is procedurally cleaner than a foreign-main-establishment provider because it reduces GDPR lead-authority and cross-border-cooperation disputes.

Claimant status changes the merits theory:

- A genuinely non-reportable user is the strongest claimant against the national section 20(1) extension because the complete tax dataset is processed even though it should never be reported.
- A reportable Austrian user is the proper claimant for a wider DAC8-validity challenge but cannot claim an incremental injury from the inclusion of non-reportable users.
- Citizenship is not the reporting criterion. Tax residence, participating-state status, dual residence, controlling-person status, and the relevant reporting period must be proved.

A CASP's direct Article 140 case should remain separate. G 178/2024 concerns the data-subject route; it does not answer whether a directly regulated provider with material compliance costs has a different reasonable remedy.

### 2. Build an evidence record before filing

An Article 15 request should ask for the personal data actually processed for Krypto-MPfG purposes, including:

- identity and tax-residence fields;
- the per-asset and per-category transaction values, units, counts, and transfer aggregates already generated or stored;
- the legal basis and exact Krypto-MPfG provisions relied on;
- sources, recipients or recipient categories, storage periods, access logs, processors, and third-country handling;
- whether the user is classified as reportable and why;
- whether a 2027 report is planned and which fields it is expected to contain.

Use Article 17 or 18 only where its conditions are actually pleaded. Article 21 objection is not a universal fallback: it ordinarily concerns Article 6(1)(e) or (f) processing, while the CASP will likely rely on Article 6(1)(c). A legally mismatched request creates noise rather than standing.

The controller normally has one month to respond under Article 12(3), with a possible reasoned extension. Preserve the request, delivery proof, answer, privacy notice, terms, account evidence, transactions, tax-residence self-certification, and all follow-up correspondence.

### 3. File the section 24 DSG complaint

The complaint should target the claimant's concrete processing, not ask the DSB for abstract review of DAC8. It should identify:

- the claimant and known CASP controller;
- the processing event and when the claimant learned of it;
- the exact affected data, purposes, classifications, retention, and planned transmission;
- the asserted personal rights: section 1 DSG and the applicable GDPR rights, supported where appropriate by Charter Articles 7, 8, and 52(1);
- the specific national and EU provisions whose application creates the conflict;
- a formal request to find the personal rights violation and grant appropriate relief.

File promptly. Section 24(4) extinguishes the treatment claim one year after knowledge and at the latest three years after the event. Do not rely on an untested theory that every day of continued processing restarts every deadline.

The DSB is not the Article 267 court. The DAC2 claimant's request that it arrange a CJEU reference was rejected. The DSB complaint should preserve EU-law and constitutional arguments, but the proposed reference belongs in the BVwG pleading.

The DSB proceeding is formally adversarial. The respondent can cure some violations during the case, creating a mootness issue under section 24(6). The complaint must distinguish a cured access defect from continuing statutory collection, profile generation, retention, or planned reporting.

### 4. Move the live case to the BVwG

A DSB merits decision is challenged within four weeks of service under section 7(4) VwGVG. The appeal must identify the decision and authority, grounds, requested result, and timeliness. Section 27 DSG provides a three-member BVwG senate with specialist lay judges.

The BVwG pleading should separate two judicial requests:

1. **National norm review.** If deciding the case requires a Krypto-MPfG provision and the BVwG has constitutional concerns, Articles 89(2), 135(4), and 140(1)(1)(a) B-VG require the court to apply to the VfGH. The party can give reasons and propose the perimeter but cannot itself compel the application.
2. **Article 267 reference.** If outcome depends on interpretation or validity of DAC8, the GDPR, or the Charter, the BVwG can refer to the CJEU. For section 20(1), an interpretation question about whether DAC8 permits universal creation of the complete reportable dataset is cleaner than an immediate attack on the whole directive. A reportable-user case can separately raise DAC8 validity.

If the DSB does not decide, section 8 VwGVG provides a delay complaint after six months unless a different period applies. Separately, section 24(8) DSG permits recourse where the DSB does not deal with the complaint or fails to provide a three-month progress or outcome update. These mechanisms address delay; they do not automatically suspend the CASP's statutory duties.

### 5. Preserve the VfGH path

If the BVwG decides against the claimant without obtaining the required constitutional review, an Article 144 B-VG complaint can be filed with the VfGH within six weeks after service under section 82 VfGG. It can allege violation of constitutionally guaranteed rights and injury through application of an unconstitutional law. The VfGH can initiate review of a prejudicial national provision and, where a necessary EU question remains, make an Article 267 reference.

The claimant should also assess the separate VwGH route. It is not automatic: admissibility depends on a qualifying legal question, and the DAC2 revision shows that abstract or poorly formulated reference requests can fail. Supreme-court deadlines, representation, fees, parallel filing, and transfer options require case-specific counsel review.

## Proposed issue architecture

### Non-reportable user: national excess

The factual proposition is that the CASP creates and stores the full section 18 transaction dataset for a user finally classified as non-reportable. The legal questions are whether section 20(1) is compatible with section 1 DSG and Articles 7, 8, and 52(1) Charter, and whether DAC8 read with the GDPR permits or requires that national expansion.

The less intrusive counterfactual must be operational: obtain universal self-certification and retain the evidence needed to determine residence, but create the annual reportable transaction profile only for a reportable user, with a defined reclassification process for changed circumstances.

### Reportable user: DAC8 validity

The factual proposition is current creation of the identity-linked annual crypto profile that will be transmitted under DAC8. The case must confront the adverse DAC2 trilogy and prove why the exact crypto dataset, available correlation, access structure, retention, and consequences create a materially different interference. Generic mass-surveillance, hacking, or wealth-register rhetoric is not enough.

### Later authority-processing case

Before the first report, the concrete respondent is normally the CASP processing data under section 20. Once information is transmitted and processed by Austrian tax authorities, a separate complaint against the responsible authority may become possible. The claims must not be blurred: source processing, national receipt, onward exchange, and foreign-authority processing are distinct acts with different controllers and evidence.

## Stop/go checklist

Do not file the lead citizen case until the file can answer yes to the applicable questions:

- Is there post-1 January 2026 processing by an identified controller?
- Is the claimant's reportable or non-reportable status proved for the exact period?
- Does the Article 15 response reveal the concrete section 18/20 data and retention position?
- Are the complaint event and knowledge dates within section 24(4)?
- Is the alleged violation personal rather than an abstract attack on public policy?
- Is the national-excess case separated from the DAC8-validity case?
- Is one proposed Article 267 question necessary to decide the live dispute?
- Is the requested national challenge perimeter complete but no broader than necessary?
- Is any claim of irreversible pre-judgment harm supported by dates, transfer mechanics, and evidence about unavailable protection?

## Strategic verdict

For an ordinary user, trying the direct Individualantrag first creates a foreseeable inadmissibility loss and may waste the best factual record. The campaign should describe G 178/2024 honestly: it does not defeat the fundamental-rights challenge, but it changes the required vehicle.

The recommended architecture is:

**user processing record → section 24 DSG complaint → BVwG → Article 267 and/or court-initiated Article 140 review → Article 144 VfGH**, with a separate, evidence-backed CASP Individualantrag where provider standing and the absence of another route can be established.

## See Also

- [[vfgh-to-cjeu-dac8-route|VfGH-to-CJEU DAC8 Route]] ([VfGH-to-CJEU DAC8 Route](../theses/vfgh-to-cjeu-dac8-route.md))
- [[individualantrag-article-140|Individualantrag under Article 140 B-VG]] ([Individualantrag under Article 140 B-VG](../concepts/individualantrag-article-140.md))
- [[dac2-crs-austrian-litigation|Austrian DAC2/CRS Litigation]] ([Austrian DAC2/CRS Litigation](../topics/dac2-crs-austrian-litigation.md))
- [[austrian-gold-plating-and-claimant-audit|Austrian DAC8 Gold-Plating and Claimant Audit]] ([Austrian DAC8 Gold-Plating and Claimant Audit](austrian-gold-plating-and-claimant-audit.md))
- [[epicenter-vorratsdatenspeicherung-precedent|Epicenter/AKVorrat Data-Retention Precedent]] ([Epicenter/AKVorrat Data-Retention Precedent](epicenter-vorratsdatenspeicherung-precedent.md))

## Sources

- [VfGH G 178/2024](../../../legal-docs/supporting/at-vfgh-g178-2024.pdf)
- [VfGH G 385/2018](../../../legal-docs/supporting/at-vfgh-g385-2018-elga.pdf)
- [VfGH G 17/2024](../../../legal-docs/core/at-vfgh-g17-2024.pdf)
- [DSG consolidated snapshot](../../../legal-docs/core/at-dsg-consolidated-2026.html)
- [VwGVG consolidated snapshot](../../../legal-docs/core/at-vwgvg-consolidated-2026.html)
- [Official DSB complaint guidance](https://dsb.gv.at/eingabe-an-die-dsb/beschwerde)
- [GDPR](../../../legal-docs/core/eu-gdpr-regulation-2016-679.pdf)
- [CJEU C-768/21, Land Hessen](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:62021CJ0768)
- [Austrian DAC2 BVwG judgment](../../../legal-docs/core/at-bvwg-w211-2232955-1-7e.pdf)
- [Foto-Frost](../../../legal-docs/core/eu-cjeu-c314-85-foto-frost.pdf)
- [KUBERA](../../../legal-docs/core/eu-cjeu-c144-23-kubera.pdf)
