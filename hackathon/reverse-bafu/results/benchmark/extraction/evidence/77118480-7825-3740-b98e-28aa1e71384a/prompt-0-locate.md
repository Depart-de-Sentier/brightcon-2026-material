You are locating the inventory table of one dataset inside a life-cycle-inventory report.

Dataset: `Heat, at 30 m2 Cu collector, multiple dwelling, flat roof, for hot water` [CH], 1 MJ, BAFU category heat / solar.
Metadata: includedProcesses: Delivery of heat with a solar system including maintenance and electricity use for operation. Excluding the necessary auxiliary heating. · technology: Solar collector system for hot water installed on the roof of a house. · comment: Use of a solar system excluding the necessary auxiliary heating. The simulation is made for solar collector systems in the city of Zurich. The annual irradiation amounts to 1249 kWh/m2. 50% solar fraction, 30° inclination, 22° southeast orientation.;
UUID: 77118480-7825-3740-b98e-28aa1e71384a

Report: `2012 - Update LCI solar collectors - Stucki.pdf` (25 PDF pages). Below is every table and figure caption found in it, with the PDF page it appears on (not the printed page number). The report may be in German, French or English; the dataset name is English — match on meaning (e.g. "gebrannter Ölschiefer" = burnt shale, "Gipsfaserplatte" = gypsum fibre board).

- p.5: Tab. 1.1 Solar thermal systems in ecoinvent v2.2 and new solar thermal systems considered in
- p.7: Fig. 2.1 Example of a solar thermal system with evacuated tube collectors installed in Italy
- p.8: Tab. 2.1 Unit process raw data of construction and disposal of flat plate collectors with copper
- p.9: Tab. 2.2 Unit process raw data of construction and disposal of an evacuated tube collector
- p.10: Tab. 2.3 EcoSpold meta information of construction and disposal of evacuated tube collectors
- p.11: Tab. 2.4 Extrapolation factors for the calculation of different storage sizes
- p.11: Tab. 2.5 Gross weights of pumps with different capacities
- p.12: Tab. 2.6 Foundation material of the considered solar thermal systems.
- p.13: Tab. 2.7 Specification of pipes, pipe insulation, and pipe insulation coating of the considered
- p.13: Tab. 2.8 Density of pipe and insulation materials
- p.15: Tab. 2.9 Unit process raw data of the construction and disposal of solar thermal systems, the last two datasets are updates of previous ecoinvent
- p.16: Tab. 2.10 EcoSpold meta information of the construction and disposal of solar thermal systems
- p.18: Tab. 3.1 Collector yield, solar net yield, converted solar energy, and auxiliary energy
- p.19: Tab. 3.2 Unit process raw data of the supply of useful heat from solar thermal systems without considering auxiliary heating
- p.20: Tab. 3.3 EcoSpold meta information of the supply of useful heat from solar thermal systems without considering auxiliary heating

Rules:
1. Choose the caption(s) that hold the unit-process inventory of this dataset — inputs, energy, emissions, transport — not impact results, not a diagram. Prefer "Sachbilanz" / "inventory" / "LCI" tables.
2. Return the PDF page range that covers those tables plus the paragraph introducing them: `first_page`, `last_page` (at most 4 pages). Tables can run onto the next page.
3. If no caption fits (the report does not document this dataset's inventory, or only as a result), return `found` = false and say why in `reason`.
4. `reason` names the caption(s) you chose and why.

Return only the JSON object described by the schema.
