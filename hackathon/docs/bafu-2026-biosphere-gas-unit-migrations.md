# BAFU 2026 resource-gas unit assumption

The [gas-unit migration](../schemas/mappings/bafu-2026-biosphere-gas-units.json) applies the user's explicit approval: **use documented 1:1 relabeling** for 363 resource-gas exchanges. Source temperature and pressure reference conditions remain unknown. This is an assumed equivalence of volume labels, not a physical temperature/pressure conversion.

All four rules retain `natural resource / in ground` and match the complete incoming name, categories, and unit. They run after the chemistry migration in the [notebook](../scripts/import_fixed_ecospold.ipynb).

| Source name | Source unit | Target name | Target unit | Occurrences |
| --- | --- | --- | --- | ---: |
| Gas, natural/m3 | cubic meter | Gas, natural | standard cubic meter | 137 |
| Gas, natural/m3 | normal cubic meter | Gas, natural | standard cubic meter | 115 |
| Gas, mine, off-gas, process, coal mining/m3 | cubic meter | Gas, mine, off-gas, process, coal mining | standard cubic meter | 99 |
| Gas, mine, off-gas, process, coal mining/m3 | normal cubic meter | Gas, mine, off-gas, process, coal mining | standard cubic meter | 12 |

The installed `ecoinvent-3.10-biosphere` provides one target for each complete target signature: natural gas UUID `7c337428-fb1b-45c7-bbb2-2ee4d29e17ba` and mine gas UUID `3ed5f377-344f-423a-b5ec-9a9a1162b944`. The helper checks target uniqueness at runtime.

Each exchange retains its incoming name, categories, and unit in `bafu original biosphere`. These are labels after the earlier import/normalization stages; the raw XML remains available unchanged. `bafu unit assumption` records the factor of one, unknown source reference conditions, and user-approved basis. The target's LCIA factors then apply to the unchanged numeric amount expressed under the assumed target label; linking does not validate the reference conditions.

There is deliberately no bw2io `multiplier` field. Even a multiplier of one can recalculate lognormal location parameters or other uncertainty fields. Ordinary bw2io metadata migration changes only the name, unit, audit metadata, and link. Amounts, uncertainty parameters, categories, CAS identifiers, and comments stay exactly unchanged.

The helper permits this exception only for these two resource-gas names, the two approved source units, the stated target names/unit and compartment, the exact documented assumption, and preserved source metadata. It rejects additional scaling or compartment changes. Other unit conversions still require a multiplier. Rerunning the same migration is idempotent because its source name and unit no longer match.

## Verification

The full collection check and its per-rule counts are recorded in `reports/generated/biosphere-gas-unit-migration-check.json`. The preceding result is `biosphere-unlinked-after-chemistry.json`; this stage's unresolved report is `biosphere-unlinked-after-gas-units.json`. Validation tests are in `scripts/ecospold importer/test_biosphere_gas_units.py`.

The full `bw` check linked **363 additional exchanges**, yielding **288,074 linked biosphere exchanges** and **5,673 unresolved across 238 signatures**. An independent comparison of every record verified exact preservation of numeric and uncertainty fields, comments, CAS values, compartments, and all non-biosphere records. All 11,947 datasets and 420,063 exchange rows remained, every target was unique, and reapplication produced identical records. No inventory database was written.

The three focused validation tests also passed, including rejection of altered assumptions, missing source metadata, multipliers, changed destinations/compartments, and absent or ambiguous targets.
