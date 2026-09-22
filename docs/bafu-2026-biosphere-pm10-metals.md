# PM10 review and restoration of mislabeled metal pairs

The [26 migration rules](../schemas/mappings/bafu-2026-biosphere-pm10-metals.json) resolve 26 of the 120 remaining `Particulates, < 10 um / air / kilogram` exchanges. Original PlasticsEurope inventories identify them as **13 palladium emissions and 13 rhodium emissions**, not particulate-size aggregates. The remaining **94 PM10-labeled exchanges** are retained for size-distribution review.

## Source identities

The affected inventories are LDPE, HDPE, LLDPE, polypropylene, emulsion PVC, suspension PVC, vinyl chloride, ethylene, ethylene glycol, PET, pyrolysis gasoline, purified terephthalic acid and xylenes. Each original process contains one palladium and one rhodium air emission at the same mass. Each corresponding BAFU process contains two PM10-labeled rows at that exact mass, plus a different PM10 quantity. Original flow definitions specify emission to unspecified air and Mass as the reference property.

| Original flow | Version | Source UUID |
| --- | --- | --- |
| [Palladium](https://plasticseurope.lca-data.com/resource/flows/0256ad73-24bd-ddec-3550-00003f819e00?format=xml&version=01.00.000) | 01.00.000 | `0256ad73-24bd-ddec-3550-00003f819e00` |
| [Rhodium](https://plasticseurope.lca-data.com/resource/flows/53a501f6-de14-0035-1899-000075b1bc20?format=xml&version=01.00.000) | 01.00.000 | `53a501f6-de14-0035-1899-000075b1bc20` |
| [palladium](https://plasticseurope.lca-data.com/resource/flows/08a91e70-3ddc-11dd-a056-0050c2490048?format=xml&version=03.00.000) | 03.00.000 | `08a91e70-3ddc-11dd-a056-0050c2490048` |
| [rhodium](https://plasticseurope.lca-data.com/resource/flows/fe0acd60-3ddc-11dd-abb5-0050c2490048?format=xml&version=03.00.000) | 03.00.000 | `fe0acd60-3ddc-11dd-abb5-0050c2490048` |

As in the [earlier EPS correction](bafu-2026-biosphere-eps-metals.md), the historical generic-metal UUIDs persist in biosphere 3.10 as `Palladium II / air / kilogram` (`51377cff-3c04-5717-8961-6819901a3e90`) and `Rhodium III / air / kilogram` (`7c651713-83f5-56e1-a67f-37b828684f3d`). This follows catalog continuity; it does not infer measured oxidation states. No metal mass conversion is applied.

`reports/generated/biosphere-pm10-metals-evidence.json` records all thirteen source processes, exact quantities, original flow UUIDs and versions, neighboring source records, both exported records, target UUIDs and artifact hashes.

## Safe handling of identical pairs

The two exported records differ only in their repaired XML exchange numbers. Brightway's `clean_integer_codes` strategy removes those numbers; at migration time the two full exchange dictionaries are identical, including amounts, uncertainty and comments. The evidence supports restoring the pair as one palladium and one rhodium quantity. It does not establish a distinct individual-row ancestry within that identical pair.

The helper requires the exact filename, complete signature and exact amount, then checks that **exactly two identical, unlinked records** are present. Two temporary `_migration_pair_member` values let standard bw2io migration rules assign one target to each record. Missing, additional, nonidentical, already-linked or partially migrated source pairs raise an error before mutation. An already completed pair is accepted on repeat application. Ordinary amount-scoped rules still reject duplicate matches.

Only names, `bafu original biosphere` metadata and input links change. All numerical fields, units, compartments, original CAS and comments remain unchanged. Temporary matching fields are removed, including on migration failure. All other records, including the distinct PM10 quantity in each of the thirteen inventories, are unchanged.

## Remaining PM10-labeled records

Biosphere 3.10 has generic-air flows for `<2.5 µm`, `2.5–10 µm` and `>10 µm`, but no combined PM10 target. The [ecoinvent guidelines](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Database/Fundamentals/dataqualityguideline_ecoinvent_3_20130506.pdf), section 5.9.4 and Table 5.3, distinguish PM10 from the coarse fraction and prioritize source-specific size distributions. They do not give one universal PM10 split.

| Source group | Remaining PM10-labeled rows |
| --- | ---: |
| Other aggregate/construction inventories | 54 |
| PlasticsEurope aggregate inventories | 14 |
| Asphalt Calculator | 12 |
| Steel/iron and reinforcing-steel reports | 12 |
| Power-to-X report | 2 |
| **Total** | **94** |

In **65 of the 94 rows**, the same source inventory and compartment have more reported PM2.5 than PM10. Subtraction would give a negative coarse fraction. Even where the result would be positive, aggregate size rows are not established as overlapping measurements of one common total.

The [2021 steel report](../data/raw/BAFU-2026%20v1%20LCI%20Reports/2021%20-%20LCI%20steel%20and%20iron%20processes%20-%20Zschokke.pdf), Table 12 (page 38), labels the converter/slag quantities as PM10 but describes them as dust without PM10/PM2.5 information. Table 16 (page 46) also calls the EAF PM10 row dust. These tables do not support reinterpreting all of those quantities as the 2.5–10 µm fraction. No particle-size proxy or subtraction has been applied. The complete remaining review is `reports/generated/biosphere-pm10-remaining-review.json`.

## Verification

The `bw` full import check passed: **26 new links**, **290,756 linked biosphere exchanges**, **2,991 unresolved across 155 signatures**, and **94 remaining in the generic-air PM10 signature**. All 11,947 datasets and 420,063 exchange rows remain, and all technosphere exchanges link. Full-record comparison verifies that only declared replacements occurred; a second application changes nothing. All **32 helper regression tests** pass. No inventory database was written.

The notebook applies this stage after the wood conversion. Wood writes `biosphere-unlinked-after-wood-density.json`; this stage writes the final `biosphere-unlinked.json`. Check results and full before/after records are in `reports/generated/biosphere-pm10-metals-migration-check.json`.

```sh
conda run -n bw python "scripts/ecospold importer/check_land_mosaic.py"
```
