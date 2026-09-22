# Historical names and exact chemical synonyms

The [two name rules](../schemas/mappings/bafu-2026-biosphere-historical-names.json) resolve **83 exchanges**: 82 urban-air exchanges labelled `Benzene, dichloro-` and one generic-air exchange labelled `1-Methyl-2-pyrrolidinone`. Their quantities, uncertainties and compartments remain unchanged.

## Dichlorobenzene evidence chain

| Step | Evidence |
| --- | --- |
| `Benzene, dichloro-` → `Benzene, dichloro` | The installed bw2io `data/simapro-biosphere.json` explicitly normalizes this legacy air-emission spelling. |
| `Benzene, dichloro` → `1,2-Dichlorobenzene` | Ecoinvent's [v3.9 change report](https://support.ecoinvent.org/hubfs/Change-Report-v3.9.pdf?hsLang=en), Table 3, page 15, records this elementary-exchange rename. Page 17 also associates `o-Dichlorobenzene` with the same new name. These pages were visually checked because much of the PDF is not text-extractable. |
| Official 1,2-dichlorobenzene → installed `o-Dichlorobenzene` | The official 3.9 master and installed 3.10 database share UUID `9645e02f-855a-4b9f-8baf-f34a08fa80c4`, CAS 95-50-1, kilogram unit and `air / urban air close to ground` compartment. The master lists `o-Dichlorobenzene` as a synonym. |

This follows the documented historical inventory naming convention. It does **not** infer isomer fractions for a measured unspecified dichlorobenzene mixture. The original name remains in `bafu original biosphere`, and the original missing BAFU CAS remains missing.

The dichlorobenzene rule selects the complete original signature and empty CAS. All 82 source files have that signature; none states a conflicting CAS. The target is unique. There is no unit conversion, compartment fallback, amount change or uncertainty change.

## N-methyl-2-pyrrolidone synonym

The [NIST Chemistry WebBook](https://webbook.nist.gov/cgi/cbook.cgi?ID=872-50-4) and [PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/13387) identify `1-Methyl-2-pyrrolidinone` and `N-Methyl-2-pyrrolidone` as names for CAS **872-50-4**, formula C5H9NO. This is a spelling correspondence, with no speciation or composition assumption.

BAFU file `process_417f3433-6ba6-351f-9b53-23ce5eba9fc9.xml` (`Cathode, lithium-ion battery, NMC111`) has one such air emission, **0.0056 kg**, citing the 2024 ICT inventory report. The same inventory uses N-methyl-2-pyrrolidone as a technosphere input. The unique target is `N-methyl-2-pyrrolidone / air / kilogram`, UUID **`bc97db5d-196f-4413-8d9b-ed5c8a0e0ce9`**, with matching CAS 872-50-4.

The rule matches the full biosphere/name/category/unit signature and empty source CAS. It retains the original name, category and unit in `bafu original biosphere`; the missing source CAS stays missing. Amount, uncertainty, compartment and the technosphere input are unchanged.

## Verification

The full `bw` check links **290,689 of 293,747 biosphere exchanges**, leaving **3,058 occurrences across 162 signatures** unresolved. All 11,947 datasets and 420,063 exchange rows remain, and every technosphere exchange links.

Complete-record verification permits only the declared name, original-label metadata and input link to change. The rules have 82 and one hits respectively; repeating them leaves all records unchanged. The regenerated worklist agrees with the importer. No inventory database was written, and the notebook's optional drop/write/LCA cells were excluded.

Evidence and all 83 source rows are recorded in `reports/generated/biosphere-historical-names-evidence.json`, including PDF, source-file and installed-catalog hashes. Verification is in `biosphere-historical-names-migration-check.json`.

The preceding plastics chemical stage writes `biosphere-unlinked-after-plastics-chemicals.json`. This stage writes `biosphere-unlinked-after-historical-names.json`; the subsequent approved NO₂ aggregation writes the final `biosphere-unlinked.json`.
