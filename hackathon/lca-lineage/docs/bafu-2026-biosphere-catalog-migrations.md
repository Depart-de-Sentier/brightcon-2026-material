# BAFU 2026 historical biosphere catalog mappings

This pass follows category normalization and the reviewed name/unit migration. The [catalog migration](../schemas/mappings/bafu-2026-biosphere-catalog.json) uses complete name/category/unit signatures **plus the source CAS number**. Missing CAS values are matched explicitly as empty. It renames flows only; amounts, uncertainty, units, compartments, comments, and original CAS values remain unchanged.

## Evidence

The first pass left metal names unresolved because selecting an oxidation state from a generic chemical name would be an assumption. Further evidence establishes historical catalog continuity:

- The installed bw2io 0.9.17 file `data/lci/ecoinvent elementary flows 2-3.xlsx` records old elementary-flow names, units, compartments, CAS numbers, and their ecoinvent v3 UUIDs. Rows whose destination metadata was highlighted as modified by bw2io were excluded. Accepted UUIDs were checked against the actual biosphere 3.10 target, with identical compartment and unit.
- `data/lci/ecoinvent elementary flows 3.9.xml` supplies official catalog names and synonyms tied to UUIDs. A unique current target was required, and chemical identifiers were checked against the old/current catalog identifiers.
- The [official ecoinvent 3.9 change report](https://support.ecoinvent.org/hubfs/Change-Report-v3.9.pdf) documents historical metal renames, including Chromium → Chromium III. The [3.9 release notes](https://support.ecoinvent.org/ecoinvent-version-3.9) explain that the nomenclature update includes names, CAS numbers, formulas, and synonyms.
- The [official ecoinvent 3.10 change report](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Database/Releases/Change%20Report%20v3.10%20-%2020231214.pdf?hsLang=en), pp. 15–17, documents further elementary-flow renames.

These are mappings between historical catalog definitions, not claims of measured chemical speciation in the BAFU inventories. For example, generic `Copper` emissions follow the documented `Copper ion` target; no particular copper oxidation state is invented. `Chromium` normally follows the documented Chromium III convention, but one source explicitly identifies chromium(VI) by CAS 018540-29-9. That occurrence instead maps to Chromium VI. The source CAS values are retained for traceability even when a catalog's historical CAS definition changed.

Historical land-use correspondences also retain the documented UUID: for example, `water bodies, artificial` maps to `lake, artificial`, whereas `water courses, artificial` maps to `river, artificial`. Some historical classifications became more specific in ecoinvent v3; the mapping follows the supplied correspondence and does not assert newly measured irrigation or land-management conditions.

A synonym entry alone was not accepted when it identified a different chemical: Metiram → Zineb is excluded. The Cyfluthrin → Beta-cyfluthrin correspondence, by contrast, retains the actual historical UUID and catalog CAS rather than selecting a target from chemical similarity.

## Audit

The migration has 464 CAS-specific rules. The detailed local audit in `reports/generated/biosphere-catalog-evidence.json` records every source signature, source CAS, target UUID and CAS, occurrence count, example consuming file, and the original correspondence-sheet row or master-data synonym record. `reports/generated/biosphere-catalog-conflicts.json` records rejected CAS conflicts; none remained after the explicit chromium(VI) exception.

The notebook applies the catalog file using the existing bw2io helper. The helper validates unique destinations before applying the migration, rejects stale existing source links, and relinks with the full name/category/unit combination. Source CAS is used to select the correction, while target matching follows the corrected flow signature.

This step does not create new elementary flows or discard any exchanges. Its unresolved report is `reports/generated/biosphere-unlinked-after-catalog.json`. The preceding name/unit result is retained separately in `reports/generated/biosphere-unlinked-after-flows.json`.

## Full-collection verification

In the `bw` environment, this pass linked **68,318 additional exchanges**, leaving **24,607 unlinked occurrences across 637 name/category/unit signatures**, with **269,140 linked biosphere exchanges**. All 11,947 datasets and 420,063 inventory rows remained. An independent complete-record comparison checked that only the declared names and new links changed, with unique targets, original CAS values retained, non-biosphere records unchanged, and identical results on reapplication. No inventory database was written. The local check report is `reports/generated/biosphere-catalog-migration-check.json`; its internal signature count additionally distinguishes source CAS values.
