# Remaining BAFU biosphere review

After the twenty-four biosphere migration stages, the full `bw` check leaves **2,991 exchange occurrences across 155 name/category/unit signatures** unresolved. **290,756 of 293,747 biosphere exchanges link**. All 11,947 datasets and 420,063 inventory rows remain, and all technosphere exchanges link. This is a linking result, not evidence that every linked flow has LCIA factors.

The notebook regenerates `reports/generated/biosphere-unlinked.json` with occurrence counts, example consuming files, and diagnostic reasons. These counts follow the approved aggregation of 4,961 regional water emissions and 2,298 regional water withdrawals, whose original regions are retained on the exchanges. A further 1,959 approved industrial-area/intensive-forest aggregations retain original detailed labels.

## Decisions already made

Genuinely missing flows, including transport-noise indicators, remain unresolved pending a supported target. No separate biosphere database or placeholder flows are created. The notebook stops before dropping exchanges or writing an incomplete inventory during Run All.

Regional water aggregation uses reviewed existing targets and retains each stated region. The [water/context rules](bafu-2026-biosphere-water-context-migrations.md) additionally document well/fossil/process-water definitions and compartment corrections. Fossil-water status is retained in the `fossil well` target compartment. These rules do not treat water withdrawals as emissions or assign an unknown water origin to a particular source.

The [chemistry rules](bafu-2026-biosphere-chemistry-migrations.md) resolve 504 approved compound-resource conversions (TiO₂ → Ti, KCl → K, and barite → Ba), scaling amounts and uncertainty by documented elemental mass fractions, plus 37 supported chemical aliases. Original compound labels and conversion bases remain on the exchanges.

The [gas-unit rules](bafu-2026-biosphere-gas-unit-migrations.md) resolve all 363 reviewed natural-gas/mine-gas resource occurrences under the explicitly approved 1:1 unit-label assumption. Source reference conditions remain unknown. Original labels and the assumption are retained; all numeric and uncertainty fields are unchanged.

The [land/resource stage](bafu-2026-biosphere-land-resource-migrations.md) adds 910 links: 434 historical land renames, 103 approved rainforest and 279 approved organic-land aggregations, 89 graphite renames, one peat category correction, three European water aliases, and one explicitly identified helium-from-natural-gas resource. All original labels are retained.

The [follow-up stage](bafu-2026-biosphere-followup-migrations.md) adds 58 links: 8 approved Swiss rail aggregations with CH retained, 26 approved broader unspecified-land mappings with original used-land labels retained, 20 caesium spelling/unit corrections, one reviewed quicklime CO₂ classification, and three exact chlorophenol synonyms. Only the caesium rows are numerically rescaled (Bq → kBq).

The [compartment stage](bafu-2026-biosphere-compartment-migrations.md) adds 1,495 links: 138 landfill indicators receive their exact official category, 913 high-altitude emissions use approved generic-air targets, 132 further emissions use approved generic parent compartments (14 urban-air/surface-water/industrial-soil, 75 fossil-water suspended solids, 38 indoor TCDD, and five chemical aliases), 112 TOC rows use approved Organic carbon aggregates, and 200 long-term river rows use approved surface-water targets. All original compartments remain in audit metadata, with every numeric field unchanged. Generic LCIA does not automatically use retained altitude, indoor-exposure, aquifer, or long-term timing distinctions. The timing approximation can include the affected emissions in `no LT` methods. The two Organic carbon targets had no factors in the 668 installed method components checked.

The [source-review stage](bafu-2026-biosphere-source-review.md) adds 13 links: one CAS-specific Metam-sodium correction, six approved broader forest mappings, and six approved generic-water mappings that preserve the in-water/in-ground compartments. The original US potato inventory identifies the quantity as Metam-sodium active ingredient, resolving the XML’s conflicting dihydrate label without a mass conversion.

The [source-file stage](bafu-2026-biosphere-context-migrations.md) adds 15 links: 14 approved sealed-soil → railway-land proxies in seven identified railway datasets, plus one source-supported water return in the RER deionised-water inventory. All amounts and uncertainty values remain unchanged. Seven sealed-soil exchanges in plastics remain unresolved. Standard LCIA loses the sealing distinction for the railway proxies.

The [plastics source-review stage](bafu-2026-biosphere-plastics-source-review.md) adds four links from original EPS inventory evidence: calcium chloride → calcium and magnesium chloride → magnesium with chemical mass factors, plus one P-cyanophenol label restored to chromium VI in industrial soil, and one aminooxy-labelled row restored to PAH with an approved generic-soil target. The original industrial-soil compartment remains in PAH audit metadata. The source flow records resolve the chloride hydration/mass basis; only the two compound amounts and their uncertainty parameters are rescaled.

The [EPS metal stage](bafu-2026-biosphere-eps-metals.md) adds two links: PM10-labelled rows restored to source-identified palladium and rhodium. Their historical ecoinvent UUIDs persist under the current Palladium II and Rhodium III names. Exact source quantities distinguish these rows from the genuine PM10 row, which remains unresolved. All numerical fields and the original labels are retained.

The [plastics conversion stage](bafu-2026-biosphere-plastics-conversions.md) adds 32 links: 28 coal resources and one peat resource use original source-defined net calorific values to convert MJ to kg, and three approved EPS oxide emissions use contained-element As/Pb/Zn masses with existing metal-ion air targets. Original labels, energy or chemical conversion bases, and compartments are retained. Amounts and uncertainty scale together. Metal LCIA loses the oxide-form distinction, including Pb(IV) in lead dioxide.

The [plastics chemical-identity stage](bafu-2026-biosphere-plastics-chemicals.md) adds three links by restoring the source-defined 1,1,2-trichloroethane isomer in EPVC, SPVC and vinyl-chloride inventories. Source CAS, mass basis and generic-air compartment agree. All numerical fields and the original generic labels are retained.

The [historical-name stage](bafu-2026-biosphere-historical-names.md) adds 83 links: 82 using the explicit legacy dichlorobenzene correspondence in bw2io and ecoinvent’s 3.9 change report, and one exact 1-Methyl-2-pyrrolidinone → N-methyl-2-pyrrolidone synonym confirmed by NIST (CAS 872-50-4). The official 1,2-dichlorobenzene UUID remains under its o-Dichlorobenzene synonym in the installed 3.10 database. Original labels, compartments and all numerical fields remain unchanged.

The [approved NO₂ aggregation](bafu-2026-biosphere-nitrogen-dioxide-proposal.md) adds two links to the existing NOx-as-NO₂ air target. It retains both source records and all numerical fields, while accepting aggregate NOx characterization.

The [mosaic-land stage](bafu-2026-biosphere-land-mosaic.md) adds 18 source-confirmed links to heterogeneous agricultural land, including six transformation-to labels that lost the mosaic qualifier. All numerical fields and original labels remain unchanged.

The [approved carbon approximation](bafu-2026-biosphere-targeted-reassessment.md) adds 12 fossil CO₂/CO links in six diesel/demolition inventories, retaining all original labels and numerical fields.

The [approved uranium and wood conversions](bafu-2026-biosphere-targeted-reassessment.md#approved-uranium-and-wood-conversions) add nine links using explicit energy/density conventions. Amounts and uncertainty scale together, while original labels, source units, compartments and the conversion assumptions remain in metadata.

The [PM10 metal-pair stage](bafu-2026-biosphere-pm10-metals.md) adds 26 links in thirteen plastics inventories. Source-defined Pd/Rh pairs are restored with amounts and uncertainty unchanged; no ordinary particulate exchange is mapped to a metal by its name alone.

## Work still requiring evidence or a decision

| Group | Examples and current scope | Why it remains unresolved |
| --- | --- | --- |
| Other land descriptions | Urban, traffic, sealed-soil, and generic agricultural classifications | Do not infer a specific urban density, road/rail subtype, or agricultural class from a broader or ambiguous label. |
| Missing indicator types | 1,423 occurrences in `non-material`, chiefly transport noise; 13 in `economic` | No reviewed equivalent in biosphere 3.10. They are retained under the user's decision. |
| Remaining water labels | Wastewater labels and chemically polluted water | Each still needs a supported complete target signature and treatment of its source/compartment or wastewater definition. The approved broader process/cooling-water mappings do not authorize treating wastewater as an ordinary water emission. |
| Other compound or ore resources | Sodium bromide and bauxite | NaBr formula and in-ground extraction are now verified, but the bromine target is in water. Bauxite still lacks an aluminium grade. See the [resource follow-up](bafu-2026-biosphere-resource-followup.md). |
| Resource corrections | 363 occurrences covering gravel, sand, eight metals, and biomass energy | These are method-specific recycling adjustments; ordinary-resource mapping would extend their effect to other LCIA methods. See the [source-based review](bafu-2026-resource-correction-review.md). |
| Carbon origin | 7 generic CO₂ and 4 generic CO occurrences | The 12 approved diesel/demolition rows are linked. Remaining plastics, shale/cement and glass-wool inventories do not establish the carbon-origin split and are outside that approval. |
| Aggregates and mixtures | Generic rock, particulate aggregates, unspecified chemical mixtures | Composition or particle-size distribution is needed to choose or split targets. A CAS match alone is insufficient. |

Groups in this table are review topics, not a mutually exclusive partition of the remaining occurrences. Only the explicitly approved compartment aggregations have been applied; no general compartment fallback, fuzzy chemical match, or arbitrary oxidation state is used. Unsupported targets and uncertain meanings remain available for review.

The completed parent-compartment decisions are recorded in `reports/generated/biosphere-parent-compartment-review.json`; the five additional chemical-alias occurrences are applied and recorded in `biosphere-remaining-parent-alias-candidates.json`. The TOC and long-term decisions are in `biosphere-timing-and-toc-review.json`. Seven generic-air TOC exchanges remain unresolved because the available Organic carbon air target specifies urban air.

The 84 chemically polluted-water occurrences have now been checked against the original oil/gas extraction report, section 10.1.4: excess produced water is intentionally excluded from water-scarcity assessment. An ordinary Water target could introduce unintended freshwater credits. The one supported deionised-water correction does not generalize to these or the other 60 `Waste water/m3` rows. Evidence is recorded in `biosphere-context-evidence.json`.

## Reproducible remaining worklist

The notebook calls `audit_unlinked_biosphere(importer, BIOSPHERE, ROOT)` after the final migration. It writes `reports/generated/biosphere-remaining-worklist.json` and `.csv`, checks occurrence counts against the live importer, and records the final report and catalog hashes. Candidate searches use current names, official catalog synonyms, source CAS, and names used by other reviewed rules. They do not apply migrations.

Candidates still require scientific review. For example, the official catalog lists Metiram as a synonym of Zineb, but the source CAS (9006-42-2) differs from the Zineb target CAS (12122-67-7); this candidate is excluded. Other matches can hide isotope, hydration, carbon-origin, unit, or compartment differences. A mapping used for one source context does not authorize reuse elsewhere.

A source review of 189 resource/land occurrences is saved in `reports/generated/biosphere-remaining-resource-land-review.json`. Subsequent work resolved 12 approved forest/water mappings, 14 approved railway-land proxies, two source-verified chloride conversions, and 29 source-verified coal/peat conversions. The later mosaic-land review resolves 18 more. The approved uranium and wood conventions resolve nine more. **105 occurrences from that review remain unresolved.**

The seven sealed-soil plastics occurrences lack a railway basis. Other land labels do not establish more specific catalog classes, and the remaining oil-energy rows still lack a supported mass conversion. Uranium and wood now use the explicitly approved conventions, with unknown source factors/moisture retained as limitations. The [resource follow-up](bafu-2026-biosphere-resource-followup.md) records the original 32 resource occurrences (23 remain after uranium/wood) and resolves the ethylene peat conversion using 8.4 MJ/kg. The coal unit conflict is resolved: the misleading Radioactivity description points to a net-calorific-value property whose reference unit is MJ. Both versions of the source flow definitions specify the calorific values applied. The hydro-labelled EPS row originates from wave energy and must not silently inherit a hydropower-reservoir target.

A further [original-plastics chemical review](bafu-2026-biosphere-plastics-chemicals.md) traces 247 occurrences and checks 97 available primary flow definitions. Seven water rows labelled sodium chloride are actually unspecified inorganic salts; six generic-hydrocarbon rows and one EPVC isobutene row originate from an unspecified HFC mixture. These remain unresolved. A mercaptan source explicitly flags an identity conflict, and equal-quantity matches between different substances were rejected. This evidence is recorded in `biosphere-plastics-chemical-source-trace.json`.

The original [particle review](bafu-2026-biosphere-particle-review.md) checked 120 PM10-labeled rows. The later [PM10 metal restoration](bafu-2026-biosphere-pm10-metals.md) resolves 26 of those. Of the 94 remaining, 65 have a larger PM2.5 quantity in the same inventory and compartment, so blindly subtracting those amounts would create negative coarse particles. All 66 black/carbon-black rows coexist with other particulate emissions; no ordinary-particulate substitution is made. The cyclic PFC, kerosene and petrol emission targets remain absent.

The [remaining chemical-definition review](bafu-2026-biosphere-remaining-chemical-definitions.md) checks 23 further occurrences. Six pesticide air emissions belong to an aggregated EPS inventory and do not establish a rural receiving compartment. Two Azadirachtin A+B rows lack an A/B composition. Thirteen tributyltin-related rows need a supported target mass basis: the official target CAS and formula do not establish the same identity. Two EPS refrigerants lack matching targets. These remain unresolved.

## Candidate readiness

The September 22 [targeted reassessment](bafu-2026-biosphere-targeted-reassessment.md) supersedes the earlier conclusion that no further supported land correspondences could be found. Eighteen mosaic rules are applied and verified. Twelve diesel/demolition CO₂/CO rows now use the approved fossil-default approximation. Seven uranium and two wood conversions now use the approved 560,000 MJ/kg and 632.5 kg/m³ conventions, respectively, with the source-defined 14.7 MJ/kg step for EPS wood. The [PM10 pair restoration](bafu-2026-biosphere-pm10-metals.md) now links 26 source-defined metal rows using strictly checked identical pairs. Ninety-four generic-air PM10-labeled rows remain; no particle-size proxy is applied.

The current audit finds same-unit, same-compartment candidate targets for **15 unresolved signatures covering 294 occurrences**. Each is excluded by an existing source or meaning constraint: context-specific PM10/metal corrections and railway-land proxies cannot be reused in other inventories; wastewater is not established as ordinary water; resource-correction rows are method-specific accounting adjustments; carbon origin and particle fractions remain unknown; Metiram is not Zineb. Matching fields alone do not make these links ready to apply.

A separate comparison with the official 3.9 master detects 118 CAS-metadata differences from the installed catalog. Checking remaining BAFU CAS fields and reviewed original PlasticsEurope CAS fields against that master surfaces one additional same-compartment candidate: the EPS NO₂ row and the NOx target. The original source confirms NO₂. The user approved the [NOx aggregation for EPS and float-glass NO₂](bafu-2026-biosphere-nitrogen-dioxide-proposal.md); its two scoped rules are now applied by the notebook. Amounts and uncertainty remain unchanged, and original labels are retained. Standard LCIA loses the separate NO₂ characterization.

`reports/generated/biosphere-mapping-readiness-audit.json` records all 155 remaining signatures, the excluded candidates and the evidence needed to proceed. `biosphere-remaining-official-cas-review.json` records the master-data comparison. The lack of a current candidate does not prove that no future correspondence can be established. It means a new mapping still needs a source definition, a compatible target, or an explicit supported representation decision; it cannot be inferred from string similarity alone.

## Current worklist counts

These groups form a mutually exclusive partition generated by the live-importer audit. They describe why further review is needed; a candidate match does not prove equivalence.

| Review group | Occurrences |
| --- | ---: |
| missing indicator type | 1,436 |
| chemical identity or compartment review | 748 |
| method-specific recycling correction | 363 |
| wastewater composition or definition unresolved | 149 |
| particle size or aggregate definition unresolved | 108 |
| land class requires correspondence or more detail | 82 |
| unspecified radionuclide or emitter type | 71 |
| resource identity, basis, or compartment review | 23 |
| carbon origin unresolved | 11 |
| **Total** | **2,991** |
