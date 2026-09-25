# Remaining chemical definitions and compartments

This review covers **23 unresolved occurrences across 12 signatures**. None has a sufficiently supported new mapping. At the time of this review, the full import result was **3,056 unresolved occurrences across 160 signatures**. This chemical review changes neither migrations nor inventory data; see the [current worklist](bafu-2026-biosphere-unresolved-review.md) for later land corrections.

## Six EPS pesticide air emissions

Atrazine, Dicamba, Dimethenamid, Glyphosate, Methomyl and Trifluralin each occur once in the generic-air compartment of `process_05a10e4b-a919-33b6-b017-7c0bf7f7a7f9.xml`. Existing same-substance air targets require `non-urban air or from high stacks`.

The source is the **aggregated EPS inventory**, including upstream processes, rather than an identified field application. Its production geography covers multiple European plants and does not identify the receiving air compartments of these upstream emissions. The original PlasticsEurope flow definitions also specify unspecified air. A pesticide name alone does not establish where its emission occurred. These six rows therefore remain unresolved; they are not moved to agricultural soil or assigned rural air.

## Two Azadirachtin A+B soil emissions

The two heated-greenhouse tomato inventories (`process_3c0a4398-92c4-3e59-8b1d-f9a871df2f89.xml` and `process_0d370e65-6c9a-3855-a715-953b8cab2e75.xml`) each contain **1.933 × 10⁻⁷ kg** of `Azadirachtin A+B` to agricultural soil, without a usable CAS identifier.

The [2021 source report](../data/raw/BAFU-2026%20v1%20LCI%20Reports/2021%20-%20LCA%20tomatoes%20and%20green%20beans%20production%20-%20Kaegi.pdf), Table 14 and the inventory appendices, calls this `Azadirachtin`, with 0.06 kg/ha and 1.93 × 10⁻⁷ kg/kg tomato respectively. This confirms the inventory row but does not specify an A/B composition or a mass basis expressed as A.

The installed target (`49cf6a32-97db-5cf4-b1d6-47ea6fd1e4c8`) has CAS **11141-17-6**, formula C35H44O16. [PubChem identifies this as azadirachtin A](https://pubchem.ncbi.nlm.nih.gov/compound/5281303); [azadirachtin B](https://pubchem.ncbi.nlm.nih.gov/compound/21725521) has a different formula, C33H42O14. Treating the A+B mass as pure A would require an additional composition or proxy assumption. The shorter report label alone does not resolve the explicit A+B wording in the XML.

## Thirteen tributyltin-related water emissions

Eight rows are labelled `Tributylstannane` (seven generic water, one surface water), and five are `Tributyltin oxide` to surface water. The installed `Tributyltin compounds` targets have no CAS number or explanatory metadata.

The official ecoinvent 3.9 master lists these same target UUIDs with **CAS 56573-85-4 and formula C12H28Sn**. These fields do not establish a unique matching source substance: the [EPA substance registry](https://cdxapps.epa.gov/oms-substance-registry-services/substance-details/307447) describes that CAS as a tributyltin chloride complex with unspecified formula, while [PubChem's tributylstannane](https://pubchem.ncbi.nlm.nih.gov/compound/5948) has formula C12H28Sn and CAS **688-73-3**. The target metadata therefore cannot be treated as an unambiguous chemical identity.

The original PET freshwater row explicitly uses CAS 688-73-3 on a mass basis. The other seven tributylstannane rows reference a version 2 elementary flow whose definition was unavailable in the source review. All five oxide rows explicitly use CAS **56-35-9**, also on a mass basis. None establishes that its quantity is measured on the same basis as the target aggregate.

[WHO/IPCS's tributyltin review](https://www.inchem.org/documents/ehc/ehc/ehc116.htm) distinguishes measurements expressed as tin, TBT, chloride and oxide. Those masses are not interchangeable. A target definition or authoritative correspondence specifying the mass basis is needed before choosing 1:1 aggregation or a chemical conversion. No factor is inferred from the word “compounds” or from the target formula alone.

## Two EPS refrigerants

The original HFC-245fa flow identifies CAS **460-73-1**. The original HFC-143 flow identifies CAS **430-66-0**, but also flags its CAS/name correspondence for verification. Neither source CAS has an existing same-compartment, same-unit target in the installed biosphere. No other HFC is substituted on the basis of a similar name.

## Evidence

`reports/generated/biosphere-remaining-chemical-definitions-review.json` records every reviewed signature and source file, the original PlasticsEurope definitions, installed target metadata, official master records, external reference URLs and file hashes. It checks that the 23 occurrences are still present in the latest worklist. This is a review artifact, not an executable migration.
