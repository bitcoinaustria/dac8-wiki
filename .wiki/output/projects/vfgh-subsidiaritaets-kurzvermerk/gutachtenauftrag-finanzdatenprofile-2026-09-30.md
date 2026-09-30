---
title: "Technischer Gutachtenauftrag zu Finanzdatenprofilen"
type: report
sources:
  - wiki/references/dac8-blockchain-linkage-expert-evidence-protocol.md
  - wiki/references/krypto-mpfg-provider-record-architecture.md
  - wiki/references/dac8-inference-linkage-and-error-evidence.md
  - wiki/theses/transaction-data-wealth-inference.md
  - wiki/references/austrian-security-evidence-access.md
  - wiki/references/dac8-field-necessity-and-alternatives.md
generated: 2026-09-30
---

# Technischer Gutachtenauftrag zu Finanzdatenprofilen

Entwurf vom 30. September 2026. Gegenstand sind Anbieteraufzeichnungen und die Zusammenführung finanzieller Daten bei Behörden. Der Auftrag legt kein Ergebnis fest. Die rechtliche Bewertung der einschlägigen Pflichten und ihrer Verhältnismäßigkeit bleibt vom technischen Befund getrennt.

## Zweck und Untersuchungsgegenstand

Das Gutachten soll eine überprüfbare technische Grundlage dafür schaffen, welchen zusätzlichen Informationsgehalt bestimmte Finanzdaten, ihre Aufbewahrung und ihre Zusammenführung haben. Untersucht werden sollen Erkenntnisse über Finanzaktivität, Vermögensindikatoren und Selbstverwahrung von Kryptowerten, einschließlich möglicher Blockchain-Zuordnungen und ihrer Unsicherheiten. Zudem sind konkrete Sicherheits- und Missbrauchsrisiken sowie alternative Daten- und Zugriffskonzepte zu vergleichen.

Die Untersuchung muss sowohl den Nutzen für die bezeichneten Steuer- oder anderen gesetzlich zulässigen Verwaltungsaufgaben als auch zusätzlichen Informationsgehalt, Fehlerrisiken und Datenexposition erfassen. Ein Ergebnis zugunsten des bestehenden Designs, kein messbarer Informationszuwachs oder fehlende Vergleichbarkeit sind ebenso auszuweisen wie ein Ergebnis zugunsten einer Alternative.

## Zwei getrennte Untersuchungsstränge

| Strang | Eingaben | Zu beantwortende Fragen |
|---|---|---|
| Tatsächlicher Bestand beim Anbieter von Kryptowerte-Dienstleistungen (CASP) | Dokumentierte Kunden-, Melde-, Einzeltransaktions-, Adress- und Kontrollnachweise; Löschungsantwort und einschlägige Rechtsgrundlagen | Welche Daten bestehen? Was verbinden sie? Welche Informationen bleiben nach einer engeren Speicherung oder Löschung unabhängig rechtmäßig verfügbar? |
| Tatsächliche oder konkret vorgesehene Behördenverarbeitung | Vorgesehene Jahresfelder, verfügbarer Bestand, zulässige Register- und Anbieterzugänge, Rollen und Lebenszyklus | Was ergibt sich aus mehreren Jahren und zusätzlichen Datenquellen? Welche Zugriffe und Verknüpfungen sind tatsächlich vorgesehen oder ausgeübt? |

Technisch mögliche, rechtlich erlaubte und tatsächlich ausgeübte Verknüpfungen sind getrennt zu kennzeichnen. Einzelunterlagen des Anbieters dürfen nicht als Inhalt einer Jahresmeldung vorausgesetzt werden. Ein Datenhalter ist nicht automatisch zu jedem technisch möglichen Zweck befugt. Welche Normen und Zeitfassungen maßgeblich sind, soll vor dem Test mit dem rechtlichen Auftraggeber geklärt werden.

## Datenmodell und Lebenszyklus

Für jedes Feld sind Inhalt, Herkunft, Granularität, Identitätsbezug, Zweck, Halter, Empfänger und Speicherfrist zu erfassen. Zu unterscheiden sind Originale, Übermittlungskopien, Archiv, Backups, Arbeitskopien, Exporte, abgeleitete Merkmale und gespeicherte Zuordnungen. Bei Löschung oder Abschottung ist zu prüfen, welche andere Kopie oder unabhängige Pflicht denselben Informationszugang erhält.

Das Modell soll Bestandsdaten, Bewegungsdaten und Registerbeziehungen getrennt führen. Wirtschaftliche Positionen, Eigenüberträge, Gemeinschaftskonten, Wiederanlage, Sicherheiten, Schulden und technische Repräsentationen sind so zu behandeln, dass keine unbemerkte Doppelzählung entsteht.

Beim CASP sind Konto- und Geschäftsbeziehungsstatus, vorhandene Kontrollnachweise selbstgehosteter Adressen und tatsächliche Weitergaben an Identifizierungs-, Support- oder Analysepartner festzustellen. Eine verlangte gesetzliche Aufzeichnung und ihr Vorliegen im konkreten Fall sind verschiedene Befunde.

## Vorab festzulegende Vergleichsfragen

Die Sachverständigen sollen vor Datenauswertung die Zielgrößen, Vergleichsmodelle und Regeln für ein nicht aussagekräftiges Ergebnis dokumentieren. Zu prüfen sind mindestens:

1. Verändern zusätzliche Felder, Jahrgänge oder verlässliche Identitätsanker messbar die untersuchte Aussagekraft? Die Gegenhypothese lautet, dass kein praktisch relevanter Zusatzgewinn entsteht oder die Fehler zunehmen.
2. Wie unterscheiden sich Schätzungen aus Brutto- und sachgerecht gebildeten Nettogrößen von bekannten Beständen? Welche strukturellen Unbestimmtheiten bleiben trotz längerer Beobachtung?
3. Kann ein engeres Daten- oder Zugriffskonzept die vorab bestimmte Verwaltungsaufgabe innerhalb einer ebenfalls vorab begründeten Toleranz erfüllen und gleichzeitig Informationsgewinn oder Exposition reduzieren? Gegenhypothesen sind Nutzenverlust, unverändertes Risiko und bloße Risikoverlagerung.

Die Wirkung eines Felds ist nicht allein danach zu beurteilen, ob es nützlich ist. Zu messen ist auch sein zusätzlicher Nutzen gegenüber bereits verfügbaren Informationen. Die rechtliche Bedeutung dieses Ergebnisses ist nicht vom Gutachten vorwegzunehmen.

## Mehrjahresprofile und Vermögensschätzung

Ein, drei, fünf und zehn gleichzeitig verfügbare Perioden sollen als Szenarien verglichen werden, soweit geeignete Daten vorhanden sind. Für 2026 beginnende Kryptomeldungen darf eine synthetische Zehnjahresreihe nicht als heute beobachtete Reihe ausgegeben werden.

Gemeldete Aktivität, Bestand einer bestimmten Position und Gesamt-Nettovermögen sind getrennte Zielgrößen. Fehlerverteilungen, systematische Über- und Unterschätzung, Rangfehler, Unsicherheitsintervalle und Abdeckung sind gegen bekannte wahre Werte zu prüfen. Unbekannte Anfangsbestände und Vorgänge außerhalb des Beobachtungsbereichs dürfen nicht stillschweigend als null behandelt werden.

Kontrollfälle sollen unter anderem identische Meldungen bei späterem Halten oder Verschenken, wiederholten Handel mit demselben Kapital, Anbieterwechsel und Eigenüberträge enthalten. Diese Fälle prüfen logische Grenzen. Eine statistische Aussage für eine Bevölkerung verlangt zusätzlich eine geeignete und ausreichend bekannte Stichprobe.

## Blockchain-Zuordnung

Gestuft zu vergleichen sind öffentliches Ledger allein, tatsächliche Jahresfelder, geprüfte öffentliche Dienstlabels, konkrete Anbieter-Adress- oder Transaktionsanker und tatsächlich vorhandene Kontrollnachweise. Jeder hinzugefügte Datensatz, Zugriffsweg und Zweck ist zu dokumentieren.

Transaktions-, Adress-, Dienst-, Personen-, Kontroll- und Eigentumszuordnung sind getrennte Endpunkte. Ein Treffer auf einer Stufe ersetzt keine Prüfung der nächsten. Bitcoin, kontobasierte Chains, Lightning und andere nicht öffentliche Vorgänge benötigen unterschiedliche Beobachtungsmodelle. Gebühren, Sammelauszahlungen, gemeinsame Wallets, CoinJoin/PayJoin, Bridges und veraltete Labels sind als Negativkontrollen einzubeziehen.

Auszuweisen sind Bezugsgröße und Kandidatenmenge, Fälle ohne Kandidaten, richtige und falsche Treffer, Anteil gefundener echter Verbindungen, Nichtentscheidungen, Stichprobenabdeckung und Unsicherheitsintervalle. Hohe Trefferpräzision nur bei vorselektierten einfachen Fällen darf nicht auf den Ausgangsbestand übertragen werden. Synthetische Fehlerraten gelten nur unter den ausdrücklich beschriebenen Szenarioannahmen.

## Sicherheitsprüfung und Alternativen

Anbieterbestände sind als eigenständiger Prüfgegenstand zu behandeln, nicht nur als Zulieferung für Behörden. Zu ermitteln ist, welche identifizierbaren Felder und Jahrgänge aufgrund von gesetzlichen Pflichten zusätzlich oder länger vorliegen als für den laufenden Dienst erforderlich. Unabhängige Pflichten und andere tatsächliche Speichergründe müssen im Vergleich erhalten bleiben. Auch rechtmäßige Speicherung kann Datenexposition erzeugen.

Die Untersuchung soll die gesamte Kette abbilden: Anbieter und Archive, ausgelagerte Identifizierungs-, Support- und Analysedienste, Übermittlung, Behördenbestand und weitere Empfänger. Bei tatsächlich zusammenführbaren Daten mehrerer Anbieter sind Reichweite und zusätzlicher Informationsgehalt eines kompromittierten Zugangs festzustellen. Gemeinsame Dienstleister, Kennungen und Exporte können Risiken koppeln; statistische Unabhängigkeit ist nicht vorauszusetzen. Ein positives Audit einer Stelle ersetzt keinen Nachweis für die übrigen Stellen.

Getrennte Szenarien sind berechtigte Einzelprüfung, zweckwidrige interne Abfrage, gestohlene berechtigte Kennung, Massenexport sowie Zugriff durch Support, Administratoren und externe Dienstleister. Zu erfassen ist, welche Daten und Personenjahre je Weg erreichbar wären, ob Verknüpfungen zusätzliche Informationen erschließen und wie Prävention, Protokollkontrolle, Erkennung und Reaktion tatsächlich geprüft werden.

Mögliche finanzielle, persönliche und körperliche Schäden sind nach Mechanismus und Schwere zu beschreiben. Dokumentierte Vorfälle aus anderen Sektoren können Mechanismen illustrieren, aber keine Eintrittsquote für das untersuchte System liefern. Bestehende positive Auditbefunde sind ebenso einzubeziehen wie belegte Schwächen und offene Nachweise.

Vergleichsmodelle sind insbesondere getrennte Identitäts- und Aktivitätsbereiche, kontrollierte Verknüpfung, abgesondertes Pflichtarchiv, befristete Zugriffsrechte, kontrollierte Massenexporte, feldweise Löschung nach Fristablauf, engerer Routinebericht mit begründeter Nachforderung und nachprüfbare Korrektur abgeleiteter Merkmale. Gesetzlich geforderte Verfügbarkeit und mögliche Rechtsänderungen sind je Modell zu kennzeichnen.

Nutzen, Nachfragen, Verzögerung, Kosten, echte und falsche Verdachtsfälle sowie erreichbare Datenmenge und zusätzliches Personenwissen sind gemeinsam zu vergleichen. Echte Verwaltungswirkung darf nicht durch den bloßen Modellscore ersetzt werden. Verfahren mit geringerer zentraler Datenmenge können Risiken zu Anbietern verlagern; dies ist im Ergebnis zu berücksichtigen.

## Machbarkeit und Zugang zu Nachweisen

Die Untersuchung soll in zwei Zugangsstufen geplant werden:

| Zugangsstufe | Mögliche Ergebnisse | Grenze |
|---|---|---|
| Kontrollierte Testdaten, freiwillige eigene Unterlagen und öffentliche Quellen | Mechanismus, logische Gegenbeispiele, konkrete CASP-Felder, Szenariovergleiche | Keine repräsentative Behördenwirkung oder reale Bevölkerungs-Fehlerquote |
| Rechtmäßig bereitgestellte Daten und Kontrollnachweise von Anbietern oder Behörden; gegebenenfalls geschützte aufsichtsbehördliche oder gerichtliche Prüfung | Tatsächliche Architektur, Zugriffsrollen, Löschwirkung, realer Vergleich von Prüfungsfällen und Alternativen | Zugang und geeignete wahre Vergleichswerte sind nicht garantiert; Einschränkungen offenlegen |

Fehlender Zugang ist als Beweisgrenze zu dokumentieren, nicht als Beleg fehlender Kontrollen. Das Gutachten soll benötigte Unterlagen benennen, aber keine unbedingte Herausgabe oder bestimmte aufsichtsbehördliche Untersuchung voraussetzen.

## Reproduzierbarkeit und Schutz der Testpersonen

Methoden, Code, Datenstand, Blockhöhen, Labelversionen, Parameter, ausgeschlossene Fälle und Erfolgskriterien sind zu sichern. Zuordnungsprüfer sollen nach Möglichkeit gegenüber den wahren Labels verblindet werden. Ein unabhängiger Wiederholungslauf und die Dokumentation gescheiterter Zuordnungen sind vorzusehen.

Das Gutachten darf selbst keine unnötige neue Exposition erzeugen. Realdaten minimieren, Identitäten und Adressanker getrennt aufbewahren, Zugriff und Übermittlung beschränken sowie spätere Löschung festlegen. Öffentliche Fassungen enthalten keine nutzbaren Identitäts-Adress-Verbindungen. Hashwerte öffentlicher Adressen sind nicht automatisch anonym. Vertrauliche Vorlage und etwaige Akteneinsichtsgrenzen sind vor einer Weitergabe rechtlich zu klären. Fremde Personen dürfen nicht zu Demonstrationszwecken deanonymisiert werden.

## Erwartete Ergebnisse

Vorzulegen sind eine verständliche Zusammenfassung, eine Aussage-Evidenz-Grenzen-Matrix, Feld- und Lebenszyklusplan, dokumentierte Vergleichstests mit Fehlermessung und Negativkontrollen sowie ein Alternativenvergleich. Für jede Schlussfolgerung sind Datensatz, Voraussetzungen, Zugriffsszenario, zusätzlicher Nutzen, Unsicherheit und Reproduzierbarkeit anzugeben.

Offene oder widerlegte Hypothesen gehören in den Schlussbericht. Ohne ausreichende Daten sind keine Genauigkeits- oder Wirksamkeitsquoten zu behaupten. Das Gutachten entscheidet nicht über einen Prozesserfolg und verlangt keine vorgegebene Feststellung zur Rechtmäßigkeit.
