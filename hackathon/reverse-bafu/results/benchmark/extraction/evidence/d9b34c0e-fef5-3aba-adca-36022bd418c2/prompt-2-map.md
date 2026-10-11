You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Kalk  (input)
  quote:                         Kalk                        kg/kg SO2                   0.2
  search: quicklime milled loose at plant
  candidates:
    - Quicklime, milled, loose, at plant [CH] (kilogram, 6 inputs)
    - Limestone, milled, loose, at plant [CH] (kilogram, 6 inputs)
    - Quicklime, milled, packed, at plant [CH] (kilogram, 3 inputs)
    - Quicklime, in pieces, loose, at plant [CH] (kilogram, 6 inputs)
    - Granite, natural stone council, milled, loose, at plant [CH] (kilogram, 4 inputs)
    - Quicklime, in pieces, loose, at plant, with carbon capture and storage [CH] (kilogram, 7 inputs)
- item: Kalkstein  (input)
  quote:                         Kalkstein                   kg/kg SO2                   1.3                      2
  search: limestone milled packed at plant
  candidates:
    - Limestone, milled, packed, at plant [CH] (kilogram, 3 inputs)
    - Limestone, milled, loose, at plant [CH] (kilogram, 6 inputs)
    - Quicklime, milled, packed, at plant [CH] (kilogram, 3 inputs)
- item: Wasser entkarbonisiert  (input)
  quote:                         Wasser entkarbonisiert      kg/kg SO2                    20                     10
  search: water decarbonised at plant
  candidates:
    - Water, decarbonised, at plant [RER] (kilogram, 7 inputs)
    - Water, completely softened, at plant [RER] (kilogram, 6 inputs)
    - Small hydropower plant, in waterworks infrastructure [RER] (unit, 30 inputs)
    - Water, deionised, water balance according to MoeK 2013, at plant [RER] (kilogram, 7 inputs)
    - Electricity, hydropower, at small hydropower plant, in waterworks infrastructure [RER] (kilowatt hour, 1 inputs)
    - Water, deionised, at plant [CH] (kilogram, 7 inputs)
    - Hot water tank 600l, at plant [CH] (unit, 19 inputs)
    - Water treatment plant, deionisation [CH] (unit, 10 inputs)
- item: Schwefelsäure H2SO4  (input)
  quote:                         Schwefelsäure H2SO4         kg/kg SO2                  0.08
  search: sulphuric acid liquid at plant
  candidates:
    - Sulphuric acid, liquid, at plant [RER] (kilogram, 7 inputs)
    - Sulphuric acid from viscose production, at plant [GLO] (kilogram, 24 inputs)
- item: Natronlauge NaOH  (input)
  quote:                         Natronlauge NaOH            kg/kg SO2                  0.02
  search: sodium hydroxide 50% in H2O production mix at plant
  candidates:
    - Sodium hydroxide, 50% in H2O, production mix, at plant [RER] (kilogram, 3 inputs)
- item: Transport Schiene  (input)
  quote:                         Transport Schiene           tkm/kg SO2                 0.17                    0.2
  search: transport freight rail
  candidates:
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
    - Transport, freight, rail, electricity only [RER] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, diesel, with particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, diesel, without particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting, Betrieb [CH] (ton kilometer, 2 inputs)
    - Transport, freight, rail, electricity with shunting, Fahrzeug [CH] (ton kilometer, 5 inputs)
- item: Transport LKW 28t  (input)
  quote:                         Transport LKW 28t           tkm/kg SO2                0.003
  search: transport lorry 28t
  candidates:
    - Lorry 28t [RER] (unit, 38 inputs)
    - Transport, freight, lorry, fleet average [RER] (ton kilometer, 4 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, diesel, fleet average, long haul [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 16t-32t gross weight, fleet average [RER] (ton kilometer, 36 inputs)
    - Transport, freight, lorry, 32t-40t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
    - Transport, freight, lorry, 7.5t-16t gross weight, fleet average [RER] (ton kilometer, 12 inputs)
    - Transport, freight, lorry, 3.5t-7.5t gross weight, fleet average [RER] (ton kilometer, 3 inputs)
- item: Schlamm, Abfälle in Reststoffdeponie  (input)
  quote:                         Schlamm ****                kg/kg SO2                  0.06
  search: disposal residual material landfill
  candidates:
    - Disposal, cement, hydrated, 0% water, to residual material landfill [CH] (kilogram, 2 inputs)
    - Disposal, drilling waste, 71.5% water, to residual material landfill [CH] (kilogram, 2 inputs)
    - Disposal, frit for CRT tube production, to residual material landfill [CH] (kilogram, 6 inputs)
    - Disposal, green liquor dregs, 25% water, to residual material landfill [CH] (kilogram, 6 inputs)
    - Disposal, nickel smelter slag, 0% water, to residual material landfill [CH] (kilogram, 2 inputs)
    - Disposal, decarbonising waste, 30% water, to residual material landfill [CH] (kilogram, 2 inputs)
    - Disposal, ash from deinking sludge, 0% water, to residual material landfill [CH] (kilogram, 6 inputs)
    - Disposal, sludge, NaCl electrolysis, 0% water, to residual material landfill [CH] (kilogram, 6 inputs)
- item: Carbon dioxide, fossil  (emission to air)
  quote:                         CO2                         kg/kg SO2                  0.55                    0.7
  candidates (flow name [compartment]):
    - Carbon Dioxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (biogenic)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic-100yr)  [air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
- item: Magnesium  (emission to water)
  quote:      Mg                 300-3500                                                0             2000            10
  candidates (flow name [compartment]):
    - Magnesium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - magnesium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Magnesium nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Magnesium Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - magnesium chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - magnesium sulphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Magnesium Carbonate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Magnesium Hydroxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Sodium  (emission to water)
  quote:      Na                 400-1000                                                               500            2.5
  candidates (flow name [compartment]):
    - Sodium  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Sodium  [water] (kilogram, ef-3.1-biosphere)
    - sodium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium-24  [water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Metam-sodium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium Azide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - metam-sodium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Chloride  (emission to water)
  quote:      Cl                5000-40000            10000                              60            5000            250
  candidates (flow name [compartment]):
    - Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Allyl Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Vinyl Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - allyl chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - vinyl chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Acetyl Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Sulfite  (emission to water)
  quote:      SO3                200-6000                -              20                              20             0.1
  candidates (flow name [compartment]):
    - Sulfite  [water] (kilogram, ef-3.1-biosphere)
    - Sodium sulfite  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - disodium sulfite  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Dipotassium Sulfite  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - dipotassium sulfite  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sulfite  [air] (kilogram, ef-3.1-biosphere)
    - Sulfite  [soil] (kilogram, ef-3.1-biosphere)
    - Sodium sulfite  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Sulfate  (emission to water)
  quote:      SO4                1300-5000             4000            2000             150            2000            10
  candidates (flow name [compartment]):
    - Sulfate  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Sulfate Ion  [water] (kilogram, ef-3.1-biosphere)
    - Zinc Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - zinc sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Barium sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cobalt Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nickel Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Nitrate  (emission to water)
  quote:      NO3                500-1500              3000                              5             1000             5
  candidates (flow name [compartment]):
    - Nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Zinc nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Barium nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cupric nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Silver Nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium Nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Ammonia  (emission to water)
  quote:      NH3                                                                        0.5            0.5           0.003
  candidates (flow name [compartment]):
    - Ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - acetaldehyde--ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - oxirane, reaction products with ammonia, distn. residues  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - ethanol, 2,2'-oxybis-, reaction products with ammonia, morpholine derivs. residues  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Ammonia  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Fluoride  (emission to water)
  quote:      F                   30-1250               30              30                              30             0.15
  candidates (flow name [compartment]):
    - fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Fluoride Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Vinyl Fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Fentin Fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium Fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - fentin fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - sodium fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Calcium Fluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: COD, Chemical Oxygen Demand  (emission to water)
  quote:      COD                  40-500              130          801)/1502)           20             150            0.75
  candidates (flow name [compartment]):
    - COD, Chemical Oxygen Demand  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Chemical Oxygen Demand  [water] (kilogram, ef-3.1-biosphere)
- item: BOD5, Biological Oxygen Demand  (emission to water)
  quote:      BSB5                                      13                               5               5            0.025
  candidates (flow name [compartment]):
    - BOD5, Biological Oxygen Demand  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Biological Oxygen Demand  [water] (kilogram, ef-3.1-biosphere)
- item: Mercury  (emission to water)
  quote:      Hg                     <2                0.13            0.05            0.001            0.05         0.0003
  candidates (flow name [compartment]):
    - Mercury  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - mercury (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Mercury  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Mercury  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Mercury  [Resources / Resources from ground] (kilogram, ef-3.1-biosphere)
    - mercury  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Cadmium  (emission to water)
  quote:      Cd                     <2                0.15            0.05             0.01            0.05         0.0003
  candidates (flow name [compartment]):
    - Cadmium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - cadmium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cadmium(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cadmium-109  [water] (kilogram, ef-3.1-biosphere)
    - cadmium (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cadmium oxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cadmium Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cadmium nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Lead  (emission to water)
  quote:      Pb                    <30                 2.5             0.1             0.05            0.1          0.0005
  candidates (flow name [compartment]):
    - Lead  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - lead  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead-210  [water] (kilo Becquerel, ef-3.1-biosphere)
    - lead (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead oxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Zinc  (emission to water)
  quote:      Zn                    1-39                 8               1               0.5             1            0.005
  candidates (flow name [compartment]):
    - Zinc  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - zinc  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Zinc-65  [water] (kilogram, ef-3.1-biosphere)
    - Zinc(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - zinc (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - zinc oxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Zinc Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Zinc nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Chromium  (emission to water)
  quote:      Cr                    <20                 2.7             0.5             0.05            0.5           0.003
  candidates (flow name [compartment]):
    - Chromium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - chromium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Chromium VI  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Chromium-51  [water] (kilogram, ef-3.1-biosphere)
    - Chromium(3+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Chromium(6+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - chromium (vi)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - chromium (iii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Copper  (emission to water)
  quote:      Cu                   0.2-26               2.1             0.5             0.05            0.5           0.003
  candidates (flow name [compartment]):
    - Copper  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - copper  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Copper(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - copper (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Oxine-copper  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - oxine-copper  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Copper hydroxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - copper (i) oxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Nickel  (emission to water)
  quote:      Ni                   0.2-5                 2              0.5             0.05            0.5           0.003
  candidates (flow name [compartment]):
    - Nickel  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - nickel  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nickel-63  [water] (kilogram, ef-3.1-biosphere)
    - Nickel(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - nickel (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nickel Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nickel Sulphide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - nickel sulphide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Arsenic  (emission to water)
  quote:      As                     10               0.001                             0.03            0.1           0.005
  candidates (flow name [compartment]):
    - Arsenic  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - arsenic  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Arsenic (v)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - arsenic (v)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Arsenic Acid  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Arsenic (iii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - arsenic (iii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - arsenic trioxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Phosphate  (emission to water)
  quote:      Phosphat                                                                   0.3            0.3           0.002
  candidates (flow name [compartment]):
    - Phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - urea phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Butyl Phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - butyl phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Dibutyl phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Diethyl phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Dimethyl phosphate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Potassium  (emission to water)
  quote:      K                     130                                                  10             10             0.05
  candidates (flow name [compartment]):
    - Potassium  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Potassium  [water] (kilogram, ef-3.1-biosphere)
    - Potassium-40  [water] (kilo Becquerel, ef-3.1-biosphere)
    - Potassium(1+)  [water] (kilogram, ef-3.1-biosphere)
    - Potassium Iodate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Potassium Iodide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - potassium iodate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - potassium iodide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Aluminium  (emission to water)
  quote:      Al                   18-160                                                0.2            0.5           0.003
  candidates (flow name [compartment]):
    - Aluminium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - aluminium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Aluminium (iii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - aluminium (iii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - aluminium sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - aluminium hydroxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - aluminium phosphide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - aluminium trilactate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Boron  (emission to water)
  quote:      B                      72                                                                 66             0.33
  candidates (flow name [compartment]):
    - Boron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - boron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Boron Carbide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - boron carbide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Boron trioxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Diethyl Ether--boron Trifluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - diethyl ether--boron trifluoride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Boron  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Iron  (emission to water)
  quote:      Fe                   37-140                                                               0.5           0.003
  candidates (flow name [compartment]):
    - Iron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - iron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iron-59  [water] (kilo Becquerel, ef-3.1-biosphere)
    - Iron(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iron(3+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - iron (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iron Oxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - iron (iii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Manganese  (emission to water)
  quote:      Mn                   40-450                                                                1            0.005
  candidates (flow name [compartment]):
    - Manganese  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - manganese  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Manganese-54  [Emissions / Emissions to water] (kilo Becquerel, ef-3.1-biosphere)
    - manganese-54  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Manganese(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - manganese (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Manganese Sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Manganese Sulphide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Molybdenum  (emission to water)
  quote:      Mo                     16                                                                 0.5           0.003
  candidates (flow name [compartment]):
    - Molybdenum  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - molybdenum  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Molybdenum-99  [water] (kilogram, ef-3.1-biosphere)
    - molybdenum (vi)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Molybdenum Dioxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - molybdenum dioxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Molybdenum Trioxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - molybdenum trioxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Vanadium  (emission to water)
  quote:      V                     4.2                                                 0.05            0.5           0.003
  candidates (flow name [compartment]):
    - Vanadium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Vanadium  [water] (kilogram, ef-3.1-biosphere)
    - vanadium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Vanadium(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - vanadium (v)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Vanadium Dioxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - vanadium dioxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Vanadium oxide (V2O5)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Antimony  (emission to water)
  quote:      Sb                     2                                                                  0.5           0.003
  candidates (flow name [compartment]):
    - Antimony  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - antimony  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Antimony(3+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Antimony(5+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Antimony-122  [water] (kilogram, ef-3.1-biosphere)
    - Antimony-124  [Emissions / Emissions to water] (kilo Becquerel, ef-3.1-biosphere)
    - Antimony-125  [Emissions / Emissions to water] (kilo Becquerel, ef-3.1-biosphere)
    - antimony (v)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Selenium  (emission to water)
  quote:      Se                     7                                                                  0.1          0.0005
  candidates (flow name [compartment]):
    - Selenium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - selenium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Selenium (iv)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - selenium (iv)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - selenium diethyldithiocarbamate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Selenium dimethyldithiocarbamate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - selenium tetrakis(dimethyldithiocarbamate)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Selenium, bis(N,N-diethylcarbamodithioato-kappaS)bis(N,N-diethylcarbamodithioato-kappaS,kappaS')-  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Tin  (emission to water)
  quote:      Sn                    1.3                                                                 0.5           0.003
  candidates (flow name [compartment]):
    - tin  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Tinkal  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Tin(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Tin(IV)  [water] (kilogram, ef-3.1-biosphere)
    - Tin-San  [water] (kilogram, ef-3.1-biosphere)
    - Tinuvin  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Tin atom  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - tin (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Suspended solids, unspecified  (emission to water)
  quote:      ungelöste          15-10000              3000          0.31)/0.5)                         0.5           0.003
  candidates (flow name [compartment]):
    - Suspended Solids, Unspecified  [water] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
