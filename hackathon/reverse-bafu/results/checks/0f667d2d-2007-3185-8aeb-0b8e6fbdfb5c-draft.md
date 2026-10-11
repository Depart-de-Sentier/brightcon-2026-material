# Check: Hydrogen cyanide, at plant (0f667d2d-2007-3185-8aeb-0b8e6fbdfb5c)

target `bafu-2026` vs explicit model `0f667d2d-2007-3185-8aeb-0b8e6fbdfb5c-draft-disagg` and hybrid `0f667d2d-2007-3185-8aeb-0b8e6fbdfb5c-draft-hybrid`

**Strategy:** S3 — top-down model drafted from the report excerpt by the LLM pipeline (reverse-bafu draft); the report's tables are literature data, the dataset itself is a cumulated inventory. basis: per kg of hydrogen cyanide, Tab. 43.2 / 43.3 / 43.4 of chapter 43 of ecoinvent report No. 8 (Althaus et al. 2007), all printed per kg or per kg in grams; allocation: None stated. The chapter reports three co-products per kg HCN - 0.23 kg hydrogen (BMA route, if not burnt), 0.34 kg ammonium sulfate sold as fertiliser and 0.02 kg sodium cyanide - but gives no allocation factor, so every burden below stays with the HCN.; 3 of 4 inputs carry a printed amount, 1 a printed range, 0 no number in the report. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** Heat, natural gas, at industrial furnace 1MW [23.2–35.4]
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 1/50 within ±10 %, median |Δ| 97.6%
- kilogram mass covered within ±10 %: 0.1% of the target's total kg mass
- of the 1781 flows of the target, 1678 are determined by the solve (103 are round-off and are not scored; see lci.determined_flows)
- 6 of those 1678 within ±10 % (0%), median |Δ| 11380.3%, 0 missing from the model, 1 extra
- hybrid vs target: 4 flows differ

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 6 | 0% |
| 10–20 % | 5 | 0% |
| 20–50 % | 15 | 1% |
| 50–100 % | 57 | 3% |
| > 100 % | 1698 | 95% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1466 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 4.72 | 2.92 | -38.1% | +1.8 |
| Methane (fossil) [Emissions/Emissions to air] (kilogram) | 0.102 | 0.000182 | -99.8% | +0.102 |
| Calcite [resources/in ground] (kilogram) | 0.0242 | 0.0342 | +41.4% | -0.01 |
| Sulfur [Resources/Resources from ground] (kilogram) | 0.0221 | 1.36e-06 | -100.0% | +0.0221 |
| Gravel [soil] (kilogram) | 0.0202 | 0.364 | +1703.4% | -0.344 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.0122 | 0.0226 | +85.6% | -0.0104 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.012 | 2.57 | +21384.9% | -2.56 |
| Sand [soil] (kilogram) | 0.0113 | 3.88e-06 | -100.0% | +0.0113 |
| Sodium chloride [resources/in ground] (kilogram) | 0.00896 | 0.0178 | +98.7% | -0.00885 |
| Sulfur Dioxide [Emissions/Emissions to air] (kilogram) | 0.00843 | 0.00328 | -61.1% | +0.00515 |
| Nitrogen Oxides [Emissions/Emissions to air] (kilogram) | 0.00732 | 0.00263 | -64.1% | +0.00469 |
| Silicon [Emissions/Emissions to water] (kilogram) | 0.00637 | 0.006 | -5.7% | +0.000364 |
| COD, Chemical Oxygen Demand [emissions to water/groundwater, long-term] (kilogram) | 0.00585 | 0.00136 | -76.7% | +0.00449 |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.00537 | 0.0431 | +703.4% | -0.0378 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.00461 | 0.018 | +290.5% | -0.0134 |
| Carbon Monoxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.00412 | 0.00115 | -71.9% | +0.00296 |
| Non-methane Volatile Organic Compounds [Emissions/Emissions to air] (kilogram) | 0.00399 | 4.98e-05 | -98.8% | +0.00394 |
| Sulfate Ion [water] (kilogram) | 0.00389 | 0.000736 | -81.1% | +0.00315 |
| Phosphorus [Resources/Resources from ground] (kilogram) | 0.00262 | 9.12e-05 | -96.5% | +0.00253 |
| TOC, Total Organic Carbon [emissions to water/groundwater, long-term] (kilogram) | 0.00232 | 0.000492 | -78.8% | +0.00182 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 1.91 | 154 | +7961.8% | -152 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 0.663 | 52.1 | +7758.2% | -51.5 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.0267 | 2.1 | +7763.4% | -2.07 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.0178 | 1.13 | +6214.1% | -1.11 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.0174 | 1.45 | +8246.5% | -1.43 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| From Pasture/meadow [Land use/Land transformation] (square meter) | 1.15e-05 | 0.000826 | +7058.8% | -0.000815 |
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 8.45e-06 | 0.00274 | +32315.1% | -0.00273 |
| To Forest [Land use/Land transformation] (square meter) | 6.46e-06 | 0.000115 | +1685.0% | -0.000109 |
| To Dump Site [Land use/Land transformation] (square meter) | 6.06e-06 | 0.000412 | +6695.6% | -0.000406 |
| From Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 5.97e-06 | 0.00194 | +32446.5% | -0.00194 |

### megajoule (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Natural Gas [Resources/Resources from ground] (megajoule) | 86.8 | 81.9 | -5.6% | +4.9 |
| Waste Heat [air] (megajoule) | 63.1 | 72.6 | +15.1% | -9.53 |
| Crude Oil [Resources/Resources from ground] (megajoule) | 13.6 | 13.1 | -3.4% | +0.467 |
| Uranium [Resources/Resources from ground] (megajoule) | 4.43 | 2.09 | -52.9% | +2.34 |
| Hard Coal [Resources/Resources from ground] (megajoule) | 2.94 | 0.669 | -77.2% | +2.27 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 0.000271 | 0.0284 | +10373.6% | -0.0281 |
| Traffic Area, Road Network [Land use/Land occupation] (square meter-year) | 0.000261 | 0.00241 | +821.7% | -0.00215 |
| Dump Site [Land use/Land occupation] (square meter-year) | 0.000172 | 0.00102 | +495.4% | -0.000852 |
| Forest [Land use/Land occupation] (square meter-year) | 7.12e-05 | 0.0143 | +19963.9% | -0.0142 |
| Construction Site [Land use/Land occupation] (square meter-year) | 2.89e-05 | 0.0011 | +3714.9% | -0.00107 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 0.122 | 3.42 | +2704.8% | -3.3 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 0.0715 | 0.00886 | -87.6% | +0.0626 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 0.0389 | 3.39 | +8626.5% | -3.35 |
| Water [Resources/Resources from water] (cubic meter) | 0.0136 | 0.0191 | +40.5% | -0.00552 |
| river water [Resources/Resources from water] (cubic meter) | 0.00198 | 0.00152 | -23.3% | +0.000463 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | 3.21e-19 | 1.03e-17 | +3104.2% | -9.98e-18 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | 1.65e-20 | 5.8e-19 | +3407.3% | -5.63e-19 |
| Thorium-232 [emissions to water/river] (Becquerel) | 3.02e-21 | 8.42e-20 | +2692.0% | -8.12e-20 |
| Uranium alpha [emissions to water/lake] (Becquerel) | 2.81e-21 | 7.72e-19 | +27400.9% | -7.7e-19 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | 3.02e-22 | 8.73e-21 | +2789.0% | -8.43e-21 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 0.00105 | 0.0417 | +3888.0% | -0.0407 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 1.81e-06 | 0.00261 | +144195.9% | -0.00261 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 0.00845 | 0.711 | +8313.9% | -0.703 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 2.19e-08 | 4.75e-06 | +21597.5% | -4.72e-06 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | 2.12e-18 | 1.45e-16 | +6742.9% | -1.43e-16 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | 6.74e-19 | 1.86e-17 | +2663.0% | -1.79e-17 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 0.00021 | 0.0218 | +10253.4% | -0.0216 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 2.68e-07 | 0.00153 | +568716.3% | -0.00153 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Chemically polluted water [emissions to water/river] (kilogram) | 0.000323 | 0.215 | +66529.8% |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.00122 | 0.544 | +44511.4% |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.012 | 2.57 | +21384.9% |
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.000424 | 0.0884 | +20758.5% |
| Platinum [air] (kilogram) | 0.000226 | 0.0305 | +13413.0% |
| Iron [Resources/Resources from ground] (kilogram) | 0.000196 | 0.0226 | +11416.5% |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.0003 | 0.034 | +11233.4% |
| Gravel [soil] (kilogram) | 0.0202 | 0.364 | +1703.4% |
| magnesium [Emissions/Emissions to water] (kilogram) | 0.000184 | 0.00291 | +1480.6% |
| Clay [soil] (kilogram) | 0.00134 | 0.0205 | +1429.7% |

## Structural checks

- ✓ 4 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 1.02 kg technosphere + 0 kg resources per 1 kg product (informational)
- ✓ all inputs resolved

residual: 97 flows under-explained, 1685 over-explained (negative residual)

## Evidence

- 2007 - LCI chemicals - Althaus.pdf — pages 436-438 -> report-p436-438.txt report sha256 68e0839ffea919f9…, text sha256 f7af81ba5953b5ff…
