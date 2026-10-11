You are locating the inventory table of one dataset inside a life-cycle-inventory report.

Dataset: `Sawnwood, production mix, hardwood, dried (u=20%), planed, at sawmill` [RER], 1 m3, BAFU category wood / wooden materials\new processes\other material.
Metadata: includedProcesses: <null> · technology: Unspecified · comment: na;
UUID: a6d07fbd-20e1-3a8b-b844-cfed67b4e587

Report: `2017 - LCI wood and wood based products - Werner.pdf` (255 PDF pages). Below is every table and figure caption found in it, with the PDF page it appears on (not the printed page number). The report may be in German, French or English; the dataset name is English — match on meaning (e.g. "gebrannter Ölschiefer" = burnt shale, "Gipsfaserplatte" = gypsum fibre board).

- (no captions found)

Rules:
1. Choose the caption(s) that hold the unit-process inventory of this dataset — inputs, energy, emissions, transport — not impact results, not a diagram. Prefer "Sachbilanz" / "inventory" / "LCI" tables.
2. Return the PDF page range that covers those tables plus the paragraph introducing them: `first_page`, `last_page` (at most 4 pages). Tables can run onto the next page.
3. If no caption fits (the report does not document this dataset's inventory, or only as a result), return `found` = false and say why in `reason`.
4. `reason` names the caption(s) you chose and why.

Return only the JSON object described by the schema.
