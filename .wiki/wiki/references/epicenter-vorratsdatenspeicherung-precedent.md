---
title: "Epicenter/AKVorrat Data-Retention Precedent"
category: reference
sources:
  - raw/articles/2026-08-27-akvorrat-vds-individualantrag-full.md
  - raw/articles/2026-08-27-vfgh-data-retention-reference-g-47-12.md
  - raw/articles/2026-08-27-vfgh-data-retention-final-decision-full-de.md
  - raw/articles/2026-08-27-vfgh-g62-2012-mass-applicant-rejection.md
  - raw/articles/2026-08-27-epicenter-vds-campaign-history.md
  - raw/articles/2026-08-27-cjeu-digital-rights-ireland.md
created: 2026-08-27
updated: 2026-08-29
tags: [epicenter-works, akvorrat, data-retention, individualantrag, vfgh, cjeu]
aliases: [AKVorrat constitutional complaint, Seitlinger and Tschohl applications]
confidence: high
volatility: cold
verified: 2026-08-29
summary: "The Austrian retention litigation separates three distinct events: an Article 267 reference, CJEU invalidation of the EU directive, and final VfGH annulment of the Austrian core provisions; its direct route still depended on exceptional facts."
---

# Epicenter/AKVorrat Data-Retention Precedent

> The precedent is genuine but narrow: Seitlinger and Tschohl succeeded as concretely affected subscribers; 11,129 additional applicants were rejected for missing individualized facts.

## Who actually applied

| Proceeding | Applicant and vehicle | Outcome |
|---|---|---|
| G 47/2012 | Kärntner Landesregierung; abstract review | Admissible only in part; omitted access provisions caused a perimeter failure. |
| G 59/2012 | Michael Seitlinger; Article 140 Individualantrag based on four subscriber lines | Core application admissible and successful. |
| G 62/2012, G 70/2012, G 71/2012 | Christof Tschohl plus 11,129 others; collective Article 140 filing | Tschohl survived; all 11,129 others were rejected. |
| C-594/12, joined with C-293/12 | VfGH preliminary reference plus Irish reference | CJEU invalidated Directive 2006/24/EC on 8 April 2014. |
| G 47/2012 ua, 27 June 2014 | Final Austrian proceedings | VfGH annulled the core Austrian retention provisions. |

AKVorrat—renamed epicenter.works in 2016—organized and financed the campaign. Christof Tschohl was the successful lead collective applicant; Ewald Scheucher/Scheucher Rechtsanwalt GmbH acted as counsel and co-drafter. The association itself was not the institutional applicant named in the judgments.

## What the legal outcome consisted of

The proceeding had three distinct stages that should not be collapsed:

1. **Procedural reference:** On 28 November 2012, the VfGH stayed the Austrian proceedings and referred EU-law validity and interpretation questions under Article 267 TFEU. The reference did not dispose of the Austrian applications.
2. **EU-law result:** On 8 April 2014, the CJEU Grand Chamber declared Directive 2006/24/EC invalid. The VfGH later recorded that the CJEU had imposed no temporal limitation, so the invalidity operated ex tunc.
3. **Austrian result:** The VfGH resumed the national proceedings and on 27 June 2014 annulled the core data-retention provisions in the TKG 2003, StPO, and SPG. It ordered immediate publication and held that earlier provisions would not revive.

Several applications or parts of applications were nevertheless rejected or dismissed. The functional result—removal of the Austrian retention system's core legal bases—therefore did not depend on every pleaded request succeeding.

**Research inference for DAC8:** an Article 267 reference is an intermediate procedural event, not the final legal outcome. Outcome analysis should separately identify the EU-law ruling, the final national disposition, and whether the challenged reporting system remains legally operable after any necessary follow-up. This is a strategic inference from the sequence, not a holding that the same result or route applies to DAC8.

## Why Seitlinger and Tschohl had standing

The full final judgment, sections III.1.5.5–1.5.7, supplies the decisive reasoning:

- provider-facing statutory wording did not prevent direct effect because the retention duty was designed to capture users' data and therefore entered their protected legal sphere;
- storage occurred automatically and continuously without a further implementing act;
- the system involved the applicants' providers and the providers of their communication partners;
- identifying every controller and every retained record was practically impossible;
- new records continually replaced old ones, while the six-month retention period risked deletion before constitutional review could become effective.

The VfGH treated this combination as exceptional. It did not announce that every provider-side processing duty creates direct standing.

## Why 11,129 co-applicants failed

The collective pleading documented Tschohl's own mobile, fixed-line, internet, email, and VoIP relationships through invoices and itemized records. For the additional applicants it relied on a general campaign instruction that only customers of retention-covered providers should sign.

The VfGH held that every applicant had to plead their own current and direct impact. The generic assurance was a substantive, non-curable defect. A DAC8 filing therefore needs, person by person:

- the actual CASP relationship and the provider's reporting status;
- 2026 activity and the statutory category involved;
- evidence of collection, retention, reporting, notice, or a concrete imminent processing step;
- the exact provisions causing the alleged injury;
- an explanation of why the ordinary data-protection route cannot protect that person effectively.

## Numbers and document integrity

Epicenter's campaign page states 11,139 complaints. The VfGH states Tschohl plus 11,129 others; the judicial figure controls the procedural analysis. The separate parliamentary petition with 106,067 signatures was political advocacy, not a court filing.

The local corpus contains the complete 51-page consolidated party application and the official 91-page German final judgment. It separately labels the often-circulated nine-page `Individualantrag_VDS_Verfahrensdokumente_HS_.pdf` as a procedural fragment, not the complete petition.

## DAC8 comparison

| Retention fact | Likely DAC8 fact | Effect |
|---|---|---|
| Many unknown providers, including communication partners' providers | Usually one or more known CASPs | Makes DSB complaints more practical. |
| Rolling six-month records could vanish during litigation | Austrian Krypto-MPfG uses a much longer retention horizon | Removes the same evidentiary urgency. |
| It was practically impossible to identify every controller | CASP and tax authority are ordinarily identifiable | Weakens the exceptional-remedy argument. |
| No single route could effectively reach the distributed system | DAC2 proves DSB → BVwG → VfGH/VwGH is operational | Makes direct Article 140 review a high-risk fallback. |

## See Also

- [[article-267-preliminary-reference|Article 267 Preliminary Reference]] ([Article 267 Preliminary Reference](../concepts/article-267-preliminary-reference.md)) — explains why a CJEU reference remains part of a live national case.
- [[vfgh-to-cjeu-dac8-route|VfGH-to-CJEU DAC8 Route]] ([VfGH-to-CJEU DAC8 Route](../theses/vfgh-to-cjeu-dac8-route.md)) — applies the procedural distinction to the current DAC8 route analysis.

## Sources

- [Complete 51-page AKVorrat application](../../../legal-docs/supporting/at-akvorrat-vds-individualantrag-full.pdf)
- [VfGH preliminary-reference order, German](../../../legal-docs/supporting/at-vfgh-g47-g59-g62-g70-g71-2012-reference-de.pdf)
- [VfGH full final judgment, German](../../../legal-docs/core/at-vfgh-g47-g59-g62-g70-g71-2012-final-de.pdf)
- [VfGH rejection of 11,129 applicants](../../../legal-docs/supporting/at-vfgh-g62-g70-g71-2012-rejection.pdf)
- [CJEU Digital Rights Ireland and Seitlinger](../../../legal-docs/core/eu-cjeu-c293-12-c594-12-digital-rights-ireland.pdf)
- [Official CJEU judgment on EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62012CJ0293)
- [Official VfGH final judgment on RIS](https://www.ris.bka.gv.at/Dokumente/Vfgh/JFT_20140627_12G00047_00/JFT_20140627_12G00047_00.pdf)
