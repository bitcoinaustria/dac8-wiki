---
title: "EBA Guidelines on the use of remote customer onboarding solutions (EBA/GL/2022/15)"
source: "https://www.eba.europa.eu/sites/default/files/document_library/Publications/Guidelines/2022/EBA-GL-2022-15%20GL%20on%20remote%20customer%20onboarding/1043884/Guidelines%20on%20the%20use%20of%20Remote%20Customer%20Onboarding%20Solutions.pdf"
type: papers
ingested: 2026-09-29
fetched: 2026-09-29
content_format: pdf
extraction_tool: "official PDF download; pdftotext"
confidence: high
tags: [eu, eba, remote-onboarding, cdd, liveness-detection, impersonation-fraud, outsourcing, eidas, casp, soft-law]
summary: "EBA final report and guidelines of 22 November 2022, applicable from 2 October 2023. They set EU expectations for remote onboarding: pre-implementation testing, liveness detection in unattended flows, anti-impersonation safeguards and outsourcing oversight. CASPs were outside the original scope; the EBA's 2024 risk-factor amendments point CASPs to them (secondary sources only)."
---

# EBA Guidelines on remote customer onboarding (EBA/GL/2022/15)

EBA Final Report, EBA/GL/2022/15, dated 22 November 2022. Application from 2 October 2023. The guidelines were issued under Article 13(1) of Directive (EU) 2015/849 at the Commission's request. Paragraph numbers are the guideline numbers.

**Purpose and risks acknowledged.** The guidelines are technology-neutral and aim to mitigate risks "such as impersonation fraud risks" (Rationale para. 6). Use of non-qualified or nationally accepted solutions is "contingent on the application of adequate safeguards that mitigate against impersonation and identity fraud risks" (Rationale para. 8). The text read contains no reference to deepfakes by name. Synthetic identities and coercion are mentioned (para. 43).

**Key requirements:**
- **Before rollout (para. 14):** assess data completeness and source reliability, business-wide risk impact and mitigations, fraud and impersonation tests, and end-to-end testing.
- **Ad hoc reviews (para. 15 ff.):** triggered by, among other things, deficiencies found by monitoring, audit or supervisors, and by "a perceived increase in fraud attempts".
- **Document checks (paras. 33–36):** detect reproductions displayed on a screen, ensure OCR and MRZ (machine-readable zone) accuracy, use chip data where feasible, and verify holograms.
- **Matching (para. 38):** the person must match the document.
- **Biometrics (para. 39):** biometric data must be sufficiently unique and use strong algorithms.
- **Insufficient evidence (para. 40):** interrupt the process or redirect to face-to-face.
- **Unattended flows (para. 41):** real-time capture, liveness detection and strong face matching.
- **Attended flows (para. 42):** trained staff, an interview guide and attention to suspicious behaviour.
- **Randomness (para. 43):** random action sequences against synthetic identities and coercion, and random staff assignment against collusion.
- **Extra risk-based controls (para. 44):** e.g. first payment from an account in the customer's name at an EEA-regulated institution, or a single-use passcode.
- **eIDAS (para. 45):** notified eID schemes at level "substantial" or "high", and qualified trust services, are deemed to meet paras. 38–43.
- **Reliance and outsourcing (paras. 46–49):** the relying institution must be satisfied with the third party's remote CDD. Outsourced providers must be monitored through reporting, on-site visits or sample testing, and assessed for staff training, technology and data governance.
- **eIDAS risks (para. 54):** institutions must still address authentication and impersonation risk, the risk that "the customer's identity is not the claimed identity", and lost or stolen evidence.

**Scope and CASPs.** In the consultation feedback table (p. 33, "Addressees"), the EBA said CASPs were not within its scope at the time, so the guidelines could not be extended to them. Secondary sources (CMS, Regulation Tomorrow, FIAU Malta; not the primary text) report that the EBA's January 2024 amending ML/TF Risk Factor Guidelines extend those guidelines to CASPs from 30 December 2024 and point firms, including CASPs, to EBA/GL/2022/15 for non-face-to-face situations. Whether the FMA declared compliance with GL/2022/15 (EBA compliance table) was not verified.

Evidence class: EU soft law (supervisory guidelines under "comply or explain"). Primary evidence of the EU standard. It shows that EU regulators treat impersonation and identity fraud as the core remote-onboarding risk and require layered controls. It also shows that QES and eID routes are deemed compliant, which parallels Austria's § 6 Abs. 4 Z 2–3. It does not measure fraud rates. For DAC8, it describes the identity-verification standard behind provider-held data; compliance with it is not proof that a given record is accurate.
