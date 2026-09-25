# Remaining resource definitions

The source review resolved one additional peat exchange and originally recorded **32 resource occurrences across 12 signatures** lacking a supported link. These counts exclude land and the method-specific recycling corrections. No unresolved resource is dropped or converted using a guessed factor.

The later [approved uranium and wood conventions](bafu-2026-biosphere-targeted-reassessment.md#approved-uranium-and-wood-conversions) resolve nine of these occurrences, leaving **23 resource occurrences across nine signatures**. The table below preserves the source findings that motivated those explicit assumptions.

## Resolved: peat energy

The ethylene inventory's `Energy, from peat` exchange is **0.000018403 MJ**. Original PlasticsEurope process `b748263b-2419-415b-98a1-cd78f7e6fc77`, version `00.00.001`, exchange 94, records 0.00001840272 MJ, agreeing to BAFU rounding precision.

Its [ILCD flow](https://eplca.jrc.ec.europa.eu/SDPDB/datasetdetail/elementaryFlow.xhtml?uuid=e2fba107-6555-11dd-ad8b-0800200c9a66&version=03.00.000) specifies **8.4 MJ/kg**. Dividing the current BAFU quantity by 8.4 gives **0.0000021908333333333333 kg**. The target is `Peat / natural resource, biotic / kilogram`, UUID `c5035ce2-5ee5-431f-a287-4b25da42be74`, using the catalog classification already applied to the earlier peat mass row.

There are errors in the source flow-property references. The PlasticsEurope copy gives the correct energy-property URI and description but a Mass UUID; it separately gives a mass conversion of 0.119047619047619. The JRC copy uses the correct energy-property UUID despite a misleading Radioactivity description. The JRC reference property, stated calorific value, and explicit mass conversion agree. This is a source-defined conversion, not an assumed average fuel value.

The rule is part of the [plastics conversions](bafu-2026-biosphere-plastics-conversions.md). It retains the original name, MJ unit, in-ground compartment, flow UUID and conversion basis. Amount and uncertainty scale together. The helper allows the biotic category only for this identified peat flow; other energy conversions retain their original category.

## Original unresolved findings (before approved uranium/wood conventions)

| Resource | Occurrences | Source finding and remaining gap |
| --- | ---: | --- |
| Bauxite | 8 | The [source definition](https://plasticseurope.lca-data.com/resource/flows/08a91e70-3ddc-11dd-97dd-0050c2490048?format=xml&version=03.00.000) specifies ore mass without aluminium grade. A contained-aluminium conversion needs that grade. |
| Uranium energy | 7 | The [version 3 flow](https://eplca.jrc.ec.europa.eu/SDPDB/datasetdetail/elementaryFlow.xhtml?uuid=3e4d2966-6556-11dd-ad8b-0800200c9a66&version=03.00.000) establishes an MJ basis but gives no energy-per-kg value. Reactor and fuel-cycle assumptions cannot be inferred from the resource label. |
| Sodium chloride from water | 7 | The [original flow](https://plasticseurope.lca-data.com/resource/flows/79552971-cc21-5963-5d61-000051b1827e?format=xml&version=01.00.000) explicitly describes sodium chloride in seawater. The catalog's same-name mass target specifies extraction from ground. |
| Sodium bromide | 2 | The [original flow](https://plasticseurope.lca-data.com/resource/flows/d13f914a-0c17-46ae-bd20-fbbfff065c1a?format=xml&version=35.00.000) confirms NaBr, CAS 7647-15-6, mass basis and extraction from ground. The available Bromine target specifies extraction from water. The chemical formula is resolved; the compartment mismatch remains. |
| Oil energy | 2 | The burnt-shale and cement inventories cite the 2020 concrete report. Section 3.6 describes oil shale and electricity coproduction, without establishing these two energy rows as crude oil or providing a compatible mass factor. A crude-oil conversion is therefore unsupported. |
| Standing wood | 2 | EPS references [wood energy at 14.7 MJ/kg](https://eplca.jrc.ec.europa.eu/SDPDB/datasetdetail/elementaryFlow.xhtml?uuid=3e4d9eab-6556-11dd-ad8b-0800200c9a66&version=03.00.000), while BAFU labels the unchanged quantity kg. The recycling-paper row is wood mass. Neither establishes density/moisture for the standing-wood target in cubic metres. |
| Air | 1 | No reviewed corresponding resource aggregate target. |
| Hydro-labelled EPS energy | 1 | The original EPS row is wave energy. A hydropower-reservoir target would change its meaning. |
| Waste-heat resource input | 1 | The steel row concerns internal electricity/steam. A waste-heat emission target has a different exchange direction and meaning. |
| Soil | 1 | No reviewed corresponding resource aggregate target or mineral composition. |
| **Total unresolved** | **32** | |

These findings do not authorize changing ground extraction to water extraction, replacing an ore with an assumed elemental grade, or treating a resource input as an emission.

The generated evidence file `reports/generated/biosphere-resource-followup-review.json` records all consuming filenames, quantities, findings and source hashes. Original flow XML is cached under `reports/generated/plasticseurope-source-review/`. Peat's applied-rule evidence is in `biosphere-plastics-conversions-evidence.json`.
