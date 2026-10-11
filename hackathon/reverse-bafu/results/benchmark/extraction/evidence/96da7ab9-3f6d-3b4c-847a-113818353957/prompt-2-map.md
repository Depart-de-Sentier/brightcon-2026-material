You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (ZA), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Vermiculite, in ground  (resource to resources)
  quote: vermiculite in ground   Î                                                              amount of waste (mainly phosphate) in        resource        in ground                          Vermiculite, in ground                 1.00E+00 kg      Palabora Mining         1     1.24   (1,4,1,1,1,5);
  candidates (flow name [compartment]):
    - Peat, In Ground  [biota] (kilogram, ef-3.1-biosphere)
    - Spodumene, In Ground  [soil] (kilogram, ef-3.1-biosphere)
    - Pyrolusite, In Ground  [soil] (kilogram, ef-3.1-biosphere)
- item: Phosphorus, 18% in apatite, 12% in crude ore, in ground  (resource to resources)
  quote: phosphate in ground     Î                                                                                                            resource       in ground                                                                 3.00E-01 kg      Palabora Mining         1     2.06   (1,4,1,1,5,5);
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Occupation, mineral extraction site  (resource to resources)
  quote: extraction site (mine) Î                                                                                                          resource          land                                                                      6.50E-04 m2a     estimation              1     1.58   (1,4,1,1,1,5);
  candidates (flow name [compartment]):
    - Mineral Extraction Site  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Mineral Extraction Site  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Mineral Extraction Site  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
- item: Transformation, to mineral extraction site  (resource to resources)
  quote: to mineral extraction   Î                                                              density: 2'000 kg/m3 of mining material;      resource       land                                                                      1.30E-05 m2      estimation              1     2.06   (1,4,1,1,1,5);
  candidates (flow name [compartment]):
    - Mineral Extraction Site  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Mineral Extraction Site  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Mineral Extraction Site  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
- item: Transformation, from unknown  (resource to resources)
  quote: mine from unknown
  candidates (flow name [compartment]):
    - (no candidate found)
- item: diesel, burned in building machine  (input)
  quote: diesel (mine)           Î                                                                                                                           machinery            No     GLO                                           6.97E-03 MJ      Palabora Mining         1     1.24   (1,4,1,1,1,5);
  search: diesel burned in building machine
  candidates:
    - Diesel, burned in building machine, average [CH] (megajoule, 4 inputs)
    - Diesel, burned in building machine, with particle filter [CH] (megajoule, 4 inputs)
    - Diesel, burned in building machine, without particle filter [CH] (megajoule, 4 inputs)
    - Diesel, burned in building machine, with particle filter, without building machine [CH] (megajoule, 3 inputs)
    - Diesel, burned in building machine, with particle filter, without building machine and lubricating oil [CH] (megajoule, 1 inputs)
    - Diesel, burned in building machine, with particle filter [GLO] (megajoule, 4 inputs)
    - Diesel, burned in agricultural machine [CH] (kilogram, 4 inputs)
    - Diesel, burned in auxillary machines at concrete crusher [CH] (kilogram, 4 inputs)
- item: light fuel oil, burned in industrial furnace 1MW, non-modulating  (input)
  quote: heating - drying of                                                                                                                                                                    light fuel oil, burned in industrial
  search: light fuel oil burned in industrial furnace 1MW
  candidates:
    - Light fuel oil, burned in industrial furnace 1MW, non-modulating [RER] (megajoule, 5 inputs)
    - Light fuel oil, burned in industrial furnace 1MW, non-modulating [CH] (megajoule, 5 inputs)
    - Light fuel oil, burned in industrial furnace, for asphalt production, 1MW, non-modulating [CH] (megajoule, 5 inputs)
    - Heat, light fuel oil, at industrial furnace 1MW [RER] (megajoule, 1 inputs)
    - Heavy fuel oil, burned in industrial furnace 1MW, non-modulating [RER] (megajoule, 5 inputs)
    - Heat, light fuel oil, at industrial furnace 1MW [CH] (megajoule, 1 inputs)
    - Heavy fuel oil, burned in industrial furnace 1MW, non-modulating [CH] (megajoule, 5 inputs)
    - District heat, at consumer, light fuel oil in industrial furnace 1MW [CH] (megajoule, 2 inputs)
- item: electricity, medium voltage, production UCTE, at grid  (input)
  quote: electricity                                                                                                                                                                            electricity, medium voltage,
  search: electricity medium voltage production UCTE at grid
  candidates:
    - Electricity, medium voltage, production from oil, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from hard coal, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from natural gas, UCTE, at grid [CH] (kilowatt hour, 3 inputs)
    - xxx Electricity, medium voltage, production UCTE, at grid [UCTE] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production ZA, at grid [ZA] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production RER, at grid [RER] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production from oil, at grid [CH] (kilowatt hour, 3 inputs)
- item: lubricating oil, at plant  (input)
  quote: lubricating oil         Î                                                              amount copied from bentonite mining           chemicals      organics             No     RER    lubricating oil, at plant              8.06E-05 kg      Süd-Chemie (1999)       1     5.00   estimation
  search: lubricating oil at plant
  candidates:
    - Lubricating oil, at plant [RER] (kilogram, 4 inputs)
    - Soya oil, at plant [RER] (kilogram, 10 inputs)
    - Oil power plant 500MW [RER] (unit, 19 inputs)
    - Heavy fuel oil, burned in power plant [RER] (megajoule, 12 inputs)
    - Fatty alcohol, from palm oil, at plant [RER] (kilogram, 10 inputs)
    - Fatty alcohol sulfate, palm oil, at plant [RER] (kilogram, 9 inputs)
    - Fatty alcohol, from coconut oil, at plant [RER] (kilogram, 10 inputs)
    - Fatty acids, from vegetarian oil, at plant [RER] (kilogram, 12 inputs)
- item: blasting  (input)
  quote: blasting                Î                                                                                                                           civil engineering    No     RER    blasting                               1.66E-04 kg      Palabora Mining         1     2.06   (1,4,1,1,5,5);
  search: blasting
  candidates:
    - Blasting [RER] (kilogram, 1 inputs)
- item: mine, vermiculite  (input)
  quote: vermiculite mine        Î                                                                                                                           additives            Yes    ZA     mine, vermiculite                      6.45E-12 unit    Palabora Mining         1     3.73   (1,4,1,1,5,5);
  search: mine vermiculite
  candidates:
    - Mine, vermiculite [ZA] (unit, 3 inputs)
    - Vermiculite, at mine [ZA] (kilogram, 6 inputs)
    - Mine, gold [ZA] (unit, 4 inputs)
    - Hard coal, at mine [ZA] (kilogram, 9 inputs)
    - Basalt, at mine [RER] (kilogram, 13 inputs)
    - Lignite, at mine [RER] (kilogram, 4 inputs)
    - Open cast mine, lignite [RER] (unit, 11 inputs)
    - Average mineral fertiliser, as N, at regional storehouse [RER] (kilogram, 5 inputs)

Return only the JSON object described by the schema.
