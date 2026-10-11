You are locating the inventory table of one dataset inside a life-cycle-inventory report.

Dataset: `Heat distribution, hydronic radiant floor heating, 150m2` [CH], 1 p, BAFU category energy, obsolete / heat, obsolete\heat pumps, obsolete\infrastructure.
Metadata: includedProcesses: The module includes the most important materials and transport needed for production. · technology: Underfloor heating. · comment: Average infrastructure.;
Synonyms: floor radiation heating, radiant floor heating, hydronic radiant floor heating; 
UUID: d4f0b20e-20b9-322f-a0a8-71083885972b

Report: `2007 - Heat pumps - Heck.pdf` (42 PDF pages). Below is every table and figure caption found in it, with the PDF page it appears on (not the printed page number). The report may be in German, French or English; the dataset name is English — match on meaning (e.g. "gebrannter Ölschiefer" = burnt shale, "Gipsfaserplatte" = gypsum fibre board).

- p.10: Fig. 2.1 Grundprinzip einer Wärmepumpe.
- p.12: Fig. 2.2 COP (Coefficient of Performance) bzw. Leistungszahl einer idealen Wärmepumpe in Abhängigkeit von der
- p.12: Tab. 2.1 Bezeichnung der Temperaturbedingungen für Wärmepumpen.
- p.14: Tab. 2.2 Ozonabbaupotential (ODP, Ozone Depletion Potential) und Treibhauspotential mit Zeithorizont 100 Jahre (GWP100,
- p.14: Tab. 2.3 Zusammensetzung der gebräuchlichen Kältemittelmischungen R404A, R407C und R410A (EPA 2002) und
- p.17: Fig. 2.3 Typische Temperaturbereiche im EWS-WP-Heizsystem.
- p.18: Tab. 3.1 Bestand an Elektromotorwärmepumpen in der Schweiz (einschliesslich Geothermienutzung mit Wärmepumpe)
- p.19: Tab. 3.2 zeigt die Stromproduktion durch geothermale Anlagen und die installierte Leistung im Jahr 2000 für
- p.20: Tab. 3.2 Installierte Leistung und Stromproduktion aus geothermaler Energie im Jahr 2000 (Huttrer 2001).
- p.21: Tab. 3.3 Direkte Nutzung von Erdwärme weltweit (ohne Stromproduktion) im Jahr 2000 (Lund & Freeston 2001).
- p.23: Tab. 4.1 zeigt die Namen der verfügbaren Datensätze zur Nutzwärme aus Wärmepumpen im Überblick.
- p.23: Tab. 4.1 Namen der Datensätze zur Nutzwärme aus Wärmepumpen.
- p.25: Tab. 5.1 Eingabedaten des Moduls "Wärmepumpe 10 kW".
- p.27: Tab. 5.2 Eingabedaten des Moduls "Erdwärmesonde 150 m".
- p.28: Tab. 5.3 Eingabedaten des Moduls "Wärmeverteilung, Fussbodenheizung, 150 m2".
- p.30: Tab. 5.4 Durchschnittliche Jahresarbeitszahlen (JAZ 2 bzw. SPF2) von Wärmepumpen in der Schweiz in Abhängigkeit vom
- p.32: Tab. 5.5 Verknüpfungen des Moduls "Nutzwärme, Erdwärmesonde, ab Sole-Wasser-Wärmepumpe 10kW" (ohne
- p.32: Tab. 5.6 Eingabedaten für Nutzwärme nach Wärmeverteilung
- p.33: Tab. 5.7 Eingabedaten der Sachbilanz zur Infrastruktur der Wärmepumpe, der Erdwärmesonde und der Wärmeverteilung.
- p.34: Tab. 5.8 Eingabedaten der Sachbilanz zur Wärme von Wärmepumpen in der Schweiz.
- p.35: Tab. 5.9 Eingabedaten der Sachbilanz zur Wärme von Wärmepumpen in Europa.
- p.36: Tab. 5.10 Eingabedaten der Sachbilanz zur Herstellung des Kältemittels R134a.
- p.38: Tab. 7.1 zeigt die Berechnungsresultate für Wärme ab Wärmepumpe vor der Wärmeverteilung im Haus, Tab.
- p.39: Tab. 7.1 Ausgewählte Resultate der kumulierten Sachbilanz und kumulierter Energieaufwand für Wärme ab 10-kW-
- p.39: Tab. 7.2 Ausgewählte Resultate der kumulierten Sachbilanz und kumulierter Energieaufwand für Wärme ab Raumheizung

Rules:
1. Choose the caption(s) that hold the unit-process inventory of this dataset — inputs, energy, emissions, transport — not impact results, not a diagram. Prefer "Sachbilanz" / "inventory" / "LCI" tables.
2. Return the PDF page range that covers those tables plus the paragraph introducing them: `first_page`, `last_page` (at most 4 pages). Tables can run onto the next page.
3. If no caption fits (the report does not document this dataset's inventory, or only as a result), return `found` = false and say why in `reason`.
4. `reason` names the caption(s) you chose and why.

Return only the JSON object described by the schema.
