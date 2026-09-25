# BAFU 2026 chemical aliases and elemental resource mass

The [chemistry migration](../schemas/mappings/bafu-2026-biosphere-chemistry.json) contains nine complete-signature rules: four user-approved compound-to-element conversions covering 504 occurrences, and five further reviewed aliases covering 37 occurrences. It follows the water/context migration.

## Approved elemental resource accounting

The user approved expressing these compound resources as the mass of their contained target element. Both units remain `kilogram`, but their material basis changes. Each exchange retains its original compound name, categories, and unit in `bafu original biosphere`. Its `bafu elemental conversion` metadata stores the source formula, target element, and atomic weights, making the basis explicit alongside the migration multiplier.

| Source resource | Target | Formula for the amount multiplier | Multiplier | Occurrences |
| --- | --- | --- | ---: | ---: |
| TiO₂ in rutile or ilmenite | Titanium | 47.867 / (47.867 + 2 × 15.999) | 0.5993489012708947 | 223 |
| Potassium chloride | Potassium | 39.098 / (39.098 + 35.45) | 0.5244674572087782 | 141 |
| Barite | Barium | 137.33 / (137.33 + 32.06 + 4 × 15.999) | 0.588424327080459 | 140 |

The weights are the conventional values in the [CIAAW abridged table](https://ciaaw.org/abridged-atomic-weights.htm). Compound formulas are supported by NIST records for [TiO₂](https://webbook.nist.gov/cgi/cbook.cgi?ID=13463-67-7), [KCl](https://webbook.nist.gov/cgi/cbook.cgi?ID=7447-40-7), and [BaSO₄](https://webbook.nist.gov/cgi/cbook.cgi?ID=7727-43-7). The historical ecoinvent 3.9 master data explicitly records formula O₂Ti for both old TiO₂ resource names; the supplied `2007 - LCI chemicals - Althaus.pdf`, mineral-sands section 97.6, documents these resource inputs. Brightway's public [correspondence table](https://github.com/brightway-lca/simapro_ecoinvent_elementary_flows/blob/main/Mapping/Output/Mapped_files/SimaProv94-ecoinventEFv3.7.csv) also connects the rutile source name to that historical UUID.

The 95%, 54%, and crude-ore percentages are descriptions of the mineral source. The source flow is already expressed on the stated compound basis; multiplying by those percentages again would apply an additional, unsupported grade correction. The target records the contained metal resource, with the original compound definition retained for traceability. This approved accounting conversion should not be treated as a claim that the source and target chemicals are identical.

All four rules are limited to `natural resource / in ground`. They do not affect emissions of these compounds. Original source CAS metadata is retained, including missing values; the linked target database carries the elemental CAS identifier.

## Amount and uncertainty checks

bw2io applies each fixed multiplier to the amount and its uncertainty parameters. The 504 converted rows comprise 49 nonzero lognormal rows and 455 rows with undefined uncertainty, including 24 zero TiO₂ quantities. For lognormal rows, `loc` changes consistently with the logarithm of the factor and `scale` remains unchanged. Undefined uncertainty stays undefined. Negative amounts retain their sign.

The helper recomputes the mass fraction from the declared formula and weights and rejects inconsistent factors. Same-unit scaling is allowed only with the explicit elemental-conversion metadata and preserved source identity. Re-execution cannot convert these rows twice because the compound name is part of the source signature and changes to the elemental target name.

## Additional aliases

| Source | Target | Occurrences | Evidence |
| --- | --- | ---: | --- |
| VOC, volatile organic compounds, unspecified origin | VOC, volatile organic compounds | 14 | Brightway correspondence to the same current UUID; neither name assigns fossil or biogenic origin |
| Dimethyl formamide | N,N-Dimethylformamide | 13 | [NIST synonyms, CAS 68-12-2](https://webbook.nist.gov/cgi/cbook.cgi?ID=C68122&Mask=8) |
| Disodium acid methane arsenate | DSMA | 2 | Brightway correspondence and [PubChem chemical identity](https://pubchem.ncbi.nlm.nih.gov/compound/8947) |
| Thiazole, 2-(thiocyanatemethylthio)benzo- | TCMTB | 1 | Brightway correspondence and [PubChem chemical identity](https://pubchem.ncbi.nlm.nih.gov/compound/30692) |
| Tin (II) | Tin ion | 7 | `Tin II` is an explicit synonym of the official 3.9 master-data target UUID, which is unchanged in 3.10 |

These aliases retain complete compartments, units, amounts, uncertainty, and original names. The Tin target groups ionic tin; the original divalent label remains on the exchange. It does not assign a new oxidation state. Missing source CAS values are not populated. No fuzzy matching is applied at runtime.

## Reports

`reports/generated/biosphere-chemistry-evidence.json` records the rules, target UUIDs, occurrence counts, and example files. `biosphere-chemistry-migration-check.json` records the full import check and numerical comparisons; `biosphere-chemistry-validation-check.json` checks rejection of wrong factors, missing weights, lost original labels, and resource/emission transfers. The preceding unresolved result is `biosphere-unlinked-after-water-context.json`; this stage's unresolved result is `biosphere-unlinked-after-chemistry.json`.

The full `bw` check resolved **541 additional exchanges**, yielding **287,711 linked biosphere exchanges** and **6,036 unresolved across 242 signatures** at this stage. It retained all 11,947 datasets and 420,063 exchange rows. Independent full-record comparisons verified the declared aliases, elemental scaling and uncertainty, unique targets, unchanged non-biosphere records, and idempotence. No inventory database was written.
