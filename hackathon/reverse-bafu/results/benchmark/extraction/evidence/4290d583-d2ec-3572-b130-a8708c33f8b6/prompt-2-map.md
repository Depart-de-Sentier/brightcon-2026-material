You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (RER), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: rape methyl ester, at esterification plant  (input)
  quote: rape methyl ester, at esterification plant                            RER             0           kg             0                52%            1   1.05     (1,1,1,1,1,1); Rape oil                                             52%
  search: rape methyl ester esterification
  candidates:
    - Rape methyl ester, at esterification plant [RER] (kilogram, 11 inputs)
    - Rape methyl ester, at esterification plant [CH] (kilogram, 11 inputs)
    - xx Glycerine, from rape oil, at esterification plant [RER] (kilogram, 11 inputs)
    - Potassium sulphate, as K2O, from rape oil, at esterification plant [RER] (kilogram, 11 inputs)
    - Rape methyl ester, at regional storage [CH] (kilogram, 11 inputs)
    - Operation, lorry 28t, rape methyl ester 100% [CH] (kilometer, 1 inputs)
    - Glycerine, from rape oil, at esterification plant [CH] (kilogram, 11 inputs)
    - Operation, passenger car, rape seed methyl ester 5% [CH] (kilometer, 2 inputs)
- item: vegetable oil methyl ester, at esterification plant (used cooking oil)  (input)
  quote: vegetable oil methyl ester, at esterification plant                    FR             0           kg             0                15%            1   1.05     (1,1,1,1,1,1); UCO (waste oils)                                     15%
  search: vegetable oil methyl ester esterification
  candidates:
    - Vegetable oil methyl ester, at esterification plant [CH] (kilogram, 10 inputs)
    - Vegetable oil methyl ester, at esterification plant [FR] (kilogram, 10 inputs)
    - Vegetable oil esterification plant [CH] (unit, 5 inputs)
    - Vegetable oil methyl ester, production FR, at service station [CH] (kilogram, 13 inputs)
    - Glycerine, from vegetable oil, at esterification plant [FR] (kilogram, 10 inputs)
- item: palm methyl ester, at esterification plant  (input)
  quote: palm methyl ester, at esterification plant                             MY             0           kg             0                13%            1   1.05     (1,1,1,1,1,1); Palm oil                                             13%
  search: palm methyl ester esterification
  candidates:
    - Palm methyl ester, at esterification plant [MY] (kilogram, 11 inputs)
    - Rape methyl ester, at esterification plant [RER] (kilogram, 11 inputs)
    - Rape methyl ester, at esterification plant [CH] (kilogram, 11 inputs)
    - Vegetable oil methyl ester, at esterification plant [CH] (kilogram, 10 inputs)
    - xx Palm methyl ester, production MY, at service station [CH] (kilogram, 14 inputs)
    - Soybean methyl ester, at esterification plant [BR] (kilogram, 13 inputs)
    - Soybean methyl ester, at esterification plant [US] (kilogram, 13 inputs)
    - Vegetable oil methyl ester, at esterification plant [FR] (kilogram, 10 inputs)
- item: soybean methyl ester, at esterification plant (soybean oil)  (input)
  quote: soybean methyl ester, at esterification plant                         BR              0           kg             0                 8%            1   1.05     (1,1,1,1,1,1); Soybean oil                                           8%
  search: soybean methyl ester esterification
  candidates:
    - Soybean methyl ester, at esterification plant [BR] (kilogram, 13 inputs)
    - Soybean methyl ester, at esterification plant [US] (kilogram, 13 inputs)
    - Rape methyl ester, at esterification plant [RER] (kilogram, 11 inputs)
    - Rape methyl ester, at esterification plant [CH] (kilogram, 11 inputs)
    - Vegetable oil methyl ester, at esterification plant [CH] (kilogram, 10 inputs)
    - Soybean methyl ester, production US, at service station [CH] (kilogram, 15 inputs)
    - xx Soybean methyl ester, production BR, at service station [CH] (kilogram, 15 inputs)
    - Palm methyl ester, at esterification plant [MY] (kilogram, 11 inputs)
- item: vegetable oil methyl ester, at esterification plant (animal fat)  (input)
  quote: vegetable oil methyl ester, at esterification plant                    FR             0           kg             0                 8%            1   1.05     (1,1,1,1,1,1); Animal fat                                            8%
  search: vegetable oil methyl ester esterification
  candidates:
    - Vegetable oil methyl ester, at esterification plant [CH] (kilogram, 10 inputs)
    - Vegetable oil methyl ester, at esterification plant [FR] (kilogram, 10 inputs)
    - Vegetable oil esterification plant [CH] (unit, 5 inputs)
    - Vegetable oil methyl ester, production FR, at service station [CH] (kilogram, 13 inputs)
    - Glycerine, from vegetable oil, at esterification plant [FR] (kilogram, 10 inputs)
- item: soybean methyl ester, at esterification plant (sunflower)  (input)
  quote: soybean methyl ester, at esterification plant                         BR              0           kg             0                 3%            1   1.05     (1,1,1,1,1,1); Sunflower                                             3%
  search: soybean methyl ester esterification
  candidates:
    - Soybean methyl ester, at esterification plant [BR] (kilogram, 13 inputs)
    - Soybean methyl ester, at esterification plant [US] (kilogram, 13 inputs)
    - Rape methyl ester, at esterification plant [RER] (kilogram, 11 inputs)
    - Rape methyl ester, at esterification plant [CH] (kilogram, 11 inputs)
    - Vegetable oil methyl ester, at esterification plant [CH] (kilogram, 10 inputs)
    - Soybean methyl ester, production US, at service station [CH] (kilogram, 15 inputs)
    - xx Soybean methyl ester, production BR, at service station [CH] (kilogram, 15 inputs)
    - Palm methyl ester, at esterification plant [MY] (kilogram, 11 inputs)

Return only the JSON object described by the schema.
