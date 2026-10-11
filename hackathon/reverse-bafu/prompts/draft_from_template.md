You are helping rebuild an aggregated life-cycle-inventory dataset as a unit process, from another unit process of the same product.

The dataset `{{target_name}}` [{{target_location}}], reference unit 1 {{target_unit}}, is shipped in the BAFU-2026 database as a system process: it has no production inputs, only ~{{n_flows}} cumulative elementary flows. No report in the documentation bundle prints its inventory:

> {{no_report_reason}}

## What the database says about the dataset

- BAFU category: {{target_category}}
- includedProcesses: {{included_processes}}
- technology: {{technology}}
- generalComment: {{general_comment}}

## Unit processes in BAFU-2026 with a similar name

Found by a deterministic name search for the same product; system processes are left out. Each candidate shows its reference unit and its technosphere inputs per 1 unit of product (the first 30).

{{candidates}}

## Rules

1. Choose a candidate only if it makes **the same product**: the same material or substance and a comparable grade, with the same reference unit. Another location, another vintage (an older ecoinvent version), another manufacturer or a closely related grade qualify; a different product, an upstream intermediate or a downstream use of the product does not. If none qualifies, set `chosen_code` to null and say why in `reason`. A wrong template is worse than none.
2. If the target is the same product *at regional storage* (or another distribution stage) and a candidate is the product *at plant*, that is not a template: set `chosen_code` to null and say so in `gaps`.
3. List every difference between template and target that you can see from the metadata (location, grade, technology, time period) in `differences`, one sentence each.
4. `free_inputs`: the template inputs whose amounts plausibly differ between template and target - the main materials and energy carriers, at most ten - copied exactly as the template lists them. They will be fitted to the target's elementary flows within 0.5x to 2x of the template amount. Every other input keeps the template amount.
5. `electricity_location`: if the target's location differs from the template's and the target's electricity would come from its own grid, the location code to switch the template's electricity inputs to (e.g. "CH"); otherwise null.
6. Do not invent inputs; the structure is the template's. Anything the target needs that the template lacks goes into `gaps`.

Return only the JSON object described by the schema.
