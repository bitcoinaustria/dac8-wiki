---
title: "DAC8 Data Lifecycle: Access, Retention and Remedies"
category: reference
sources:
  - raw/articles/2026-08-28-eu-directive-2011-16-consolidated-2026.md
  - raw/articles/2026-08-30-edps-opinion-9-2023-dac8-detailed-extraction.md
  - raw/articles/2026-08-30-austria-eu-ahg-sections-15-19.md
  - raw/articles/2026-08-30-austria-krypto-mpfg-section-39-records.md
  - raw/articles/2026-08-28-cjeu-c154-21-recipient-identity.md
  - raw/articles/2026-08-28-cjeu-c487-21-access-copy.md
  - raw/articles/2026-08-30-cjeu-c57-23-policejni-retention-review.md
  - raw/articles/2026-08-30-vfgh-g2-2013-purpose-limitation.md
  - raw/articles/2026-08-30-vfgh-g7-2012-retention-maximum.md
  - raw/articles/2026-08-30-vfgh-b1187-2013-financial-data-retention.md
  - raw/articles/2026-08-30-vfgh-e3249-2016-retention-necessity.md
  - raw/articles/2026-08-30-vwgh-ro2020-04-0015-access-recipients.md
  - raw/articles/2026-08-30-vwgh-ro2021-04-0030-recipient-identity.md
  - raw/articles/2026-08-30-bvwg-w137-2314413-access-restriction.md
  - raw/articles/2026-08-30-austria-krypto-mpfg-section-19-reporting-date.md
  - raw/articles/2026-08-30-cjeu-c579-21-pankki-access-logs.md
  - raw/articles/2026-08-27-cjeu-etat-luxembourgeois-tax-information-remedy.md
  - raw/articles/2026-08-27-cjeu-c414-24-parallel-gdpr-remedies.md
  - raw/articles/2026-09-04-krypto-mpfg-section-39-timing-correction.md
  - raw/articles/2026-09-04-cjeu-c340-21-tax-authority-breach-security.md
  - raw/articles/2026-09-04-france-dgfip-tax-data-breach.md
  - raw/articles/2026-09-04-france-ficoba-account-register-breach.md
  - raw/articles/2026-09-04-eu-delegated-regulation-2025-1140-mica-records.md
  - raw/articles/2026-09-04-cjeu-c77-21-digi-purpose-storage.md
  - raw/articles/2026-09-04-cjeu-c268-21-norra-stockholm-tax-data-reuse.md
  - raw/articles/2026-09-04-eu-dac8-xml-correction-deletion.md
  - raw/articles/2026-09-04-ireland-dac8-si-584-2025-retention-copy.md
  - raw/articles/2026-09-04-netherlands-dac8-decision-records-retention.md
  - raw/articles/2026-09-04-france-dac8-prefiling-copy-and-records.md
  - raw/articles/2026-09-04-cjeu-c817-19-ligue-purpose-database.md
  - raw/articles/2026-09-04-austria-dac8-controller-and-authority-retention-precision.md
  - raw/articles/2026-09-04-cjeu-c129-21-proximus-recipient-propagation.md
  - raw/articles/2026-09-04-ecthr-ferrieri-bonassisa-tax-bank-data-review.md
  - raw/articles/2026-09-04-dac8-eu-carf-routing-purpose-chain.md
  - raw/articles/2026-09-04-carf-mcaa-bilateral-activation.md
  - raw/articles/2026-09-04-tax-assistance-convention-article-22.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-bgbl-96-2025.md
created: 2026-08-30
updated: 2026-09-04
tags: [dac8, purpose-limitation, retention, access, correction, recipients, remedies]
aliases: [DAC8 lifecycle, DAC8 downstream use, DAC8 access and retention]
confidence: high
volatility: hot
verified: 2026-09-04
summary: "Controller-by-controller map of DAC8 collection, exchange, further use, retention and data-subject rights, separating facial issues from concrete access, correction and deletion claims."
---

# DAC8 Data Lifecycle: Access, Retention and Remedies

> The lifecycle is broader than a single annual tax report but is legally structured. The strongest claims target an identified controller's unlawful reuse, overbroad access restriction, failed correction propagation or unnecessary continued storage—not an inaccurate theory of secret or unlimited access.

## Data path and legal boundary

| Stage | Data and actor | Governing boundary | Decision-relevant question |
|---|---|---|---|
| Collection and aggregation | CASP determines reportability and produces per-asset annual fields | DAC Annex VI; Krypto-MPfG sections 18 and 20; GDPR | Is the complete section 18 annual aggregate profile created for a non-reportable user? Are value and category choices accurate and intelligible? |
| Pre-report notice | CASP informs the user sufficiently early | DAC Article 25(4); Krypto-MPfG section 20(2) for notice and section 20(3) for timely rights information | Did notice identify the collection/transfer, purposes, controller and recipients or recipient categories as legally required, early enough to exercise rights? |
| Austrian receipt and exchange | Austrian competent authority exchanges data with residence states | DAC Articles 8ad, 21 and 25 | Which controller holds which copy, and was the information sent only to the competent state and systems? |
| Central directory | A secure directory is due by 31 December 2026; the CCN carries the exchange until it is operational | DAC Article 21(5); maintenance access under Article 21(3) | Is access residence-gated and role-limited? The Commission's ordinary data access is limited to statistical purposes; separate technical access is confined to maintenance, upkeep and development. |
| Further use | Recipient authority uses exchanged data | DAC Article 16; EU-AHG section 15 | Is the use one of the listed purposes, a permitted other purpose, or an unauthorised linkage? |
| Onward transmission | Information may move to another Member State under the statutory conditions | DAC Article 16(3); EU-AHG section 15(4) | Was the onward recipient and purpose recorded and available to the data subject where required? |
| Retention and deletion | Provider records, Austrian transmitted copies, recipient copies and downstream files can have different periods | Annex VI V.B.1; DAC Articles 22(3), 25(5); Krypto-MPfG sections 20(4), 39 | Which rule applies to each copy, is it a minimum or maximum, and is earlier deletion reviewed? |

## Operational timeline

| Event | Date for the first reporting period |
|---|---|
| Reportable activity is measured | Calendar year 2026 |
| Austrian provider report to the BMF | By 31 July 2027 under Krypto-MPfG section 19(2) |
| First exchange between competent authorities | By 30 September 2027 under DAC Article 8ad(6) |
| Secure central directory | Due by 31 December 2026; exchange uses the CCN until the directory is operational |

No 2026 inter-state DAC8 dataset should be described as already exchanged.

## Further-purpose architecture

Article 16(1) allows exchanged information to be used for taxes covered by DAC, VAT, other indirect taxes, customs, AML/CFT, recovery claims, compulsory social-security contributions and tax-law penalty proceedings. Article 16(2) permits other uses with the originating State's approval and a lawful recipient-state basis; an originating State's communicated purpose list can replace case-specific approval. Uses for restrictive measures under Article 215 TFEU are separately included. Information may be transmitted onward to another Member State under the Directive's conditions.

The routing rule is narrower than the range of permitted later uses. Article 8ad(2) sends the report to the affected Member States, ordinarily the tax-residence State or States identified for the reportable user. Article 21(5) limits a Member State's directory access to information concerning its own resident users. Section 21 Krypto-MPfG should therefore be read with those limits despite its reference to each participating country. A broader-routing claim requires the actual Austrian routing logic or an actual transmission record.

The EDPS recommended an exhaustive purpose list and a harmonised maximum retention period. The final text contains enumerated and conditional purposes, not a tax-only closed box. This creates a real multi-purpose lifecycle, but not unbounded use. The strongest purpose-limitation claim requires an identified use outside Article 16 and EU-AHG section 15 or an imprecise national authorisation. VfGH G 2/2013 supports precise authority, substantive connection and proportionality for secondary use.

EU-DAC and CARF third-country information require separate source labels and purpose controls. CARF-MCAA activation is bilateral; signature alone does not establish an active exchange relationship with every signatory. Article 22 of the multilateral tax-assistance convention does not automatically import DAC Article 16's express AML/CFT, customs and social-security uses. A third-country chain must therefore identify the active relationship, notifications, safeguards, transfer basis and origin-state permission for any other-purpose use.

C-817/19 adds an architectural proposition: where the source regime's purpose list is exhaustive, the data may not be kept in a single database consultable both for authorised and other purposes. DAC's Article 16 list is materially broader than the PNR rule in that case. The defensible DAC8 use is therefore to require access controls and logs that enforce the line between Article 16 uses and unauthorised purposes, not to claim that tax data can never share infrastructure with another authorised function.

Article 22(1a) also requires tax authorities to have access, for DAC purposes, to specified AML customer-due-diligence mechanisms and records. This is an express access pathway. It is not evidence that all AML, TFR and DAC8 datasets are automatically or indiscriminately fused.

C-77/21 confirms that any later storage, copying, alignment or combination is further processing. Where the later purpose differs and no specific Union or national legal basis governs it, Article 6(4) requires a concrete compatibility assessment of purpose connection, context, data nature, consequences and safeguards. The judgment is also adverse to a categorical fusion argument: compatible further processing is permitted. C-268/21 adds that even legally authorised reuse of a tax register in civil proceedings remained subject to case-specific proportionality and data minimisation. A viable join claim must therefore identify five separate facts: the legal basis, competent controller, actual access, actual combination and resulting use or decision.

## Security architecture and proof

Articles 21 and 25 DAC allocate security responsibilities for Member-State systems and the CCN, restrict technical access, residence-gate access to DAC8 records in the central directory and provide breach notification, exchange suspension and remediation mechanisms. Austria's section 19a EU-AHG implements authority-side suspension. These rules are material adverse authority against a claim that the exchange lacks safeguards.

CJEU C-340/21 nevertheless requires a concrete examination of the nature, content, implementation and practical effects of security measures against the risks of the processing. In its Article 82 setting, the controller bears the burden of showing appropriate measures, but third-party access or a breach does not itself prove inadequacy. The French DGFiP and FICOBA incidents demonstrate credential-based extraction paths in tax and financial-register systems; they do not establish a deficiency in Austrian or DAC8 systems.

The evidence inquiry should therefore identify the controller, data combination and control at each copy: compartmentalisation, least-privilege access, bulk-export rights, contractor and administrator access, multifactor authentication, anomaly detection, immutable access logs, correction propagation and tested incident response. Provider-held MiCA on-chain records and TFR address records must not be treated as part of the DAC8 authority copy unless a lawful and factual join is shown.

## Access and correction

DAC Article 25(1) directs Member States to restrict GDPR Articles 13, 14(1) and 15, but only to the extent required for GDPR Article 23(1)(e) objectives. EU-AHG section 19 likewise conditions the restriction on suitability, necessity and proportionality. It is not a categorical exclusion.

CJEU C-487/21 requires a faithful and intelligible reproduction of the data where needed to verify lawfulness and accuracy. C-154/21, VwGH Ro 2020/04/0015 and Ro 2021/04/0030 support identification of actual recipients where possible because recipient knowledge enables correction, deletion, restriction, objection and judicial rights. C-579/21 supports access to the dates and purposes of actual consultations, without automatically disclosing every employee's identity. BVwG W137 2314413-1 rejects abstract task-risk as a sufficient authority refusal and requires consideration of partial access.

A concrete request should distinguish:

- the provider's stored source fields and valuation/classification method;
- the exact report sent or planned;
- Austrian and foreign controllers and actual recipients;
- consultation and onward-transmission logs where legally accessible;
- correction status in each recipient and downstream system.

At the notice stage, the provider must supply the recipients or recipient categories required by GDPR Articles 13 or 14; actual recipient identity is principally an Article 15 access issue. There is no categorical right to a pre-transfer hearing. CJEU C-245/19 and C-246/19 accepts effective later or indirect review for a taxpayer in some tax-information settings. C-414/24 confirms that GDPR supervisory and judicial remedies are parallel and independent. The better case is failure to provide the notice already required by Article 25(4), an inaccurate or unintelligible report, a disproportionate restriction, or absence of an effective correction path.

The ECtHR's final 2026 judgment in *Ferrieri and Bonassisa* confirms both sides of that line. It rejected a general right to advance notice and accepted possible ex-post review, but required the route to be sufficiently certain, timely, independent and binding. A later tax-assessment case that may never arise or may arise only years later was insufficient in the Italian setting. The judgment concerned discretionary targeted access under overbroad national law; it does not decide DAC8's annual, rule-based reporting or the adequacy of Austria's DSB/BVwG route.

France requires the concrete information to be transmitted about the person to be supplied before filing. That is strong evidence that pre-filing error review is practicable, but it creates neither a user veto nor an automatic suspension. The binding EU exchange schema separately supports corrected-data and deletion-of-data messages that reference the earlier record. A correction inquiry should ask whether the provider changed only its local data or also issued the corresponding downstream message and obtained recipient confirmation.

C-129/21 supports appropriate recipient notification when the underlying correction or erasure is legally effective. Applied cautiously, the inquiry must follow each copy separately: provider source, planned report, Austrian originating copy, recipient-state copy and any derived audit, AML or risk record. Notification does not itself compel a recipient to erase data held under a separate continuing legal basis.

## Retention layers

| Copy or record | Rule | Correct argument |
|---|---|---|
| Provider reporting and due-diligence records | Annex VI V.B.1 covers Sections II and III records and sets a five-to-ten-year period with an ambiguous final reportability clause | Test the clause's scope, the covered record and the provider's actual interpretation; do not assume non-reportable-user due-diligence records are excluded. |
| Austrian section 39 documentation | Ten-year affirmative recordkeeping from the end of the relevant `Meldezeitraum`; the text omits Annex VI's final reportability phrase | Unresolved textual difference, not an established excess. It becomes material only with a non-reportable claimant and proved covered records. The period does not begin at the end of the later reporting-due year. |
| Austrian BMF originating copy of the CASP report | Section 20(4) does not govern this copy; DAC Article 25(5) requires no longer than necessary and compliance with domestic limitation rules | Identify the actual Austrian retention basis, maximum or review interval, and interaction with BAO, archival and pending-proceeding rules. Article 22(3)'s five-year minimum does not necessarily govern a domestically submitted originating copy. |
| Copies received by another authority through automatic exchange | DAC Article 22(3): no longer than necessary but at least five years | No EU-wide maximum exists for these recipient copies. By analogy from law-enforcement data, C-57/23 weakens a per se maximum-period claim if meaningful periodic strict-necessity review exists. |
| Downstream audit, AML/CFT or penalty files | Article 25(5)'s no-longer-than-necessary rule remains horizontal for information processed under DAC; purpose-specific rules can add constraints | Identify the further-use basis, continuing necessity, period and correction/deletion propagation; copying does not erase the DAC/GDPR limits. |

VfGH B 1187/2013 upheld necessary automated retention and required effective cessation/destruction only for separate paper records; E 3249/2016 concerned an intimate paper file. They support a decision and current-necessity review but transfer only by analogy to routine electronic DAC8 data. A deletion claim against the Austrian originating copy need not wait for Article 22(3)'s five-year recipient-copy minimum; the applicable copy and rule must be identified first.

Ireland's six-year and the Netherlands' seven-year provider periods show that DAC8 does not compel a ten-year national provider period. They are concrete comparators, not proof of invalidity. The Austrian record category, tax purpose, audit period and any open proceeding must be compared before claiming that the shorter term is equally effective.

## Facial and as-applied split

| Level | Plausible issue | Limit |
|---|---|---|
| Legislative text | Article 16's breadth and conditional list mechanism; no Union-wide maximum for recipient-state copies; controller-role precision; section 39's unresolved difference from Annex VI V.B.1 | The text contains explicit purposes, secrecy, role and necessity rules. A defect must be tied to a precise provision and severable requested result. |
| Concrete provider practice | Full-profile creation for a non-reportable user; late or vague notice; inaccurate report; excessive supporting-record retention | Requires a real provider, dataset, timing and request response. |
| Concrete authority practice | Unauthorised further use, blanket access restriction, unknown recipients, failed correction propagation or retention without current review | Stronger remedial case, but it does not by itself invalidate DAC8 or Krypto-MPfG generally. |

## Automated risk use is conditional

DAC8 transmits data; it does not itself make an automated decision. GDPR Article 22 requires a solely automated decision with legal or similarly significant effect. An Article 22 scoring claim therefore needs evidence that an Austrian or recipient system uses DAC8 fields and that the output strongly or decisively causes an audit, assessment, referral or comparable significant effect. Even below that threshold, GDPR Articles 5 and 6 and Charter proportionality still govern profiling and risk selection. Without the model, inputs, validation, human role and claimant-specific consequence, automated-decision doctrine remains an evidence request rather than a pleaded violation.

## Ranked claims

| Weight | Claim | Required proof | Likely result if proved |
|---|---|---|---|
| Strong as applied | Concrete inaccurate field was transmitted and not corrected across recipients | Report, source data, correction request, propagation trail | Correction, restriction, recipient notification; possible damages if conditions are met. |
| Strong as applied | Authority refuses actual data or recipient identity by an abstract blanket formula | Request, refusal, invoked restriction, partial-access analysis | Tailored access or a new lawful decision. |
| Strong as applied | Identified use or linkage falls outside Article 16/EU-AHG section 15 | Access/use logs, recipient, purpose and legal basis | Cessation, deletion/restriction or exclusion from the downstream process. |
| Medium, copy-specific | Continued storage lacks real necessity review under the rule applicable to that copy | Dataset, controller, source/recipient status, period, review logic and deletion refusal | Earlier deletion or a lawful individual decision. |
| Claimant-dependent interpretation issue | Section 39 records retained ten years for a genuinely non-reportable user | Completed status determination, provider records and interpretation evidence | Clarification, narrow interpretation or, only if a national excess is established, partial review. |
| Weak without facts | Central EU wealth register, unrestricted AML fusion or decisive secret score | Current law contradicts the broad version; implementation facts missing | Retire until concrete contrary evidence exists. |

## Evidence requests

1. Provider Article 15 request: source fields, actual report, methods, recipients, periods and reportability decision.
2. BMF request: controller identity, exact data, actual recipients, onward uses, access logs, periods and restriction basis.
3. Correction test: follow one controlled correction through every controller and derived system.
4. Retention map: active stores, archives, backups, downstream cases, deletion triggers and periodic review.
5. Purpose map: every tax, customs, AML/CFT, social-security, sanction or other use with its exact Article 16 and national basis.
6. Routing map: residence rule, actual recipients, onward notices and objections, and separate source and purpose codes for EU-DAC and CARF data.
7. Third-country relationship file: activation, reciprocity, notifications, safeguards, transfer basis and suspension status for each proposed partner.
6. Risk-system discovery: fields used, rule/model version, validation, human authority and consequence.

Two Austrian text checks should be added to that evidence request. First, current EU-AHG section 19(2) lists financial institutions, intermediaries, platform operators and the Austrian authority as controllers but not crypto reporting providers, whereas DAC Article 25(3) includes them. Second, Krypto-MPfG section 20(4) governs provider deletion only. Neither point proves invalidity; both require the State and provider to identify the operative controller allocation and authority-copy retention basis precisely.

## See Also

- [[dac8-field-necessity-and-alternatives|DAC8 Field Necessity and Less-Intrusive Alternatives]] ([DAC8 Field Necessity and Less-Intrusive Alternatives](dac8-field-necessity-and-alternatives.md))
- [[dac8-inference-linkage-and-error-evidence|DAC8 Inference, Linkage and Error Evidence]] ([DAC8 Inference, Linkage and Error Evidence](dac8-inference-linkage-and-error-evidence.md))
- [[austrian-gold-plating-and-claimant-audit|Austrian Gold-Plating and Claimant Audit]] ([Austrian Gold-Plating and Claimant Audit](austrian-gold-plating-and-claimant-audit.md))
- [[krypto-mpfg-provider-record-architecture|Krypto-MPfG Provider Record Architecture]] ([Krypto-MPfG Provider Record Architecture](krypto-mpfg-provider-record-architecture.md))
- [[financial-data-breach-and-security-authorities|Financial-Data Breach and Security Authorities]] ([Financial-Data Breach and Security Authorities](financial-data-breach-and-security-authorities.md))
- [[dac8-member-state-implementation-comparators|DAC8 Member-State Implementation Comparators]] ([DAC8 Member-State Implementation Comparators](dac8-member-state-implementation-comparators.md))
- [[dsb-bvwg-evidence-and-interim-toolkit|DSB and BVwG Evidence and Interim-Protection Toolkit]] ([DSB and BVwG Evidence and Interim-Protection Toolkit](dsb-bvwg-evidence-and-interim-toolkit.md))
- [[dac8-remedy-and-outcome-matrix|DAC8 Remedy and Outcome Matrix]] ([DAC8 Remedy and Outcome Matrix](dac8-remedy-and-outcome-matrix.md))

## Sources

- [Consolidated Directive 2011/16/EU](../../../legal-docs/core/eu-directive-2011-16-consolidated-2026.pdf)
- [EDPS Opinion 9/2023](https://www.edps.europa.eu/system/files/2023-04/23-04-03_opinion_proposal_council_directive_cooperation_field_taxation_en.pdf)
- [EU-AHG section 15](https://ris.bka.gv.at/eli/bgbl/i/2012/112/P15/NOR40273392)
- [EU-AHG section 19](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008121&Paragraf=19)
- [CJEU C-57/23](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62023CJ0057)
- [Krypto-MPfG section 19](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20013064&Paragraf=19)
- [Krypto-MPfG section 20](https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40273819/NOR40273819.html)
- [Krypto-MPfG section 39](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20013064&Paragraf=39)
- [CJEU C-154/21](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0154)
- [CJEU C-487/21](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0487)
- [CJEU C-579/21](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0579)
- [CJEU C-245/19 and C-246/19](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62019CJ0245)
- [CJEU C-414/24](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62024CJ0414)
- [CJEU C-340/21](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0340)
- [Commission Delegated Regulation (EU) 2025/1140](https://eur-lex.europa.eu/eli/reg_del/2025/1140/oj/eng)
- [CJEU C-77/21](../../raw/articles/2026-09-04-cjeu-c77-21-digi-purpose-storage.md)
- [CJEU C-268/21](../../raw/articles/2026-09-04-cjeu-c268-21-norra-stockholm-tax-data-reuse.md)
- [EU XML correction and deletion](../../raw/articles/2026-09-04-eu-dac8-xml-correction-deletion.md)
- [Ireland SI 584/2025](../../raw/articles/2026-09-04-ireland-dac8-si-584-2025-retention-copy.md)
- [Netherlands implementing decision](../../raw/articles/2026-09-04-netherlands-dac8-decision-records-retention.md)
- [France pre-filing copy](../../raw/articles/2026-09-04-france-dac8-prefiling-copy-and-records.md)
- [CJEU C-817/19](../../raw/articles/2026-09-04-cjeu-c817-19-ligue-purpose-database.md)
- [Austrian controller and authority-retention text comparison](../../raw/articles/2026-09-04-austria-dac8-controller-and-authority-retention-precision.md)
- [CJEU C-129/21 Proximus](../../raw/articles/2026-09-04-cjeu-c129-21-proximus-recipient-propagation.md)
- [ECtHR Ferrieri and Bonassisa](../../raw/articles/2026-09-04-ecthr-ferrieri-bonassisa-tax-bank-data-review.md)
- [DAC8 and CARF routing and purpose chain](../../raw/articles/2026-09-04-dac8-eu-carf-routing-purpose-chain.md)
- [CARF MCAA, bilateral activation](../../raw/articles/2026-09-04-carf-mcaa-bilateral-activation.md)
- [Tax-assistance convention, Article 22](../../raw/articles/2026-09-04-tax-assistance-convention-article-22.md)
- [Krypto-MPfG, including sections 14 and 21](../../raw/articles/2026-08-27-austria-krypto-mpfg-bgbl-96-2025.md)
