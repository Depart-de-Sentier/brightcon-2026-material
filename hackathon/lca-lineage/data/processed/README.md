# Processed data

Generated database files are not included in the current repository tree. First
download BAFU:2026 version 1 in EcoSpold 1 format from
[openLCA Nexus](https://nexus.openlca.org/database/BAFU), accepting its terms, and
place the XML as described in the [raw-data instructions](../raw/README.md).

Then follow the [environment setup and reproduction steps](../../README.md#2-prepare-the-python-environment).
From `hackathon/lca-lineage/`, with the `bw` environment prepared:

```bash
conda run --no-capture-output -n bw python "scripts/ecospold importer/repair_all.py"
conda run --no-capture-output -n bw python "scripts/ecospold importer/import_export_ecospold2.py"
```

The first command creates and validates `ecospold1-schema-fixed/`; the second
produces `ecospold2-biosphere310/`, including `datasets/*.spold`, `MasterData/`,
audits, a manifest, and the re-import helper. No baseline import is required between
the two commands. First use downloads the Brightway biosphere project.

The documented release yields 11,947 datasets, 417,072 retained exchanges, and
2,991 audited exclusions. See the [export documentation](../../docs/bafu-2026-ecospold2-export.md)
for checks, reruns with unused output/database names, uncertainty preservation,
and the scope of modifications. All generated payloads stay local and are ignored
by Git; do not force-add them.

