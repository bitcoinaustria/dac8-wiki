---
title: "Vermögensschätzung aus Transaktionsdaten als Analogie für DAC8"
type: thesis
status: completed
verdict: partially-supported
confidence: medium
core_claim: "Transaktionsdaten erlauben statistische Schätzungen von Vermögen, Einkommen oder Kontoständen einzelner Personen; Forschung und Marktprodukte belegen das als Analogie für DAC8-Jahresaggregate."
key_variables: [transaction-features, wealth-income-balance, data-granularity, individual-accuracy]
falsification: "Schätzungen erreichen keine brauchbare Genauigkeit, funktionieren nur mit Einzelposten, oder aus Jahressummen und Zählungen ist keine Rangbildung möglich."
sources:
  - raw/papers/2026-09-23-twi-blumenstock-phone-metadata-wealth.md
  - raw/papers/2026-09-23-twi-aiken-togo-phone-targeting.md
  - raw/papers/2026-09-23-twi-aiken-four-country-phone-wellbeing.md
  - raw/papers/2026-09-23-twi-singh-money-walks.md
  - raw/papers/2026-09-23-twi-tobback-martens-payment-data-credit.md
  - raw/papers/2026-09-23-twi-saez-zucman-capitalized-income.md
  - raw/papers/2026-09-23-twi-smith-zidar-zwick-heterogeneous-returns.md
  - raw/papers/2026-09-23-twi-statcan-capitalization-of-income.md
  - raw/papers/2026-09-23-twi-ecb-arrondel-wealth-income-link.md
  - raw/papers/2026-09-23-twi-oecd-eurostat-joint-icw-matching.md
  - raw/papers/2026-09-23-twi-aiello-crypto-wealth-imputation.md
  - raw/papers/2026-09-23-twi-aiello-who-invests-in-crypto.md
  - raw/articles/2026-09-23-twi-plaid-consumer-report.md
  - raw/articles/2026-09-23-twi-tink-income-check.md
  - raw/articles/2026-09-23-twi-prism-cashscore.md
  - raw/articles/2026-09-23-twi-equifax-ixi-wealthcomplete.md
  - raw/articles/2026-09-23-twi-edpb-psd2-transaction-inference.md
  - raw/articles/2026-09-23-twi-edps-fida-financial-data-sensitivity.md
  - raw/articles/2026-09-23-twi-cfpb-1033-secondary-use-limits.md
  - raw/articles/2026-09-23-twi-eba-loan-origination-account-statements.md
  - raw/articles/2026-09-23-twi-cfpb-1033-status-2026.md
  - raw/papers/2026-09-23-twi-finreglab-cash-flow-underwriting-2019.md
  - raw/papers/2026-09-23-twi-hair-howell-fico-to-cash-flow.md
  - raw/papers/2026-09-23-twi-baker-kueng-transaction-data-limits.md
created: 2026-09-23
updated: 2026-09-23
tags: [dac8, inference, wealth-estimation, profiling, credit-scoring, open-banking, adverse-evidence]
aliases: [Vermögensschätzung aus Transaktionen, wealth inference from transaction data, Sortierbar nach Vermögen]
volatility: warm
verified: 2026-09-23
summary: "Aus Einzeltransaktionen werden Einkommen, Kontostände und Kreditrisiko routinemäßig geschätzt; für Jahressummen ist nur die Gruppen- und Rangschätzung belegt, individuelle Vermögenswerte bleiben ungenau."
---

# Vermögensschätzung aus Transaktionsdaten als Analogie für DAC8

## Ergebnis

**Teilweise gestützt, mittlere Sicherheit.** Dass Transaktionsdaten die finanzielle Lage einer Person offenlegen, ist wissenschaftlich, kommerziell und behördlich gut belegt. Belegt ist das aber fast durchweg für **Einzelposten** mit Datum, Betrag und oft Gegenpartei. Für **jährliche, identitätsbezogene Summen** ist die engste Analogie die Kapitalisierungsmethode aus Steuerdaten. Sie trägt Aussagen über Gruppenanteile und Ränge, liefert aber für Einzelpersonen erhebliche Fehler. Eine Studie, die aus DAC8-artigen Brutto-Jahresflüssen (Summe, Stückzahl, Anzahl) individuelles Vermögen schätzt und validiert, wurde nicht gefunden.

Für die DAC8-Argumentation folgt daraus eine Trennung:

- **Ohne Modell ablesbar:** Jahresvolumen je Kategorie und durchschnittliche Transaktionsgröße (Summe ÷ Anzahl) sind Rechenschritte, keine statistische Schätzung ([[dac8-inference-linkage-and-error-evidence|DAC8 Inference, Linkage and Error Evidence]] ([DAC8 Inference, Linkage and Error Evidence](../references/dac8-inference-linkage-and-error-evidence.md))). Eine Rangordnung gemeldeter Personen nach Aktivitätsumfang ist damit ohne Weiteres möglich.
- **Nur als Schätzung mit großem Fehler:** der Schluss von diesen Flüssen auf den aktuellen Bestand oder das Gesamtvermögen einer bestimmten Person.

Für ein Auswahlrisiko nach einem Datenleck genügt die erste Stufe. Ein Täter braucht keine genaue Vermögenszahl, sondern eine Liste von Personen, die vermögend wirken. Das ist eine Sicherheitsfolgerung, kein gemessener DAC8-Effekt ([[dac8-physical-risk-causation|DAC8 Physical-Risk Causation and Evidence]] ([DAC8 Physical-Risk Causation and Evidence](../references/dac8-physical-risk-causation.md))).

## Evidenz dafür

| Befund | Quelle | Granularität | Stärke |
|---|---|---|---|
| Telefon-Metadaten sagen einen Vermögensindex voraus: individuell r = 0,68, auf Bezirksebene gemittelt r ≈ 0,92 | Blumenstock/Cadamuro/On, *Science* 2015 ([Record](../../raw/papers/2026-09-23-twi-blumenstock-phone-metadata-wealth.md)) | Einzelne Verbindungsdaten, tausende Merkmale | Stark |
| Kapitalisierung jährlicher Kapitaleinkommen aus Steuererklärungen ergibt Vermögensverteilungen; Top-Anteile im SCF-Abgleich nahe an direkt gemessenen Werten | Saez/Zucman, *QJE* 2016 ([Record](../../raw/papers/2026-09-23-twi-saez-zucman-capitalized-income.md)) | Jahressummen je Steuerfall | Stark für Gruppenanteile |
| Amtliche Statistik imputiert Vermögen personenbezogen aus jährlichen Steuerdaten (experimentell) | Statistics Canada 2025 ([Record](../../raw/papers/2026-09-23-twi-statcan-capitalization-of-income.md)) | Jährliche Kapitalerträge je Steuerpflichtigem | Mittel |
| Behörden: Die Gesamtheit der Finanztransaktionen kann Verhaltensmuster und besondere Datenkategorien offenlegen; die Bewertung der finanziellen Lage aus Kontodaten ist Profiling | EDPB-Leitlinien 06/2020, Rn. 52 und Abschnitt 6.5 ([Record](../../raw/articles/2026-09-23-twi-edpb-psd2-transaction-inference.md)) | Zahlungskontodaten nach PSD2 | Stark (unverbindlich) |
| Persönliche Finanzdaten sind „inherently sensitive“; Risiko von Ausgrenzung und Diskriminierung | EDPS-Stellungnahme 38/2023, Rn. 12, 14 ([Record](../../raw/articles/2026-09-23-twi-edps-fida-financial-data-sensitivity.md)) | Bei Finanzinstituten gehaltene Daten | Mittel (beratend) |
| Transaktionsdaten können „financial abundance that could make them the target of criminal activity“ offenlegen, ebenso Krankheiten und finanzielle Verletzlichkeit | CFPB, ANPR zur Überprüfung der § 1033-Regel, 90 FR 40986, 22.8.2025, Abschnitt zu Privacy Concerns ([Record](../../raw/articles/2026-09-23-twi-cfpb-1033-status-2026.md)) | Transaktionsdaten von Konten | Stark als behördliche Feststellung; nennt den Zielauswahl-Mechanismus ausdrücklich |
| Kontodaten gelten als potenziell sensibel; Zweitnutzung begrenzt; Cashflow-Daten zeigen Kreditrisiko | CFPB-Regel § 1033, 2024 ([Record](../../raw/articles/2026-09-23-twi-cfpb-1033-secondary-use-limits.md)) | Kontodaten | Mittel: § 1033.421 steht noch im CFR, ist aber in Überprüfung und seit Oktober 2025 gerichtlich ausgesetzt (*Forcht Bank v. CFPB*, E.D. Ky. 5:24-cv-00304); als Begründung der Behörde zitierbar, nicht als durchsetzbare Pflicht ([Status](../../raw/articles/2026-09-23-twi-cfpb-1033-status-2026.md)) |
| Kontoauszüge gelten als Einkommensnachweis, Sparbuchauszüge als Vermögensnachweis | EBA/GL/2020/06, Rn. 85, 90, 106 ([Record](../../raw/articles/2026-09-23-twi-eba-loan-origination-account-statements.md)) | Kontoauszüge | Mittel |
| Marktprodukte leiten Einkommen, Durchschnittssalden und Ausfallrisiko aus Kontotransaktionen ab | Plaid, Tink, Prism ([Plaid](../../raw/articles/2026-09-23-twi-plaid-consumer-report.md), [Tink](../../raw/articles/2026-09-23-twi-tink-income-check.md), [Prism](../../raw/articles/2026-09-23-twi-prism-cashscore.md)) | Einzeltransaktionen über 3–24 Monate | Belegt als Praxis; Genauigkeit nur herstellerseitig oder gar nicht angegeben |
| Vermögensschätzung je Haushalt in Dollar als kommerzielles Produkt | Equifax/IXI WealthComplete ([Record](../../raw/articles/2026-09-23-twi-equifax-ixi-wealthcomplete.md)) | Gepoolte Salden, keine Transaktionen | Belegt als Praxis; keine Fehlerkennzahlen |
| Kartenzahlungen nach Ort und Zeit sagen finanzielle Schwierigkeiten voraus (AUC 0,77–0,83 gegenüber etwa 0,59 für Demografie) | Singh/Bozkaya/Pentland, *PLOS ONE* 2015 ([Record](../../raw/papers/2026-09-23-twi-singh-money-walks.md)) | Einzelkäufe mit Zeit und Ort | Mittel; Ziel ist finanzielle Belastung, nicht Vermögen |

## Evidenz dagegen und Grenzen

| Befund | Quelle | Bedeutung |
|---|---|---|
| Gleiche Renditeannahme überschätzt Spitzenvermögen deutlich; der Zinssatz ganz oben liegt bei etwa dem 3,5-Fachen des Durchschnitts | Smith/Zidar/Zwick, *QJE* 2023 ([Record](../../raw/papers/2026-09-23-twi-smith-zidar-zwick-heterogeneous-returns.md)) | Von Flüssen auf Bestände zu schließen ist individuell fehleranfällig, Trends bleiben erhalten |
| Erstes Modell erfasste nur 44 % der Finanzvermögen, erst nach Kalibrierung 80 % | Statistics Canada 2025 ([Record](../../raw/papers/2026-09-23-twi-statcan-capitalization-of-income.md)) | Die Imputation braucht Referenzsummen von außen |
| Nettovermögen korreliert nur 0,33 mit dem Gesamteinkommen; in mittleren Quintilen stimmen Einkommens- und Vermögensrang kaum besser überein als zufällig | Arrondel/Roger/Savignac, EZB WP 1709 ([Record](../../raw/papers/2026-09-23-twi-ecb-arrondel-wealth-income-link.md)) | Ein Strom ist ein schwacher Einzelprädiktor für einen Bestand |
| Vermögensimputation auf Einkommens- und Konsumdaten verzerrt selbst die Randverteilung (Median AT, DE, FR, PT +16 bis +19 %) | Balestra/Oehler, OECD/Eurostat 2023 ([Record](../../raw/papers/2026-09-23-twi-oecd-eurostat-joint-icw-matching.md)) | Amtliche Verfahren bleiben unsicher, auch auf Verteilungsebene |
| Telefondaten: Korrelation mit Konsum etwa 0,46; etwa die Hälfte der Armen wird nicht erkannt; Genauigkeit sinkt mit dem Alter der Daten | Aiken et al., *Nature* 2022 ([Record](../../raw/papers/2026-09-23-twi-aiken-togo-phone-targeting.md)) | Moderate, nicht zuverlässige Einzelzuordnung |
| In vier Ländern: Vermögensindex nur mäßig, Konsum schwach vorhersagbar | Aiken, Blumenstock et al., Preprint ([Record](../../raw/papers/2026-09-23-twi-aiken-four-country-phone-wellbeing.md)) | Nicht begutachtet; die Einkommenszahl wurde nicht im Volltext geprüft und wird hier nicht verwendet |
| Signal liegt darin, *an wen* gezahlt wurde, nicht in Betrag oder Häufigkeit; Monatsaggregate verlieren Information | Tobback/Martens, *JRSS-A* 2019 ([Record](../../raw/papers/2026-09-23-twi-tobback-martens-payment-data-credit.md)) | Ziel ist Kreditausfall; spricht dagegen, dass Summen und Zählungen allein die stärksten Merkmale sind |
| Unabhängige Auswertung: Modelle nur aus Cashflow-Daten erreichen AUC 0,572–0,725 für Kreditausfall; kombiniert mit klassischen Daten 0,758 statt 0,720 (S. 25, 27). Die Einkommensangaben der Kreditgeber unterschätzen das tatsächliche Einkommen eher (S. 31) | FinRegLab 2019 ([Record](../../raw/papers/2026-09-23-twi-finreglab-cash-flow-underwriting-2019.md)) | Ziel ist Ausfall; eine unabhängige Fehlerrate für Einkommensschätzungen gibt es nicht |
| Kontoauszüge verbessern die Ausfallvorhersage bei Kleinunternehmen nur wenig; ein reines Cashflow-Modell liegt etwa auf FICO-Niveau (AUC 0,642) | Hair/Howell/Johnson/Matsumoto, NBER WP 33367 ([Record](../../raw/papers/2026-09-23-twi-hair-howell-fico-to-cash-flow.md)) | Nicht begutachtet; bestätigt ein reales, aber mäßiges Signal |
| Forscher sehen nie sicher alle Konten einer Person; aus Transaktionen gemessene Einkommensniveaus sind deshalb schwer zu deuten | Baker/Kueng, NBER 2021, Abschnitt 3.2.1 ([Record](../../raw/papers/2026-09-23-twi-baker-kueng-transaction-data-limits.md)) | Gilt ebenso für DAC8: andere Anbieter und Selbstverwahrung fehlen |
| Krypto-Vermögen lässt sich aus datierten Bank-Börsen-Überweisungen imputieren, aber ohne Abgleich mit tatsächlichen Beständen | Aiello et al., NBER WP 31445 ([Record](../../raw/papers/2026-09-23-twi-aiello-crypto-wealth-imputation.md)) | Braucht Einzeldaten mit Datum; nicht validiert |

## Einschränkungen

- **Granularität entscheidet.** Die stärksten Genauigkeitswerte stammen aus Einzelposten mit Zeit, Ort oder Gegenpartei. Der DAC8-Jahresbericht enthält keine dieser Angaben ([[dac8-transaction-granularity-and-reporting-layers|DAC8 Transaction Granularity and Reporting Layers]] ([DAC8 Transaction Granularity and Reporting Layers](../references/dac8-transaction-granularity-and-reporting-layers.md))). Die Anbieteraufzeichnungen nach § 20 Krypto-MPfG und dem FM-GwG enthalten sie dagegen. Für ein Leck beim Anbieter sind die Einzelposten-Befunde deshalb die passendere Analogie.
- **EDPB-Formulierung.** „The sum of financial transactions“ in Rn. 52 bezeichnet die Gesamtheit der Transaktionen eines Kontos, nicht eine arithmetische Jahressumme. Die Stelle darf nicht als Aussage über Aggregatmeldungen zitiert werden.
- **Brutto- statt Ertragsgrößen.** Die Kapitalisierungsmethode rechnet aus Erträgen auf Bestände hoch. DAC8 meldet Brutto-Kauf- und Verkaufsvolumina. Kumulierte Käufe über mehrere Jahre sind eher eine grobe Untergrenze investierter Mittel als ein Vermögensschätzer. Selbstverwahrung, andere Anbieter und Kursänderungen fehlen.
- **Herstellerangaben.** Plaid, Tink, Prism und Equifax veröffentlichen keine unabhängig geprüften Fehlerraten für Einkommen oder Vermögen. Sie belegen die Praxis, nicht die Genauigkeit. Die gefundenen unabhängigen Auswertungen (FinRegLab 2019, Hair/Howell et al. 2025) messen nur die Vorhersage von Kreditausfällen, nicht die Genauigkeit von Einkommens- oder Vermögensschätzungen. Eine veröffentlichte Auswertung von FCA, Bank of England oder BIS mit Fehlerraten wurde nicht gefunden.
- **Gegenargument des Staates.** Die Behörde erhält die Aggregate zu Steuerzwecken, darf sie nicht beliebig weiterverwenden und unterliegt Vertraulichkeitsregeln. Das Auswahlrisiko setzt ein Leck oder einen Missbrauch voraus.

## Verdict

**Status:** Teilweise gestützt
**Confidence:** Mittel

**Zusammenfassung:** Transaktionsdaten legen die finanzielle Lage offen. Das bestätigen Forschung, Marktpraxis und Datenschutzbehörden, belegt ist es aber vor allem für Einzelposten. Für jährliche Summen ist nur die Schätzung von Gruppenanteilen und Rängen belegt; individuelle Vermögenswerte bleiben ungenau. Die DAC8-Aussage „sortierbar nach Aktivitätsumfang“ ist ohne Statistik ableitbar; die Aussage „das Vermögen einer Person lässt sich genau bestimmen“ wäre überzogen.

**Stärkste stützende Evidenz:** Blumenstock et al. 2015; Saez/Zucman 2016 (Aggregate, Gruppenebene); EDPB 06/2020 Rn. 52 und Abschnitt 6.5; CFPB-ANPR 2025 zur Offenlegung von „financial abundance“ als Ziel krimineller Handlungen; dokumentierte Marktprodukte.

**Stärkste Gegenevidenz:** Smith/Zidar/Zwick 2023; Arrondel et al. 2014; Aiken et al. 2022; Tobback/Martens 2019 zum Informationsverlust durch Aggregation.

**Was das Ergebnis ändern würde:** eine Studie, die aus jährlichen Brutto-Kauf- und Verkaufssummen mit Transaktionszahlen individuelles Krypto- oder Gesamtvermögen schätzt und gegen tatsächliche Bestände validiert; ein realer DAC8-Datensatz oder Testdaten eines Anbieters, an denen sich die Rangtrennung messen lässt.

## Offene Fragen

1. Wie gut trennt die durchschnittliche Transaktionsgröße allein vermögende von weniger vermögenden Personen? Dazu wurde keine Studie gefunden.
2. Die Überprüfung der CFPB-Regel § 1033 ist offen: Ein Regelungsvorschlag nach dem ANPR war bis 23.9.2026 nicht veröffentlicht; die Berufungen im 6. Circuit (25-6164, 26-5005) sind anhängig. Vor jeder Verwendung neu prüfen.
3. Eine unabhängige Fehlerrate für Einkommensschätzungen aus Transaktionsdaten im Abgleich mit Steuer- oder Lohndaten wurde nicht gefunden.

## See Also

- [[dac8-inference-linkage-and-error-evidence|DAC8 Inference, Linkage and Error Evidence]] ([DAC8 Inference, Linkage and Error Evidence](../references/dac8-inference-linkage-and-error-evidence.md))
- [[dac8-transaction-granularity-and-reporting-layers|DAC8 Transaction Granularity and Reporting Layers]] ([DAC8 Transaction Granularity and Reporting Layers](../references/dac8-transaction-granularity-and-reporting-layers.md))
- [[dac8-and-the-wealth-register-risk|DAC8 and the Wealth-Register Risk]] ([DAC8 and the Wealth-Register Risk](../topics/dac8-and-the-wealth-register-risk.md))
- [[dac8-physical-risk-causation|DAC8 Physical-Risk Causation and Evidence]] ([DAC8 Physical-Risk Causation and Evidence](../references/dac8-physical-risk-causation.md))
- [[bitcoin-payment-profile-retention|Bitcoin-Zahlungsprofile aus gespeicherten Identitätszuordnungen]] ([Bitcoin-Zahlungsprofile aus gespeicherten Identitätszuordnungen](bitcoin-payment-profile-retention.md))
