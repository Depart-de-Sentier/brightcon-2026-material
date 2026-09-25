# Chemical identities in the original plastics inventories

The [three migration rules](../schemas/mappings/bafu-2026-biosphere-plastics-chemicals.json) restore the source-defined **1,1,2-trichloroethane** identity in three inventories. BAFU shortened their names to `Trichloroethane`, leaving the isomer unspecified and preventing an exact link.

## Applied corrections

The original process records all reference [ILCD flow `08a91e70-3ddc-11dd-9304-0050c2490048`, version 02.00.000](https://plasticseurope.lca-data.com/resource/flows/08a91e70-3ddc-11dd-9304-0050c2490048?format=xml&version=02.00.000). Its name is 1,1,2-trichloroethane, CAS **79-00-5**, with a Mass reference property and unspecified-air compartment. These independent identity, unit and compartment checks agree with the source process labels and quantities.

| BAFU inventory / filename | Original process / exchange | Amount, kg |
| --- | --- | ---: |
| Emulsion PVC — `process_015cd7db-8a64-3f0b-ba15-6ff81e3d1eb4.xml` | [EPVC](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=090f9f55-f67e-9063-a5bf-000022b1107c&version=00.00), row 202 | 1.4351e-8 |
| Suspension PVC — `process_48985f3e-97b4-3128-a1a8-a5ba91a1cb88.xml` | [SPVC](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=113089b0-a343-c0d8-c684-000059d236c1&version=00.00), row 203 | 1.6717e-9 |
| Vinyl chloride — `process_99a93e93-a8a8-34f3-88f3-6af0c21c4762.xml` | [VCM](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=01ecbf06-8b73-1977-af65-00005296a89e&version=00.00), row 202 | 3.7281e-9 |

Each BAFU amount equals its source amount. The target is `1,1,2-Trichloroethane / air / kilogram`, UUID **`b32061b1-8d24-4663-b10d-0a1c705f2937`**. This restores an identified isomer; it does not approximate a mixture or substitute the 1,1,1 isomer.

The rules select the source filename, complete original flow signature and missing BAFU CAS. They retain the original label in `bafu original biosphere`. Amounts, uncertainty parameters, units, compartments, comments and original CAS fields remain unchanged. Raw and repaired XML remain unchanged.

## Why the other apparent matches were rejected

The review compared **247 remaining chemical occurrences** in the 14 cached original plastics inventories. Quantity matching nominated source rows for inspection; it did not establish identity by itself. The 98 referenced flow/version pairs yielded **97 primary flow definitions**. One historical tributyltin version returned HTTP 404 on both the PlasticsEurope and JRC servers; no other version was substituted.

The following findings prevent unsupported mappings:

| BAFU label and scope | Original evidence | Decision |
| --- | --- | --- |
| `Sodium chloride / water`, seven older plastics rows | All seven reference [Salts, inorganic](https://plasticseurope.lca-data.com/resource/flows/14ad538b-9aec-5c2b-a1af-000049991c5e?format=xml&version=01.00.000), with no stated composition. | Do not assume NaCl or split the amounts into sodium and chloride. |
| `Hydrocarbons, unspecified / air`, six rows, and one `Isobutene / air` row in EPVC | These reference [Hydrocarbons, fluorinated (HFC)](https://plasticseurope.lca-data.com/resource/flows/377cc135-6601-a1d6-a032-000058f46dc0?format=xml&version=01.00.000), an unspecified mixture. | Neither an ordinary hydrocarbon target nor an individual HFC is supported. The EPVC finding does not apply to the other, correctly identified isobutene rows. |
| `Methyl mercaptan / air`, EPS | The [original mercaptan flow](https://eplca.jrc.ec.europa.eu/SDPDB/datasetdetail/elementaryFlow.xhtml?uuid=08a91e70-3ddc-11dd-9343-0050c2490048&version=03.00.000) gives ethanethiol CAS 75-08-1 and synonyms, but explicitly flags the name/CAS correspondence as potentially wrong. BAFU specifies methyl mercaptan. | Keep unresolved until the identity conflict is resolved. The CAS identifies [ethanethiol](https://webbook.nist.gov/cgi/cbook.cgi?ID=C75081), but that alone does not prove which mercaptan the inventory represents. |
| `Methane, monochloro-, R-40 / water`, SPVC | R-40 and chloroethane each occur at 3.4656e-10 kg in both original and BAFU inventories. | The available monochloroethane target belongs to the separate chloroethane row. Do not use the numerical coincidence to change R-40's identity. |
| `Biphenyl / air`, PET | Biphenyl and phenanthrene each occur at 7.6522e-20 kg in both original and BAFU inventories. | The phenanthrene row is separate. Do not link biphenyl to phenanthrene because their amounts coincide. |
| `4,4'-Biphenol / air`, seven rows | Original biphenol quantities coincide with phenanthrene and sometimes fluorene quantities. | No substitution to those other substances is supported. |

The other reviewed source definitions did not establish additional exact substance/unit/compartment targets. Broader or different compartments, unspecified mixtures and unresolved identity conflicts remain unlinked under the existing decision to retain unsupported flows.

## Evidence and verification

`reports/generated/biosphere-plastics-chemical-source-trace.json` records all 247 reviewed occurrences, original flow UUIDs/versions, CAS candidates, source warnings, decisions, downloaded URLs and SHA-256 hashes. `biosphere-plastics-chemicals-evidence.json` records the three applied rules and their source rows.

The notebook runs these corrections after the plastics conversions. The preceding stage writes `biosphere-unlinked-after-plastics-conversions.json`; this stage writes `biosphere-unlinked-after-plastics-chemicals.json`. The subsequent [historical-name stage](bafu-2026-biosphere-historical-names.md) writes the final report and regenerates the remaining worklist. The full verification is recorded in `biosphere-plastics-chemicals-migration-check.json` and excludes the optional drop/write/LCA cells.

The full `bw` check passed: **3 new links**, **290,606 linked of 293,747 biosphere exchanges**, and **3,141 unresolved across 164 signatures**. All 11,947 datasets and 420,063 exchange rows remain, and all technosphere exchanges link. Complete-record checks allow only the declared names, audit metadata and links to change; all numerical fields are preserved. Each rule has one hit, repeated application is unchanged, the live audit agrees, and no inventory database was written.
