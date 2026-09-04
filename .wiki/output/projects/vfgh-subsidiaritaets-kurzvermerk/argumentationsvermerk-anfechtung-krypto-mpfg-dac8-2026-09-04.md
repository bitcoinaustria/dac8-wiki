---
title: "Argumentationsvermerk zur Anfechtung von Krypto-MPfG und DAC8"
type: report
sources:
  - wiki/references/dac8-field-necessity-and-alternatives.md
  - wiki/references/dac8-vs-dac2-distinguishing-arguments.md
  - wiki/references/dac8-inference-linkage-and-error-evidence.md
  - wiki/references/dac8-data-lifecycle-access-retention-remedies.md
  - wiki/references/austria-eu-precedent-matrix.md
  - wiki/topics/dac8-charter-proportionality.md
  - wiki/topics/dac8-fundamental-rights-and-public-risks.md
  - wiki/references/krypto-mpfg-provider-record-architecture.md
  - wiki/references/identity-to-public-ledger-linkage-evidence.md
  - wiki/references/financial-data-breach-and-security-authorities.md
  - wiki/references/dac8-bulk-data-case-transfer-matrix.md
  - wiki/references/dac8-equality-and-technology-neutrality.md
  - wiki/references/dac8-dpia-accountability-and-security-evidence.md
  - wiki/references/dac8-remedy-and-outcome-matrix.md
  - wiki/references/dac8-aeoi-effectiveness-and-evidence-limits.md
  - wiki/references/krypto-mpfg-dv-formality-and-technical-specifications.md
  - wiki/references/dac8-challenge-scope-and-residual-duties.md
  - wiki/references/dsb-bvwg-evidence-and-interim-toolkit.md
generated: 2026-09-04
verified: 2026-09-04
---

# Argumentationsvermerk zur Anfechtung von Krypto-MPfG und DAC8

**Stand: 4. September 2026. Mit [LLM Wiki](https://github.com/bitcoinaustria/dac8-wiki) erstellt. Rechercheunterlage, keine Rechtsberatung.**

## Kurzbefund

Ein konkreter Prüfungsansatz ist die Erforderlichkeit einzelner Meldedaten: Welchen zusätzlichen steuerlichen Nutzen haben Einheiten, Transaktionsanzahlen und Transferfelder gegenüber einem engeren Datensatz? Hinzu kommen die durch zusätzliche Daten mögliche Blockchain-Verknüpfung und eigenständige österreichische Speicherentscheidungen.

Gegen einen pauschalen Angriff sprechen die österreichische DAC2-Judikatur, die EuGH-Entscheidung zu DAC6 und die dokumentierte Prüfung verschiedener Meldemodelle durch den Unionsgesetzgeber. Entscheidend sind daher nachweisbare Unterschiede, gleich wirksame mildere Mittel und die im Ausgangsverfahren tatsächlich angewendeten Normen. Die folgenden Ansätze sind keine Einschätzung der Erfolgswahrscheinlichkeit.

## 1. Erforderlichkeit des Meldedatensatzes

### Angreifbare Feldgruppen

[§ 18 Abs. 1 Krypto-MPfG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20013064&Paragraf=18) verbindet Identitäts- und Ansässigkeitsdaten mit Jahresaggregaten je meldepflichtigem Kryptowert und Transaktionskategorie. Der reguläre Bericht enthält keine einzelnen Transaktionszeitpunkte, Transaktionskennungen, Gegenparteien oder Wallet-Adressen.

- **Krypto-zu-Krypto-Tausch, Z 3 lit. d und e:** Marktwert, Einheiten und Anzahl werden für Erwerbs- und Veräußerungsseite getrennt aggregiert. Soweit § 27b EStG anwendbar ist und beide Vermögenswerte Kryptowährungen nach dessen Abs. 4 sind, ist der Tausch nach [§ 27b Abs. 3 EStG](https://ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=27b) keine Realisierung. Anschaffungskostenfortführung und abweichendes ausländisches Steuerrecht bleiben mögliche Rechtfertigungen.
- **Übertragungen, lit. g und h:** Gemeldet werden Marktwert, Einheiten und Anzahl, aufgeschlüsselt nach Übertragungsart, soweit bekannt. Eigenübertragungen, Darlehen oder Sicherheiten sind nicht schon als solche steuerpflichtige Vorgänge.
- **External-Address-Aggregat, lit. i:** Marktwert und Einheiten von Übertragungen an DLT-Adressen, die dem Anbieter nicht als mit einem Anbieter von Dienstleistungen für virtuelle Vermögenswerte oder Finanzinstitut verbunden bekannt sind. Ausschlaggebend ist das Anbieterwissen über einen Intermediär, nicht Eigentum oder Verdacht. Eigene selbstverwahrte Adressen können erfasst sein. Dieses Feld enthält weder Adressen noch Transaktionsanzahl.
- **Einheiten und Anzahlen, lit. b bis h:** Sie erlauben Durchschnittsgrößen und implizite Durchschnittsbewertungen. Bei nur einem Vorgang in einer Asset- und Transaktionskategorie entsprechen die Aggregate dessen Quantität. Daraus folgt noch keine eindeutige On-Chain-Zuordnung.

Die parallelen EU-Vorgaben stehen in Art. 8ad Abs. 3 lit. c und Anhang VI Abschnitt II.B.3 der [Richtlinie 2011/16/EU](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02011L0016-20260101): Für lit. d/e entsprechen Z iv/v, für lit. g bis i Z vii bis ix; die Buchstaben in Anhang VI sind jeweils gleich. Die Identitätsverknüpfung folgt aus Art. 8ad Abs. 3 lit. a und Anhang VI Abschnitt II.B.1.

### Maßstab, Gegenposition und verbleibender Angriff

Maßstab für die EU-Vorgaben sind Art. 7, 8 und 52 Abs. 1 [GRC](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12016P/TXT). [EuGH C-175/20, Rn. 63 bis 84](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62020CJ0175) verlangt bestimmte Zwecke und objektive, zeitliche und sachliche Grenzen einer steuerbehördlichen Datenanforderung. Der Fall prüft kein automatisches EU-Meldesystem. [C-394/23, Mousse, Rn. 22 bis 29 und 36 bis 43](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62023CJ0394) konkretisiert die Datenminimierung außerhalb des Steuerrechts. [C-484/24, NTH Haustechnik, Rn. 70 bis 73, 91 bis 103 und 116](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62024CJ0484) unterwirft auch gesetzlich vorgeschriebene Verarbeitung der Erforderlichkeits- und Verhältnismäßigkeitsprüfung.

Die [Folgenabschätzung SWD(2022) 401](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=SWD:2022:401:FIN) verglich Salden-, Aggregat- und Einzeltransaktionsmodelle und wählte bewusst ein hybrides Aggregatmodell. Transferdaten sollen unter anderem Cold-Wallet-Abflüsse sichtbar machen und den Abgleich mehrerer Anbieter ermöglichen. Eine Eigenwallet-Ausnahme wurde erwogen, aber nicht allgemein übernommen. Die Behauptung, mildere Modelle seien überhaupt nicht geprüft worden, wäre falsch.

Offen bleibt der zusätzliche Nutzen jedes Feldes gegenüber einem engeren Modell. Als Alternativen kommen Wertmeldungen ohne Einheiten oder Anzahl, gesonderte Behandlung nachgewiesener Eigenwallet-Transfers und Detailnachforderungen bei objektiven Diskrepanzen in Betracht. Ihre gleichwertige Wirksamkeit ist zu belegen, nicht vorauszusetzen. Ein Vergleich sollte Detektionsleistung, Fehlalarme und Umgehungsmöglichkeiten erfassen.

Die [TFR, Art. 14 Abs. 5 und Art. 16 Abs. 2](https://eur-lex.europa.eu/eli/reg/2023/1113/oj), verlangt bei erfassten Transfers über 1.000 Euro zu oder von selbst gehosteten Adressen Maßnahmen zur Prüfung von Eigentum oder Kontrolle. Solche Nachweise können die technische Machbarkeit einer Differenzierung stützen. Ihre AML/CFT-Zweckbindung erlaubt keine automatische steuerliche Wiederverwendung; eine festgestellte Eigenwallet beseitigt die DAC8-Meldepflicht nicht.

Ein allgemeines Wirkungslosigkeitsargument wäre ebenfalls zu weit: Die [Kommissionsbewertung 2025](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025SC0365) stützt Compliance-Effekte bestehender Austauschsysteme, misst aber weder DAC8 noch den Zusatznutzen seiner einzelnen Felder. Fehlende veröffentlichte Feldstudien beweisen keine Wirkungslosigkeit.

## 2. DAC2-Abgrenzung und Blockchain-Verknüpfung

### Nachteilige Rechtsprechung

[VfGH E 2097/2021](https://www.ris.bka.gv.at/Dokumente/Vfgh/JFT_20230309_21E02097_00/JFT_20230309_21E02097_00.pdf) akzeptierte im damaligen DAC2-Fall die Verarbeitung von Konto-, Saldo- beziehungsweise Wert- und Zinsinformationen. Anlasslosigkeit, fehlende Bagatellgrenze, Steuerehrlichkeit und abstrakte Sicherheitsrisiken begründeten keine ernstlichen Gültigkeitszweifel. Zur nachteiligen Linie gehören auch [BVwG W211 2232955-1/7E](https://www.ris.bka.gv.at/Dokumente/Bvwg/BVWGT_20210412_W211_2232955_1_00/BVWGT_20210412_W211_2232955_1_00.pdf) und [VwGH Ro 2023/04/0021](https://www.ris.bka.gv.at/Dokumente/Vwgh/JWT_2023040021_20251210J00/JWT_2023040021_20251210J00.pdf).

DAC8 unterscheidet sich durch assetbezogene Aktivitätskategorien, Mengen, Häufigkeiten und Transferinformationen. Wiederholte Meldungen ergeben mehrjährige Aktivitätsprofile, aber keinen aktuellen Bestand und keine Einzelchronologie. Beweisbedürftig ist die zusätzliche Aussagekraft gegenüber dem damals geprüften Datensatz, nicht bloß dessen größere Feldzahl.

[EuGH C-623/22, Rn. 143 bis 149](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62022CJ0623) verwarf die geprüften Gültigkeitseinwände gegen DAC6 und akzeptierte eine Gesamtprüfung des Informationspakets. Ein möglicher Unterschied: DAC6 knüpft an grenzüberschreitende Gestaltungen mit gesetzlichen Risikokennzeichen an, DAC8 an meldepflichtige Kryptoaktivität ohne vergleichbaren individuellen Risikofilter. Das allein begründet keine Ungültigkeit.

### Besonderes Schadenspotenzial einer belegten Verknüpfung

Bei einer erfolgreichen Verbindung von Identität und öffentlicher Blockchain kann ein Datenleck mehr offenlegen als den entwendeten Bericht: Historische Transaktionen bleiben öffentlich auswertbar; weitere Daten können spätere Zuordnungen ermöglichen. Die Entfernung der geleakten Identitätszuordnung macht bereits gezogene Verknüpfungen nicht rückgängig. Die [EDPB-Leitlinien 02/2025, Version 2.0, Rn. 26, 50, 61 und 63 bis 64](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf) stützen diesen Mechanismus. Sie belegen nicht, dass DAC8-Jahresaggregate allein regelmäßig eine bestimmte On-Chain-Transaktion identifizieren.

Zusätzliche Verknüpfungsdaten können beim Anbieter bestehen: Die [Delegierte Verordnung (EU) 2025/1140](https://eur-lex.europa.eu/eli/reg_del/2025/1140/oj/eng) sieht für erfasste MiCA-Dienstleistungen in Tabelle 3 identifizierte Käufer-/Verkäuferdaten und gegebenenfalls einen Transaktionshash, in Tabelle 4 unter anderem Hash, Wallet-Adressen und Zeitstempel vor. Die interne Transaktionsdatensatznummer verbindet die Tabellen. Diese Aufzeichnungen sind nicht Teil des regulären DAC8-Berichts. Ihr Vorhandensein beweist weder Steuerbehördenzugriff noch eine zulässige Sekundärnutzung.

**Nachweisbedarf:** Ein Sachverständigentest sollte zunächst nur die DAC8-Jahresaggregate verwenden und zusätzliche Adress-, Hash-, Zeit- oder Providerdaten getrennt hinzufügen. Zu dokumentieren sind Voraussetzungen, Treffer, Fehlzuordnungen und verbleibende Unsicherheit. Rechtmäßiger behördlicher Abgleich und illegale Verknüpfung nach einem Datenleck sind getrennte Szenarien. Für Letzteres ist keine rechtliche Zugriffsbefugnis vorauszusetzen.

[EuGH C-340/21, Rn. 39 und 42 bis 52](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62021CJ0340) verlangt eine konkrete Prüfung der Sicherheitsmaßnahmen und ihrer praktischen Wirksamkeit; ein Datenleck allein beweist deren Unzulänglichkeit nicht. Die amtlich bestätigten Vorfälle bei [DGFiP](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/) und [FICOBA](https://www.impots.gouv.fr/actualite/acces-illegitimes-au-fichier-national-des-comptes-bancaires-ficoba) belegen reale Angriffswege auf französische Steuer- und Kontendaten, keine österreichischen oder DAC8-spezifischen Mängel. Entscheidend sind beim betroffenen System insbesondere Datentrennung, Zugriffs- und Exportrechte, Protokollierung und Reaktion auf Vorfälle.

[Gutachten 1/15, Rn. 124 bis 141](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A62015CV0001%2801%29), [C-817/19, Ligue des droits humains](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62019CJ0817) und [EGMR L.B. gegen Ungarn](https://hudoc.echr.coe.int/eng?i=001-223675) liefern ergänzende Prüffaktoren, keine unmittelbare DAC8-Entscheidung. Eine allgemeine Erhebung kann zulässig bleiben, während spätere Speicherung oder Nutzung enger zu begrenzen ist. Eine bloß denkbare mildere Regel genügt nicht.

## 3. Österreichische Speicherung

### Drei unterschiedliche Datenbestände

- **Bereits übermittelte Informationen beim Anbieter:** [§ 20 Abs. 4 Krypto-MPfG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20013064&Paragraf=20) sieht Löschung zehn Jahre nach Ablauf des Meldezeitraums vor. Vor der ersten Meldung ist diese Regel regelmäßig noch nicht entscheidungserheblich.
- **Dokumentation der Melde- und Sorgfaltsschritte:** [§ 39 Krypto-MPfG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20013064&Paragraf=39) verlangt zehn Jahre ab Ablauf des Meldezeitraums. Anhang VI Abschnitt V.B.1 DAC8 sieht fünf bis zehn Jahre vor, allerdings ab Ende des Zeitraums, innerhalb dessen zu melden ist. Dauer und Fristbeginn sind getrennt zu prüfen.
- **Behördenkopien:** Art. 22 Abs. 3 der Richtlinie verlangt für durch automatischen Austausch erhaltene Informationen mindestens fünf Jahre ab Eingang, aber nicht länger als erforderlich. Für die österreichische Ursprungskopie sind Art. 25 Abs. 5 und die einschlägige nationale Grundlage gesondert zu bestimmen. Die Anbieterfrist ist kein allgemeines Behördenlimit.

### Konkreter Vergleich und Gegenposition

[§ 5 Abs. 3 GMSG](https://ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009250&Paragraf=5) sieht für übermittelte Informationen fünf Jahre vor; die [Materialien 2018](https://www.parlament.gv.at/dokument/XXVI/I/190/fnameorig_698479.html) bezeichneten diese Dauer als datenschutzrechtlich angemessen. [§ 7a GMSG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009250&Paragraf=7a) verwendet für Compliance-Unterlagen sieben Jahre. Das Krypto-MPfG wählt jeweils zehn.

Die [Krypto-MPfG-Materialien](https://www.parlament.gv.at/dokument/XXVIII/I/306/fnameorig_1723216.html) nennen Vereinfachung, absolute Verjährung nach § 209 Abs. 3 BAO und die EU-Spanne von fünf bis zehn Jahren, erörtern aber die GMSG-Abweichung nicht. Die EU-Spanne betrifft unmittelbar die Dokumentation der Melde- und Sorgfaltsschritte, nicht selbstverständlich das vollständige Profil bereits übermittelter Informationen. Österreich kann für Letzteres dennoch eine eigenständige Rechtfertigung vorbringen.

[VfGH G 7/2012](https://www.ris.bka.gv.at/VfghEntscheidung.wxe?Abfrage=Vfgh&Dokumentnummer=JFT_09879371_12G00007_00&IncludeSelf=True) deutet die Frist des § 75 Abs. 3 StPO als Höchstfrist und verlangt frühere Löschung bei weggefallener Erforderlichkeit. Diese Analogie stützt die Prüfung einer Ablehnung früherer Löschung, die zehn Jahre unterschiedslos als Mindestdauer behandelt. Dokumentation, Meldedaten und zusätzliche Providerdaten dürfen dabei nicht gleichgesetzt werden.

Die isolierte Aufhebung einer Löschungsfrist kann den Schutz verschlechtern, wenn lediglich die Höchstfrist entfällt. Bei § 39 bleibt außerdem die unionsrechtliche Mindestaufbewahrung zu berücksichtigen. Ein sinnvoller Angriff muss die verbleibenden Pflichten und die betroffene Datenkopie bestimmen, nicht nur „zehn Jahre“ beanstanden.

## 4. Ergänzende, tatsachenabhängige Ansätze

**Bewertung und Berichtigung.** § 18 Abs. 2 bis 4 lässt unterschiedliche Bewertungsmethoden zu; Abweichungen sind nicht automatisch Fehler. Ein dokumentierter Bewertungs- oder Klassifikationsfehler kann Art. 5 Abs. 1 lit. d, 16 und 19 [DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) aktivieren. [C-487/21, CRIF](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62021CJ0487) stützt die verständliche Datenkopie, [C-154/21, Österreichische Post](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62021CJ0154) grundsätzlich die Benennung tatsächlicher Empfänger. Nach Übermittlung ist die Berichtigung einschließlich Empfängerverständigung je Verantwortlichem zu prüfen.

**Sekundärnutzung.** Art. 16 der Richtlinie und [§ 15 EU-AHG](https://ris.bka.gv.at/eli/bgbl/i/2012/112/P15/NOR40273392) eröffnen für ausgetauschte Informationen mehrere Steuer-, Zoll-, AML/CFT- und Beitreibungszwecke sowie weitere bedingte Nutzungen. Sie rechtfertigen nicht automatisch jede Verwendung der österreichischen Ursprungskopie. [VfGH G 2/2013](https://www.ris.bka.gv.at/VfghEntscheidung.wxe?Abfrage=Vfgh&Dokumentnummer=JFT_20131001_13G00002_00&IncludeSelf=True) verlangt eine hinreichend bestimmte und verhältnismäßige Ermächtigung. Nachzuweisen wäre ein konkreter Zugriff, Abgleich oder Weiterempfänger. DAC8 verteilt Daten ansässigkeitsbezogen, nicht unterschiedslos an alle Staaten; für CARF-Daten aus Drittstaaten gilt ein anderes Vertragsregime.

**DSFA und Durchführungsverordnung.** Eine fehlende Datenschutz-Folgenabschätzung macht das Gesetz nicht automatisch ungültig ([C-61/22, Rn. 64 bis 68](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62022CJ0061)). Relevant sind tatsächliche DSFA-Pflichten oder Ausnahmen der Verantwortlichen. Für die Verordnung sind die Anhörung nach [§ 21 Abs. 1 DSG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001597&Artikel=2&Paragraf=21) und etwaige zusätzliche materielle Pflichten in externen XML-/XSD-/WSDL-Vorgaben zu prüfen. Eine unveröffentlichte Stellungnahme beweist keine unterlassene Anhörung. [VfGH V 531/2020](https://www.ris.bka.gv.at/Dokumente/Vfgh/JFT_20220317_20V00531_00/JFT_20220317_20V00531_00.pdf) betrifft eine andere Anhörungspflicht, nach § 94f StVO. Bei unmittelbar anbieterbezogenen Pflichten der Krypto-MPfG-DV ist die Präjudizialität im Nutzerverfahren gesondert zu begründen.

**DLT-Fehlverweis.** Das [DAC8-Korrigendum](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32023L2226R%2801%29) verweist für die DLT-Adresse auf Art. 3 Z 18 der Verordnung (EU) 2023/1113. [§ 4 Abs. 7 Krypto-MPfG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20013064&Paragraf=4) und § 18 Abs. 1 Z 3 lit. i nennen weiterhin 2023/1114. Bei erfassten Transfers entsteht eine Bestimmtheitsfrage. Ein korrigierbares Redaktionsversehen ist die naheliegende Gegenposition; daraus folgt kein tragfähiger Systemangriff.

## 5. Entscheidende Punkte für den Verfahrensaufbau

**Aktuelle Verarbeitung und anwendbare Norm.** [VfGH G 178/2024](https://www.ris.bka.gv.at/Dokumente/Vfgh/JFT_20260428_24G00178_00/JFT_20260428_24G00178_00.pdf) spricht für ein erhebliches Subsidiaritätsrisiko des direkten Nutzer-Individualantrags bei zumutbarem DSB/BVwG-Weg. Eine Beschwerde nach [§ 24 DSG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001597&Artikel=2&Paragraf=24) benötigt eine konkrete Verarbeitung durch den bezeichneten Verantwortlichen. Eine bloße Auskunftsbeschwerde macht die Meldepflichten noch nicht entscheidungserheblich. Ein Löschungsbegehren ist erforderlich, wenn dessen Ablehnung oder Nichtbeantwortung gerügt wird, aber keine allgemeine Voraussetzung jeder Datenschutzbeschwerde.

Für 2026 meldet der Anbieter spätestens am [31. Juli 2027, § 19](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20013064&Paragraf=19); der Austausch erfolgt spätestens am [30. September 2027, § 21](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20013064&Paragraf=21). Bereits laufende Ermittlung, Aggregation oder Speicherung ist von einer nur künftigen Übermittlung zu unterscheiden ([DSB 2023-0.632.875](https://www.ris.bka.gv.at/JudikaturEntscheidung.wxe?Abfrage=Dsk&Dokumentnummer=DSBT_20230919_2023_0_632_875_00&ShowPrintPreview=True)). Die tatsächlichen Verarbeitungsschritte und Termine sind zu belegen.

**Normebene und Rechtsfolge.** Die EU-Gültigkeitsfrage kann bereits das BVwG vorlegen. Nationale Gerichte dürfen einen Gültigkeitseinwand verwerfen, aber entscheidungserhebliche EU-Normen nicht selbst für ungültig erklären ([Foto-Frost, C-314/85](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:61985CJ0314)). Österreichische Gestaltungsspielräume sind davon getrennt verfassungsrechtlich zu prüfen. Bei einzelnen Feldgruppen müssen die nationalen und beide EU-Regelungsstellen erfasst sein; ihre Abtrennbarkeit darf Geist oder Wesen der Regelung nicht verändern ([C-121/14, Rn. 20 bis 21](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62014CJ0121)).

§ 24 Abs. 5 DSG sichert bei privaten Verantwortlichen gegebenenfalls die Erfüllung der dort genannten Betroffenenanträge, keinen allgemeinen Wiederherstellungsanspruch. Weitergehende Maßnahmen richten sich nach Art. 58 Abs. 2 DSGVO. Eine Aufhebung oder Ungültigkeitsentscheidung bedeutet nicht automatisch sofortige Löschung sämtlicher Datenkopien; Reichweite, zeitliche Wirkung und operative Abhilfe sind getrennt zu bestimmen.

**Vorläufiger Schutz.** Die Beschwerde stoppt die Verarbeitung nicht automatisch. Nach [§ 25 Abs. 1 DSG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001597&Artikel=2&Paragraf=25) kann die DSB bei glaubhaft gemachter wesentlicher Beeinträchtigung nach [§ 22 Abs. 4 DSG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001597&Artikel=2&Paragraf=22) vorgehen. Das vorläufige Verbot erfordert nach [DSB 2024-0.215.259, D.1](https://www.ris.bka.gv.at/Dokumente/Dsk/DSBT_20240328_2024_0_215_259_00/DSBT_20240328_2024_0_215_259_00.pdf) einen begründeten Verdacht rechtswidriger Verarbeitung und eine wesentliche unmittelbare Gefährdung schutzwürdiger Geheimhaltungsinteressen (Gefahr im Verzug). Allgemeine Befürchtungen reichen nicht. Eine Entscheidung vor der ersten Meldung ist nicht gesichert.

**Abweichende Nutzerkonstellationen.** § 20 Abs. 1 betrifft die Verarbeitung für alle Kunden. Ein nicht meldepflichtiger Nutzer könnte damit einen anderen nationalen Angriff eröffnen; das ist nicht mit dem EU-Gültigkeitsangriff eines meldepflichtigen Nutzers gleichzusetzen. Eine eigenständige österreichische Gleichheitsrüge benötigt einen präzisen Vergleich im nationalen Gestaltungsspielraum, nicht nur fehlenden Verdacht oder eine fehlende Bagatellgrenze.

Für die Zuständigkeit und den Beschwerdegegenstand sind verantwortlicher Anbieter, österreichischer Anknüpfungspunkt, Steueransässigkeit, Nutzerstatus und tatsächlich gebildete Datenfelder festzustellen. Bei grenzüberschreitender Verarbeitung ist die Behördenzuständigkeit gesondert zu bestimmen.
