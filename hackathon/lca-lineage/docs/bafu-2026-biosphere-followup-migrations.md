# BAFU 2026 follow-up biosphere mappings

The [follow-up migration](../schemas/mappings/bafu-2026-biosphere-followup.json) contains eight full-signature rules after the land/resource stage. Every affected exchange retains its incoming name, categories, and unit in `bafu original biosphere`. The rules use standard bw2io migration and matching against unique biosphere 3.10 targets.

| Source | Target or correction | Occurrences |
| --- | --- | ---: |
| Occupation, traffic area, rail network, CH | Same name without `, CH`; retain `region: CH` | 4 |
| Occupation, traffic area, rail/road embankment, CH | Same name without `, CH`; retain `region: CH` | 4 |
| Transformation, from unspecified, used | Transformation, from unspecified; correct missing or in-ground category to land | 24 |
| Occupation, unspecified, used | Occupation, unspecified | 2 |
| Cesium-136, surface water, Bq | Caesium-136, surface water, kBq; multiply by 0.001 | 20 |
| Carbon dioxide, non-urban air, in the reviewed quicklime-with-CCS dataset | Carbon dioxide, fossil; retain amount and compartment | 1 |
| Phenol, 2-chloro-, water | 2-Chlorophenol; retain compartment and amount | 3 |

## Approved land aggregation

The user approved both the generic rail targets with Switzerland retained and the broader unspecified-land class with original labels retained. These rules keep occupation distinct from transformation, preserve transformation direction, and preserve area or area-time units. Twenty-one transformation rows lack a resource subcategory and three incorrectly use `in ground`; their names and area units identify land transformation. Their original categories remain in the audit metadata.

All 34 land amounts and uncertainty fields remain unchanged. Generic LCIA uses the target's factors; it does not automatically distinguish the retained `used` qualifier or Swiss geography. The helper permits regional metadata for these two reviewed Swiss rail signatures in addition to the previously approved water rules. It rejects a different country or rail-to-road substitution.

## Caesium spelling and activity units

Cesium and caesium identify the same element, as documented by [IUPAC's elemental review](https://ciaaw.org/pubs/EXER-2000.pdf), section 55 (printed p. 771). Isotope 136 and the surface-water compartment remain unchanged. The target UUID is `fd000a8d-2e90-4042-b148-cfb6bdfbbff5`, also present for the historical Cesium-136 river flow in the `ecoinvent elementary flows 2-3.xlsx` correspondence bundled with bw2io.

The [BIPM SI prefix definition](https://www.bipm.org/fr/measurement-units/si-prefixes) gives kilo = 1,000. Thus the numerical amount in kBq equals the amount in Bq × 0.001. The rule uses bw2io's multiplier support, including uncertainty rescaling; all 20 affected source rows have undefined uncertainty. Source comments and CAS metadata are retained. Rows already expressed in kBq are outside this rule.

The public SimaPro correspondence was used only to identify a candidate. Its factor of 1 for this Bq-to-kBq row is inconsistent with the stated units and is not used.

## Exact chlorophenol synonym

The [NIST Chemistry WebBook entry for CAS 95-57-8](https://webbook.nist.gov/cgi/cbook.cgi?ID=95-57-8) explicitly lists `Phenol, 2-chloro-` and `2-Chlorophenol` as names of the same substance. Three water-emission exchanges have no source CAS but unambiguously name this positional isomer. The unique target is `2-Chlorophenol / water / kilogram`, UUID `5b1bd939-79af-4513-af34-5f532295744f`. Their amounts, uncertainty, compartment, and comments are unchanged; no CAS value is invented on the source. The six air exchanges have no matching target compartment and remain unresolved.

## Reviewed carbon origin

The one low-population-air `Carbon dioxide` exchange belongs to `process_a2f73ca7-bb25-4507-ba8e-6903274b95b1.xml`, **Quicklime, in pieces, loose, at plant, with carbon capture and storage**. It emits 0.284 kg CO₂ and consumes 1.73 kg limestone and 0.0914 kg heavy fuel oil. Its comments describe adding CCS to the ordinary quicklime dataset.

The linked heavy-fuel-oil supplier, `process_8203dcbb-a27f-3cfd-9e7b-944305d7d285.xml`, consumes refinery heavy fuel oil in quantities of 0.17041 and 0.8296 kg. This was checked from its actual inputs, rather than relying on generic distribution comments mentioning biofuel shares. Geological carbonate and petroleum carbon support the **inference** that this CO₂ belongs to the fossil category. Ecoinvent likewise classifies CO₂ from geological limestone as fossil in its [model description, section 2.8](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Database/Sectors/Ecoinvent_Tool_Model_Description_20180130.pdf?hsLang=en).

The target is `Carbon dioxide, fossil / air / non-urban air or from high stacks / kilogram`, UUID `aa7cac3a-3625-41d4-bc54-33e2cf11ec46`. No CCS efficiency, amount, or uncertainty parameter is recalculated. This signature occurs only in that reviewed source in BAFU 2026; recheck the provenance before reusing this rule for another release. Other generic CO₂ compartments are excluded.

Three diesel machinery datasets were also reviewed, but their generic CO₂ and CO remain unresolved. Their actual diesel supplier (`process_113af6ac-ff61-3bbc-b52b-009a3eb1afcf.xml`) includes 0.0028393 + 0.02299 kg vegetable-oil methyl ester as well as refinery diesel. Assigning all six emissions to fossil carbon would require further reconciliation of the original emission factors and fuel carbon shares. A fuel mass fraction alone is insufficient. The source machinery files are `process_5f88ed47-bde5-4c8c-983d-c669049d61de.xml`, `process_c023e201-b139-4ff6-85df-52edb6415f3b.xml`, and `process_ec4009ae-3a1d-4084-93dc-159e195b6fbb.xml`.

## Verification

Rule evidence, target UUIDs, source filenames, and occurrence counts are saved locally in `reports/generated/biosphere-followup-evidence.json`. The preceding stage writes `biosphere-unlinked-after-land-resources.json`; this stage writes `biosphere-unlinked-after-followup.json`. The independent full-collection check is `biosphere-followup-migration-check.json`.

The full `bw` check resolved **58 additional occurrences**, yielding **289,042 linked biosphere exchanges** and **4,705 unresolved across 212 signatures**. All 11,947 datasets and 420,063 exchange rows remained. Independent full-record comparison verified only declared replacements, unique target links, and the exact conversion for 20 caesium rows. Every unscaled amount and uncertainty field, comment, original CAS value, and non-biosphere record/link was preserved. Reapplication was idempotent; no inventory database was written. All six migration guard tests passed, including invalid regional-land substitutions and the existing gas-unit safeguards.
