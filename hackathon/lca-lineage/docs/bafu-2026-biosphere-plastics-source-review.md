# Source-verified corrections in the EPS inventory

The [plastics source-review migration](../schemas/mappings/bafu-2026-biosphere-plastics-source-review.json) resolves four exchanges in `process_05a10e4b-a919-33b6-b017-7c0bf7f7a7f9.xml`, **Polystyrene, expandable, at plant / RER**. It follows the established compound-to-element resource convention, with a source-specific basis for these two compounds.

## Source identity and mass basis

The original [PlasticsEurope EPS inventory, version 09.00.000](https://plasticseurope.lca-data.com/datasetdetail/process.xhtml?uuid=b60b30bf-991d-41b8-a295-5d0b2e5f2bb5&version=09.00.000) references these elementary flows:

| Source | Original flow UUID | CAS in original flow | Original amount (kg) | BAFU amount (kg) |
| --- | --- | --- | ---: | ---: |
| Calcium chloride | `08a91e70-3ddc-11dd-97ec-0050c2490048` | 10043-52-4 | 2.95987531736421 × 10⁻¹² | 2.9599 × 10⁻¹² |
| Magnesium chloride | `fe0acd60-3ddc-11dd-acd8-0050c2490048` | 7786-30-3 | 3.64410020877926 × 10⁻⁴ | 3.6441 × 10⁻⁴ |

The names, extraction compartment, and quantities agree with the BAFU rows to rounding precision. Both referenced flow records specify **Mass** as their reference property. Their CAS identifiers establish [CaCl₂](https://pubchem.ncbi.nlm.nih.gov/compound/Calcium-Chloride) and [MgCl₂](https://janaf.nist.gov/tables/Mg-index.html). This supplies the chemical basis that was missing from the BAFU rows.

The calcium flow's broad synonym list also includes hydrated/product names; these are not used to determine hydration. The conversion follows its stated CAS identity and mass reference. It does not generalize to a separately specified hydrate or solution. The missing CAS fields in BAFU remain missing; the source evidence is recorded separately.

## Conversion and retained information

The rules select the exact source filename, type, name, full categories, unit, and original empty CAS. Both keep `natural resource / in ground` and convert kilogram of compound to kilogram of contained element:

| Source → target | Factor | Target UUID |
| --- | ---: | --- |
| Calcium chloride → Calcium | 40.078 / (40.078 + 2 × 35.45) = 0.36113463929787887 | `c8fc4197-7410-42f2-aeb4-c08c6a693992` |
| Magnesium chloride → Magnesium | 24.305 / (24.305 + 2 × 35.45) = 0.2552912136967596 | `9e5823ad-9d9b-4b98-b627-e39611b6a8bd` |

Weights follow the [CIAAW abridged atomic-weight table](https://www.ciaaw.org/abridged-atomic-weights.htm). The original name/categories/unit remain in `bafu original biosphere`, and the formula, element, and atomic weights remain in `bafu elemental conversion`. Original comments and CAS fields are unchanged. No additional chlorine resource flow is created; this uses the same contained-element convention as the earlier chloride-resource mapping.

bw2io scales the amount and uncertainty together. For these lognormal exchanges, `loc` shifts by ln(factor), while `scale` stays unchanged. Reapplying the migration does not convert them again.

## Restore the original chromium-VI label

The EPS row named `P-cyanophenol` emits 4.7885 × 10⁻¹⁵ kg to industrial soil. In the original PlasticsEurope process, exchange 222 is **chromium VI to non-agricultural soil**, 4.78846854081047 × 10⁻¹⁵ kg. The two preceding chromium-VI air/water rows and the two following chrysene rows also align in order and quantity. The source process contains no P-cyanophenol row.

The referenced flow UUID `4d9a8790-3ddd-11dd-9c1e-0050c2490048` confirms chromium VI on a mass basis. The rule restores that identity and links the unique `Chromium VI / soil, industrial / kilogram` target `58060894-19d9-4855-84d8-58935a5325f8`. It preserves the amount, uncertainty, compartment, original BAFU label, and original missing CAS. This is a correction for one identified source row, not a chemical equivalence between cyanophenol and chromium.

## Restore PAH identity with the approved generic-soil target

The row labelled `(Aminooxy)(hydroxy)sulfane dioxide` emits 1.3782 × 10⁻¹¹ kg to industrial soil. Original EPS exchange 421 instead identifies **polycyclic aromatic hydrocarbons to non-agricultural soil**, 1.37822521718833 × 10⁻¹¹ kg (flow UUID `08a91e70-3ddc-11dd-9816-0050c2490048`). Its preceding air/water PAH rows and following two potassium rows align in order and quantity, within BAFU rounding precision. This establishes a source transcription error, not chemical equivalence between the two names.

The user approved restoring PAH identity and broadening the compartment to generic soil. The target is `PAH, polycyclic aromatic hydrocarbons / soil / kilogram`, UUID `6d74bab2-969f-419c-a2dc-4dde50cf2553`. Both the original mislabel and `soil / industrial` remain in `bafu original biosphere`. Amount, uncertainty, comments and original missing CAS stay unchanged. Standard LCIA uses generic-soil factors and loses the industrial-soil distinction.

## Related findings that do not authorize new mappings

The [2025 plastics report](../data/raw/BAFU-2026%20v1%20LCI%20Reports/2025%20-%20LCI%20plastics%20-%20Rajabihamedani.pdf), table 3.3 on PDF pages 17–18, identifies coal calorific values but initially left a unit conflict: version 3 flow XML labels its referenced property Radioactivity. The subsequent [plastics conversion stage](bafu-2026-biosphere-plastics-conversions.md) follows that property UUID to its actual net-calorific-value definition and MJ reference unit. Both flow versions specify 11.9 MJ/kg for brown coal and 26.3 MJ/kg for hard coal. All 28 coal occurrences have now been traced to original process quantities and converted in that later stage, preserving existing BAFU adjustments. This four-rule stage does not itself convert coal.

The same table explicitly assigns **primary energy from waves** to BAFU's `Energy, from hydro power`. The EPS quantities agree at 2.1968 × 10⁻¹³; its genuine hydropower input is a separate 0.30209 MJ row already present in BAFU. The wave-derived row therefore remains unresolved rather than being linked to a hydropower-reservoir target. Section 3.8 describes the source's erroneous renewable-energy kg labels and the report authors' assumed MJ corrections.

Section 3.9 recognizes pesticide emissions in air, water, and soil, and the limited compartment coverage of ecological-scarcity factors. It does not support moving the remaining air/water pesticide emissions to agricultural soil.

The apparent `Isobutene` → `Butene` shortcut is also not applied: the target's CAS 25167-67-3 is associated with [linear 1-/2-butene mixtures](https://pubchem.ncbi.nlm.nih.gov/compound/n-butene), which does not establish equivalence to isobutene.

## Verification

At this stage, the full `bw` import check adds **four links**, reaching **290,569 linked of 293,747 biosphere exchanges**. **3,178 occurrences across 171 signatures remain unresolved.** All 11,947 datasets and 420,063 exchange rows are preserved, and all technosphere exchanges link.

Independent complete-record comparison checks the two chemical mass fractions and their lognormal parameters. Only declared conversion fields, names, audit metadata, and unique input links change. The chromium and PAH corrections leave all their numerical fields unchanged; only the PAH rule broadens the compartment as approved. Existing links, other exchanges, original CAS values, and comments are unchanged. All four rules match once; reapplication is idempotent. The worklist at this stage matches the live importer. No inventory database is written.

Evidence and hashes are in `reports/generated/biosphere-plastics-source-review-evidence.json`, with downloaded source XML under `reports/generated/plasticseurope-source-review/`. Verification is in `biosphere-plastics-source-review-migration-check.json`. This stage writes `biosphere-unlinked-after-plastics-source-review.json`; the preceding context stage writes `biosphere-unlinked-after-context.json`.

Further EPS source comparisons are saved in `biosphere-eps-quantity-review-candidates.json`. Two PM10-labelled rows originate from palladium/rhodium emissions; the subsequent [EPS metal stage](bafu-2026-biosphere-eps-metals.md) resolves them with exact quantity-and-filename selection and historical catalog UUIDs. The genuine PM10 row in the same file stays unresolved. A matching freshwater-TOC quantity was checked and is already a water emission in BAFU; it is not an air-compartment correction.
