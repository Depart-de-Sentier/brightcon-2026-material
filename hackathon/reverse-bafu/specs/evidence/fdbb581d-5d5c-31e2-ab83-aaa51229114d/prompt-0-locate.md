You are locating the inventory table of one dataset inside a life-cycle-inventory report.

Dataset: `xx Packaging glass, green, at regional storage` [CH], 1 kg, BAFU category material, obsolete / glass, obsolete\packaging, obsolete.
Metadata: includedProcesses: This module includes the average composition of the consumed empty container glass in Switzerland and the therefore needed transport amounts. · technology: Present situation in Switzerland · comment: A production site with a sorting capacity of 100 kt per year and a total life span of 50 a is assumed.;
UUID: fdbb581d-5d5c-31e2-ab83-aaa51229114d

Report: `2007 - LCI packagings and graphical papers - Hischier.pdf` (17 PDF pages). Below is every table and figure caption found in it, with the PDF page it appears on (not the printed page number). The report may be in German, French or English; the dataset name is English — match on meaning (e.g. "gebrannter Ölschiefer" = burnt shale, "Gipsfaserplatte" = gypsum fibre board).

- p.12: Fig. 4.1 Decision criteria for packagings and instruments for their ecological evaluation (Fig. 5.1 from Habersatter et

Rules:
1. Choose the caption(s) that hold the unit-process inventory of this dataset — inputs, energy, emissions, transport — not impact results, not a diagram. Prefer "Sachbilanz" / "inventory" / "LCI" tables.
2. Return the PDF page range that covers those tables plus the paragraph introducing them: `first_page`, `last_page` (at most 4 pages). Tables can run onto the next page.
3. If no caption fits (the report does not document this dataset's inventory, or only as a result), return `found` = false and say why in `reason`.
4. `reason` names the caption(s) you chose and why.

Return only the JSON object described by the schema.
