You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Sulphuric acid  (input)
  quote: Sulphuric acid   2.4 – 3.5   [Tab. 85.3 precursors for TiO2 production, sulfate-process column, 'Kg per kg of product']
  search: sulphuric acid liquid plant
  candidates:
    - Sulphuric acid, liquid, at plant [RER] (kilogram, 7 inputs)
    - Sulphuric acid from viscose production, at plant [GLO] (kilogram, 24 inputs)
- item: Rutile, ilmenite  (input)
  quote: Rutile, ilmenite   Ca. 2   na   Industry sources   [Tab. 85.3 precursors for TiO2 production, sulfate-process column]
  search: titanium dioxide ilmenite rutile
  candidates:
    - Rutile, 95% titanium dioxide, at plant [AU] (kilogram, 7 inputs)
    - xx Ilmenite, 54% titanium dioxide, at plant [AU] (kilogram, 7 inputs)
- item: Electric energy  (input)
  quote: Electric energy   1.5 – 2.31   0.6 – 1.46   0.13-1.3   [Tab. 85.4 energy consumption for TiO2 production (sulfate process)]
  search: electricity medium voltage UCTE
  candidates:
    - Electricity, medium voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from hard coal, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from natural gas, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - xxx Electricity, medium voltage, production UCTE, at grid [UCTE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
- item: Steam  (input)
  quote: Steam   3.7 – 7.7   6.7 – 10.47   0 – 6.07   [Tab. 85.4 energy consumption for TiO2 production (sulfate process)]
  search: heat natural gas industrial furnace
  candidates:
    - xxx Heat, natural gas, at industrial furnace low-NOx >100kW [RER] (megajoule, 1 inputs)
    - Heat, natural gas, at industrial furnace 1MW [CH] (megajoule, 1 inputs)
    - District heat, at consumer, natural gas in industrial furnace 1MW [CH] (megajoule, 2 inputs)
    - Industrial furnace, 1MW, natural gas [RER] (unit, 18 inputs)
    - Natural gas, burned in industrial furnace 1MW [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace 1MWth [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace, for asphalt production, 1MWth [CH] (megajoule, 4 inputs)
- item: Gas  (input)
  quote: Gas   7.3 – 11.85   2.37 – 4.22   0 – 0.1   [Tab. 85.4 energy consumption for TiO2 production (sulfate process)]
  search: natural gas burned industrial furnace
  candidates:
    - Natural gas, burned in industrial furnace 1MW [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace 1MWth [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace, for asphalt production, 1MWth [CH] (megajoule, 4 inputs)
    - Industrial furnace, 1MW, natural gas [RER] (unit, 18 inputs)
    - xxx Heat, natural gas, at industrial furnace low-NOx >100kW [RER] (megajoule, 1 inputs)
    - Heat, natural gas, at industrial furnace 1MW [CH] (megajoule, 1 inputs)
    - District heat, at consumer, natural gas in industrial furnace 1MW [CH] (megajoule, 2 inputs)
- item: Coal  (input)
  quote: Coal   na   na   5.8 – 8.5   [Tab. 85.4 energy consumption for TiO2 production (sulfate process), acid concentration and filter salt decomposition column]
  search: hard coal burned industrial furnace
  candidates:
    - Hard coal, burned in industrial furnace 1-10MW [RER] (megajoule, 6 inputs)
    - Heat, at hard coal industrial furnace 1-10MW [RER] (megajoule, 1 inputs)
- item: Particles (air)  (emission to air)
  quote: Particles   0.001 – 0.04   ng   0.13-1.3 *   0.002 – 0.12   * 0.7 g / kg is used in this report   [Tab. 85.6 direct air emissions for TiO2 production (sulfate process)]
  candidates (flow name [compartment]):
    - Particulates, unspecified  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
    - Metals, unspecified  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
    - Acidity, unspecified  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
    - Radioactive species, unspecified  [emissions to air / unspecified] (kilo Becquerel, bafu-2026-residual)
    - Oils, Unspecified  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Aldehydes, Unspecified  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chlorides, Unspecified  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Fungicides, Unspecified  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: NOx (air)  (emission to air)
  quote: NOx   0.001 – 0.043   ng   0 – 6.07   [Tab. 85.6 direct air emissions for TiO2 production (sulfate process)]
  candidates (flow name [compartment]):
    - Nitrogen Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Mustard  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Trifluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen oxide (N2O4)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: SO2 (air)  (emission to air)
  quote: SO2   ng   0 – 0.119   1*   ng   ** This value is used for the model sulfate plant.   [Tab. 85.6 direct air emissions for TiO2 production (sulfate process)]
  candidates (flow name [compartment]):
    - Sulfur Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [soil] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [water] (kilogram, ef-3.1-biosphere)
    - Sulfur  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
- item: H2S (air)  (emission to air)
  quote: H2S   ng   0 – 0.005   ng   ng   [Tab. 85.6 direct air emissions for TiO2 production (sulfate process)]
  candidates (flow name [compartment]):
    - Hydrogen Sulfide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen Sulfide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Hydrogen Sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - hydrogen sulfide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - hydrogen sulfide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Hydrogen  [air] (kilogram, ef-3.1-biosphere)
    - Hydrogen-3  [Emissions / Emissions to air] (kilo Becquerel, ef-3.1-biosphere)
    - Sulfide ion  [air] (kilogram, ef-3.1-biosphere)
- item: Sulfate (water)  (emission to water)
  quote: Sulfate   30 – 300 *   80 - 110   * This report uses a value of 150 g sulfate per kg produced TiO2   [Tab. 85.8 wastewater emissions for TiO2 production (sulfate process)]
  candidates (flow name [compartment]):
    - Sulfate  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Sulfate Ion  [water] (kilogram, ef-3.1-biosphere)
    - Zinc Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - zinc sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Barium sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cobalt Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nickel Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Sulfate from spent acid (water)  (emission to water)
  quote: According to (UBA BAT Notes, 2001) Figure 2.1.3.1, sulphuric acid that enters the wastewater from the sulfate process contains 30 – 300 g sulfate per kg spent acid (see Tab. 85.9). An average of roughly 50 g sulfate / kg product.is assumed in this report.
  candidates (flow name [compartment]):
    - Sulfate  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Sulfate Ion  [water] (kilogram, ef-3.1-biosphere)
    - Zinc Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - zinc sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Barium sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cobalt Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nickel Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Iron (water)  (emission to water)
  quote: Iron   0.25 – 5 **   ng   ** This report uses a value of 2 g iron per kg produced TiO2   [Tab. 85.8 wastewater emissions for TiO2 production (sulfate process)]
  candidates (flow name [compartment]):
    - Iron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - iron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iron-59  [water] (kilo Becquerel, ef-3.1-biosphere)
    - Iron(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iron(3+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - iron (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Cadmium (water)  (emission to water)
  quote: Cadmium   0.000001   ng   [Tab. 85.8 wastewater emissions for TiO2 production (sulfate process)]
  candidates (flow name [compartment]):
    - Cadmium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - cadmium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Bromide ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cadmium(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cadmium-109  [water] (kilogram, ef-3.1-biosphere)
- item: Mercury (water)  (emission to water)
  quote: Mercury   0.00000032   ng   [Tab. 85.8 wastewater emissions for TiO2 production (sulfate process)]
  candidates (flow name [compartment]):
    - Mercury  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Bromide ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lithium ion  [water] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sulfate Ion  [water] (kilogram, ef-3.1-biosphere)
- item: Ore digestion residues, solidified in cement and landfilled  (input)
  quote: Sulfate process: According to (UBA BAT Notes, 2001), residues generated from ore digestion total 340 – 670 g / kg product. These wastes are disposal of as hazardous wastes. ... This report assumes that 480 g / kg product are produced, solidified in cement and landfilled.
  search: disposal residue TiO2 landfill
  candidates:
    - xx Disposal, residue from TiO2 prod. Cl, 56% water, to residual material landfill [CH] (kilogram, 2 inputs)
    - xx Disposal, residue from TiO2 prod. SO4, 30% water, to residual material landfill [CH] (kilogram, 6 inputs)
    - Disposal, limestone residue, 5% water, to construction waste landfill [CH] (kilogram, 18 inputs)
    - Disposal, residue from cooling tower, 30% water, to sanitary landfill [CH] (kilogram, 25 inputs)
    - Disposal, H3PO4 purification residue, 0% water, to residual material landfill [CH] (kilogram, 6 inputs)
    - Disposal, average incineration residue, 0% water, to residual material landfill [CH] (kilogram, 6 inputs)
    - Disposal, residues Na-dichromate prod., 0% water, to residual material landfill [CH] (kilogram, 6 inputs)

Return only the JSON object described by the schema.
