You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process, from what the dataset says about itself.

The dataset `Polycarbonate, at plant` [RER], reference unit 1 kg, is shipped in the BAFU-2026 database as a system process: it has no production inputs, only ~152 cumulative elementary flows. No report in the documentation bundle prints its inventory, and no unit process of the same product was found to copy:

> 2007 - LCI packagings and graphical papers - Hischier.pdf: The cited report `2007 - LCI packagings and graphical papers - Hischier.pdf` is, in this documentation bundle, only the 17-page front matter of ecoinvent report No. 11 (cover, commissioners, author page, preface, acknowledgement, table of contents and one figure). Caption extraction over the whole file finds exactly one caption, 'Fig. 4.1 Decision criteria for packagings and instruments for their ecological evaluation' (p.12). Part II, the plastics part that holds this dataset's chapter, is not in the bundle. Per the rule that the cited report is not the only report that may document a dataset, all 114 bundled reports were converted 

What is left is the dataset's own ecoSpold metadata and its name. Often they name the inputs ("production by interfacial polycondensation out of phosgene and bisphenol A"), and the amounts then follow from chemistry.

## What the database says about the dataset

- name: Polycarbonate, at plant
- BAFU category: plastics / thermoplasts
- includedProcesses: Aggregated data for all processes from raw material extraction until delivery at plant
- technology: production by interfacial polycondesation out of phosgene and bisphenol A
- generalComment: Data are from the Eco-profiles of the European plastics industry (PlasticsEurope). Not included are the values reported for: recyclable wastes, amount of air / N2 / O2 consumed, unspecified metal emission to air and to water, mercaptan emission to air, unspecified CFC/HCFC emission to air, dioxin to water. The amount of "sulphur (bonded)" is assumed to be included into the amount of raw oil.;
UUID: 53117f8b-9311-37b3-bf5b-6e14b2ae711c

## Rules

1. List only inputs that the metadata or the name states. Each item quotes the exact phrase it comes from (`quote`) and names the field (`field`: name, technology, includedProcesses or generalComment). Never invent an input.
2. Give every item exactly one `basis` for its amount, per 1 kg of product:
   - `stoichiometry`: the named reaction fixes the amount. Write the balanced equation in `equation` with IUPAC standard atomic weights, and the per-unit arithmetic in `calculation` (e.g. "228.291 / 254.285 = 0.89777 kg per kg"). The value is the 100 %-yield floor; say so in `note`.
   - `mass-balance`: a chain-growth (addition) polymer carries its monomer unchanged, so 1 kg of polymer needs 1.000 kg of monomer (a loss can only raise it; say so in `note`). A physical blend adds up to 1 kg in the same way.
   - `composition-split`: the name or metadata states the components (a copolymer, a filled or blended grade) but not their shares. Give `amount` null; the shares are fitted under a mass constraint, which you state in `mass_sum` (usually 1.0 for a kilogram product).
   - `named-only`: the metadata names the input (an energy carrier, an auxiliary) but gives no amount. Give `amount` null; it is fitted.
   - `implied`: a reagent that the named process variant requires by definition, e.g. the alkali that neutralises the HCl of an *interfacial* polycondensation. Use this sparingly, with `confidence` low and the chemical reason in `note`.
3. Solvents, catalysts, yields or co-product credits that the metadata does not quantify are not guessed: name them in `gaps`.
4. `utility_block`: true if the product is a chemical made in a chemical plant and the metadata does not describe its utilities. The code then adds the standard block every ecoinvent-v2 organic chemical in BAFU-2026 carries (electricity, heat, rail and lorry transport of the precursors, a chemical-plant share) as free inputs to be fitted. Do not list those yourself.
5. If the metadata describes a multi-output process without an allocation (a steam cracker, a refinery slate), or names no input at all, return no items and explain in `gaps`: without a mass balance, a fitted input list would say nothing.
6. `search` is a 2-4 word phrase that finds the supplying dataset by name in an ecoinvent-2-style database (e.g. "bisphenol A powder", "phosgene liquid").

Return only the JSON object described by the schema.
