You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Synthetic rutile  (input)
  quote: Synthetic rutile   ng   1.06   (Chemlink.com)   [Tab. 85.3 precursors for TiO2 production, chloride-process column, 'Kg per kg of product']
  search: titanium dioxide ilmenite rutile
  candidates:
    - Rutile, 95% titanium dioxide, at plant [AU] (kilogram, 7 inputs)
    - xx Ilmenite, 54% titanium dioxide, at plant [AU] (kilogram, 7 inputs)
- item: Chlorine  (input)
  quote: Chlorine   na   0.18   (UBA BAT Notes, 2001)   [Tab. 85.3 precursors for TiO2 production, chloride-process column]
  search: chlorine liquid plant
  candidates:
    - Chlorine, liquid, production mix, at plant [RER] (kilogram, 4 inputs)
    - Hydrogen, liquid, from chlorine electrolysis, production mix, at plant [RER] (kilogram, 3 inputs)
    - Argon, liquid, at plant [RER] (kilogram, 4 inputs)
    - Ozone, liquid, at plant [RER] (kilogram, 2 inputs)
    - Oxygen, liquid, at plant [RER] (kilogram, 3 inputs)
    - Acetone, liquid, at plant [RER] (kilogram, 8 inputs)
    - Toluene, liquid, at plant [RER] (kilogram, 8 inputs)
    - Chlorine dioxide, at plant [RER] (kilogram, 8 inputs)
- item: Electric energy  (input)
  quote: Electric energy   1.51   0.83   [Tab. 85.5 energy consumption for TiO2 production (chloride process), TiO2 manufacture + Follow-up treatment]
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
  quote: Steam   1.7   7.7   [Tab. 85.5 energy consumption for TiO2 production (chloride process)]
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
  quote: Gas   2.9   4.2   [Tab. 85.5 energy consumption for TiO2 production (chloride process)]
  search: natural gas burned industrial furnace
  candidates:
    - Natural gas, burned in industrial furnace 1MW [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace 1MWth [CH] (megajoule, 4 inputs)
    - Natural gas, burned in industrial furnace, for asphalt production, 1MWth [CH] (megajoule, 4 inputs)
    - Industrial furnace, 1MW, natural gas [RER] (unit, 18 inputs)
    - xxx Heat, natural gas, at industrial furnace low-NOx >100kW [RER] (megajoule, 1 inputs)
    - Heat, natural gas, at industrial furnace 1MW [CH] (megajoule, 1 inputs)
    - District heat, at consumer, natural gas in industrial furnace 1MW [CH] (megajoule, 2 inputs)
- item: Particles (air)  (emission to air)
  quote: Particles   0.005   ng   ng   0.186   [Tab. 85.7 direct air emissions for TiO2 production (chloride process)]
  candidates (flow name [compartment]):
    - Particulates, unspecified  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
- item: HCl (air)  (emission to air)
  quote: HCl   ng   0.007   0.024 *   ng   * This value is used for the model chloride plant.   [Tab. 85.7]
  candidates (flow name [compartment]):
    - Hydrogen Chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen Chloride  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Hydrogen Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - hydrogen chloride  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - hydrogen chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen  [air] (kilogram, ef-3.1-biosphere)
    - Hydrogen-3  [Emissions / Emissions to air] (kilo Becquerel, ef-3.1-biosphere)
- item: SO2 (air)  (emission to air)
  quote: SO2   ng   ng   1.68   ng   [Tab. 85.7 direct air emissions for TiO2 production (chloride process), off-gas treatment]
  candidates (flow name [compartment]):
    - Sulfur Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [soil] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [water] (kilogram, ef-3.1-biosphere)
    - Sulfur  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
- item: Iron (water)  (emission to water)
  quote: Iron   0.011 *   ng   ...   This report uses a value of 0.5 g iron per kg produced TiO2   [Tab. 85.9 wastewater emissions (chloride process)]
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
  quote: Cadmium   0.00000022   ng   [Tab. 85.9 wastewater emissions for TiO2 production (chloride process)]
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
  quote: Mercury   0.00000022   ng   [Tab. 85.9 wastewater emissions for TiO2 production (chloride process)]
  candidates (flow name [compartment]):
    - Mercury  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Bromide ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lithium ion  [water] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sulfate Ion  [water] (kilogram, ef-3.1-biosphere)
- item: Filter residues  (input)
  quote: Filter residues   0.11   2.25   [Tab. 85.9 wastewater emissions for TiO2 production (chloride process)]
  search: disposal residue TiO2 landfill
  candidates:
    - xx Disposal, residue from TiO2 prod. Cl, 56% water, to residual material landfill [CH] (kilogram, 2 inputs)
    - xx Disposal, residue from TiO2 prod. SO4, 30% water, to residual material landfill [CH] (kilogram, 6 inputs)
    - Disposal, limestone residue, 5% water, to construction waste landfill [CH] (kilogram, 18 inputs)
    - Disposal, residue from cooling tower, 30% water, to sanitary landfill [CH] (kilogram, 25 inputs)
    - Disposal, H3PO4 purification residue, 0% water, to residual material landfill [CH] (kilogram, 6 inputs)
    - Disposal, average incineration residue, 0% water, to residual material landfill [CH] (kilogram, 6 inputs)
    - Disposal, residues Na-dichromate prod., 0% water, to residual material landfill [CH] (kilogram, 6 inputs)
- item: Chloride process sludges  (input)
  quote: Chloride process. According to (UBA BAT Notes, 2001), chloride process sludges total 184 g / kg product. Industry sources however suggest somewhat higher values, ranging up to 1 kg / kg product
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
