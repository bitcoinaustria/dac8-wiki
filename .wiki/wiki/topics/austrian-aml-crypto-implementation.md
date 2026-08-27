---
title: "Austrian AML Crypto Implementation"
category: topic
sources:
  - raw/articles/2026-08-27-austria-fm-gwg-current-crypto.md
  - raw/articles/2026-08-27-austria-fm-gwg-section-11a-version-correction.md
  - raw/articles/2026-08-27-austria-wiereg-current.md
  - raw/articles/2026-08-27-austria-kontregg-current.md
  - raw/articles/2026-08-27-austria-wiereg-2027-ministerial-draft.md
  - raw/papers/2026-08-27-austria-nra-fatf-2026.md
  - raw/articles/2026-08-27-fma-mica-transition-2026.md
  - raw/articles/2026-08-27-fma-tfr-guidance.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-bgbl-96-2025.md
created: 2026-08-27
updated: 2026-08-27
tags: [austria, aml, fm-gwg, casp, wiereg, kontregg, fma, fiu]
aliases: [Austria crypto AML law, Austrian AML implementation]
confidence: high
volatility: hot
verified: 2026-08-27
summary: "Austria's 2026 crypto AML baseline consists of FM-GwG, TFR, MiCA supervision, WiEReG, and KontRegG; most of the 2024 EU AML package is future law, and the located WiEReG 2027 proposal is still only a ministerial draft."
---

# Austrian AML Crypto Implementation

> The current Austrian system must be separated from the 2027 AML package. FM-GwG, TFR, MiCA supervision, WiEReG, and KontRegG apply now; the located WiEReG 2027 implementation text is a proposal, not enacted law.

## Current legal layers

| Layer | Current function | Crypto relevance |
|---|---|---|
| FM-GwG | customer due diligence, risk management, suspicious-transaction reporting, retention, and FMA supervision | applies to covered CASPs and TFR compliance |
| TFR | originator and beneficiary traceability for CASP-involved transfers | directly applicable since 30 December 2024 |
| MiCA-VVG | Austrian MiCA authority, supervision, sanctions, and appeal route | FMA supervises Austrian CASPs; legacy transition has ended |
| WiEReG | beneficial ownership and control of entities and arrangements | CASPs are among obliged entities with defined access |
| KontRegG | central discovery of defined bank, payment, securities, depot, and safe-deposit relationships | not currently a register of self-hosted wallets or every CASP transaction |
| Krypto-MPfG | tax due diligence and annual DAC8 reporting | distinct tax-purpose processing from 1 January 2026 |

The institutional roles differ. The FMA supervises CASPs under MiCA, FM-GwG, and TFR. The Austrian FIU receives suspicious-transaction reports. The BVwG is the ordinary appeal forum for MiCA administrative decisions. The BFG supplies the statutory single-judge authorisation for tax inspection of underlying account information under KontRegG.

## FM-GwG duties that matter to the DAC8 counterfactual

FM-GwG section 6 requires risk-based customer and beneficial-owner identification and verification. Section 16 requires prompt reporting to the FIU where the statutory knowledge or suspicion threshold is met; section 20 prohibits tipping off. Sections 25, 31, and 34 provide FMA supervision, corrective measures, licence consequences, and administrative fines.

Section 11a began applying on 30 December 2024; its current amended wording applies from 1 January 2026. It requires a CASP to assess AML/CFT and sanctions risk for transfers to or from self-hosted addresses and use suitable mitigation. The statutory examples include ownership or control verification, additional origin or destination information, and enhanced monitoring. This is a risk rule for a CASP-involved transfer, not a ban on self-custody.

Section 21 currently keeps the necessary CDD material and necessary transaction evidence and records for ten years; it does not say that every crypto-related datum must be retained. It then requires deletion, subject to another federal retention authority and specified pending criminal proceedings, and prohibits incompatible or commercial reuse. By contrast, future AMLR Article 77 starts at five years and permits up to five additional years only by a competent authority, case by case, where necessary for AML/CFT, while preserving other compliant bases and pending-proceeding rules. That contrast is relevant to future harmonisation and proportionality, but Austria's current ten-year period lies within the existing AMLD4/TFR maximum and is not automatically invalid.

For a Krypto-MPfG challenge, the claimant must subtract this AML baseline. Existing identification, transaction, monitoring, and storage costs are not proof of a tax-specific burden. The useful evidence is the incremental section 18 tax dataset, tax-residence and TIN processing, annual aggregation, access controls, deletion logic, notices, and historical reconstruction that remain after FM-GwG, TFR, and MiCA duties are removed from the calculation.

## Austrian register boundaries

WiEReG records beneficial-owner identity and control information for entities and arrangements. It does not record every crypto transfer or wallet address. Section 9 gives defined obliged entities, including CASPs, access for their AML duties; section 10a supplies an exceptional access-restriction mechanism; section 11 prevents exclusive reliance on the register. Beneficial-owner due-diligence material is kept for at least five years after the relationship ends; register accessibility, reports, annotations, and access logs have separate ten-year rules, while technical logs have a one-year rule.

KontRegG records relationships with covered institutions, including identity, institution, account type, and opening or closing information. It is not a balance register and currently does not capture public-chain addresses, self-hosted wallets, or a CASP customer's complete transfer history. Access is purpose-limited and logged. Persons can inspect their own register data; tax queries trigger a FinanzOnline notice; access to underlying account information requires BFG authorisation under section 9.

These limits matter to any “wealth register” claim. Existing Austrian law already permits significant institutional account discovery, but a complete crypto-wealth register must not be presented as current fact without a provision that creates the relevant fields, holders, links, access, and valuation date.

## The 2024 EU package is not fully implemented yet

No enacted Austrian full-package implementation of AMLR and Directive 2024/1640 was located as of 27 August 2026. Ministerial draft 93/ME would replace and expand WiEReG from 10 July 2027. It proposes sanctions screening, nominee and source-of-funds information, legitimate-interest access, inspection powers, and implementing measures for the new Union framework.

The explanatory materials expressly contemplate full implementation of FATF Recommendations 24 and 25 even where that goes beyond the minimum rules of Directive 2024/1640 and AMLR. That is a concrete proposed gold-plating position, but only for the beneficial-ownership framework. It also gives the State an express policy justification. It is not evidence that Austria has already enacted broader AML gold-plating across the entire package.

The Austrian National Risk Assessment and FATF evaluation support the public-interest case for effective AML controls. They also report uneven operational effectiveness and resource constraints. More collection therefore cannot be treated as a substitute for a demonstrated enforcement need, accurate analysis, targeted access, and adequate resourcing.

## Litigation and communications consequences

### Current Krypto-MPfG Individualantrag

- Use FM-GwG and TFR as the existing baseline, not as additional provisions to attack.
- Prove the tax-specific processing increment for reliably non-reportable users.
- Separate current enacted duties from 2027 AMLR and BARIS rules.
- Avoid double-counting MiCA, TFR, and FM-GwG compliance costs.

### Future Austrian AML challenge

Review the enacted implementation provision by provision: account and ownership fields, reporting persons, data quality, access tiers, logs, notifications, retention, sanctions, automated risk inferences, correction, deletion, and independent review. A ministerial draft can guide monitoring and consultation, but ordinarily does not yet create the direct legal effect needed for an Individualantrag.

## Claims to avoid

- “Austria already implemented the whole 2024 AML package.”
- “Self-hosted wallets are illegal.”
- “KontRegG contains every wallet, transaction, and balance.”
- “WiEReG is a crypto-transfer register.”
- “All FM-GwG costs prove an additional Krypto-MPfG burden.”
- “The WiEReG 2027 ministerial draft is already law.”

## See Also

- [[eu-aml-crypto-regulatory-stack|EU AML Crypto Regulatory Stack]] ([EU AML Crypto Regulatory Stack](eu-aml-crypto-regulatory-stack.md))
- [[aml-financial-intelligence-and-fundamental-rights|AML Financial Intelligence and Fundamental Rights]] ([AML Financial Intelligence and Fundamental Rights](aml-financial-intelligence-and-fundamental-rights.md))
- [[mica-tfr-krypto-mpfg-nexus|MiCA, TFR, and the Krypto-MPfG Nexus]] ([MiCA, TFR, and the Krypto-MPfG Nexus](mica-tfr-krypto-mpfg-nexus.md))
- [[dac8-and-the-wealth-register-risk|DAC8 and the Wealth-Register Risk]] ([DAC8 and the Wealth-Register Risk](dac8-and-the-wealth-register-risk.md))
- [[aml-directives-regulations-timeline|AML Directives and Regulations Timeline]] ([AML Directives and Regulations Timeline](../references/aml-directives-regulations-timeline.md))

## Sources

- [Current FM-GwG crypto duties](../../raw/articles/2026-08-27-austria-fm-gwg-current-crypto.md)
- [FM-GwG section 11a version correction](../../raw/articles/2026-08-27-austria-fm-gwg-section-11a-version-correction.md)
- [Current WiEReG](../../raw/articles/2026-08-27-austria-wiereg-current.md)
- [Current KontRegG](../../raw/articles/2026-08-27-austria-kontregg-current.md)
- [WiEReG 2027 ministerial draft](../../raw/articles/2026-08-27-austria-wiereg-2027-ministerial-draft.md)
- [Austria NRA and FATF evaluation](../../raw/papers/2026-08-27-austria-nra-fatf-2026.md)
- [FMA MiCA transition](../../raw/articles/2026-08-27-fma-mica-transition-2026.md)
- [FMA TFR guidance](../../raw/articles/2026-08-27-fma-tfr-guidance.md)
- [Krypto-MPfG official publication](../../raw/articles/2026-08-27-austria-krypto-mpfg-bgbl-96-2025.md)
