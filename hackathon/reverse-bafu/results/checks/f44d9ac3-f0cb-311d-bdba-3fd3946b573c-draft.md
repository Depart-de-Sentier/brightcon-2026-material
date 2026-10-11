# Check: Acetone, liquid, at plant (f44d9ac3-f0cb-311d-bdba-3fd3946b573c)

target `bafu-2026` vs explicit model `f44d9ac3-f0cb-311d-bdba-3fd3946b573c-draft-disagg` and hybrid `f44d9ac3-f0cb-311d-bdba-3fd3946b573c-draft-hybrid`

**Strategy:** S1 — transcription drafted from the report excerpt by the LLM pipeline (reverse-bafu draft). basis: per 1000 kg of acetone, the basis of the only quantitative statement in the chapter (sec. 1.5.2, citing Wells 1999); allocation: None. Acetone and phenol are co-products of the cumene process - 'Acetone and phenol are co-products and their production and demand are intertwined' - and the excerpt states that the cumene figure excludes the phenol ('The production of the co-product phenol is not included in this figure'), i.e. 100 % of the cumene is charged to the acetone. No burden is shifted to phenol here either.; 1 of 1 inputs carry a printed amount, 0 a printed range, 0 no number in the report. Review every derivation; unreviewed entries have reviewed_by = null.
**Calibrated inputs:** none
**Links to rebuilt nodes:** none

## Flow agreement (explicit vs target, per elementary flow)

- the 50 largest kilogram flows: 1/50 within ±10 %, median |Δ| 123.6%
- kilogram mass covered within ±10 %: 0.0% of the target's total kg mass
- of the 1782 flows of the target, 1666 are determined by the solve (116 are round-off and are not scored; see lci.determined_flows)
- 1 of those 1666 within ±10 % (0%), median |Δ| 36139.8%, 0 missing from the model, 0 extra
- hybrid vs target: 6 flows differ

| \|Δ\| bucket | flows | share of target flows |
|---|---|---|
| ≤ 10 % | 1 | 0% |
| 10–20 % | 0 | 0% |
| 20–50 % | 10 | 1% |
| 50–100 % | 41 | 2% |
| > 100 % | 1730 | 97% |
| missing (0 in model) | 0 | 0% |

## Largest target flows (by amount, per unit) and their agreement

### kilogram (1467 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 1.8 | 4.06 | +125.8% | -2.26 |
| Sodium chloride [resources/in ground] (kilogram) | 0.0762 | 0.00484 | -93.6% | +0.0714 |
| Methane (fossil) [Emissions/Emissions to air] (kilogram) | 0.0171 | 0.0302 | +76.7% | -0.0131 |
| Calcite [resources/in ground] (kilogram) | 0.008 | 0.0319 | +298.4% | -0.0239 |
| Sulfate Ion [water] (kilogram) | 0.00772 | 0.00201 | -73.9% | +0.0057 |
| Sodium [water] (kilogram) | 0.00721 | 0.00176 | -75.7% | +0.00546 |
| Sulfur Dioxide [Emissions/Emissions to air] (kilogram) | 0.00688 | 0.00883 | +28.4% | -0.00196 |
| Carbon Dioxide (biogenic) [Emissions/Emissions to air] (kilogram) | 0.00478 | 0.0413 | +765.8% | -0.0366 |
| Nitrogen Oxides [Emissions/Emissions to air] (kilogram) | 0.0046 | 0.0066 | +43.5% | -0.002 |
| Gravel [soil] (kilogram) | 0.00403 | 0.236 | +5751.8% | -0.232 |
| Non-methane Volatile Organic Compounds [Emissions/Emissions to air] (kilogram) | 0.00352 | 0.00532 | +50.9% | -0.00179 |
| Chloride [Emissions/Emissions to water] (kilogram) | 0.00305 | 0.00576 | +88.6% | -0.00271 |
| Sulfur [Resources/Resources from ground] (kilogram) | 0.00239 | 0.000154 | -93.6% | +0.00224 |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.00231 | 0.0921 | +3889.3% | -0.0898 |
| Carbon Monoxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.00187 | 0.00525 | +180.8% | -0.00338 |
| Suspended Solids, Unspecified [water] (kilogram) | 0.00181 | 0.000389 | -78.5% | +0.00142 |
| Silicon [Emissions/Emissions to water] (kilogram) | 0.00137 | 0.00929 | +579.5% | -0.00792 |
| COD, Chemical Oxygen Demand [emissions to water/groundwater, long-term] (kilogram) | 0.00104 | 0.00258 | +147.1% | -0.00153 |
| Sulfate [emissions to water/groundwater, long-term] (kilogram) | 0.00104 | 0.0299 | +2772.7% | -0.0289 |
| Oils, Unspecified [Emissions/Emissions to water] (kilogram) | 0.000778 | 0.000104 | -86.6% | +0.000674 |

### kilo Becquerel (171 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.638 | 235 | +36797.4% | -235 |
| Noble Gases, Radioactive, Unspecified [air] (kilo Becquerel) | 0.223 | 83.3 | +37288.0% | -83.1 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.00897 | 3.35 | +37293.0% | -3.35 |
| Radon-222 [Emissions/Emissions to air] (kilo Becquerel) | 0.00584 | 2.17 | +37011.1% | -2.16 |
| Hydrogen-3 [Emissions/Emissions to water] (kilo Becquerel) | 0.00411 | 0.904 | +21903.3% | -0.9 |

### square meter (50 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| To Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 2.77e-06 | 0.00185 | +66784.2% | -0.00185 |
| From Pasture/meadow [Land use/Land transformation] (square meter) | 2.55e-06 | 0.000578 | +22586.9% | -0.000576 |
| From Arable, Non-irrigated, Intensive [Land use/Land transformation] (square meter) | 1.96e-06 | 0.00131 | +66937.3% | -0.00131 |
| To Arable, Non-irrigated [Land use/Land transformation] (square meter) | 1.37e-06 | 0.000768 | +55883.0% | -0.000766 |
| To Forest [Land use/Land transformation] (square meter) | 1.31e-06 | 0.000219 | +16653.6% | -0.000218 |

### megajoule (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Natural Gas [Resources/Resources from ground] (megajoule) | 33.9 | 60.7 | +79.0% | -26.8 |
| Waste Heat [air] (megajoule) | 29.2 | 60.4 | +106.8% | -31.2 |
| Crude Oil [Resources/Resources from ground] (megajoule) | 25.5 | 96 | +275.9% | -70.5 |
| Uranium [Resources/Resources from ground] (megajoule) | 2.26 | 7.7 | +240.3% | -5.44 |
| Hard Coal [Resources/Resources from ground] (megajoule) | 1.64 | 3.05 | +85.4% | -1.4 |

### square meter-year (27 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Forest, Intensive [Land use/Land occupation] (square meter-year) | 0.000103 | 0.0434 | +41966.4% | -0.0433 |
| Traffic Area, Road Network [Land use/Land occupation] (square meter-year) | 4.98e-05 | 0.00078 | +1466.4% | -0.000731 |
| Dump Site [Land use/Land occupation] (square meter-year) | 3.3e-05 | 0.000875 | +2549.2% | -0.000842 |
| Forest [Land use/Land occupation] (square meter-year) | 2.5e-05 | 0.0278 | +111470.4% | -0.0278 |
| Industrial Area [Land use/Land occupation] (square meter-year) | 9.09e-06 | 0.00418 | +45869.2% | -0.00417 |

### cubic meter (23 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Water [Emissions/Emissions to water] (cubic meter) | 0.0908 | 4.98 | +5389.4% | -4.89 |
| Water To Cooling [Resources/Resources from water] (cubic meter) | 0.0788 | 0.215 | +172.8% | -0.136 |
| Water to turbine [Resources/Resources from water] (cubic meter) | 0.0129 | 4.75 | +36761.1% | -4.73 |
| Water [Resources/Resources from water] (cubic meter) | 0.00312 | 0.0318 | +918.7% | -0.0287 |
| Water, salt, ocean [resources/in water] (cubic meter) | 0.0008 | 0.642 | +80126.0% | -0.641 |

### Becquerel (9 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Uranium alpha [emissions to water/river] (Becquerel) | 9.16e-22 | 7.05e-20 | +7594.8% | -6.96e-20 |
| Uranium alpha [emissions to water/lake] (Becquerel) | 4.29e-22 | 3.3e-20 | +7594.8% | -3.26e-20 |
| Uranium alpha [emissions to air/low. pop.] (Becquerel) | 7.8e-23 | 6e-21 | +7594.8% | -5.92e-21 |
| Thorium-232 [emissions to water/river] (Becquerel) | 9.26e-25 | 7.13e-23 | +7594.8% | -7.04e-23 |
| Thorium-232 [emissions to air/low. pop.] (Becquerel) | 2.74e-25 | 2.11e-23 | +7594.8% | -2.08e-23 |

### kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (kilometer) | 0.000242 | 0.0472 | +19359.5% | -0.0469 |
| Noise, road, passenger car, average [non material emissions/unspecified] (kilometer) | 6.06e-07 | 0.000814 | +134174.9% | -0.000814 |

### ton kilometer (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, rail, freight train [non material emissions/unspecified] (ton kilometer) | 0.00289 | 1.58 | +54466.2% | -1.58 |
| Noise, aircraft, freight [non material emissions/unspecified] (ton kilometer) | 7.92e-09 | 9.65e-06 | +121759.4% | -9.64e-06 |

### meter (2 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, road, lorry, average [non material emissions/unspecified] (meter) | -5.61e-19 | -2.36e-17 | +4103.3% | +2.3e-17 |
| Noise, road, passenger car, average [non material emissions/unspecified] (meter) | 8.66e-23 | 6.67e-21 | +7594.8% | -6.58e-21 |

### cubic meter-year (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Volume Occupied, Reservoir [land use] (cubic meter-year) | 7.44e-05 | 0.0308 | +41331.5% | -0.0307 |

### person kilometer (1 flows)

| flow | target | explicit | Δ | residual |
|---|---|---|---|---|
| Noise, aircraft, passenger [non material emissions/unspecified] (person kilometer) | 1.02e-07 | 0.000128 | +125839.8% | -0.000128 |

## Worst deviations among the 50 largest kilogram flows

| flow | target | explicit | Δ |
|---|---|---|---|
| Waste mass, total, placed in landfill [resources/in ground] (kilogram) | 0.000146 | 0.118 | +80716.3% |
| Platinum [air] (kilogram) | 9.43e-05 | 0.0468 | +49499.3% |
| carbon dioxide (biogenic) [Resources/Resources from air] (kilogram) | 0.000106 | 0.0501 | +47119.6% |
| Carbon Dioxide (fossil) [Emissions/Emissions to air] (kilogram) | 0.000455 | 0.127 | +27733.2% |
| Chemically polluted water [emissions to water/river] (kilogram) | 0.00012 | 0.0198 | +16385.4% |
| Clay [soil] (kilogram) | 0.000264 | 0.0397 | +14943.1% |
| Chemical Oxygen Demand [water] (kilogram) | 0.000438 | 0.0362 | +8170.4% |
| magnesium [Emissions/Emissions to water] (kilogram) | 6.23e-05 | 0.00459 | +7267.1% |
| calcium [Emissions/Emissions to water] (kilogram) | 0.000341 | 0.0231 | +6675.2% |
| Gravel [soil] (kilogram) | 0.00403 | 0.236 | +5751.8% |

## Structural checks

- ✓ 1 explicit input(s) over 1 node(s)
- ✓ no decomposed grid mixes
- ✓ no dependency on another system process
- ✓ mass in: 2.3 kg technosphere + 0 kg resources per 1 kg product (informational)
- ✓ all inputs resolved

residual: 46 flows under-explained, 1736 over-explained (negative residual)

## Evidence

- 2007 - LCI chemicals - Althaus.pdf — pages 98-99 -> report-p98-99.txt report sha256 68e0839ffea919f9…, text sha256 3d1e65fc1ab8cd34…
