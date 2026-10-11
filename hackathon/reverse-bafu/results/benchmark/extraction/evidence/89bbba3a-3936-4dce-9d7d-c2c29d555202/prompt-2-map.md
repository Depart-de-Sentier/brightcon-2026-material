You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: electricity, medium voltage, at grid  (input)
  quote: electricity, medium voltage, at grid                                            CH kWh                         5.20E+05            1                       2               own calculation after key data on power.
  search: electricity medium voltage at grid
  candidates:
    - Electricity, medium voltage, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, SBB, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import AT, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import DE, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import FR, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import IT, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, import ENTSO, at grid [CH] (kilowatt hour, 3 inputs)
    - Electricity, medium voltage, production CH, at grid [CH] (kilowatt hour, 3 inputs)
- item: light fuel oil, at regional storage  (input)
  quote: light fuel oil, at regional storage                                             CH kg                          3.60E+03            1                       2               own calculation.
  search: light fuel oil at regional storage
  candidates:
    - Light fuel oil, at regional storage [CH] (kilogram, 14 inputs)
    - Light fuel oil, at regional storage [RER] (kilogram, 12 inputs)
    - Heavy fuel oil, at regional storage [CH] (kilogram, 14 inputs)
    - Heavy fuel oil, at regional storage [RER] (kilogram, 12 inputs)
- item: ammonia, liquid, at regional storehouse  (input)
  quote: ammonia, liquid, at regional storehouse                                         RER kg                         1.80E+02            1                      1.3              based on flowsheet design estimation
  search: ammonia liquid at regional storehouse
  candidates:
    - Ammonia, liquid, at regional storehouse [CH] (kilogram, 4 inputs)
    - Ammonia, liquid, at regional storehouse [RER] (kilogram, 4 inputs)
- item: sulphuric acid, liquid, at plant  (input)
  quote: sulphuric acid, liquid, at plant                                                RER kg                         1.80E+01            1                      1.3              based on flowsheet design estimation
  search: sulphuric acid liquid at plant
  candidates:
    - Sulphuric acid, liquid, at plant [RER] (kilogram, 7 inputs)
    - Sulphuric acid from viscose production, at plant [GLO] (kilogram, 24 inputs)
- item: transport, lorry 28t  (input)
  quote: transport, lorry 28t                                                            CH tkm                         1.53E+03            1                      2.1              standard
  search: transport lorry 28t
  candidates:
    - Disposal, lorry 28t [CH] (unit, 6 inputs)
    - Maintenance, lorry 28t [CH] (unit, 11 inputs)
    - Transport, freight, lorry, fleet average [CH] (ton kilometer, 4 inputs)
    - xxx Operation, lorry >28t, fleet average [CH] (kilometer, 1 inputs)
    - xxx Operation, lorry 20-28t, fleet average [CH] (kilometer, 1 inputs)
    - Operation, lorry 28t, rape methyl ester 100% [CH] (kilometer, 1 inputs)
    - Transport, municipal waste collection, lorry 21t [CH] (ton kilometer, 5 inputs)
    - Transport, freight, lorry, 3.5t gross weight, fleet average [CH] (ton kilometer, 22 inputs)
- item: transport, freight, rail  (input)
  quote: transport, freight, rail                                                        RER tkm                        1.19E+02            1                      2.1              standard
  search: transport freight rail
  candidates:
    - Transport, freight, rail, electricity with shunting [CH] (ton kilometer, 10 inputs)
    - Transport, freight, rail, diesel, with particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity without shunting [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, diesel, without particle filter [CH] (ton kilometer, 9 inputs)
    - Transport, freight, rail, electricity with shunting, Betrieb [CH] (ton kilometer, 2 inputs)
    - Transport, freight, rail, electricity with shunting, Fahrzeug [CH] (ton kilometer, 5 inputs)
    - Transport, freight, rail, electricity with shunting, Infrastruktur [CH] (ton kilometer, 3 inputs)
    - Transport, freight, rail [RER] (ton kilometer, 10 inputs)
- item: radioactive waste, in final repository for nuclear waste LLW  (input)
  quote: radioactive waste, in final repository for nuclear waste LLW                             CH m3                                    1.00E+00                                   1                             1                 all waste in will move out to final repository
  search: radioactive waste in final repository for nuclear waste LLW
  candidates:
    - Radioactive waste, in final repository for nuclear waste LLW [CH] (cubic meter, 5 inputs)
    - Final repository for nuclear waste LLW [CH] (unit, 10 inputs)
    - Radioactive waste, in interim storage, for final repository LLW [CH] (cubic meter, 5 inputs)
    - Radioactive waste, in final repository for nuclear waste SF, HLW, and ILW [CH] (cubic meter, 9 inputs)
- item: Heat, waste  (emission to air)
  quote: Heat, waste                                                                          MJ                        2.50E+06            1                       2               same as for electricity
  candidates (flow name [compartment]):
    - Waste Heat  [air] (megajoule, ef-3.1-biosphere)
    - Energy, waste heat, air  [resources / in air] (megajoule, bafu-2026-residual)
    - Waste Heat  [soil] (megajoule, ef-3.1-biosphere)
    - Waste Heat  [water] (megajoule, ef-3.1-biosphere)
    - Heat, waste  [emissions to water / groundwater, long-term] (megajoule, bafu-2026-residual)
    - Waste water/m3  [emissions to water / unspecified] (cubic meter, bafu-2026-residual)
    - Waste water  [emissions to water / ocean] (kilogram, bafu-2026-residual)
    - Waste water  [emissions to water / river] (kilogram, bafu-2026-residual)
- item: Ammonia  (emission to air)
  quote: Ammonia                                                                              kg                        1.44E+00            1                      1.2              expected emissions used, range with guaranteed value
  candidates (flow name [compartment]):
    - Ammonia  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Acetaldehyde--ammonia  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Cadmium  (emission to air)
  quote: Cadmium                                                                              kg                        5.40E-06            1                      20               expected emissions used, range with guaranteed value
  candidates (flow name [compartment]):
    - Cadmium  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium(2+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium oxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium Sulfate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium nitrate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium sulfide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium Chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Cadmium Carbonate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Carbon dioxide, fossil  (emission to air)
  quote: Carbon dioxide, fossil                                                               kg                        1.14E+04            1                      1.2              own estimation of uncertainty
  candidates (flow name [compartment]):
    - Carbon Dioxide (fossil)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (fossil)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - carbon dioxide (biogenic)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (biogenic-100yr)  [air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Carbon Dioxide (land Use Change)  [Resources / Resources from air] (kilogram, ef-3.1-biosphere)
- item: Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin  (emission to air)
  quote: Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin                             kg                        3.60E-11            1                       5               own estimation of uncertainty
  candidates (flow name [compartment]):
    - (no candidate found)
- item: Hydrogen chloride  (emission to air)
  quote: Hydrogen chloride                                                                    kg                        8.10E-01            1                       4               expected emissions used, range with guaranteed value
  candidates (flow name [compartment]):
    - Hydrogen Chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen Chloride  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Hydrogen Chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - hydrogen chloride  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - hydrogen chloride  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen  [air] (kilogram, ef-3.1-biosphere)
    - Hydrogen-3  [Emissions / Emissions to air] (kilo Becquerel, ef-3.1-biosphere)
- item: Lead  (emission to air)
  quote: Lead                                                                                 kg                        2.20E-04            1                      20               expected emissions used, range with guaranteed value
  candidates (flow name [compartment]):
    - Lead  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead(2+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead-210  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead oxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead nitrate  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Sulfochromate Yellow  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Nitrogen oxides  (emission to air)
  quote: Nitrogen oxides                                                                      kg                        2.16E+01            1                      1.3              expected emissions used, range with guaranteed value
  candidates (flow name [compartment]):
    - Nitrogen Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Mustard  [air] (kilogram, ef-3.1-biosphere)
    - Nitrogen Trifluoride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Nitrogen oxide (N2O4)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: NMVOC, non-methane volatile organic compounds, unspecified origin  (emission to air)
  quote: NMVOC, non-methane volatile organic compounds, unspecified origin                    kg                        3.60E-03            1                       5               own estimation of uncertainty
  candidates (flow name [compartment]):
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Non-methane Volatile Organic Compounds  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - non-methane volatile organic compounds  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - non-methane volatile organic compounds  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Particulates, < 2.5 um  (emission to air)
  quote: Particulates, < 2.5 um                                                               kg                        1.80E-03            1                       5               own estimation of uncertainty
  candidates (flow name [compartment]):
    - Particulates, unspecified  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
- item: Sulfur dioxide  (emission to air)
  quote: Sulfur dioxide                                                                       kg                        5.04E+00            1                       2               expected emissions used, range with guaranteed value
  candidates (flow name [compartment]):
    - Sulfur Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [air] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [soil] (kilogram, ef-3.1-biosphere)
    - Sulfur Dioxide  [water] (kilogram, ef-3.1-biosphere)
    - Sulfur  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Sulfur Oxides  [air] (kilogram, ef-3.1-biosphere)
- item: Carbon-14  (emission to air)
  quote: Carbon-14                                                                           kBq                        1.66E+06            1                       2               own estimation of uncertainty
  candidates (flow name [compartment]):
    - Carbon-14  [Emissions / Emissions to air] (kilo Becquerel, ef-3.1-biosphere)
    - Carbon-14  [Emissions / Emissions to water] (kilo Becquerel, ef-3.1-biosphere)
    - Carbon-14  [soil] (kilogram, ef-3.1-biosphere)
    - carbon-14  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Black carbon  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
    - Carbon black  [emissions to air / unspecified] (kilogram, bafu-2026-residual)
    - PFC-14  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - HFC-143  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Hydrogen-3, Tritium  (emission to air)
  quote: Hydrogen-3, Tritium                                                                 kBq                        3.04E+06            1                       2               own estimation of uncertainty
  candidates (flow name [compartment]):
    - Hydrogen  [air] (kilogram, ef-3.1-biosphere)
    - Hydrogen-3  [Emissions / Emissions to air] (kilo Becquerel, ef-3.1-biosphere)
    - Hydrogen Iodide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen Sulfide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen cyanide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogenated mdi  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen Arsenide  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrogen Chloride  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Aluminum  (emission to water)
  quote: Aluminum                                                                             kg                        2.40E-01            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Aluminium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - aluminium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Aluminium (iii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - aluminium (iii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - aluminium sulfate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - aluminium hydroxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - aluminium phosphide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - aluminium trilactate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Cadmium, ion  (emission to water)
  quote: Cadmium, ion                                                                         kg                        2.40E-03            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Cadmium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - cadmium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Bromide ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cadmium(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cadmium-109  [water] (kilogram, ef-3.1-biosphere)
- item: Chlorinated solvents, unspecified  (emission to water)
  quote: Chlorinated solvents, unspecified                                                    kg                        2.40E-03            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Chlorinated Solvents, Unspecified  [water] (kilogram, ef-3.1-biosphere)
    - Chlorinated Solvents, Unspecified  [air] (kilogram, ef-3.1-biosphere)
- item: Chromium VI  (emission to water)
  quote: Chromium VI                                                                          kg                        2.40E-03            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Chromium VI  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - chromium (vi)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - chromium (vi)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Chromium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - chromium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - vitamin D2  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Chromium-51  [water] (kilogram, ef-3.1-biosphere)
    - Vinclozolin  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Chromium, ion  (emission to water)
  quote: Chromium, ion                                                                        kg                        4.80E-02            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Chromium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - chromium  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Bromide ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Chromium VI  [emissions to water / groundwater, long-term] (kilogram, bafu-2026-residual)
    - Chromium-51  [water] (kilogram, ef-3.1-biosphere)
- item: Cobalt  (emission to water)
  quote: Cobalt                                                                               kg                        1.20E-02            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Cobalt  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - cobalt  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cobalt-57  [water] (kilogram, ef-3.1-biosphere)
    - Cobalt-58  [Emissions / Emissions to water] (kilo Becquerel, ef-3.1-biosphere)
    - Cobalt-60  [Emissions / Emissions to water] (kilo Becquerel, ef-3.1-biosphere)
    - cobalt-58  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - cobalt-60  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Cobalt(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Copper, ion  (emission to water)
  quote: Copper, ion                                                                          kg                        1.20E-02            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Copper  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - copper  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Copper(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Bromide ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lithium ion  [water] (kilogram, ef-3.1-biosphere)
- item: Hydrocarbons, unspecified  (emission to water)
  quote: Hydrocarbons, unspecified                                                            kg                        2.40E-01            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Hydrocarbons (unspecified)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - hydrocarbons (unspecified)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, Aliphatic, Alkanes, Unspecified  [water] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons (unspecified)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons (unspecified)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - hydrocarbons (unspecified)  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Hydrocarbons, Aliphatic, Alkanes, Unspecified  [air] (kilogram, ef-3.1-biosphere)
    - Acidity, unspecified  [emissions to water / unspecified] (kilogram, bafu-2026-residual)
- item: Iron, ion  (emission to water)
  quote: Iron, ion                                                                            kg                        4.80E-02            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Iron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - iron  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iron-59  [water] (kilo Becquerel, ef-3.1-biosphere)
    - Iron(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iron(3+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - iron (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Lead  (emission to water)
  quote: Lead                                                                                 kg                        1.20E-02            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Lead  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - lead  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead-210  [water] (kilo Becquerel, ef-3.1-biosphere)
    - lead (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead oxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead Dioxide  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Lead nitrate  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Mercury  (emission to water)
  quote: Mercury                                                                              kg                        2.40E-04            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Mercury  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - mercury (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Mercury  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
    - Mercury  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Mercury  [Resources / Resources from ground] (kilogram, ef-3.1-biosphere)
    - mercury  [Emissions / Emissions to soil] (kilogram, ef-3.1-biosphere)
    - Mercury(2+)  [Emissions / Emissions to air] (kilogram, ef-3.1-biosphere)
- item: Nickel, ion  (emission to water)
  quote: Nickel, ion                                                                          kg                        4.80E-02            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Nickel  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - nickel  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nickel-63  [water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Nickel(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)
    - Bromide ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
- item: Radioactive species, Nuclides, unspecified  (emission to water)
  quote: Radioactive species, Nuclides, unspecified                                          kBq                        6.00E+02            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Radioactive Species, Nuclides, Unspecified  [water] (kilo Becquerel, ef-3.1-biosphere)
    - Radioactive species, unspecified  [emissions to air / unspecified] (kilo Becquerel, bafu-2026-residual)
    - Radioactive species, unspecified  [emissions to air / low. pop.] (kilo Becquerel, bafu-2026-residual)
- item: Zinc, ion  (emission to water)
  quote: Zinc, ion                                                                            kg                        4.80E-02            1                       5               own estimation of uncertainty, guaranted releases given
  candidates (flow name [compartment]):
    - Zinc  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - zinc  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Zinc-65  [water] (kilogram, ef-3.1-biosphere)
    - Zinc(2+)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - β-Ionone  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - zinc (ii)  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Iodide Ion  [Emissions / Emissions to water] (kilogram, ef-3.1-biosphere)
    - Sodium ion  [water] (kilogram, ef-3.1-biosphere)

Return only the JSON object described by the schema.
