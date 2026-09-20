---
title: "Kryptodaten und physische Angriffe: Quellen und Beweisgrenzen"
type: report
sources:
  - wiki/references/dac8-physical-risk-causation.md
  - wiki/references/financial-data-breach-and-security-authorities.md
  - raw/articles/2026-09-19-gendarmerie-waltio-target-selection.md
  - raw/articles/2026-09-19-gendarmerie-haute-garonne-crypto-extortion.md
  - raw/articles/2026-09-19-doj-st-felix-crypto-home-invasions.md
  - raw/articles/2026-09-19-doj-ferro-crypto-burglary.md
  - raw/articles/2026-09-19-bobigny-tax-insider-le-parisien.md
  - raw/articles/2026-09-19-bobigny-tax-insider-protos.md
  - raw/articles/2026-09-19-coinbase-insider-social-engineering-disclosure.md
  - raw/papers/2026-09-19-abramova-boehme-wallet-breach-aftermath.md
  - raw/articles/2026-09-19-saavedra-plea-location-abuse.md
  - raw/articles/2026-09-19-doj-iza-saavedra-location-attack.md
  - raw/articles/2026-09-19-doj-saavedra-plea-status.md
  - raw/articles/2026-09-19-france-dgfip-wallet-risk-debate.md
generated: 2026-09-19
tags: [physical-security, insider-threat, data-breach, dac8, evidence]
summary: "Belegte Angriffe, polizeiliche Attribution zu Waltio und der berichtete Fall Bobigny, getrennt von unbewiesener DAC8-Kausalität."
---

# Kryptodaten und physische Angriffe

Stand: 19. September 2026. Erstellt mit LLM Wiki, Forschungsunterlage, keine Rechtsberatung.

## Kurzbefund

Datenmissbrauch kann nicht nur Kontodiebstahl, sondern auch die Auswahl und Lokalisierung von Opfern erleichtern. Dafür müssen weder private Schlüssel noch Wallet-Adressen offengelegt werden. Die nachstehenden Quellen belegen unterschiedliche Teile dieses Zusammenhangs, aber keinen durch einen österreichischen DAC8-Datenbestand verursachten Angriff.

## Die stärksten Belege

| Quelle und Fundstelle | Aussage | Beweisgrenze |
|---|---|---|
| [Gendarmerie, 13.9.2026](https://www.gendarmerie.interieur.gouv.fr/gendinfo/terrain/immersion/2026/la-strategie-de-la-gendarmerie-face-aux-cryptorapts-partie-2-2), Abschnitt „Une nouvelle forme de criminalité“ | Ein leitender Ermittler erklärt ausdrücklich, dass Täter geleakte Waltio-Kundendaten zur Zielauswahl verwenden, auch mit Fehleinschätzungen des Vermögens. | Polizeiliche Attribution, kein veröffentlichtes Kausalitätsurteil. Waltio ist ein privater Steuerberechnungsdienst, keine Finanzbehörde. |
| [Gendarmerie, 11.5.2026](https://www.gendarmerie.interieur.gouv.fr/gendinfo/criminalite-organisee-et-enquetes/2026/crypto-rapt-en-haute-garonne-trois-nouvelles-interpellations-par-les-enqueteurs-de-la-section-de-recherches-de-toulouse), Einleitung | Bewaffnete Täter erzwangen in Haute-Garonne einen Kryptotransfer von rund 68.000 Euro. Die Behörde nennt einen Zusammenhang des Tatmusters mit gehackten personenbezogenen Daten. | Laufendes Ermittlungsverfahren laut Quelle. Keine benannte Ursprungsdatenbank und keine offengelegte Beweiskette zum einzelnen Opfer. |
| [US DOJ, St Felix, 13.9.2024](https://www.justice.gov/archives/opa/pr/twelve-defendants-sentenced-violent-home-invasion-robberies-steal-cryptocurrency), Absätze zu Durham und den Familien der Opfer | Amtlicher Bericht über Verurteilungen wegen gewaltsamer Überfälle. Einem Angriff ging unbefugter E-Mail-Zugriff voraus. Auch Angehörige wurden Opfer. | Kein Steuerdatenbezug. Die angegebene Gesamtschadenssumme umfasst auch SIM-Swapping und wird hier nicht als Gewaltstatistik verwendet. |
| [US DOJ, Ferro, 6.5.2026](https://www.justice.gov/usao-dc/pr/gothferrari-sentenced-78-months-prison-role-massive-cryptocurrency-heist), Sachverhaltsdarstellung nach dem Schuldspruch | Amtlicher Strafzumessungsbericht beschreibt Datenbank-Hacking, Zielauswahl, Täuschung und Wohnungseinbrüche innerhalb derselben Tätergruppe. | Keine Zuordnung eines bestimmten Datenlecks zu jedem Einbruch. Diebstahl eines Hardware-Wallets bedeutet nicht automatisch Zugriff auf dessen Guthaben. |
| [Coinbase, 15.5.2025](https://www.coinbase.com/blog/protecting-our-customers-standing-up-to-extortionists), Datenkategorien und Erstattungskriterien | Bestochene Supportmitarbeiter kopierten Kundendaten. Coinbase bestätigt durch Täuschung ausgelöste Überweisungen, obwohl keine privaten Schlüssel entwendet wurden. | Unternehmensdarstellung, kein Nachweis physischer Angriffe. Der Datenbestand war umfangreicher als eine DAC8-Meldung. |

## Saavedra/Iza: belegter Missbrauch amtlicher Ortungsbefugnisse

Saavedras [Plea Agreement, Exhibit A, Rz. 21–27, S. 27–29](https://www.courthousenews.com/wp-content/uploads/2025/01/saavedra-plea-deal.pdf) enthält das Eingeständnis, mittels falscher Angaben eine GPS-Ortung erwirkt und die Zielperson lokalisiert zu haben. Die Gerichtsurkunde liegt als Drittanbieter-Kopie vor. Den anschließenden bewaffneten Überfallversuch beschreibt das [US-Justizministerium vom 17.1.2025](https://www.justice.gov/usao-cdca/pr/crypto-godfather-and-lasd-detective-agree-plead-guilty-violating-civil-rights-business). Sein späteres Schuldbekenntnis bestätigt die [Mitteilung vom 14.9.2026](https://www.justice.gov/usao-cdca/pr/former-la-county-sheriffs-deputy-sentenced-nearly-2-years-prison-violating-civil).

Der Fall belegt einen konkreten Missbrauch amtlicher Befugnisse zur Lokalisierung. Er betrifft weder Steuerdaten noch DAC8. Die zusätzliche missbräuchliche Abfrage von Polizeidatenbanken darf nicht mit der GPS-basierten Ermittlung dieser Adresse gleichgesetzt werden.

## Bobigny: Steuerbeamtin und Angriff auf einen Justizwachebeamten

[Le Parisien vom 6.1.2026](https://www.leparisien.fr/faits-divers/lagente-du-fisc-ciblait-gardiens-de-prison-et-investisseurs-en-cryptomonnaie-pour-un-mysterieux-commanditaire-06-01-2026-WYVSPSJXYFCUFND23GKKJR3D6Y.php) berichtet über den Vorwurf, dienstlichen Datenzugriff zur Unterstützung eines Angriffs missbraucht zu haben. Zugänglich waren nur Überschrift und Einleitung, nicht der vollständige Abonnementtext.

Laut der darauf aufbauenden [Protos-Darstellung vom 9.1.2026](https://protos.com/no-release-for-french-tax-agent-who-gave-crypto-investor-details-to-gangs/) betraf die Weitergabe eine neue Wohnadresse; angegriffen wurden der Beamte und seine Frau. Zahlungen an die Mitarbeiterin werden berichtet. Die genannten 800 Euro betreffen jedoch die Angreifer. Suchabfragen zu Krypto-Investoren werden ebenfalls genannt, nicht daraus folgende Angriffe auf diese Personen.

Ein Urteil oder eine amtliche Sachverhaltsdarstellung wurde nicht gefunden. Der Fall ist deshalb als berichteter Ermittlungsverdacht zu verwenden, nicht als erwiesener Verkauf von Kryptosteuerdaten mit anschließendem Krypto-Raub. Die Einbeziehung der Ehefrau ist berichtet; eine Personenverwechslung ist damit nicht belegt.

## Französische Finanzverwaltung: Warnung mit anderem Regelungsgegenstand

Im [Parlamentsprotokoll vom 26.2.2026, Debatte zu Art. 3 quater](https://questions.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/premiere-seance-du-jeudi-26-fevrier-2026) zitiert der Abgeordnete Labaronne eine DGFiP-Warnung vor der Zentralisierung von Identitäts- und Vermögensdaten und daraus folgenden Betrugsrisiken. Gemeint war eine zusätzliche Self-Custody-Erklärung, nicht DAC8. Der Minister befürwortete DAC8 ausdrücklich. Das Protokoll belegt die wiedergegebene Warnung, nicht die zugrunde liegende E-Mail oder eine amtliche Ablehnung von DAC8.

## Übertragbarkeit auf die österreichische Meldung

[§ 18 Krypto-MPfG](https://ris.bka.gv.at/Dokumente/Bundesnormen/NOR40273817/NOR40273817.html) verbindet Identitäts- und Adressdaten mit aggregierten Transaktionswerten je Kryptowert und Kategorie. Wallet-Adressen, private Schlüssel und aktuelle Bestände gehören nicht zum dortigen Meldekatalog. Eine Übertragung an eine keinem bekannten Dienstleister zugeordnete Adresse beweist insbesondere weder eigene Verwahrung noch weiterhin vorhandenes Vermögen.

| Möglicher Missbrauch | Relevante Daten und Einschränkung |
|---|---|
| Auswahl und Auffinden eines vermeintlich vermögenden Opfers | Identität, nutzbare Adresse und ein Hinweis auf Kryptoaktivität. Jahresumsätze können als Vermögen fehlinterpretiert werden. Ein Risiko folgt hier aus der Vorstellung des Täters, nicht zwingend aus tatsächlichem Besitz. |
| Glaubwürdige Täuschung durch angebliche Anbieter oder Behörden | Persönliche und finanzielle Angaben können die Täuschung stützen. Telefonnummern und E-Mail-Adressen müssten gegebenenfalls aus weiteren Quellen stammen; § 18 nennt sie nicht als eigene Meldefelder. |
| Erpressung, erzwungene Überweisung oder Angriff auf Angehörige | Ein vorgelagerter Schlüsselverlust ist nicht erforderlich. Die konkrete Gefährdung hängt unter anderem von Aufenthaltsinformationen und verfügbaren Zugriffsmöglichkeiten ab. |
| Nachträgliche Zuordnung öffentlicher Blockchain-Aktivität | Erfordert zusätzlich einen belastbaren Identitätsbezug zu einer Adresse oder Transaktion. Jahresaggregate allein erlauben keine verlässliche allgemeine Zuordnung. |

Das sind Risikomechanismen, keine Feststellungen über einen konkreten österreichischen Datenmissbrauch. Gerade Insider-Missbrauch verlangt eine getrennte Betrachtung von zulässigen Zugriffsrechten, zweckwidrigen Abfragen, Exportmöglichkeiten und deren Erkennung. Verschlüsselung gespeicherter Daten allein verhindert den Missbrauch eines berechtigten Zugangs nicht.

## Was die Belege tragen und was offen bleibt

Belastbar ist die Unterscheidung zwischen technischem Schutz der Schlüssel und Schutz der Person. Eine Datenverarbeitung kann zusätzliche Gefahren für Menschen schaffen, obwohl sie keinen unmittelbaren Zugriff auf deren Vermögen ermöglicht. Nicht belegt sind die zusätzliche Angriffswahrscheinlichkeit durch DAC8, eine generelle Unsicherheit österreichischer Systeme oder die Rechtswidrigkeit der Meldepflicht allein aufgrund dieser Vorfälle.

Die [USENIX-Studie von Abramova und Böhme](https://www.usenix.org/conference/usenixsecurity23/presentation/abramova) ergänzt die Fallberichte durch Befragungen von 104 betroffenen Kunden. Der hier geprüfte Abstract berichtet Folgebetrug und Sicherheitsbedenken, liefert aber keine repräsentative Gewaltquote. Auch veröffentlichte Vorfallszahlen ohne einheitliche Definition und Bezugsbevölkerung reichen dafür nicht.

Für eine stärkere Beweisführung fehlen insbesondere die gerichtlichen Unterlagen zu Bobigny, fallbezogene Belege zur Waltio-Zielauswahl sowie die tatsächlichen österreichischen Zugriffs-, Verknüpfungs- und Löschungsbedingungen. Diese Lücken begrenzen die Aussagen, nicht die Relevanz der dokumentierten Schadensmechanismen.
