# BAFU 2026 source review and approved broader resources

The [source-review migration](../schemas/mappings/bafu-2026-biosphere-source-review.json) runs after the compartment/aggregate stage. Its rules match type, name, complete categories, unit, and the stated source CAS number. They retain incoming names, categories, and units in `bafu original biosphere`; original CAS values and comments remain on the exchanges.

## Metam-sodium: resolve a conflicting hydration label

One exchange in `process_d8ce066d-8d42-3875-be68-99445d4b3fb6.xml`, **Potatoes, at farm / US**, is named `Metam-sodium dihydrate` but states CAS `000137-42-8`. Its amount is **0.00066972 kg** to `soil / agricultural` per kilogram of potatoes.

The cited [2007 agricultural inventory report](../data/raw/BAFU-2026%20v1%20LCI%20Reports/2007%20-%20LCI%20agricultural%20prod.%20systems%20-%20Nemecek.pdf) resolves the mass basis:

- Report 15b, section 1.2.7, printed page 15 (combined PDF page 329), describes pesticide use as active-ingredient mass.
- Table 1.13, printed page 20 (PDF page 334), records `Metam, sodium` at approximately 27.5 kg/ha/year for potatoes.
- Appendix A, printed page 41 (PDF page 355), lists **Metam-sodium**, `soil/agricultural`, **6.70 × 10⁻⁴ kg** for the same US potato inventory. This agrees with the XML amount at the report's three-significant-figure precision. Its matching pesticide input is also 6.70 × 10⁻⁴ kg.

The unique biosphere 3.10 target is `Metam-sodium`, `soil / agricultural`, kilogram, UUID `00acb9f0-1640-4f8c-89ef-d857e1428be0`, CAS `000137-42-8`.

The rule therefore corrects the conflicting name while keeping the source quantity on its documented active-ingredient basis. **No hydration mass conversion is applied.** This conclusion relies on the original inventory, its quantity, and the source CAS together; a matching CAS alone would not resolve an ambiguous hydrate label. The rule does not cover missing or different CAS values, including a dihydrate-specific CAS. The original `Metam-sodium dihydrate` name remains in audit metadata.

Local evidence, source-document SHA-256, page references, target UUID, and the exact source quantity are recorded in `reports/generated/biosphere-source-review-evidence.json`.

## Approved broader forest and water targets

Three additional rules cover the 12 explicitly approved occurrences:

| Source | Count | Target and treatment |
| --- | ---: | --- |
| Transformation, from forest, natural | 6 | Forest, unspecified; same square-metre unit and resource/land compartment |
| Water, process, surface | 4 | Water, unspecified natural origin; same resource/in-water compartment; kg → m³ at 0.001 |
| Water, cooling, unspecified natural origin, RER | 2 | Water, unspecified natural origin; same resource/in-ground compartment and cubic-metre unit |

All original names, categories, and units remain in `bafu original biosphere`; the two cooling exchanges also retain `region: RER`. These rules do not infer primary versus secondary forest, river versus lake, or a surface source for groundwater. Standard LCIA uses the broader classes and does not automatically read the retained natural-forest, surface/process-water, cooling-purpose, or regional distinctions.

The four water mass-to-volume conversions use the previously adopted **1,000 kg/m³** catalog convention. bw2io scales their amounts and uncertainty consistently; lognormal `loc` shifts by ln(0.001), with `scale` unchanged. The other nine occurrences in this stage keep all numerical fields unchanged.

Target UUIDs are `0930b6b8-d9c6-4462-966f-ac7495b63bed` for forest, `831f249e-53f2-49cf-a93c-7cee105f048e` for in-water withdrawals, and `478e8437-1c21-4032-8438-872a6b5ddcdf` for in-ground withdrawals. The original source rows and decisions are recorded in `biosphere-remaining-resource-land-review.json` and `biosphere-source-review-evidence.json`.

## A reviewed candidate left unresolved

The float-glass inventory's `Nitrogen dioxide` emission now uses an approved NOx aggregate mapping. Its [original 2011 source report](https://glassforeurope.com/wp-content/uploads/2018/04/Life-Cycle-Assessment.pdf), printed pages 8–9 and table 1, deliberately distinguishes nitrogen dioxide from the other nitrogen oxides for photochemical ozone assessment. The reported NO₂ amount, 2.22 × 10⁻⁴ kg/kg glass, matches the XML. Although ecoinvent's [LCIA implementation report](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Database/Fundamentals/201007_hischier_weidema_implementation_of_lcia_methods.pdf) uses NOx expressed as NO₂, mapping this separate NO₂ row to the aggregate would lose the source's deliberate distinction. It has not been treated as a spelling correction. The original EPS process and ILCD flow now confirm the separate `Nitrogen dioxide, RAF` row as NO₂ on a mass basis, although the suffix itself remains unexplained. The user approved the [two-row NOx aggregation](bafu-2026-biosphere-nitrogen-dioxide-proposal.md). Both rows are now linked with original labels, quantities and uncertainty retained; standard LCIA uses the aggregate NOx factors.

## Verification

The full `bw` import check links **13 additional exchanges**, reaching **290,550 linked biosphere exchanges** with **3,197 unresolved across 176 signatures**. All 11,947 datasets and 420,063 exchange rows remain; all technosphere exchanges link.

Independent complete-record comparison checks that only the declared names, units, four water conversions, audit metadata, and unique input links change. Water conversions are checked independently, including their lognormal parameters. All unscaled numerical fields, comments, source CAS values, existing links, and non-biosphere records are preserved. Reapplication is idempotent. The remaining-flow audit agrees with the live importer and leaves it unchanged. No inventory database or LCIA method is written.

The preceding report is `biosphere-unlinked-after-compartments.json`; this stage writes `biosphere-unlinked-after-source-review.json`. The check is saved as `reports/generated/biosphere-source-review-migration-check.json`.
