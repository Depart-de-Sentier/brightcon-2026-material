You are locating the inventory table of one dataset inside a life-cycle-inventory report.

Dataset: `Natural gas, production MY, at evaporation plant` [TW], 1 Nm3, BAFU category fuels / natural gas\produced gas.
Metadata: includedProcesses: This dataset describes the gasification of Malaysian natural gas in a Taiwanese evaporation plant. · technology: European technology average. · comment: The process is normalized on the gaseous form of gas. The net calorific value of natural gas is 36.0 MJ/Nm³. UUID=e56db2a1-e909-381e-80ba-6a08ef8a2866

Report: `2025 - LCI long-distance transport crude oil - Meili.pdf` (32 PDF pages). Below is every table and figure caption found in it, with the PDF page it appears on (not the printed page number). The report may be in German, French or English; the dataset name is English — match on meaning (e.g. "gebrannter Ölschiefer" = burnt shale, "Gipsfaserplatte" = gypsum fibre board).

- p.9: Tab. 1.1 Countries and world regions for which crude oil markets are modelled in this study. Port of destination
- p.10: Tab. 2.1 Amount and share of crude oil imported to Switzerland in 2023, by country of origin ([Avenergy_Suisse,
- p.11: Tab. 2.2 Amount of crude oil extracted in, imported to and exported from EU-28 countries ([EI, 2024 #5179]). Only
- p.13: Tab. 2.4 Amount of crude oil extracted in and imported to global region ([EI, 2024 #5179]). Only amounts for coun-
- p.18: Fig. 3.1 Crude oil production in Russia and Europe according to Harvard World Map.23 Arrow in orange and green
- p.19: Fig. 3.2 Map of oil & natural gas drilling in the US, 2016, red and yellow colour means high and blue and green
- p.20: Tab. 3.1 Overview of transport distances and export shares used for modelling of long-distance transports to Swit-
- p.21: Tab. 3.2 Overview of transport distances and export shares used for modelling of long-distance transports to Eu-
- p.22: Tab. 3.4 Overview of transport distances and export shares used for modelling of long-distance transports to the
- p.23: Tab. 4.1 Composition of vapours from crude oil according to former and current source for modelling (numbers in
- p.24: Tab. 5.1 Unit process raw data for transport of crude oil in an onshore pipeline
- p.24: Tab. 5.2 Unit process raw data for transport of crude oil in an offshore pipeline
- p.26: Tab. 5.3 Unit process raw data for pipeline construction, offshore
- p.27: Tab. 5.4 Unit process raw data for pipeline construction, onshore
- p.28: Tab. 6.1 Unit process raw data for produced crude oil transported to refineries in Switzerland.
- p.29: Tab. 6.2 Tab. 6.5 Meta information (X-Process) for one example of the investigated life cycle invento-

Rules:
1. Choose the caption(s) that hold the unit-process inventory of this dataset — inputs, energy, emissions, transport — not impact results, not a diagram. Prefer "Sachbilanz" / "inventory" / "LCI" tables.
2. Return the PDF page range that covers those tables plus the paragraph introducing them: `first_page`, `last_page` (at most 4 pages). Tables can run onto the next page.
3. If no caption fits (the report does not document this dataset's inventory, or only as a result), return `found` = false and say why in `reason`.
4. `reason` names the caption(s) you chose and why.

Return only the JSON object described by the schema.
