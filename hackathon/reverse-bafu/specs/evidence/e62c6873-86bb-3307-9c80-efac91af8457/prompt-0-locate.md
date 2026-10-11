You are locating the inventory table of one dataset inside a life-cycle-inventory report.

Dataset: `Cellulose fibres (injected) (isofloc 2012)` [CH], 1 kg, BAFU category construction materials / others.
Metadata: includedProcesses: This data set includes the material use for the production or the disposal of building materials · technology: none · comment: The materials reflect average construction materials in Switzerland and are based on data from one company. Input is mainly waste paper. Waste paper from printing shops are not treated before use but only transported and used directly. Only transport is considered for these kind of papers (42% of in

Report: `2014 - Update material data in KBOB list - Wyss.pdf` (23 PDF pages). Below is every table and figure caption found in it, with the PDF page it appears on (not the printed page number). The report may be in German, French or English; the dataset name is English — match on meaning (e.g. "gebrannter Ölschiefer" = burnt shale, "Gipsfaserplatte" = gypsum fibre board).

- p.7: Tab. 2.1 Übersicht über die im Vergleich zum ecoinvent Datenbestand v2.2 aktualisierten Sachbilanzda-
- p.9: Tab. 3.1 Änderungen der Daten der Kategorie „02 Mauersteine“
- p.9: Tab. 3.2 Änderungen und Anpassungen der Daten der Kategorie „03 andere Massivbaustoffe“
- p.10: Tab. 3.3 Änderungen der Daten der Kategorie „05 Fenster oder Metall-Glas-Fassaden“
- p.11: Tab. 3.4 Änderungen der Daten der Kategorie „06 Metallbaustoffe“
- p.12: Tab. 3.4 Änderungen der Daten der Kategorie „06 Metallbaustoffe“ (Fortsetzung)
- p.13: Tab. 3.5 Änderungen der Daten der Kategorie „07 Holzwerkstoffe“
- p.14: Tab. 3.5 Änderungen der Daten der Kategorie „07 Holzwerkstoffe“ (Fortsetzung)
- p.15: Tab. 3.6 Änderungen der Daten der Kategorie „08 Klebstoffe und Fugendichtungsmassen“
- p.15: Tab. 3.7 Änderungen der Daten der Kategorie „09 Dichtungsbahnen und Schutzfolien“
- p.16: Tab. 3.8 Änderungen der Daten der Kategorie „10 Wärmedämmstoffe“
- p.16: Tab. 3.9 Änderungen der Daten der Kategorie „12 Türen“
- p.16: Tab. 3.10 Änderungen der Daten der Kategorie „13 Rohre“
- p.17: Tab. 3.11 Änderungen der Daten der Kategorie „14 Kunststoffe“

Rules:
1. Choose the caption(s) that hold the unit-process inventory of this dataset — inputs, energy, emissions, transport — not impact results, not a diagram. Prefer "Sachbilanz" / "inventory" / "LCI" tables.
2. Return the PDF page range that covers those tables plus the paragraph introducing them: `first_page`, `last_page` (at most 4 pages). Tables can run onto the next page.
3. If no caption fits (the report does not document this dataset's inventory, or only as a result), return `found` = false and say why in `reason`.
4. `reason` names the caption(s) you chose and why.

Return only the JSON object described by the schema.
