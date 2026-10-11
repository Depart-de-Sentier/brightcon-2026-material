You are locating the inventory table of one dataset inside a life-cycle-inventory report.

Dataset: `Disposal, digester sludge, to municipal incineration` [CH], 1 kg, BAFU category waste management / municipal incineration.
Metadata: includedProcesses: Waste incineration from waste reception gate further downstream (excluding transport to the MSWI plant). Waste-specific air and water emisions from incineration, auxiliary material consumption for flue gas cleaning. Short-term emissions to river water and long-term emisisons to ground water from sla · technology: average Swiss MSWI plants in 2010 (grate incinerators) with electrostatic precipitator for fly ash (ESP), wet flue gas scrubber and 25%  SNCR , 42.77%  SCR-high dust , 32.68%  SCR-low dust -DeNOx faci · comment: This dataset represents the activity of waste disposal of digester sludge in a municipal solid waste incinerator (MSWI) Recommended use of this dataset: for incineration of fermented (digested) sewage sludge from treatment of average municipal wastewater Waste composition (wet, in ppm): upper heatin

Report: `2013 - Updates LCI waste treatment services - Doka.pdf` (48 PDF pages). Below is every table and figure caption found in it, with the PDF page it appears on (not the printed page number). The report may be in German, French or English; the dataset name is English — match on meaning (e.g. "gebrannter Ölschiefer" = burnt shale, "Gipsfaserplatte" = gypsum fibre board).

- p.9: Tab. 6.2 on page 34. It turns out that the average waste composition (Iaverage e) is not really needed here,
- p.11: Tab. 2.1 Share of chemical elements in burnable waste fractions of average waste frbrunable e (left); share of boiler ash
- p.13: Fig. 2.1 Total Swiss dioxin and furan emissions 1950-2000 (adopted from BFS 2002:143)
- p.15: Fig. 2.2 Scheme of the new modelling of incomplete combustion products depending on
- p.17: Tab. 2.2 Former and new DeNOX technology mix in the MSWI model.
- p.17: Tab. 2.3 Input of ancillary materials during average MSWI operation
- p.18: Tab. 2.4 Synopsis of the allocation of auxiliary material consumption to various allocation recipients.
- p.19: Fig. 2.3 Gross energy production efficiencies of Swiss MSWI plants in 2011 ( ) and in 2000 for comparison ( ). The
- p.20: Tab. 2.5 Contribution to internal energy demand in MSWI, based on MSWI Niederurnen, Linthgebiet (Egli 2005)
- p.21: Tab. 2.6 Attribution of internal energy demand in MSWI model
- p.22: Fig. 2.4 Scheme of internal electricity redistribution between incineration datasets for high- and low-calorific wastes
- p.23: Fig. 2.5 Extended scheme of internal electricity redistribution for a consequential System Model. The (constrained)
- p.27: Tab. 3.1 Material fractions in shredder residues of electronic devices
- p.28: Tab. 3.2 Material fractions in separated used LCD modules
- p.29: Tab. 3.3 Composition of waste capacitors (Hischier et al. 2007-V:113)
- p.33: Tab. 6.1 Average transfer coefficients in municipal waste incinerators (working point data for operation with average
- p.34: Tab. 6.2 Derived transfer coefficients for burnable waste in municipal waste incinerators.
- p.35: Fig. 6.1 Transfer coefficients for burnable waste in municipal waste incinerators
- p.36: Tab. 6.3 Average municipal waste composition. Details see chapter 3.1 'Average Municipal Solid Waste' on page 26.
- p.37: Tab. 6.4 Various emissions to air from recent measurement reports in Swiss MSWIs (in mg/Nm flue gas, dioxins in
- p.38: Tab. 6.5 Various auxiliary material inputs to from recent measurement reports in MSWIs (in grams per kg waste
- p.40: Tab. 6.6 Oxygen demand for chemical elements as air emissions

Rules:
1. Choose the caption(s) that hold the unit-process inventory of this dataset — inputs, energy, emissions, transport — not impact results, not a diagram. Prefer "Sachbilanz" / "inventory" / "LCI" tables.
2. Return the PDF page range that covers those tables plus the paragraph introducing them: `first_page`, `last_page` (at most 4 pages). Tables can run onto the next page.
3. If no caption fits (the report does not document this dataset's inventory, or only as a result), return `found` = false and say why in `reason`.
4. `reason` names the caption(s) you chose and why.

Return only the JSON object described by the schema.
