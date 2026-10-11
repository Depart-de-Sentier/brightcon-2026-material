You are locating the inventory table of one dataset inside a life-cycle-inventory report.

Dataset: `Wind turbine 6.2MW, onshore, foundation` [RER], 1 unit, BAFU category wind power / production of components.
Metadata: includedProcesses: Wind turbine foundation, at site including manufacturing, transports, installation, replacements, decommission and waste treatement. Calculated for FU of 1p.
Data are based on the Vestas V162-6.2MW onshore wind turbine (Mali & Garrett, 2023).
Assumed lifetime is 25 years. · technology: — · comment: UUID=9e23b3a7-bb0d-3010-91f2-e71170fcc8a3

Report: `2025 - LCI wind Energy - Kroehnert.pdf` (84 PDF pages). Below is every table and figure caption found in it, with the PDF page it appears on (not the printed page number). The report may be in German, French or English; the dataset name is English — match on meaning (e.g. "gebrannter Ölschiefer" = burnt shale, "Gipsfaserplatte" = gypsum fibre board).

- p.15: Figure 4 System boundary and structure of the datasets for the electricity production from wind power. Green
- p.40: Table 18 Share of electricity from offshore and onshore wind power, as well as from different wind turbines sizes
- p.44: Figure 5 Life cycle greenhouse gas emissions of 1 kWh of electricity at the different onshore and offshore wind
- p.45: Figure 6 Non-renewable energy demand for 1 kWh of electricity at the different onshore and offshore wind farms,
- p.47: Figure 7 Total environmental impact of 1 kWh of electricity at the different onshore and offshore wind farms and

Rules:
1. Choose the caption(s) that hold the unit-process inventory of this dataset — inputs, energy, emissions, transport — not impact results, not a diagram. Prefer "Sachbilanz" / "inventory" / "LCI" tables.
2. Return the PDF page range that covers those tables plus the paragraph introducing them: `first_page`, `last_page` (at most 4 pages). Tables can run onto the next page.
3. If no caption fits (the report does not document this dataset's inventory, or only as a result), return `found` = false and say why in `reason`.
4. `reason` names the caption(s) you chose and why.

Return only the JSON object described by the schema.
