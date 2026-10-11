You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: biogas, from sewage sludge, at storage  (input)
  quote:                                                              CH             0                    Nm3                                                                                                     1.02E+0               1            1.21                     (1,1,1,1,1,5,BU:1.05); ;
  search: biogas from sewage sludge at storage
  candidates:
    - Biogas, from sewage sludge, at storage [CH] (cubic meter, 4 inputs)
- item: biogas, mix, at agricultural co-fermentation, covered  (input)
  quote:                                                              CH             0                    Nm3                                                                                                     2.67E-2               1            1.21                     (1,1,1,1,1,5,BU:1.05); ;
  search: biogas mix agricultural co-fermentation covered
  candidates:
    - Biogas, mix, at agricultural co-fermentation, covered [CH] (cubic meter, 3 inputs)
    - Biogas, from slurry, at agricultural co-fermentation, covered [CH] (cubic meter, 6 inputs)
    - Biogas, from biowaste, at agricultural co-fermentation, covered [CH] (cubic meter, 7 inputs)
    - Biogas, from fat and oil, at agricultural co-fermentation, covered [CH] (cubic meter, 7 inputs)
- item: biogas, from biowaste, at storage  (input)
  quote:                 biogas, from biowaste, at storage            CH             0                    Nm3                                                                                                     6.25E-1               1            1.21                     (1,1,1,1,1,5,BU:1.05); ;
  search: biogas from biowaste at storage
  candidates:
    - Biogas, from biowaste, at storage [CH] (cubic meter, 2 inputs)
    - Biogas, from biowaste, at storage, economic allocation [CH] (cubic meter, 5 inputs)
    - Biogas, from sewage sludge, at storage [CH] (cubic meter, 4 inputs)
    - xx Biogas, from whey, digestion, at storage [CH] (cubic meter, 10 inputs)
    - xx Biogas, from grass, digestion, at storage [CH] (cubic meter, 8 inputs)
    - Biogas, from molasses, co-digestion, at storage [CH] (cubic meter, 7 inputs)
    - Biogas, from glycerine, co-digestion, at storage [CH] (cubic meter, 7 inputs)
    - Biogas, from sugar beet, co-digestion, at storage [CH] (cubic meter, 7 inputs)
- item: biogas purification, to methane, 99 vol-%, membrane technology process  (input)
  quote:                                                              CH             0                    Nm3                                                                                                     2.65E-1               1            1.21                     (1,1,1,1,1,5,BU:1.05); ;
  search: biogas purification membrane technology
  candidates:
    - Biogas purification, to methane, 99 vol-%, membrane technology process [CH] (cubic meter, 6 inputs)
- item: biogas purification, to methane, 99 vol-%, amino washing process  (input)
  quote:                                                              CH             0                    Nm3                                                                                                     5.78E-1               1            1.21                     (1,1,1,1,1,5,BU:1.05); ;
  search: biogas purification amino washing
  candidates:
    - Biogas purification, to methane, 99 vol-%, amino washing process [CH] (cubic meter, 14 inputs)
    - Biogas purification, to methane, 97 vol-%, glycol washing process [CH] (cubic meter, 10 inputs)
- item: biogas purification, to methane, 96 vol-%, pressure swing adsorption  (input)
  quote:                                                              CH             0                    Nm3                                                                                                     1.57E-1               1            1.21                     (1,1,1,1,1,5,BU:1.05); ;
  search: biogas purification pressure swing adsorption
  candidates:
    - Biogas purification, to methane, 96 vol-%, pressure swing adsorption [CH] (cubic meter, 7 inputs)

Return only the JSON object described by the schema.
