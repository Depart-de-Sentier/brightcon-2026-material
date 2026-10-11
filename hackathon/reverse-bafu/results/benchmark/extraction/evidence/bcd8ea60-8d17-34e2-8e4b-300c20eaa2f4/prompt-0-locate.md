You are locating the inventory table of one dataset inside a life-cycle-inventory report.

Dataset: `Canning of legumes` [CH], 1 kg, BAFU category food industry / processing.
Metadata: includedProcesses: nan · technology: nan · comment: The inventory applies to the canning of 1kg of legumes.

Report: `2021 - LCA tomatoes and green beans production - Kaegi.pdf` (71 PDF pages). Below is every table and figure caption found in it, with the PDF page it appears on (not the printed page number). The report may be in German, French or English; the dataset name is English — match on meaning (e.g. "gebrannter Ölschiefer" = burnt shale, "Gipsfaserplatte" = gypsum fibre board).

- p.5: Figure 1: Steps of a life cycle assessment according to ISO 14040/44
- p.8: Figure 2: Schematic representation of the processes considered for green beans
- p.8: Figure 3: Schematic representation of the processes considered for tomato
- p.10: Table 1: Key data for greenhouse, glass walls and roof
- p.10: Table 2: Key data for plastic tunnels
- p.11: Table 3: Composition of average N-fertiliser (per kg, according to Koch & Salou, 2015)
- p.11: Table 4: Composition of average P2O5-fertiliser (per kg, according to Koch & Salou, 2015)
- p.11: Table 5: Composition of average K2O-fertiliser (per kg, according to Koch & Salou, 2015)
- p.12: Table 6: Yields for tomato cultivation
- p.12: Table 7: Yields for green beans cultivation
- p.13: Table 8: Material inputs for tomato cultivation
- p.14: Table 9: Material inputs for green beans cultivation
- p.15: Table 10: Energy and machinery use for tomato cultivation
- p.15: Table 11: Energy and machinery use for green beans cultivation
- p.16: Table 12: Emissions to air for tomato cultivation
- p.16: Table 13: Emissions to air for green bean cultivation
- p.17: Table 14: Emissions to soil for tomato cultivation
- p.18: Table 15: Emissions to soil for green bean cultivation
- p.18: Table 16: Emissions to water for tomato cultivation
- p.19: Table 17: Emissions to water for green bean cultivation
- p.21: Figure 4: Basic scheme of the ecological scarcity method (graphic from Frischknecht u. a., 2021)
- p.22: Figure 4 shows the environmental footprint of the different tomato variants.
- p.23: Figure 5: Process contributions to the environmental impact for tomato, distributed to generic Swiss store
- p.23: Figure 6: Environmental impact for tomato, distributed to generic Swiss store
- p.24: Figure 6 shows the environmental footprint of the different green bean variants.
- p.24: Figure 7: Process contributions to the environmental impact for green beans, ready-to-eat at Swiss household
- p.25: Figure 8: Environmental impact for green beans, ready-to-eat at Swiss household
- p.29: Figure 9: carbon footprint for tomato, delivered to Swiss store
- p.29: Figure 10: carbon footprint for green beans, ready-to-eat at Swiss household
- p.30: Figure 11: environmental footprint according to EF v3.0 for tomato, delivered to Swiss store
- p.30: Figure 12: environmental footprint according to EF v3.0 for green beans, ready-to-eat at Swiss household
- p.31: Table 18: Results for green beans calculated with ecological scarcity 2021
- p.31: Table 19: Results for tomato calculated with ecological scarcity 2021
- p.31: Table 20: Carbon footprint of green beans
- p.31: Table 21: Carbon footprint of tomato
- p.32: Table 22: Results for green beans calculated with EF v3.0
- p.33: Table 23: Results for tomato calculated with EF v3.0
- p.34: Figure 1: Metadata of greenhouse with glass walls production
- p.36: Figure 2: Unit process raw data of greenhouse with glass walls production production
- p.36: Figure 3: Metadata of plastic tunnel production CH
- p.37: Figure 4: Unit process raw data of plastic tunnel production CH
- p.38: Figure 5: Metadata of plastic tunnel production ES
- p.39: Figure 6: Unit process raw data of plastic tunnel production ES
- p.40: Figure 7: Metadata of K2O fertiliser production
- p.40: Figure 8: Unit process raw data of K2O fertiliser production
- p.41: Figure 9: Metadata of N fertiliser production
- p.41: Figure 10: Unit process raw data of N fertiliser production
- p.42: Figure 11: Metadata of P2O5 fertiliser production
- p.42: Figure 12: Unit process raw data of P2O5 fertiliser production
- p.43: Figure 13: Metadata of irrigation by sprinkler
- p.44: Figure 14: Unit process raw data of irrigation by sprinkler
- p.45: Figure 15: Metadata of desalinated tap water
- p.46: Figure 16: Unit process raw data of desalinated tap water
- p.47: Figure 17: Metadata of tomato seedling production
- p.48: Figure 18: Unit process raw data of tomato seedling production
- p.49: Figure 19: Metadata of canning of food
- p.49: Figure 20: Unit process raw data of canning of food
- p.50: Figure 21: Metadata of drying of food
- p.50: Figure 22: Unit process raw data of drying of food
- p.51: Figure 23: Metadata of freezing and storing of food
- p.51: Figure 24: Unit process raw data of freezing and storing of food
- p.52: Figure 25: Metadata of green beans production in Kenya
- p.53: Figure 26: Unit process raw data of green beans production in Kenya
- p.54: Figure 27: Metadata of IP green beans production in Switzerland
- p.55: Figure 28: Unit process raw data of IP green beans production in Switzerland
- p.56: Figure 29: Metadata of organic green beans production in Switzerland
- p.57: Figure 30: Unit process raw data of organic green beans production in Switzerland
- p.57: Figure 31: Metadata of tomato production in unheated greenhouse in Almeria
- p.58: Figure 32: Unit process raw data of tomato production in unheated greenhouse in Almeria
- p.59: Figure 33: Metadata of tomato production in heated greenhouse in Switzerland, late harvest
- p.60: Figure 34: Unit process raw data of tomato production in heated greenhouse in Switzerland, late harvest
- p.61: Figure 35: Metadata of tomato production in heated greenhouse in Switzerland, early harvest
- p.62: Figure 36: Unit process raw data of tomato production in heated greenhouse in Switzerland, early harvest
- p.64: Figure 37: Metadata of organic tomato production in unheated greenhouse in Switzerland
- p.64: Figure 38: Unit process raw data of organic tomato production in unheated greenhouse in Switzerland

Rules:
1. Choose the caption(s) that hold the unit-process inventory of this dataset — inputs, energy, emissions, transport — not impact results, not a diagram. Prefer "Sachbilanz" / "inventory" / "LCI" tables.
2. Return the PDF page range that covers those tables plus the paragraph introducing them: `first_page`, `last_page` (at most 4 pages). Tables can run onto the next page.
3. If no caption fits (the report does not document this dataset's inventory, or only as a result), return `found` = false and say why in `reason`.
4. `reason` names the caption(s) you chose and why.

Return only the JSON object described by the schema.
