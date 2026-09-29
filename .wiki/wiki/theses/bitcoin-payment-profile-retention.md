---
title: "Bitcoin-Zahlungsprofile aus gespeicherten Identitätszuordnungen"
type: thesis
sources:
  - raw/papers/2026-09-20-meiklejohn-bitcoin-payment-counterparties.md
  - raw/papers/2026-09-20-lightning-payment-observation-limits.md
  - raw/papers/2026-09-04-goldfeder-cookie-blockchain-popets-2018.md
  - raw/papers/2026-09-04-kappos-bitcoin-cluster-validation-usenix-2022.md
  - raw/papers/2026-09-04-moeser-narayanan-bitcoin-clustering-fc-2022.md
  - raw/articles/2026-08-27-edpb-blockchain-guidelines-02-2025-final.md
  - raw/articles/2026-09-20-cjeu-c184-20-indirect-sensitive-data.md
  - raw/articles/2026-09-20-ferrieri-financial-data-counterauthority.md
  - raw/articles/2026-08-27-cjeu-c37-c601-20-aml-register.md
  - raw/articles/2026-08-27-vfgh-e-2097-2021-dac2.md
  - raw/articles/2026-08-27-austria-fm-gwg-current-crypto.md
  - raw/articles/2026-09-04-eu-delegated-regulation-2025-1140-mica-records.md
  - raw/articles/2026-08-30-austria-krypto-mpfg-section-39-records.md
  - raw/articles/2026-09-04-krypto-mpfg-section-39-timing-correction.md
  - raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md
  - raw/articles/2026-09-29-profiling-cjeu-c252-21-meta-sensitive-inference.md
  - raw/articles/2026-09-29-profiling-chainalysis-kyt-exposure-scoring.md
created: 2026-09-20
updated: 2026-09-29
tags: [bitcoin, payments, profiling, retention, erasure, proportionality, austria]
aliases: [Bitcoin als Geld und Zahlungsprofil, Identitaetsanker und Loeschung]
confidence: medium
volatility: hot
verified: 2026-09-20
summary: "Identitätszuordnungen können weitere Bitcoin-Zahlungsbeziehungen erschließen; sensible Lebensprofile und ein daraus folgender Löschungsanspruch benötigen zusätzliche Tatsachen und eine genaue Zuordnung der Speicherpflichten."
---

# Bitcoin-Zahlungsprofile aus gespeicherten Identitätszuordnungen

## Ergebnis

**Die technische Kernthese ist gestützt, ihre rechtliche Folge bleibt fallabhängig.** Eine verlässliche Zuordnung von Identität zu einer Bitcoin-Adresse oder einem bestimmten Transaktionsausgang kann weitere Zahlungszusammenhänge erschließen. Ob diese Aussagen über private Gewohnheiten, Beziehungen oder sensible Umstände ermöglichen, hängt zusätzlich von Empfängerzuordnungen und Kontext ab. Weder ein vollständiges Alltagsprofil noch die Unverhältnismäßigkeit einer Speicherpflicht folgt allein aus Bitcoin-Nutzung.

Die These betrifft zunächst **Anbieteraufzeichnungen**, nicht den DAC8-Jahresbericht ohne Walletadressen. Bei einer verweigerten Löschung ist der Informationsgehalt der tatsächlich betroffenen Daten maßgeblich. Eine TXID allein bezeichnet eine Transaktion mit möglicherweise vielen Ein- und Ausgängen; sie ordnet nicht jeden Beteiligten dem Kunden zu.

## Technische Beweiskette

| Stufe | Was belegbar sein muss | Grenze |
|---|---|---|
| Person → Adresse/Transaktionsausgang | CASP-Aufzeichnung verbindet den Kunden mit dem konkreten Vorgang; Auszahlung an sich selbst oder Dritten unterscheiden | Ein Kundenauftrag beweist nicht die Kontrolle sämtlicher beteiligter Adressen |
| Ausgang → weitere Vorgänge | Nachvollziehbare Graphanalyse und gegebenenfalls validierte Wechselgeld-/Clusteringannahmen | Gemeinsam verwendete Wallets, Batching und CoinJoin können falsche Zuordnungen erzeugen |
| Vorgang → Empfänger/Zweck | Verlässliches Adresslabel, Rechnung oder sonstige unabhängige Zuordnung | Zahlungsabwickler ist nicht zwingend Händler; Händler ist nicht Kaufgegenstand |
| Zahlungsfolge → persönliche Aussage | Wiederkehrende Vorgänge und belastbare Kontextdaten | Spende beweist keine Überzeugung, Apothekenzahlung keine Erkrankung; Fehlzuschreibungen bleiben relevant |

[Meiklejohn et al.](https://conferences.sigcomm.org/imc/2013/papers/imc182-meiklejohnA.pdf), § 5.2 und Tabelle 2, PDF S. 11, belegen zusätzliche Zahlungsflüsse zu benannten Diensten. Die Identität des Ausgangseigentümers blieb dort offen. Historische Machbarkeit ist keine heutige Erfolgsquote.

[Goldfeder et al.](https://petsymposium.org/popets/2018/popets-2018-0038.php) untersuchen reale Webkäufe mit zusätzlichen Händler-/Trackingdaten und präzisen Betrags-/Zeitinformationen. Das stützt die Verbindung von Kaufkontext und Blockchain, nicht die Rekonstruktion allein aus DAC8-Jahressummen. [Kappos et al. 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/kappos) und [Möser/Narayanan](https://arxiv.org/abs/2107.05749) verlangen zugleich eine Prüfung der Zuordnungsfehler und wechselnden Walletmuster.

**Lightning ist gesondert zu behandeln.** Einzelne geroutete Zahlungen stehen nicht im öffentlichen Transaktionsregister. Aus einer bekannten Kanalfinanzierung folgt keine vollständige Einkaufshistorie. Andere Angriffe oder Anbieterunterlagen benötigen zusätzliche Beobachtungsmöglichkeiten. [Kappos et al., S. 2–3 und §§ 4–6](https://arxiv.org/pdf/2003.12470).

## Grundrechtliche Bedeutung und Gegenargumente

Die [EDPB-Leitlinien 02/2025, Version 2.0](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf), Rn. 26 und 93, erfassen Identifizierbarkeit und Risiken off-chain gespeicherter personenbezogener Daten mit Bezug zu On-Chain-Kennungen. Rn. 103 behandelt die Entfernung zusätzlicher Identifizierungsdaten, Rn. 111 Datenmenge, Dauer und Zugänglichkeit. Die Leitlinien beurteilen nicht die Gültigkeit einer konkreten österreichischen Aufbewahrungspflicht.

**DAC2 bleibt die zentrale Gegenautorität.** [VfGH E 2097/2021, III.2.2.4.6–7](https://www.ris.bka.gv.at/Dokumente/Vfgh/JFT_20230309_21E02097_00/JFT_20230309_21E02097_00.pdf) unterscheidet die damaligen Kontodaten von detaillierten Alltags- und Bewegungsprofilen. Belegte zusätzliche Aussagekraft kann eine tatsächliche Unterscheidung tragen; sie beseitigt weder das legitime Steuerziel noch übernimmt sie automatisch die Kommunikationsrechtsprechung.

[Luxembourg Business Registers, Rn. 41–44 und 83–84](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62020CJ0037), berücksichtigt finanzielle Profile, betrifft aber allgemeinen öffentlichen Zugang. Der VfGH hat diesen Unterschied bereits ausdrücklich behandelt. Ein mögliches Leck ist nicht mit gesetzlich angeordneter Veröffentlichung gleichzusetzen.

[Ferrieri und Bonassisa, Rn. 58 und 105–107](https://hudoc.echr.coe.int/eng?i=001-247632), wahrt für rein finanzielle Daten einen weiten staatlichen Beurteilungsspielraum. Die festgestellte Verletzung betraf Gesetzesqualität und Kontrolle, nicht ein allgemeines Verbot langfristiger Finanzdatenspeicherung.

Nach [C-184/20, Rn. 119–128](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62020CJ0184) können auch mittelbar erschlossene sensible Angaben unter Art. 9 DSGVO fallen. Das macht nicht sämtliche Zahlungsdaten zu besonderen Kategorien. Eine entsprechende Inferenz und die anwendbaren Ausnahmen sind gesondert zu prüfen. Nach [C-252/21, Rn. 68–73](../../raw/articles/2026-09-29-profiling-cjeu-c252-21-meta-sensitive-inference.md) genügt, dass die Verarbeitung sensible Angaben offenzulegen „erlaubt“, unabhängig von Richtigkeit und Zweck; nach Rn. 89 kann ein en bloc erhobener Mischdatensatz insgesamt erfasst sein. Anbieter führen zudem teils automatisierte Risikobewertungen von Gegenparteikategorien wie Glücksspieldiensten ([Herstellerbeschreibung Chainalysis KYT](../../raw/articles/2026-09-29-profiling-chainalysis-kyt-exposure-scoring.md), ohne veröffentlichte Fehlerraten).

„Zahlungsprofil“ bezeichnet hier den möglichen Informationsgehalt. **Profiling nach Art. 4 Z 4 DSGVO** setzt automatisierte Bewertung persönlicher Aspekte voraus; bloße Speicherung ist nicht schon Profiling. Für den Grundrechtseingriff muss weder ein fertiges Profil noch ein Schaden entstanden sein. Für seine Intensität zählt die nachvollziehbare zusätzliche Aussagekraft.

## Löschung: Norm und Datensatz zusammen prüfen

Art. 17 Abs. 1 DSGVO benötigt einen Löschungsgrund; Abs. 3 lit. b nimmt erforderliche gesetzliche Verarbeitung aus. Ein bloßer Verweis des Anbieters auf Gesetze ersetzt nicht die Prüfung, ob sie gerade die betroffenen Felder, Zwecke und Zeiträume tragen. Umgekehrt entfällt eine eigenständige Speicherpflicht nicht durch die erfolgreiche Anfechtung einer anderen.

| Grundlage | Gegenstand und Dauer | Relevanz |
|---|---|---|
| § 39 Krypto-MPfG | Dokumentierte Melde-/Sorgfaltsschritte, zehn Jahre nach Ende des jeweiligen Meldezeitraums | Keine ausdrückliche Aufzählung jeder TXID; Einbeziehung konkreter Belege prüfen |
| § 20 Abs. 4 Krypto-MPfG | Löschung übermittelter Informationen beim Anbieter zehn Jahre nach Ende des betreffenden Meldezeitraums | Nicht automatisch Regel für jeden Rohdatensatz oder noch nie übermittelte Daten |
| MiCA Art. 68 Abs. 9; VO 2025/1140 | Erfasste Aufzeichnungen fünf Jahre, auf rechtzeitiges Behördenverlangen bis sieben; je Vorgang auch Hash-/Adressdaten | Anwendbarkeit auf Dienstleistung und Vorgang prüfen; nicht jede Eigenübertragung erzeugt automatisch sämtliche Tabellenfelder |
| § 21 Abs. 1 FM-GwG | Erforderliche Identifizierungs- und Transaktionsunterlagen zehn Jahre nach Ende der Geschäftsbeziehung bzw. gelegentlicher Transaktion | Selbständige österreichische Speicherpflicht mit anderem Fristbeginn; kann denselben Identitätsbezug erhalten |

Primärtexte: [Krypto-MPfG § 39](https://ris.bka.gv.at/Dokumente/Bundesnormen/NOR40273838/NOR40273838.html), [§ 20](https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40273819/NOR40273819.pdf), [MiCA](https://eur-lex.europa.eu/eli/reg/2023/1114/oj/eng), [VO 2025/1140](https://eur-lex.europa.eu/eli/reg_del/2025/1140/oj/eng), [FM-GwG § 21](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009769), [DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32016R0679).

**Strategische Folgerung:** Der Informationsgehalt stärkt eine Erforderlichkeits- und Verhältnismäßigkeitsrüge. Welches Ergebnis erreichbar ist, hängt aber davon ab, ob die streitige Norm für die Entscheidung benötigt wird und welche Verarbeitung nach ihrem Wegfall fortbestünde. Eine zusätzliche steuerliche Nutzung kann gesondert prüfbar sein, auch ohne physisch getrennte Datenbank. Die rechtmäßige Speicherung für einen Zweck erlaubt nicht automatisch jede weitere Verwendung.

## Noch erforderlicher Tatsachennachweis

1. Tatsächliche Anbieterfelder samt Kundenbezug, Zwecken, Fristbeginn und Ablehnungsgrund; keine bloß vermutete Datenarchitektur.
2. Kleine, freiwillig bereitgestellte Stichprobe realer Zahlungsnutzung mit Ausgangszuordnung und unabhängigen Zahlungsbelegen. Private Unterlagen bleiben außerhalb des öffentlichen Wikis.
3. Getrennte Analyse mit Jahresmeldung allein, mit tatsächlich vorhandenen Anbieterzuordnungen und erst danach mit zusätzlichen Empfängerlabels. Keine dem jeweiligen Akteur unbekannten Daten heimlich hinzufügen.
4. Vorab festgelegte Zuordnungsregeln, Treffer und Fehlzuordnungen, Abbruch an unsicheren Stellen, Gegenproben für Eigenüberträge, Batching und Lightning.
5. Konkreter Mehrwert der beantragten Abhilfe: welcher Personenbezug, welche Nutzung, welcher Zugang oder welche zusätzliche Dauer entfällt tatsächlich? Keine behauptete vollständige Anonymisierung, wenn andere Stellen dieselbe Zuordnung behalten.

Ein solcher Versuch wurde hier **nicht durchgeführt**. Die ausgewerteten Studien belegen Mechanismen unter bestimmten Bedingungen, keine Erfolgswahrscheinlichkeit der österreichischen Anfechtung.

## See Also

- [[transaction-profiling-and-sensitive-inference|Profiling and Sensitive Inference from Transaction Records]] ([Profiling and Sensitive Inference from Transaction Records](../references/transaction-profiling-and-sensitive-inference.md)) — Art.-9-Test nach C-252/21 und empirische Profiling-Befunde nach Datengranularität.
- [[account-model-linkage-exposure|Account-Model Chains and Exposure After an Identity Link]] ([Account-Model Chains and Exposure After an Identity Link](account-model-linkage-exposure.md)) — account-model counterpart: one linked address exposes balance and ordered history directly.
- [[identity-to-public-ledger-linkage-evidence|Identity-to-Public-Ledger Linkage Evidence]] ([Identity-to-Public-Ledger Linkage Evidence](../references/identity-to-public-ledger-linkage-evidence.md))
- [[krypto-mpfg-provider-record-architecture|Krypto-MPfG Provider Record Architecture]] ([Krypto-MPfG Provider Record Architecture](../references/krypto-mpfg-provider-record-architecture.md))

## Quellenprovenienz

- [Neue historische Gegenparteienmessung](../../raw/papers/2026-09-20-meiklejohn-bitcoin-payment-counterparties.md)
- [Lightning-Beobachtungsgrenzen](../../raw/papers/2026-09-20-lightning-payment-observation-limits.md)
- [Mittelbare sensible Inferenz](../../raw/articles/2026-09-20-cjeu-c184-20-indirect-sensitive-data.md)
- [Ferrieri-Gegenautorität](../../raw/articles/2026-09-20-ferrieri-financial-data-counterauthority.md)
- Weitere Ausgangsquellen sind im Frontmatter aufgeführt. Rechtsstand am 20. September 2026 geprüft; spätere Änderungen und die tatsächliche Anbieterpraxis sind nicht vorweggenommen.
