You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (GLO), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: diesel, at regional storage  (input)
  quote: technosphere       diesel, at regional storage            RER 0                             kg         2.34E-2              1              1.24              (3,3,3,3,1,BU:1.05); Calculation
  search: diesel at regional storage
  candidates:
    - Diesel, at regional storage [RER] (kilogram, 15 inputs)
    - xxx Diesel, at regional storage [RER] (kilogram, 14 inputs)
    - Diesel, at regional storage [CH] (kilogram, 18 inputs)
    - xxx Diesel, at regional storage [CH] (kilogram, 16 inputs)
    - Diesel, fossil, at regional storage [CH] (kilogram, 17 inputs)
    - Tantalum, powder, capacitor-grade, at regional storage [GLO] (kilogram, 16 inputs)
    - Tin, at regional storage [RER] (kilogram, 13 inputs)
    - Gold, at regional storage [RER] (kilogram, 4 inputs)
- item: lubricating oil, at plant  (input)
  quote:                    lubricating oil, at plant              RER 0                             kg         6.70E-5              1              2.06
  search: lubricating oil at plant
  candidates:
    - Lubricating oil, at plant [RER] (kilogram, 4 inputs)
    - Production plant crude oil, onshore [GLO] (unit, 6 inputs)
    - Soya oil, at plant [RER] (kilogram, 10 inputs)
    - Oil power plant 500MW [RER] (unit, 19 inputs)
    - Heavy fuel oil, burned in power plant [RER] (megajoule, 12 inputs)
    - Fatty alcohol, from palm oil, at plant [RER] (kilogram, 10 inputs)
    - Fatty alcohol sulfate, palm oil, at plant [RER] (kilogram, 9 inputs)
    - Fatty alcohol, from coconut oil, at plant [RER] (kilogram, 10 inputs)
- item: diesel-electric generating set production 10MW  (input)
  quote:                    diesel-electric generating set production
  search: diesel-electric generating set production 10MW
  candidates:
    - Diesel-electric generating set production 10MW [RER] (unit, 5 inputs)
- item: disposal, used mineral oil, 10% water, to hazardous waste incineration  (input)
  quote:                    disposal, used mineral oil, 10% water, to
  search: disposal used mineral oil hazardous waste incineration
  candidates:
    - Disposal, used mineral oil, 10% water, to hazardous waste incineration [CH] (kilogram, 15 inputs)
- item: Benzene  (emission to air)
  quote:                    Benzene                                    -               -             kg         2.00E-8              1              3.03              (3,3,3,3,1,BU:3); Extrapolation
  candidates (flow name [compartment]):
    - Benzene  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ethyl Benzene  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - 1,3-benzenediamine  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Benzenesulfonic acid  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Benzenepentanoic acid  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Benzenepropanoic acid  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Di(propan-2-yl)benzene  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - (Trifluoromethyl)benzene  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Benzo(a)pyrene  (emission to air)
  quote: sumed to be emitted with 0.02 kg/TJIn and Benzo(a)pyrene with 0.1E-3 kg/TJIn and heavy metal
  candidates (flow name [compartment]):
    - Benzo[a]pyrene  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Benzo[a]pyrene  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Benzo[a]pyrene  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - benzo[a]pyrene  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - benzo[a]pyrene  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Pyrene  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Benzocaine  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Benzoic Acid  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Carbon dioxide, fossil  (emission to air)
  quote:                    Carbon dioxide, fossil                     -               -             kg         7.30E-2              1              1.10              (2,3,2,3,1,BU:1.05); Literature
  candidates (flow name [compartment]):
    - Carbon Dioxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (biogenic)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic-100yr)  [air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
- item: Carbon monoxide, fossil  (emission to air)
  quote:                    Carbon monoxide, fossil                    -               -             kg         6.80E-4              1              5.03              (3,3,3,3,1,BU:5); Literature
  candidates (flow name [compartment]):
    - Carbon Monoxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - carbon monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - carbon monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Black carbon  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
- item: Dinitrogen monoxide  (emission to air)
  quote:                    Dinitrogen monoxide                        -               -             kg         6.00E-6              1              1.54              (3,3,3,3,1,BU:1.5); Literature
  candidates (flow name [compartment]):
    - Carbon Monoxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - lead monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - lead monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Carbon Monoxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - carbon monoxide  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
- item: Mercury  (emission to air)
  quote:                    Mercury                                    -               -             kg         4.67E-10             1              5.08              (3,3,3,3,3,BU:5); Literature on content in diesel
  candidates (flow name [compartment]):
    - Mercury  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Mercury  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Mercury  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Mercury  [Resources / Resources from ground] (kilogram, ef-3.1-biosphere)
    - mercury  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: NMVOC, non-methane volatile organic compounds, unspecified origin  (emission to air)
  quote:                    NMVOC, non-methane volatile organic
  candidates (flow name [compartment]):
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - non-methane volatile organic compounds  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - non-methane volatile organic compounds  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Particulates, < 2.5 um  (emission to air)
  quote:                    Particulates, < 2.5 um                     -               -             kg         1.70E-4              1              3.03              (3,3,3,3,1,BU:3); Literature
  candidates (flow name [compartment]):
    - Particulates, unspecified  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
- item: Cadmium  (emission to air)
  quote:                    Cadmium                                    -               -             kg         2.34E-10             1              5.06              (2,3,1,1,3,BU:5); Literature for automobile emissions
  candidates (flow name [compartment]):
    - Cadmium  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium(2+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium oxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium Sulfate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium nitrate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium sulfide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium Chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium Carbonate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Copper  (emission to air)
  quote:                    Copper                                     -               -             kg         3.97E-8              1              5.06              (2,3,1,1,3,BU:5); Literature for automobile emissions
  candidates (flow name [compartment]):
    - Copper  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Copper(2+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Oxine-copper  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Copper hydroxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Copper (i) Iodide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Copper (ii) Oxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Copper(ii) Acetate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Copper (ii) Sulfate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Chromium  (emission to air)
  quote:                    Chromium                                   -               -             kg         1.17E-9              1              5.06              (2,3,1,1,3,BU:5); Literature for automobile emissions
  candidates (flow name [compartment]):
    - Chromium  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chromium-51  [air] (kilogram, ef-3.1-biosphere)
    - Chromium(3+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chromium(6+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chromium(3+) Triacetate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chromium (iii) Hydroxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chromium(3+) Trichloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chromium, 3-hydroxy-4-[(2-hydroxy-1-naphthalenyl)azo]-7-nitro-1-naphthalenesulfonic Acid Complex  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Chromium VI  (emission to air)
  quote:                    Chromium VI                                -               -             kg         2.34E-12             1              5.06
  candidates (flow name [compartment]):
    - Chromium VI  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - chromium (vi)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - chromium (vi)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Chromium  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chromium-51  [air] (kilogram, ef-3.1-biosphere)
    - Vinclozolin  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chromium(3+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Chromium(6+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Nickel  (emission to air)
  quote:                    Nickel                                     -               -             kg         1.64E-9              1              5.06              (2,3,1,1,3,BU:5); Literature for automobile emissions
  candidates (flow name [compartment]):
    - Nickel  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nickel-63  [air] (kilogram, ef-3.1-biosphere)
    - Nickel(2+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nickel Sulfate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nickel Sulphide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nickel (ii) Oxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nickel Difluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nickel Subsulfide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Selenium  (emission to air)
  quote:                    Selenium                                   -               -             kg         2.34E-10             1              5.06              (2,3,1,1,3,BU:5); Literature for automobile emissions
  candidates (flow name [compartment]):
    - Selenium  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Selenium (iv)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Selenium Gaseous  [air] (kilogram, ef-3.1-biosphere)
    - Selenium dimethyldithiocarbamate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Selenium, bis(N,N-diethylcarbamodithioato-kappaS)bis(N,N-diethylcarbamodithioato-kappaS,kappaS')-  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Selenium  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Selenium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Selenium  [Resources / Resources from ground] (kilogram, ef-3.1-biosphere)
- item: Zinc  (emission to air)
  quote:                    Zinc                                       -               -             kg         2.34E-8              1              5.06              (2,3,1,1,3,BU:5); Literature for automobile emissions
  candidates (flow name [compartment]):
    - Zinc  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Zinc-65  [air] (kilogram, ef-3.1-biosphere)
    - Zinc(2+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Zinc Sulfate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Zinc nitrate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Zincchloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Zinc Stannate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Zinc Dibromide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
