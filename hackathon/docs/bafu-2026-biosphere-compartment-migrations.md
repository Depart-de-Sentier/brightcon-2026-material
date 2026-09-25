# BAFU 2026 compartment mappings

The [compartment migration](../schemas/mappings/bafu-2026-biosphere-compartments.json) contains 32 full-signature rules and follows the reviewed follow-up stage. It preserves all amounts, signs, units, uncertainty fields, CAS metadata, and comments. Every affected exchange retains its incoming name, complete category, and unit in `bafu original biosphere`.

## Exact landfill indicators

Two rules correct 138 exchanges from `natural resource / in ground` to `inventory indicator / waste`, keeping their names unchanged:

| Indicator | Occurrences | Existing biosphere 3.10 UUID |
| --- | ---: | --- |
| Waste mass, total, placed in landfill | 72 | `6bc06a91-ae35-4a2b-ab39-da4dd36b621a` |
| Organic carbon, placed in landfill | 66 | `4044e84c-26c5-4cef-b76c-8c660d60bcfe` |

The [ecoinvent 3.9 change report, section 10.1.5](https://support.ecoinvent.org/hubfs/Change-Report-v3.9.pdf?hsLang=en) defines these two exchanges as ecological-scarcity inventory indicators. Waste mass is the wet mass deposited in a landfill; organic carbon is the mass of organic carbon deposited. The official 3.9 master data bundled with bw2io uses the same UUIDs, kilogram units, and indicator compartment as the installed 3.10 database. Its definitions restrict these indicators to ecological-scarcity use.

BAFU's actual source comments agree. For example, `process_fabc49d1-577c-4234-910a-2e0f40e84ba5.xml` (gravel disposal to construction-waste landfill) explicitly identifies both quantities as landfill indicators for ecological-scarcity LCIA. Its rows contain 1 kg waste and 0.00029165 kg organic carbon. All 138 source rows use the incorrect resource compartment and have nonnegative amounts.

The helper permits this change of main compartment only for the two exact source signatures, with original metadata retained and without renaming or rescaling. Tests reject other resources, source categories, target indicator categories, changed units, or missing audit metadata. These rules do not map recycling corrections to ordinary resources.

A read-only check of the installed `Ecological Scarcity 2021` methods found 24 UBP/kg for waste mass and 6,200 UBP/kg for organic carbon in the total and non-radioactive waste-disposal indicators, including their `no LT` versions. The check is saved as `reports/generated/biosphere-landfill-indicator-factors.json`. No LCIA method was edited.

## Approved generic-air targets

The user explicitly approved linking 913 high-altitude emissions to generic air, retaining their original altitude compartment. Nine full-signature rules change `air / lower stratosphere + upper troposphere` to `air`:

| Incoming substance | Occurrences | Generic-air target name |
| --- | ---: | --- |
| Benzene | 116 | Benzene |
| Butadiene | 116 | Butadiene |
| Formaldehyde | 116 | Formaldehyde |
| Heat, waste | 116 | Heat, waste |
| Dinitrogen monoxide | 93 | Dinitrogen monoxide |
| Ethylene oxide | 93 | Ethylene oxide |
| Hydrogen chloride | 93 | Hydrochloric acid |
| Methane, fossil | 93 | Methane, fossil |
| Ethene | 77 | Ethylene |

Every target has the same unit and a unique complete name/category/unit signature. For all eight chemical substances, every stated source CAS agrees with the target after removing leading zero padding. Waste heat has no CAS. The two changed names are synonyms of the same compounds; neither requires a chemical mass conversion.

**This is an approved compartment approximation.** Standard LCIA uses generic-air factors and does not automatically read the retained altitude metadata. Original source comments, uncertainty, and any stated CAS remain unchanged. Existing links to supported altitude-specific targets are outside these rules.

The [ecoinvent 3.10 change report, section 2.2.3](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Database/Releases/Change%20Report%20v3.10%20-%2020231214.pdf) explains that some unused or inappropriate altitude flows were deleted and certain incorrectly classified datasets were changed to unspecified air. That catalog cleanup does not prove the BAFU source categories are erroneous: some affected BAFU rows are explicitly in aircraft operations, while others appear in aggregated inventories. These mappings rely on the user's approval of generic characterization, rather than claiming a source-error correction.

## Other approved parent-compartment targets

The user separately approved these ten rules for 127 occurrences, preserving every original category in audit metadata:

| Source compartment and substances | Generic target compartment | Occurrences |
| --- | --- | ---: |
| Urban air: anthracene and naphthalene | Air | 8 |
| Industrial soil: chlorine, nitrate, sulfate | Soil | 3 |
| Surface water: fipronil, mancozeb, sulfur trioxide | Water | 3 |
| Fossil water: suspended solids, unspecified | Water | 75 |
| Indoor air: 2,3,7,8-tetrachlorodibenzo-p-dioxin (TCDD) | Air | 38 |

Names stay unchanged except TCDD, which uses the existing target `Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin`. All 38 source rows state CAS 1746-01-6, agreeing with the target. Pure TCDD has an equivalency factor of one relative to the TCDD reference, as defined in [EPA's toxicity equivalence guidance](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1009HJ9.TXT); no mixture composition or conversion factor is inferred. The other nine signatures keep their exact chemical/aggregate names. Every rule preserves the kilogram unit and all numerical/uncertainty fields.

These are explicit approximations, not evidence that the source categories were erroneous. Generic-air factors may not represent indoor exposure, generic-water factors no longer distinguish the fossil aquifer, and parent compartments omit urban density or specific water/soil classes. Retained metadata does not change standard LCIA characterization automatically. `reports/generated/biosphere-parent-compartment-review.json` records each approved source and target.

Three additional rules apply the same approved surface-to-generic-water approach to five occurrences: `Benzene, hexachloro-` → `Hexachlorobenzene` (2), `Benzene, pentachloro-` → `Pentachlorobenzene` (2), and `Hydrogen chloride` → `Hydrochloric acid` (1). Chemical aliases are supported by [NIST's hexachlorobenzene record](https://webbook.nist.gov/cgi/cbook.cgi?ID=C118741), [NIST's pentachlorobenzene record](https://webbook.nist.gov/cgi/cbook.cgi?ID=608-93-5), and the official catalog's HCl formula and synonym. Missing source CAS values stay missing. All original names and compartments are retained.

## Approved TOC aggregate mappings

Two rules map 112 `TOC, Total Organic Carbon` exchanges to `Organic carbon` without changing their compartments or kilogram units:

| Compartment | Occurrences | Existing biosphere 3.10 UUID |
| --- | ---: | --- |
| Air / urban air close to ground | 57 | `d7a10d03-8f76-4b5f-8dd5-5b0f827568fc` |
| Soil / unspecified | 55 | `e61443a5-41b6-4407-a1cd-116bdfb38a67` |

These are user-approved aggregate mappings. The catalog supplies little definition beyond name, unit, and compartment; this is not a claim of a documented historical rename. The original TOC labels remain in `bafu original biosphere`. A check of all 668 installed LCIA method components found no factors for either target (`reports/generated/biosphere-organic-carbon-factor-review.json`), so linking these flows does not itself add characterized impacts. Seven generic-air TOC occurrences remain unresolved because there is no corresponding generic-air Organic carbon target.

## Approved long-term river mappings

The user approved six rules for 200 `water / river, long-term` occurrences. Each uses an existing **surface-water** target, preserving the river receiving environment while omitting the unsupported timing distinction:

| Incoming name | Occurrences | Surface-water target | Target UUID |
| --- | ---: | --- | --- |
| Benzene, chloro- | 105 | Monochlorobenzene | `e38eb567-b080-4f80-894c-f6984eec5119` |
| Chloride | 91 | Chloride | `5e050fab-1837-4c42-b597-ed2f376f768f` |
| Dioxin, 2,3,7,8 Tetrachlorodibenzo-p- | 1 | Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin | `d1d77d54-e19f-4c3d-8fdc-389f78e72515` |
| Ethene, chloro- | 1 | Vinyl chloride | `cfe43cd8-3356-4d29-bb02-5b9c9ede0aec` |
| Methane, tetrachloro-, CFC-10 | 1 | Carbon tetrachloride | `4d93311d-5fc2-4f86-ab4f-b223ee9350e5` |
| Silver | 1 | Silver I | `af9793ba-25a1-4928-a14a-4bcf7d5bd3f7` |

Every exchange retains the complete original `['water', 'river, long-term']` category, name, and kilogram unit in `bafu original biosphere`. Amounts, signs, uncertainty, comments, and source CAS values stay unchanged. **Standard LCIA does not read this timing metadata: these emissions can now contribute to methods labelled `no LT`.** This is an explicitly approved timing approximation. The blank historical long-term correspondence destinations do not establish that the source timing was wrong.

The chemical renames follow the reviewed catalog aliases. The Silver target's official 3.9 UUID record lists `Silver` and `Silver ion` as synonyms of `Silver I`, matching the convention already used for 229 ordinary surface-water occurrences in the [catalog stage](bafu-2026-biosphere-catalog-migrations.md). This follows the catalog's historical naming convention and does not assert measured source speciation. The explicitly named TCDD uses the reference substance's equivalency factor of one. Missing source CAS values are not filled in.

`reports/generated/biosphere-timing-and-toc-review.json` records these eight approved rules, targets, counts, source examples, and limitations.

## Verification and local evidence

`reports/generated/biosphere-compartment-evidence.json` records targets, source examples, counts, and definitions. The altitude review is `biosphere-altitude-review.json`. The full check is `biosphere-compartment-migration-check.json`. The preceding unresolved report is `biosphere-unlinked-after-followup.json`; this stage writes `biosphere-unlinked-after-compartments.json`, followed by the [source-review stage](bafu-2026-biosphere-source-review.md).

At this stage, the full `bw` check resolved **1,495 additional occurrences**, yielding **290,537 linked biosphere exchanges** and **3,210 unresolved across 180 signatures**. All 11,947 datasets and 420,063 exchange rows remained. Independent complete-record comparison verified only declared name/category/metadata changes and unique links, with every numerical and uncertainty field unchanged. Existing links and all non-biosphere records were unchanged; reapplication was idempotent. All eight migration guard tests passed. No inventory database or LCIA method was written.

The notebook also regenerates `biosphere-remaining-worklist.json` and `.csv` from the live importer and current target database. The audit requires its counts to match the final unresolved report and records catalog/report hashes. Candidate names, synonyms, and CAS matches are review leads only; the audit applies no mappings. Complete-record comparison also checks that generating the worklist leaves the importer unchanged.
