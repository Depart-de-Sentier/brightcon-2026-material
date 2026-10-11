You are locating the inventory table of one dataset inside a life-cycle-inventory report.

Dataset: `Electricity, medium voltage, at grid` [HU], 1 kWh, BAFU category electricity / supply mix.
Metadata: includedProcesses: Included are the shares of corresponding electricity production by technology and country at the busbar. Not included are transformation, transport or distribution losses. · technology: No technology description is provided because the dataset just describes the power plant portfolio of the respective country using current average technology per energy carrier. · comment: Electricity domestic net consumption shares are based on annual averages for 2023. Losses are distributed across voltage levels with total losses for the same time frame as well as older proxy data for disaggregation. Electricity trade between countries is not included so the consumption reflects th

Report: `2025 - Electricity mixes in UVEK database - Oberschelp.pdf` (43 PDF pages). Below is every table and figure caption found in it, with the PDF page it appears on (not the printed page number). The report may be in German, French or English; the dataset name is English — match on meaning (e.g. "gebrannter Ölschiefer" = burnt shale, "Gipsfaserplatte" = gypsum fibre board).

- p.4: Table 1: Role of the different datasets for the update of UVEK mixes, distinguished by country group.
- p.8: Table 2: Nuclear power generation splits to disaggregate to UVEK generation datasets per region.
- p.9: Table 3: Hydro power splits to disaggregate to UVEK generation datasets per region.
- p.11: Table 4: Pumped hydro power losses per geography per kWh of net electricity output.
- p.12: Table 5: Permitted and plausible COMTRADE trade data based on neighboring regions (all other
- p.15: Figure 1: Electricity imports of Luxembourg in 2023 with the width of connection representing the
- p.16: Figure 2: Typical example for commercial and physical net electricity supply in comparison actual
- p.17: Table 6: Default technology mapping per fuel type.
- p.18: Figure 3: ENTSO-E member countries covered in high resolution modeling in the UVEK database
- p.23: Figure 4: Production mixes calculated for the UVEK database for the year 2023.
- p.24: Figure 4 (continued): Production mixes calculated for the UVEK database for the year 2023.
- p.26: Figure 5: Supply mixes calculated for the UVEK database highlighting the contributions of domestic
- p.27: Figure 5 (continued): Supply mixes calculated for the UVEK database highlighting the contributions
- p.28: Figure 6: Supply mix contributions from domestic supply in 2023 in contrast to direct electricity
- p.30: Figure 7: Comparison of supply mix carbon footprints per kWh electricity in the old version of the
- p.31: Figure 7 (continued): Comparison of supply mix carbon footprints per kWh electricity in the old
- p.32: Figure 8: Comparison of supply mix ecoscarcity scores per kWh electricity in the old version of the
- p.33: Figure 8 (continued): Comparison of supply mix ecoscarcity scores per kWh electricity in the old

Rules:
1. Choose the caption(s) that hold the unit-process inventory of this dataset — inputs, energy, emissions, transport — not impact results, not a diagram. Prefer "Sachbilanz" / "inventory" / "LCI" tables.
2. Return the PDF page range that covers those tables plus the paragraph introducing them: `first_page`, `last_page` (at most 4 pages). Tables can run onto the next page.
3. If no caption fits (the report does not document this dataset's inventory, or only as a result), return `found` = false and say why in `reason`.
4. `reason` names the caption(s) you chose and why.

Return only the JSON object described by the schema.
