---
title: "Bitcoin als Zahlungsmittel: Identitätszuordnung und Zahlungsprofile"
type: report
sources:
  - wiki/theses/bitcoin-payment-profile-retention.md
  - wiki/references/identity-to-public-ledger-linkage-evidence.md
  - wiki/references/krypto-mpfg-provider-record-architecture.md
generated: 2026-09-20
created: 2026-09-20
updated: 2026-09-20
tags: [bitcoin, payments, retention, erasure, profiling, austria]
summary: "Forschungsbefund zu zusätzlicher Aussagekraft gespeicherter Bitcoin-Zuordnungen, zur Abgrenzung von DAC2 und zu eigenständigen österreichischen Aufbewahrungspflichten."
---

# Bitcoin als Zahlungsmittel: Identitätszuordnung und Zahlungsprofile

Stand: 20. September 2026. Erstellt mit [LLM Wiki](https://github.com/bitcoinaustria/dac8-wiki). Recherche, keine Rechtsberatung.

## Kurzbefund

**Die These ist in begrenzter Form belastbar:** Speichert ein Anbieter eine verlässliche Verbindung zwischen einer Person und konkreten Bitcoin-Adressen oder Transaktionsausgängen, kann dies weitere Zahlungsbeziehungen erschließen. Bei tatsächlicher Zahlungsnutzung kann der Informationsgehalt damit über eine Vermögensangabe oder den DAC8-Jahresbericht hinausgehen. Welche privaten Lebensumstände erkennbar werden, benötigt einen gesonderten Nachweis.

## Belege und Grenzen

**Zahlungszusammenhänge sind technisch erschließbar.** Empirische Arbeiten zeigen die Verfolgung von Transaktionsketten zu benannten Diensten sowie die Verknüpfung realer Webkäufe mit Blockchain-Vorgängen. Sie belegen weder die vollständige Zahlungshistorie jedes Nutzers noch automatisch Kaufgegenstände oder sensible Eigenschaften. Ein Dienstleisterlabel kann lediglich einen Zahlungsabwickler identifizieren. [Meiklejohn, § 5.2/Tabelle 2](https://conferences.sigcomm.org/imc/2013/papers/imc182-meiklejohnA.pdf); [Goldfeder et al.](https://petsymposium.org/popets/2018/popets-2018-0038.php).

**Auch die außerhalb der Blockchain gespeicherte Zuordnung zählt.** Die EDPB-Leitlinien nennen solche Verknüpfungsdaten ausdrücklich als Risikofaktor. Die Öffentlichkeit der Blockchain beseitigt nicht die Schutzwürdigkeit des zusätzlich gespeicherten Personenbezugs. [EDPB 02/2025, Version 2.0, Rn. 26, 93 und 103](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf).

**Nicht jede Bitcoin-Zahlung ist so sichtbar.** Lightning-Zahlungen stehen nicht einzeln im öffentlichen Register. Ein Finanzierungsdatensatz allein erschließt ihre gesamte Folge nicht. Zusätzliche Anbieter- oder Netzwerkdaten wären getrennt zu prüfen. [Kappos et al., S. 2–3](https://arxiv.org/pdf/2003.12470).

## Rechtlicher Ansatz

Der mögliche Unterschied zu DAC2 liegt in der **belegten zusätzlichen Aussagekraft**, nicht im Etikett „Kryptodaten“. Der VfGH hielt die dort geprüften Kontodaten für weniger aufschlussreich als Kommunikationsvorratsdaten. Zugleich hat er den Unterschied zwischen vertraulichem Behördenzugang und öffentlichen Registern bereits ausdrücklich behandelt. [VfGH E 2097/2021, III.2.2.4.6–7](https://www.ris.bka.gv.at/Dokumente/Vfgh/JFT_20230309_21E02097_00/JFT_20230309_21E02097_00.pdf).

Die Gegenposition bleibt erheblich: Der EGMR wahrt bei rein finanziellen Informationen einen weiten staatlichen Beurteilungsspielraum. „Finanzprofile sind mindestens so schwerwiegend wie Kommunikationsprofile“ ist keine gesicherte Rechtsaussage. [Ferrieri und Bonassisa, Rn. 58](https://hudoc.echr.coe.int/eng?i=001-247632). Mittelbare sensible Rückschlüsse können rechtlich relevant sein, machen aber nicht sämtliche Zahlungsdaten zu besonderen Kategorien. [EuGH C-184/20, Rn. 119–128](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62020CJ0184).

## Bedeutung für ein Löschungsbegehren

Es kommt auf die **tatsächlich gespeicherten Zuordnungen und die sie tragenden Vorschriften** an, nicht nur auf die spätere Jahresmeldung. Art. 17 DSGVO nimmt erforderliche gesetzliche Verarbeitung vom Löschungsrecht aus. Zu prüfen sind daher sowohl die Reichweite der Pflicht als auch gegebenenfalls ihre Grundrechtskonformität.

Besonders wichtig ist [§ 21 Abs. 1 FM-GwG](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009769): Er verlangt für erforderliche Identifizierungs- und Transaktionsunterlagen grundsätzlich **zehn Jahre nach Ende der Geschäftsbeziehung bzw. einer gelegentlichen Transaktion**. Diese Pflicht besteht unabhängig von DAC8. Daneben stehen MiCA-Aufzeichnungen und die anders abgegrenzten Pflichten nach §§ 20 und 39 Krypto-MPfG. Die Formel „jede TXID zehn Jahre wegen DAC8“ vermischt diese Grundlagen. [Feld- und Fristenvergleich](../wiki/theses/bitcoin-payment-profile-retention.md).

Ein Erfolg gegen eine DAC8-Pflicht würde deshalb nicht zwingend denselben Personenbezug aus sämtlichen Beständen entfernen. Umgekehrt rechtfertigt eine zulässige Aufbewahrung nicht jede zusätzliche Auswertung oder Verwendung.

## Entscheidender Nachweis

Eine überschaubare, überprüfbare Beweiskette wäre aussagekräftiger als eine allgemeine Profilbehauptung: **Anbieterzuordnung → weitere tatsächlich zuordenbare Zahlung → unabhängig belegter Empfänger oder Zweck.** Dabei sind Fehlzuordnungen, Eigenüberträge, Zahlungsabwickler und Lightning getrennt auszuweisen. Anschließend ist festzustellen, welche Information oder Nutzung durch die beantragte Abhilfe tatsächlich entfiele.

Ein solcher nutzerbezogener Test liegt dieser Recherche nicht zugrunde. Die These liefert damit einen begründeten Prüfungsansatz, noch keinen Nachweis der Rechtswidrigkeit einer konkreten Speicherung.

[Ausführliche These mit Quellenprovenienz und Beweisgrenzen](../wiki/theses/bitcoin-payment-profile-retention.md).
