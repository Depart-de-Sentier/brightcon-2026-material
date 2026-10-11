You are mapping line items of a unit process to datasets and elementary flows in the BAFU-2026 life-cycle database.

For each line item below, candidates were found by a keyword search — over the 11,947 dataset names for inputs, over the EF 3.1 elementary-flow list for emissions and resources. Pick the candidate that supplies what the line item consumes (inputs) or names the substance and compartment released or extracted (emissions, resources), or say that none fits. Rules:

1. Prefer the dataset that matches the substance, the physical form and the technology stated in the line item (e.g. "50% in H2O, production mix" for an unspecified caustic soda; "at plant" for a purchased chemical; "burned in industrial furnace" for a fuel that is combusted on site rather than delivered).
2. Prefer a *unit process* over a candidate marked `aggregated` (those are themselves sealed inventories); if only an aggregated candidate fits, choose it and set `dependency` = true.
3. Location: prefer the process's own location (CH), then RER/Europe, then CH, then GLO. If the candidate list shows several locations, name the one you choose.
4. Never map a chemical to a similarly spelled different chemical. If no candidate is the right substance, set `chosen` to null and explain in `reason`; the code will report the line as missing.
5. For emissions and resources, choose the flow whose substance matches and whose compartment is the one stated (air / water / soil / resources); prefer the 'unspecified' sub-compartment unless the excerpt says otherwise; copy the compartment string into `compartment`. Geogenic (carbonate) CO2 is characterised as fossil CO2 in EF 3.1.
6. `reason` must say why the chosen candidate beats the runner-up, in one sentence.

Line items and their candidates:

- item: connector, PCI bus, at plant  (input)
  quote:                          H                                                                                        elect ronics   component     No        GLO    connector, PCI bus, at plant               1.82E-01 kg                                    1     2.29
  search: connector PCI bus at plant
  candidates:
    - Connector, PCI bus, at plant [GLO] (kilogram, 7 inputs)
- item: connector, computer, peripherical type, at plant  (input)
  quote:                          H                                                                                        elect ronics   component     No        GLO                                               1.03E-01 kg                                    1     2.29
  search: connector computer peripherical type at plant
  candidates:
    - Connector, computer, peripherical type, at plant [GLO] (kilogram, 9 inputs)
- item: capacitor, Tantalum-, through-hole mounting, at plant  (input)
  quote: tant alum capacitor      H                                                                                        elect ronics   component     No        GLO                                              3.48E-02 kg                                     1     2.29
  search: capacitor tantalum through-hole mounting at plant
  candidates:
    - Capacitor, Tantalum-, through-hole mounting, at plant [GLO] (kilogram, 10 inputs)
    - Capacitor, film, through-hole mounting, at plant [GLO] (kilogram, 15 inputs)
- item: capacitor, electrolyte type, < 2cm height, at plant  (input)
  quote: elect rolyt capacit or   H                                                                                        elect ronics   component     No        GLO                                               1.39E-01 kg                                    1     2.29
  search: capacitor electrolyte type < 2cm height at plant
  candidates:
    - Capacitor, electrolyte type, < 2cm height, at plant [GLO] (kilogram, 15 inputs)
    - Capacitor, electrolyte type, > 2cm height, at plant [GLO] (kilogram, 12 inputs)
- item: capacitor, SMD type, surface-mounting, at plant  (input)
  quote: SM D t ype capacitor     H                                                                                        elect ronics   component     No        GLO                                              4.38E-02 kg                                     1     2.29
  search: capacitor SMD type surface mounting at plant
  candidates:
    - Capacitor, SMD type, surface-mounting, at plant [GLO] (kilogram, 9 inputs)
    - Resistor, SMD type, surface mounting, at plant [GLO] (kilogram, 17 inputs)
    - Transistor, SMD type, surface mounting, at plant [GLO] (kilogram, 18 inputs)
    - Diode, glass-, SMD type, surface mounting, at plant [GLO] (kilogram, 9 inputs)
- item: capacitors, unspecified, at plant  (input)
  quote:                          H                                                                                        elect ronics   component     No        GLO                                               1.05E-01 kg                                    1     2.29
  search: capacitor unspecified at plant
  candidates:
    - Capacitor, unspecified, at plant [GLO] (kilogram, 5 inputs)
    - Cement, unspecified, at plant [CH] (kilogram, 5 inputs)
    - Ethoxylated alcohols, unspecified, at plant [RER] (kilogram, 6 inputs)
    - Metal working machine, unspecified, at plant [RER] (kilogram, 30 inputs)
    - Industrial machine, heavy, unspecified, at plant [RER] (kilogram, 8 inputs)
    - Pigments, paper production, unspecified, at plant [RER] (kilogram, 3 inputs)
    - Biocides, for paper production, unspecified, at plant [RER] (kilogram, 4 inputs)
    - Diode, unspecified, at plant [GLO] (kilogram, 3 inputs)
- item: inductor, ring core choke type, at plant  (input)
  quote: coils & induct ors       H                                                                                        elect ronics   component     No        GLO                                               3.36E-01 kg                                    1     2.29
  search: inductor ring core choke type at plant
  candidates:
    - Inductor, ring core choke type, at plant [GLO] (kilogram, 9 inputs)
- item: resistor, unspecified, at plant  (input)
  quote: resistor mix             H                                                                                        elect ronics   component     No        GLO    resistor, unspecified, at plant            5.67E-02 kg                                    1     2.29
  search: resistor unspecified at plant
  candidates:
    - Resistor, unspecified, at plant [GLO] (kilogram, 4 inputs)
    - Cement, unspecified, at plant [CH] (kilogram, 5 inputs)
    - Ethoxylated alcohols, unspecified, at plant [RER] (kilogram, 6 inputs)
    - Metal working machine, unspecified, at plant [RER] (kilogram, 30 inputs)
    - Industrial machine, heavy, unspecified, at plant [RER] (kilogram, 8 inputs)
    - Pigments, paper production, unspecified, at plant [RER] (kilogram, 3 inputs)
    - Biocides, for paper production, unspecified, at plant [RER] (kilogram, 4 inputs)
    - Diode, unspecified, at plant [GLO] (kilogram, 3 inputs)

Return only the JSON object described by the schema.
