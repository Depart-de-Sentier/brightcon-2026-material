You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: Transformation, from unknown  (resource to resources)
  quote:                         Î                                                                                        resource       land                                                           7.69E+04   m2     ÖSPAG (2002)         1     2.02   (1,3,1,3,1,4,8)
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Transformation, to industrial area, vegetation  (resource to resources)
  quote:                         Î                                                                                        resource       land                                                           3.59E+04   m2     ÖSPAG (2002)         1     2.02   (1,3,1,3,1,4,8)
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Transformation, to industrial area, built up  (resource to resources)
  quote:                         Î                                                                                        resource       land                                                           3.28E+04   m2     ÖSPAG (2002)         1     2.03   (3,3,1,3,1,4,8)
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Transformation, to traffic area, road network  (resource to resources)
  quote:       paved parking     Î                                                                                        resource       land                                                           8.20E+03   m2     ÖSPAG (2002)         1     2.03   (3,3,1,3,1,4,8)
  candidates (flow name [compartment]):
    - Traffic Area, Road Network  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Traffic Area, Road Network  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Traffic Area, Road Network  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - Traffic Area, Rail/road Embankment  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Traffic Area, Rail/road Embankment  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Traffic Area, Rail/road Embankment  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
- item: Occupation, industrial area, vegetation  (resource to resources)
  quote:                         Î                                                                                        resource       land                                                           1.80E+06   m2a    ÖSPAG (2002)         1     1.54   (3,3,1,3,1,4,7)
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Occupation, industrial area, built up  (resource to resources)
  quote:       built up area     Î                                                                                        resource       land                                                           1.64E+06   m2a    ÖSPAG (2002)         1     1.54   (3,3,1,3,1,4,7)
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Occupation, traffic area, road network  (resource to resources)
  quote:       paved parking     Î                                                                                        resource       land                                                           4.10E+05   m2a    ÖSPAG (2002)         1     1.54   (3,3,1,3,1,4,7)
  candidates (flow name [compartment]):
    - Traffic Area, Road Network  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Traffic Area, Road Network  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Traffic Area, Road Network  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - Traffic Area, Rail/road Embankment  [Land use / Land occupation] (square meter-year, ef-3.1-biosphere)
    - To Traffic Area, Rail/road Embankment  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
    - From Traffic Area, Rail/road Embankment  [Land use / Land transformation] (square meter, ef-3.1-biosphere)
- item: building, hall  (input)
  quote:       building hall     Î                                                                                        construction                                                                                    assumption, based
  search: building hall
  candidates:
    - Building, hall [CH] (square meter, 2 inputs)
    - Building, hall, wood construction [CH] (square meter, 22 inputs)
    - Building, hall, steel construction [CH] (square meter, 23 inputs)
    - Disposal, paper, as building waste [CH] (kilogram, 4 inputs)
    - Disposal, steel, as building waste [CH] (kilogram, 3 inputs)
    - Storage building, chemicals, solid [CH] (unit, 1 inputs)
    - Rammed earth wall, at building site [CH] (kilogram, 0 inputs, aggregated)
    - Hemp lime concrete, at building site [CH] (kilogram, 0 inputs, aggregated)
- item: building, multi-storey  (input)
  quote:                         Î                                                                                                        buildings        Yes    RER    building, multi-storey          2.63E+04   m3                          1     3.03   (3,3,1,3,1,4,9)
  search: building multi-storey
  candidates:
    - Building, multi-storey [RER] (cubic meter, 24 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [CH] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, laminated, integrated, at building [CH] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [RER] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, laminated, integrated, at building [RER] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [APAC] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [CN] (unit, 7 inputs)
    - 3kWp facade installation, multi-Si, panel, mounted, at building [US] (unit, 7 inputs)
- item: industrial machine, heavy, unspecified, at plant  (input)
  quote:       machines          Î                                                                                                        machinery        Yes    RER                                    1.68E+05   kg     assumption           1     3.23
  search: industrial machine heavy unspecified
  candidates:
    - Industrial machine, heavy, unspecified, at plant [RER] (kilogram, 8 inputs)

Return only the JSON object described by the schema.
