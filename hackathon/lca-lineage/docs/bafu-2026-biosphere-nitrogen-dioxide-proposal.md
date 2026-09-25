# Approved NO₂-to-NOx aggregation

**User approved: “Use documented NOx aggregation; retain originals.”** The [active migration](../schemas/mappings/bafu-2026-biosphere-nitrogen-dioxide.json) links two source-file-specific NO₂ emissions to `Nitrogen oxides / air / kilogram`, UUID `c1b91234-6f24-417b-8309-46111d09c457`.

| Source | Original label | Amount retained |
| --- | --- | ---: |
| Float glass, `process_f14cf204-38f4-3670-ad3e-bffb9d82762a.xml` | Nitrogen dioxide | 0.000222 kg |
| EPS, `process_05a10e4b-a919-33b6-b017-7c0bf7f7a7f9.xml` | Nitrogen dioxide, RAF | 0.0033963 kg |

The target uses the conventional **NOx expressed as NO₂** mass basis, so these already-NO₂ quantities use a 1:1 mapping. The [ecoinvent LCIA implementation report](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Database/Fundamentals/201007_hischier_weidema_implementation_of_lcia_methods.pdf), printed page 77, identifies that basis. Printed page 151 also explains that separate NO₂ factors in TRACI were not implemented as a distinct elementary flow. The official 3.9 master assigns the same target UUID CAS 10102-44-0; the installed 3.10 target leaves its CAS blank. CAS correspondence alone does not make a species-specific flow equivalent to an LCIA aggregate.

The [glass source report](https://glassforeurope.com/wp-content/uploads/2018/04/Life-Cycle-Assessment.pdf), printed pages 8–9, deliberately separates NO and NO₂ for photochemical ozone assessment. Table 1 reports the same 0.000222 kg NO₂ quantity. The approved mapping retains the record and uses the aggregate NOx factors, losing that source-specific treatment.

For EPS, original PlasticsEurope process `b60b30bf-991d-41b8-a295-5d0b2e5f2bb5`, version 09.00.000, exchange 388, references [ILCD nitrogen dioxide flow `08a91e70-3ddc-11dd-96e5-0050c2490048`](https://plasticseurope.lca-data.com/resource/flows/08a91e70-3ddc-11dd-96e5-0050c2490048?format=xml&version=03.00.000), version 03.00.000. The flow defines CAS 10102-44-0, a mass basis and unspecified air. Its 0.00339627949445496 kg source quantity agrees with the BAFU value to export precision. The source has no RAF suffix or additional amount adjustment. The suffix itself remains unexplained and is retained in the audit label. The separate NO and N₂O rows remain unchanged.

Both rules retain original names, units, compartments and uncertainty. No amounts are rescaled, no exchange rows merged or dropped, and neither XML inputs nor the biosphere catalog is edited. Standard LCIA uses aggregate NOx factors; retaining the NO₂ labels does not restore separate NO₂ characterization automatically.

The notebook applies the approved rules after the historical-name stage. That preceding stage writes `biosphere-unlinked-after-historical-names.json`; this stage now writes `biosphere-unlinked-after-nitrogen-dioxide.json`, before the subsequent mosaic-land stage writes the final report. The original candidate and `reports/generated/biosphere-nitrogen-dioxide-proposal-check.json` remain as proposal-history snapshots; only the active mapping is loaded.

## Verification

The full `bw` import check at the NO₂ stage passes: **two new links**, **290,691 of 293,747 biosphere exchanges linked**, and **3,056 unresolved occurrences across 160 signatures**. All 11,947 datasets and 420,063 exchange rows remain, and all technosphere exchanges link.

Complete-record comparison confirms that only the two names, original-label audit metadata and input links change. Amounts, uncertainty, units, categories, comments and original missing CAS fields are unchanged. Each rule matches once; repeating the stage changes nothing. No inventory database was written. The notebook’s optional drop/write/LCA cells were excluded from verification.

Results are recorded in `reports/generated/biosphere-nitrogen-dioxide-migration-check.json`; original sources, the approval and file hashes are in `biosphere-nitrogen-dioxide-evidence.json`.

The later [mosaic-land stage](bafu-2026-biosphere-land-mosaic.md) updates the final counts. The NO₂ check remains a historical verification snapshot of its own notebook stage.
