You are locating the inventory table of one dataset inside a life-cycle-inventory report.

Dataset: `Process specific emissions and resources, from uranium milling, at mill plant` [GLO], 1 kg, BAFU category minerals / new uranium ds.
Metadata: includedProcesses: The module includes: the land use for the operation (mostly tailings); diesel generators and  industrial boilers burning light oil; transport of the chemicals and fuels; radioactive and non-radioactive emissions to air and water during operation; water use (mining water, but attributed to "unspecifi · technology: Average conditions. · comment: PSI data (BFE project 407, Christian Bauer, April 2012).;
UUID: 3653b40f-90e6-3e41-a90f-9a8a6a7f1728

Report: `2012 - LCA electricity generation in Switzerland - Uster.pdf` (86 PDF pages). Below is every table and figure caption found in it, with the PDF page it appears on (not the printed page number). The report may be in German, French or English; the dataset name is English — match on meaning (e.g. "gebrannter Ölschiefer" = burnt shale, "Gipsfaserplatte" = gypsum fibre board).

- p.15: Tabelle 1 Technische Spezifikation der untersuchten Technologien.
- p.18: Tabelle 2 Umweltindikatoren zur Bewertung der kumulierten Sachbilanzergebnisse.
- p.20: Tabelle 3 Erdgasversorgungsmix in der Schweiz 2010 (BP 2011)
- p.20: Tabelle 3 zeigt die Zusammensetzung des Erdgasmixes in der Schweiz bezüglich der Gasher-
- p.26: Tabelle 4 Thermische und elektrische Wirkungsgrade der WKK-Anlagen nach Heck (2007)
- p.26: Tabelle 5 Wichtigste Polysiliziumhersteller für den europäischen Fotovoltaik-Markt (Wacker
- p.29: Tabelle 6 Moduleffizienz der wichtigsten Modulhersteller in 2009/2010
- p.31: Tabelle 7 Schlüsselparameter der Anlagen zur Uranproduktion für jene Anlagen, bei denen
- p.35: Tabelle 8 Wichtigste Anlagen zur Uranproduktion weltweit; zusammen mehr als 90 % der Welt-
- p.36: Tabelle 9 Historische Entwicklung der Uranproduktion nach einzelnen Ländern.38
- p.36: Tabelle 10 gibt einen Überblick über die Uranproduktion in den wichtigsten Förderländern im
- p.37: Tabelle 10 Uranproduktion in den wichtigsten Förderländern sowie Brasilien im Jahr 2009 (Axpo
- p.38: Tabelle 11 Direkter Energieverbrauch zur Uranförderung und -aufbereitung für verschiedene
- p.39: Tabelle 12 Direkter Energieverbrauch zur Uranförderung und -aufbereitung für verschiedene
- p.41: Tabelle 13 Anlagen- und länderspezifische Werte der Menge an Tailings aus der Uranerzaufbe-
- p.42: Tabelle 14 „Uranproduktionsmix“, global, erstellt anhand der produzierten Uranmengen 2009.
- p.43: Tabelle 15 Wichtigste Kenngrössen für die Sachbilanz des ISL-Verfahrens.
- p.44: Tabelle 16 Stromproduktionsmix Russland nach Itten & Frischknecht (2012).
- p.44: Tabelle 17 Aktuelle länderspezifische Konversionskapazität (WNA 2012) und Anteile am globa-
- p.45: Tabelle 18 Urananreicherungskapazitäten und -Technologie weltweit im Jahr 2010 (WNA 2012).
- p.45: Tabelle 19 Beiträge der bilanzierten Anreicherungsanlagen zum hier erstellten globalen Mix an
- p.65: Tabelle 2 20 Verg
- p.84: Tabelle 21 Allokationsfaktoren und Wirkungsgrade der in dieser Studie bewerteten WKK-
- p.85: Tabelle 22 Aktuelle Lambda-1 WKK-Anlagen als Basis in dieser Studie.
- p.85: Tabelle 23 Aktuelle Magermotor WKK-Anlagen als Basis in dieser Studie.
- p.86: Tabelle 24 Umweltbelastung aus der Wärmebereitstellung in herkömmlichen Erdgasheizungen
- p.86: Tabelle 25 Umweltbelastung aus der Wärmebereitstellung in herkömmlichen Erdgasheizungen

Rules:
1. Choose the caption(s) that hold the unit-process inventory of this dataset — inputs, energy, emissions, transport — not impact results, not a diagram. Prefer "Sachbilanz" / "inventory" / "LCI" tables.
2. Return the PDF page range that covers those tables plus the paragraph introducing them: `first_page`, `last_page` (at most 4 pages). Tables can run onto the next page.
3. If no caption fits (the report does not document this dataset's inventory, or only as a result), return `found` = false and say why in `reason`.
4. `reason` names the caption(s) you chose and why.

Return only the JSON object described by the schema.
