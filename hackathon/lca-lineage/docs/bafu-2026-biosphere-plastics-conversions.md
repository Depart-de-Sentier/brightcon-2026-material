# Source-based plastics conversions

The [32 migration rules](../schemas/mappings/bafu-2026-biosphere-plastics-conversions.json) convert 28 coal and one peat resource exchanges from energy to mass and apply three approved EPS oxide-to-element mappings. Each rule selects its reviewed source filename, full name/category/unit signature, and original empty CAS. Raw and repaired XML files remain unchanged.

## Coal: source-defined energy-to-mass conversion

The 14 original PlasticsEurope inventories reference the same two ILCD elementary flows, even when their exchange descriptions omit the calorific value:

| Original flow | Flow UUID | Net calorific value | Target | kg per MJ |
| --- | --- | ---: | --- | ---: |
| Brown coal | `fe0acd60-3ddc-11dd-a6f9-0050c2490048` | 11.9 MJ/kg | Coal, brown | 1 / 11.9 |
| Hard coal | `fe0acd60-3ddc-11dd-a6fc-0050c2490048` | 26.3 MJ/kg | Coal, hard | 1 / 26.3 |

Both version 02.00.000 and version 03.00.000 flow definitions include these calorific values in their names. The version 3 XML has a misleading `Radioactivity` short description on its reference property. Following the referenced UUID resolves that conflict: [property `93a60a56-a3c8-11da-a746-0800200c9a66`](https://plasticseurope.lca-data.com/datasetdetail/flowproperty.xhtml?uuid=93a60a56-a3c8-11da-a746-0800200c9a66&version=03.00.000) defines **Net calorific value**, and its referenced unit group uses **MJ** as the reference unit. The version 2 short description already identifies net calorific value.

The targets are `Coal, brown / natural resource, in ground / kilogram` (`024c9722-1e88-412b-8c4b-10c532be8dca`) and `Coal, hard` in the same compartment and unit (`b6d0042d-0ef8-49ed-9162-a07ff1ccf750`). The conversion preserves the source-specific energy basis rather than substituting a generic coal heating value.

### Confirmed inventories

Every pair of coal quantities agrees with the original process to BAFU rounding precision. All 14 BAFU records cite the [2025 plastics report](../data/raw/BAFU-2026%20v1%20LCI%20Reports/2025%20-%20LCI%20plastics%20-%20Rajabihamedani.pdf). The original process versions are fixed in the evidence.

| BAFU inventory / source file | Original process | Version |
| --- | --- | --- |
| Polyvinylchloride, emulsion polymerised, at plant (`process_015cd7db-8a64-3f0b-ba15-6ff81e3d1eb4.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=090f9f55-f67e-9063-a5bf-000022b1107c&version=00.00) | 00.00 |
| Polystyrene, expandable, at plant (`process_05a10e4b-a919-33b6-b017-7c0bf7f7a7f9.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=b60b30bf-991d-41b8-a295-5d0b2e5f2bb5&version=09.00.000) | 09.00.000 |
| Polypropylene, granulate, at plant (`process_09cda8b1-b652-39b2-8761-c93aecc29f70.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=5070854e-e2fb-a816-c4ba-00000bb60d3d&version=00.00) | 00.00 |
| Ethylene, average, at plant (`process_298abdac-f564-358c-95a3-7a43418d2671.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=b748263b-2419-415b-98a1-cd78f7e6fc77&version=00.00.001) | 00.00.001 |
| Polyvinylchloride, suspension polymerised, at plant (`process_48985f3e-97b4-3128-a1a8-a5ba91a1cb88.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=113089b0-a343-c0d8-c684-000059d236c1&version=00.00) | 00.00 |
| Ethylene glycol, at plant (`process_582ad303-7f18-3110-83c2-bccca0dc995f.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=58aa0dd1-04b0-6918-96cc-000027963c0f&version=00.00.001) | 00.00.001 |
| Polyethylene, HDPE, granulate, at plant (`process_6738f024-eb64-3ef8-837e-05b84c6e43da.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=652939ff-9892-740d-68f7-0000208d2e34&version=00.00) | 00.00 |
| Vinyl chloride, at plant (`process_99a93e93-a8a8-34f3-88f3-6af0c21c4762.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=01ecbf06-8b73-1977-af65-00005296a89e&version=00.00) | 00.00 |
| Xylene, at plant (`process_a29aa0d5-9e37-34d7-8868-8a4fff95350a.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=f3ff31e4-9a54-4c5f-b148-1c1630d0ff17&version=00.00.001) | 00.00.001 |
| Purified terephthalic acid, at plant (`process_bfff239d-8ae3-3730-a048-dffb312515f3.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=5e3636e6-7674-48d7-a57d-ceb94c891e63&version=00.00.001) | 00.00.001 |
| Polyethylene, LDPE, granulate, at plant (`process_c4dbbb99-22d0-37c1-8cc7-fc5a8c64329b.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=7770c27b-648e-c089-58fb-00005d4910b8&version=00.00) | 00.00 |
| Polyethylene terephthalate, granulate, bottle grade, at plant (`process_c7af8832-9551-38fd-a628-363e6fc17c8e.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=d24d3589-f97b-404c-80af-ec4fd80ca9d9&version=00.00.001) | 00.00.001 |
| Pyrolysis gasoline, production mix, at plant (`process_dab0fa22-ba8d-34a9-b594-c980886b0b14.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=7bef11c6-93e6-4ff3-a423-00f3e500747d&version=00.00.001) | 00.00.001 |
| Polyethylene, LLDPE, granulate, at plant (`process_df878822-0deb-3a59-a6b4-396d94a3b654.xml`) | [PlasticsEurope](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=367fd8e9-fd6a-f5f1-6fab-0000626e5b98&version=00.00) | 00.00 |

EPS hard coal is the documented exception to direct numerical equality: the report already applied a factor of 0.06 to the original 1.51979282961504 MJ, producing the BAFU value 0.091188 MJ. The migration converts that **existing BAFU value** by 1 / 26.3. It neither repeats nor undoes the report’s correction. EPS brown coal remains the BAFU value 0.7134 MJ before its 1 / 11.9 conversion.

The original name, categories and MJ unit remain in `bafu original biosphere`. `bafu energy conversion` records the net calorific value and source flow UUID. The helper checks that the multiplier equals its reciprocal and restricts this metadata to source-file-specific MJ → kg conversions from in-ground resources. Coal retains its category; only the identified peat flow may use the catalog’s biotic category.

## Peat: one further source-defined conversion

Ethylene file `process_298abdac-f564-358c-95a3-7a43418d2671.xml` has one `Energy, from peat` row, 0.000018403 MJ. Original process exchange 94 references ILCD flow `e2fba107-6555-11dd-ad8b-0800200c9a66`, which specifies **8.4 MJ/kg**. Dividing by 8.4 gives 0.0000021908333333333333 kg, linked to `Peat / natural resource, biotic / kilogram` (`c5035ce2-5ee5-431f-a287-4b25da42be74`). The original in-ground category is retained in metadata. This uses the same catalog classification as the earlier peat mass correction.

The [resource follow-up](bafu-2026-biosphere-resource-followup.md) explains the source-property identifier conflict and its resolution using the JRC reference property, the stated 8.4 MJ/kg value, and the separate source mass property of 1/8.4. Source XML and hashes are included in the conversion evidence.

## Approved oxide-to-element air mappings

The original EPS process and referenced elementary-flow definitions identify these compounds on a Mass basis. Source CAS identifiers and formulas agree with [arsenic trioxide](https://pubchem.ncbi.nlm.nih.gov/compound/14888), [lead dioxide](https://pubchem.ncbi.nlm.nih.gov/compound/14793), and [zinc oxide](https://pubchem.ncbi.nlm.nih.gov/compound/zinc-oxide). Atomic weights use the [CIAAW abridged table](https://ciaaw.org/abridged-atomic-weights.htm): As 74.922, Pb 207.2, Zn 65.38 and O 15.999.

| Original label / formula | CAS in original flow | Target | kg element per kg compound | Target UUID |
| --- | --- | --- | ---: | --- |
| Arsenic trioxide / As2O3 | 001327-53-3 | Arsenic ion | 0.757396090800188 | `dc6dbdaa-9f13-43a8-8af5-6603688c6ad0` |
| Lead dioxide / PbO2 | 001309-60-0 | Lead II | 0.866227978494803 | `8e123669-94d3-41d8-9480-a79211fe7c43` |
| Zinc oxide / ZnO | 001314-13-2 | Zinc II | 0.803401368903526 | `5ce378a0-b48d-471c-977d-79681521efde` |

The factors are 2As/(2As + 3O), Pb/(Pb + 2O), and Zn/(Zn + O). All three targets retain the generic-air compartment and kilogram unit. The rules apply only to EPS file `process_05a10e4b-a919-33b6-b017-7c0bf7f7a7f9.xml`.

The user approved using contained-element masses with the existing metal-ion targets. **LCIA loses the oxide-form distinction, including Pb(IV) in lead dioxide.** These are documented representation choices, not evidence of a chemical transformation or measured ionic speciation. The full original names remain in `bafu original biosphere`; `bafu elemental conversion` retains formula, target element and atomic weights. The original missing BAFU CAS fields are unchanged. No separate oxygen emission is added.

The EPS `Tin oxide` row remains unresolved. Its source CAS is 1332-29-2 and the available record does not establish a unique formula or tin mass fraction; the script does not assume SnO or SnO₂.

## Uncertainty and validation

bw2io scales each amount and its uncertainty together. These 32 source exchanges use lognormal uncertainty: `loc` shifts by ln(factor), `scale` is preserved, and any bounds scale with the amount. Reapplication does not convert them twice. Other exchange fields, comments, existing links, and all other records are preserved.

The full `bw` check passed: **32 new links**, **290,603 linked of 293,747 biosphere exchanges**, and **3,144 unresolved occurrences across 165 signatures**. All 11,947 datasets and 420,063 exchange rows remain, with every technosphere exchange linked. The 25 regression tests pass. No inventory database was written. Verification is recorded in `reports/generated/biosphere-plastics-conversions-migration-check.json`. It independently checks all three calorific values and the three elemental fractions, target UUIDs and uniqueness, the complete before/after records, one hit per rule, uncertainty, repeat application and live-audit consistency. The notebook’s optional drop/write/LCA cells are excluded.

Source rows, original process/flow versions, URLs and SHA-256 hashes are recorded in `reports/generated/biosphere-plastics-conversions-evidence.json`. The coal trace is also in `biosphere-coal-source-review.json`; downloaded primary XML is cached under `plasticseurope-source-review/`.

This stage writes `biosphere-unlinked-after-plastics-conversions.json`; the previous EPS metal stage writes `biosphere-unlinked-after-eps-metals.json`. The subsequent chemical-identity and [historical-name stages](bafu-2026-biosphere-historical-names.md) continue linking before the final report.
