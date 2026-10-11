# Check: Cement ZN, D, at plant (c3490cfc-bcf2-38a2-a8c1-2d50ba65c83e)

target `bafu-2026` vs explicit model `c3490cfc-bcf2-38a2-a8c1-2d50ba65c83e-draft-disagg` and hybrid `c3490cfc-bcf2-38a2-a8c1-2d50ba65c83e-draft-hybrid`

**Strategy:** S3 — top-down model drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: per 1 kg cement ZN/D, ab Werk (Tab. 3.14, Werner 2018); the composition rows are percentage ranges of the kg; allocation: none stated for the cement itself; the burnt-shale input carries the economic allocation of section 3.6; 7 of 13 inputs carry a printed amount, 6 a printed range, 0 no number in the report. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** Clinker, at plant [0.4–0.7], Gypsum, mineral, at mine [0–0.1], Recycling aggregate from mixed demolition, dry, at plant [0.15–0.3], Burnt shale, at plant [0.15–0.3], Iron sulphate, at plant [0–0.01], Limestone, milled, loose, at plant [0–0.1]; mass sum 1.0
**Links to rebuilt nodes:** Burnt shale, at plant

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 16/50 within ±10 %, median |Δ| 19.4%
- kilogram mass covered within ±10 %: 4.0% of the target's total kg mass
- of the 1326 flows of the target, 1326 are determined by the solve (0 are round-off and are not scored; see lci.determined_flows)
- 192 of those 1326 within ±10 % (14%), median |Δ| 25.8%, 0 missing from the model, 445 extra
- hybrid vs target: identical on every flow

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 192 | 14% |
| 10–20 % | 291 | 22% |
| 20–50 % | 510 | 38% |
| 50–100 % | 199 | 15% |
| > 100 % | 134 | 10% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1084 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Calcite [resources/in ground] (kilogram) | 0.833 | 0.603 | -27.6% | +0.23 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.483 | 0.43 | -11.0% | +0.0531 |
| Shale [soil] (kilogram) | 0.13 | 0.288 | +121.1% | -0.158 |
| Clay [soil] (kilogram) | 0.0547 | 0.0357 | -34.7% | +0.019 |
| Gypsum [resources/in ground] (kilogram) | 0.0303 | 1.84e-08 | -100.0% | +0.0303 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.0263 | 0.0249 | -5.4% | +0.00142 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0229 | 0.0217 | -5.2% | +0.0012 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.0161 | 0.00805 | -49.9% | +0.00801 |
| Gravel [soil] (kilogram) | 0.0102 | 0.0126 | +23.5% | -0.0024 |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.00705 | 0.0066 | -6.4% | +0.000453 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.00443 | 0.00408 | -8.0% | +0.000355 |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.00259 | 0.00291 | +12.5% | -0.000324 |
| calcium [Emissions/Emissions to water] (kilogram) | 0.00202 | 0.00186 | -7.7% | +0.000156 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00178 | 0.00238 | +33.3% | -0.000594 |
| Carbon Monoxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.000985 | 0.00113 | +14.9% | -0.000147 |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.000979 | 0.000261 | -73.4% | +0.000718 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.000919 | 0.000305 | -66.8% | +0.000614 |
| Silicon [Emissions/Emissions to water] (kilogram) | 0.000742 | 0.000624 | -15.9% | +0.000118 |
| Iron [Resources/Resources from ground] (kilogram) | 0.000718 | 0.000553 | -22.9% | +0.000165 |
| Nitrogen Oxides [Emissions/Emissions to air] (kilogram) | 0.000602 | 0.000377 | -37.3% | +0.000224 |

### kilo Becquerel (138 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 45.9 | 35.3 | -23.2% | +10.7 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 17.8 | 12 | -32.7% | +5.81 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.717 | 0.483 | -32.7% | +0.234 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.71 | 0.313 | -55.8% | +0.396 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.0783 | 0.467 | +496.5% | -0.389 |

### square meter (37 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 7.7e-05 | 6.45e-05 | -16.2% | +1.25e-05 |
| From Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 5.46e-05 | 4.52e-05 | -17.2% | +9.39e-06 |
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 3.09e-05 | 3.07e-05 | -0.7% | +2.29e-07 |
| From Arable, Non-irrigated [Land use/Land transformation] (square meter) | 2.98e-05 | 2.83e-05 | -5.0% | +1.49e-06 |
| To Forest, Intensive [Land use/Land transformation] (square meter) | 2.5e-05 | 2.87e-05 | +14.9% | -3.72e-06 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 1.03 | 0.724 | -29.6% | +0.304 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 1.03 | 0.722 | -29.6% | +0.304 |
| Water [Resources/Resources from water] (cubic meter) | 0.000992 | 0.00108 | +8.4% | -8.36e-05 |
| river water [Resources/Resources from water] (cubic meter) | 0.000586 | 0.000441 | -24.6% | +0.000144 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 0.000568 | 0.000358 | -37.0% | +0.00021 |

### megajoule (21 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Crude Oil [Resources/Resources from ground] (megajoule) | 0.994 | 1.47 | +48.1% | -0.478 |
| Waste Heat [air] (megajoule) | 0.938 | 0.732 | -22.0% | +0.206 |
| Uranium [Resources/Resources from ground] (megajoule) | 0.707 | 0.477 | -32.5% | +0.23 |
| Hard Coal [Resources/Resources from ground] (megajoule) | 0.583 | 0.105 | -81.9% | +0.478 |
| Waste Heat [air] (megajoule) | 0.559 | 0.387 | -30.7% | +0.172 |

### square meter-year (17 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 0.00215 | 0.00254 | +18.1% | -0.00039 |
| Forest [Land use/Land occupation] (square meter-year) | 0.00128 | 0.00128 | -0.2% | +2e-06 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 0.000426 | 0.000325 | -23.8% | +0.000101 |
| Mineral Extraction Site [Land use/Land occupation] (square meter-year) | 0.000197 | 0.000102 | -48.4% | +9.55e-05 |
| Traffic Area, Road Network [Land use/Land occupation] (square meter-year) | 0.000195 | 0.000208 | +6.3% | -1.24e-05 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 0.00406 | 0.00562 | +38.3% | -0.00156 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 2.48e-05 | 1.95e-05 | -21.3% | +5.29e-06 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 0.0595 | 0.0817 | +37.3% | -0.0222 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 3.24e-07 | 3.15e-07 | -2.8% | +9.11e-09 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 0.00455 | 0.00306 | -32.7% | +0.00149 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 1.89e-06 | 1.67e-06 | -11.7% | +2.21e-07 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Shale [soil] (kilogram) | 0.13 | 0.288 | +121.1% |
| Gypsum [resources/in ground] (kilogram) | 0.0303 | 1.84e-08 | -100.0% |
| Non-methane Volatile Organic Compounds [Emissions/Emissions to air] (kilogram) | 5.23e-05 | 1.89e-06 | -96.4% |
| Methane (fossil) [Emissions/Emissions to air] (kilogram) | 0.000359 | 5.97e-05 | -83.4% |
| Sodium [water] (kilogram) | 0.000319 | 8.26e-05 | -74.1% |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.000979 | 0.000261 | -73.4% |
| Calcium [Emissions/Emissions to water] (kilogram) | 8.22e-05 | 2.33e-05 | -71.7% |
| Sodium chloride [resources/in ground] (kilogram) | 7.06e-05 | 0.000119 | +68.3% |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.000919 | 0.000305 | -66.8% |
| Sulfur Dioxide [Emissions/Emissions to air] (kilogram) | 8.37e-05 | 3.73e-05 | -55.5% |

## Structural checks

- ✓ 13 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✗ depends on system processes (rebuild those first): ['Ethylene glycol, at plant']
- ✓ mass in: 1.05 kg technosphere + 0 kg resources per 1 kg product (informational)
- ✓ all inputs resolved

residual: 950 flows under-explained, 821 over-explained (negative residual)

## Evidence

- 2020 - LCA selected types of concrete - Tschuemperlin.pdf — pages 25-26 -> report-p25-26.txt report sha256 83e2e7ea46d35899…, text sha256 95d82d20fed0b8de…
