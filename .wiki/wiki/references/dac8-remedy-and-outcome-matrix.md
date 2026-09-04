---
title: "DAC8 Remedy and Outcome Matrix"
category: reference
sources:
  - raw/articles/2026-09-04-cjeu-c46-23-supervisory-erasure-power.md
  - raw/articles/2026-09-04-cjeu-c129-21-proximus-recipient-propagation.md
  - raw/articles/2026-09-04-cjeu-c121-14-severability.md
  - raw/articles/2026-09-04-cjeu-case-66-80-invalidity-effect.md
  - raw/articles/2026-09-04-cjeu-c191-14-borealis-temporal-effects.md
  - raw/articles/2026-09-04-vfgh-g252-2016-g188-2021-challenge-scope.md
  - raw/articles/2026-09-04-austria-vfgh-and-dsb-remedy-effects.md
  - raw/articles/2026-09-04-cjeu-c378-17-administrative-disapplication.md
  - raw/articles/2026-09-04-eu-dac8-xml-correction-deletion.md
  - raw/articles/2026-09-04-ecthr-ferrieri-bonassisa-tax-bank-data-review.md
  - raw/articles/2026-09-04-austria-bvg-vfgg-annulment-temporal-effects.md
  - raw/articles/2026-09-04-bvg-article-139-regulation-effects.md
  - raw/articles/2026-09-04-vfgg-85-suspensive-effect.md
  - raw/articles/2026-09-04-vfgg-87-binding-restoration.md
  - raw/articles/2026-09-04-austria-dsg-section-24-complaint-relief-correction.md
  - raw/articles/2026-09-04-austria-vwgvg-merits-substitution.md
  - raw/articles/2026-09-04-gdpr-articles-19-58-correction-propagation.md
  - raw/articles/2026-09-04-austria-individual-application-anlassfall-effect.md
  - raw/articles/2026-09-04-edpb-document-5-2021-article-55-2-complaints.md
  - raw/articles/2026-09-04-cjeu-2024-recommendations-accelerated-procedure.md
created: 2026-09-04
updated: 2026-09-04
tags: [dac8, krypto-mpfg, dsb, bvwg, vfgh, cjeu, remedies, legal-effects]
aliases: [DAC8 success ladder, Krypto-MPfG remedy matrix]
confidence: high
volatility: hot
verified: 2026-09-04
summary: "Forum-by-forum map distinguishing evidence, individual relief, concrete disapplication, limiting interpretation, national annulment, EU invalidity and operational effect."
---

# DAC8 Remedy and Outcome Matrix

> A favourable ruling, a binding legal consequence and an operational stop are separate dimensions. The requested remedy should name all three.

## Forum and legal effect

| Forum | Legally available favourable result | Persons and acts directly affected | What does not follow automatically |
|---|---|---|---|
| DSB | Access, correction, restriction, erasure, recipient information, specified compliance step, processing limit or prohibition | Identified controller or processor and the processing within the order | Annulment of Krypto-MPfG or invalidity of DAC8 |
| BVwG | Full factual and legal review; merits decision under section 28 VwGVG or remittal; concrete disapplication of conflicting national law; application to the VfGH; Article 267 reference | The DSB proceeding and parties; concrete national-law non-application where EU primacy requires it | General removal of national text or independent invalidation of DAC8 |
| VfGH under Article 144 | Annulment of the BVwG judgment and binding constitutional direction for the renewed proceeding | The originating matter; administrative institutions must restore a conforming legal state | Direct provider-facing deletion or prohibition order |
| VfGH under Articles 139 or 140 | Annulment of the properly delimited Austrian regulation or statutory provisions | Binding removal subject to publication and any delayed effect | Invalidity of DAC8 or automatic removal of every downstream copy |
| CJEU under Article 267 | Binding interpretation or invalidity of a severable EU provision | Referring court directly; an invalidity ruling supplies other national courts sufficient reason to treat the EU provision as invalid | Decision of the Austrian facts, amendment of Austrian statutory text or guaranteed immediate effect |

The DSB row does not identify which national supervisory authority may issue the binding decision. Article 55(2) covers private bodies as well as public authorities where the specific processing rests on Article 6(1)(c) or (e) GDPR; Article 56 then does not apply. For Krypto-MPfG processing attributed to Article 6(1)(c), the controller, sections 15 to 17 nexus, any exemption and the Member State concerned must be established. Article 77 may permit lodging the complaint with another authority, but that does not necessarily make it the authority competent to decide the complaint. Other provider purposes require a separate competence analysis and may remain within Article 56.

## Outcome ladder

1. **Evidence outcome:** binding access to the person's data, processing facts, actual recipients and identified consultation information.
2. **Accuracy and propagation outcome:** restriction or correction at source, recipient notice and a traceable correction or deletion message where legally required.
3. **Individual processing outcome:** final prohibition or material limit on an identified collection, profile, retention, join, use or transfer.
4. **Structural interpretation outcome:** binding interpretation that excludes a field, user group, duration or use, or requires an operative safeguard.
5. **National norm outcome:** removal of the necessary and severable Krypto-MPfG or implementing-regulation provisions without leaving the same processing duty intact.
6. **EU validity outcome:** invalidity of a necessary and severable DAC8 provision, with national courts no longer applying it subject to the CJEU's temporal ruling.
7. **Operational system outcome:** the challenged processing can no longer occur in materially the same form and existing copies are corrected, restricted or deleted where the governing law permits.

## Copy-by-copy remedy chain

| Data layer | Potential operative remedy | Proof required |
|---|---|---|
| Provider source and derived record | Correct source, stop unlawful aggregation or join, delete or restrict identified record, change access or retention | Data copy, derivation, purpose, legal basis, controller and implementation evidence |
| Planned provider report | Correct or restrict before submission; provide intelligible report view where legally required | Planned payload, filing timing, error or unlawful field, current processing |
| Austrian originating authority copy | Correct, restrict, cease unauthorised use or delete when no longer lawfully needed | Controller, actual copy, purpose, applicable domestic basis, use and retention |
| Recipient-state copy | Article 19 notification and a linked correction or deletion message; local restriction or deletion if that controller lacks a continuing basis | Actual recipient, original message identifier, recipient basis and acknowledgment |
| Downstream audit, AML or risk system | Correct or remove derived result, cease unauthorised join or use, review resulting decision | Actual linkage, input, purpose, legal authority, consequence and propagation path |

Proximus supports recipient notification through a processing chain where the underlying change is legally effective. The EU DAC8 schema provides typed correction and deletion messages. Neither source creates a free-standing right to erase data that a recipient remains legally required to hold.

Section 24(2)(5) DSG requires the complaint to request a finding of the alleged infringement. For a successful complaint attributable to a private-sector controller, section 24(5) requires an order to comply with the complainant's underlying request for access, rectification, erasure, restriction or portability to the extent necessary to eliminate the infringement. It does not create a free-standing claim to a complainant-selected Article 58(2) measure. Public-controller relief must be matched to the infringement and the DSB's GDPR Article 58(2) powers. Article 58(2)(g) expressly joins correction, erasure or restriction to Article 19 recipient notification. Section 30(5) DSG excludes fines against public authorities, not corrective orders.

## Scope traps

- A reference to the CJEU is a route decision, not substantive relief.
- Remittal or annulment of a BVwG judgment does not itself stop provider processing.
- Suspensive effect against a refusal does not create the refused prohibition.
- Removal of a technical reporting-channel rule can be replaced while the statutory data duty remains.
- Isolated removal of section 20(4)'s deletion rule can remove an outer limit without removing collection or section 39 records.
- A national challenge framed too narrowly can leave the alleged defect intact or produce an unusable remainder.
- A DAC8 field-level validity challenge must establish severability.
- The VfGH or CJEU may delay the effect of a successful norm ruling.
- Under B-VG Article 140(7), a statute can continue to govern facts realised before delayed expiry except for the true Anlassfall and unless the VfGH directs otherwise. A successful direct individual application does not itself create that privileged case effect. General annulment, applicant effect and operational timing are therefore separate.
- In an Article 144 complaint, suspensive effect under section 85 VfGG can preserve an existing position but does not create a prohibition that the BVwG refused to grant. Section 85 does not govern a direct Article 139 or 140 application.

## Austrian temporal-effect map

| Result | Immediate case effect | General effect | Timing risk |
|---|---|---|---|
| Article 144 annulment of BVwG judgment | Authorities must restore the lawful state under section 87(2) VfGG | No automatic repeal | Renewed proceedings may still be required. |
| Article 140 review on a court application or incidentally from Article 144 | The originating case is privileged under Article 140(7) | Provision ceases to apply according to the published ruling | The VfGH may set up to 18 months and can determine treatment of other earlier facts. |
| Direct Article 140 individual application | No automatic Anlassfall effect for the applicant | Provision ceases to apply according to the published ruling | Earlier facts remain governed unless the VfGH makes an express Article 140(7) pronouncement. |
| Article 139 review on a court application or incidentally from Article 144 | The originating case receives the parallel privileged effect | Regulation or part is removed according to the published ruling | General effect may be delayed; a replacement technical rule may leave the statutory duty intact. |
| Direct Article 139 individual application | No automatic Anlassfall effect for the applicant | Regulation or part is removed according to the published ruling | Broader non-application requires an express Article 139(6) pronouncement. |
| CJEU invalidity | Referring court gives effect subject to the ruling | Other courts have sufficient reason not to apply the invalid EU provision | The CJEU may preserve effects temporarily; Austrian text and operational copies still require implementation. |

## Effective-review timing

*Ferrieri and Bonassisa v Italy* makes a route's practical characteristics part of the Article 8 analysis. Review may be ex post, but it must be sufficiently certain, timely, independent and binding and must permit examination of the criteria and scope of the data-access measure. A possible later tax assessment is not an adequate answer merely because it may eventually create proceedings.

That holding is not a finding against DAC8 or Austria. DAC8 is more textually structured than the Italian access power, and DSB plus BVwG can provide independent and binding review. It does, however, require the litigation file to specify which present processing is reviewable, when review becomes available, what the decision-maker can order and whether the relief can operate before the challenged transfer.

The referring court may request accelerated CJEU treatment under Article 105 of the Rules of Procedure. Exceptionally, the President of the Court may order it ex officio. The scale or economic importance of a case and the referring court's need for a rapid answer do not by themselves establish the required urgency.

## Functionally precise favourable outcome

A materially favourable outcome exists where a final and operative decision attributable to the proceeding prevents or materially limits the identified Krypto-MPfG or DAC8 processing through a binding corrective measure, concrete non-application, binding limiting interpretation, annulment of the necessary national provisions or invalidity of the necessary severable EU provisions.

A referral, remittal, fine, costs decision, easily replaceable technical correction or ruling without practical effect on the identified processing is a different and narrower result.

## See Also

- [[dsb-bvwg-evidence-and-interim-toolkit|DSB and BVwG Evidence and Interim-Protection Toolkit]] ([DSB and BVwG Evidence and Interim-Protection Toolkit](dsb-bvwg-evidence-and-interim-toolkit.md))
- [[dac8-data-lifecycle-access-retention-remedies|DAC8 Data Lifecycle: Access, Retention and Remedies]] ([DAC8 Data Lifecycle: Access, Retention and Remedies](dac8-data-lifecycle-access-retention-remedies.md))
- [[vfgh-to-cjeu-dac8-route|VfGH-to-CJEU DAC8 Route]] ([VfGH-to-CJEU DAC8 Route](../theses/vfgh-to-cjeu-dac8-route.md))

## Sources

- [CJEU C-46/23](../../raw/articles/2026-09-04-cjeu-c46-23-supervisory-erasure-power.md)
- [CJEU C-129/21 Proximus](../../raw/articles/2026-09-04-cjeu-c129-21-proximus-recipient-propagation.md)
- [CJEU C-121/14](../../raw/articles/2026-09-04-cjeu-c121-14-severability.md)
- [CJEU Case 66/80](../../raw/articles/2026-09-04-cjeu-case-66-80-invalidity-effect.md)
- [CJEU Borealis](../../raw/articles/2026-09-04-cjeu-c191-14-borealis-temporal-effects.md)
- [VfGH challenge-scope authorities](../../raw/articles/2026-09-04-vfgh-g252-2016-g188-2021-challenge-scope.md)
- [Austrian remedy provisions](../../raw/articles/2026-09-04-austria-vfgh-and-dsb-remedy-effects.md)
- [ECtHR Ferrieri and Bonassisa](../../raw/articles/2026-09-04-ecthr-ferrieri-bonassisa-tax-bank-data-review.md)
- [Austrian annulment and temporal effects](../../raw/articles/2026-09-04-austria-bvg-vfgg-annulment-temporal-effects.md)
- [B-VG Article 139](../../raw/articles/2026-09-04-bvg-article-139-regulation-effects.md)
- [VfGG section 85](../../raw/articles/2026-09-04-vfgg-85-suspensive-effect.md)
- [VfGG section 87](../../raw/articles/2026-09-04-vfgg-87-binding-restoration.md)
- [DSG section 24 complaint relief](../../raw/articles/2026-09-04-austria-dsg-section-24-complaint-relief-correction.md)
- [VwGVG merits substitution](../../raw/articles/2026-09-04-austria-vwgvg-merits-substitution.md)
- [GDPR correction propagation](../../raw/articles/2026-09-04-gdpr-articles-19-58-correction-propagation.md)
- [Direct individual application and Anlassfall effect](../../raw/articles/2026-09-04-austria-individual-application-anlassfall-effect.md)
- [EDPB Internal Document 5/2021](../../raw/articles/2026-09-04-edpb-document-5-2021-article-55-2-complaints.md)
- [CJEU 2024 Recommendations on accelerated procedure](../../raw/articles/2026-09-04-cjeu-2024-recommendations-accelerated-procedure.md)
