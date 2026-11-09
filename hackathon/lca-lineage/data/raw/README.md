# Raw data

Download the source files yourself from the
[BAFU page on openLCA Nexus](https://nexus.openlca.org/database/BAFU).
Sign in or create an account if requested, select **BAFU:2026 version 1** and the
**EcoSpold 1** download, and read and accept the applicable terms in Nexus before
downloading or using the files. The
[BAFU terms of use](https://www.bafu.admin.ch/dam/fr/sd-web/-9ZObeMCZy8A/BAFU-20XY%20Terms%20of%20Use_EN%201.pdf)
are available for reference. A repository clone does not record licence acceptance.

Extract the source archive and put its XML files directly in the following folder,
relative to `hackathon/lca-lineage/`:

```text
data/raw/
├── README.md
├── ecoSpold files/
│   ├── process_<uuid>.xml
│   └── ...                     # 11,947 original XML files
└── BAFU-2026 v1 LCI Reports/    # Optional Nexus documentation download
    └── ...                     # 114 PDF inventory reports
```

If the archive has an enclosing directory, copy its XML files into `ecoSpold files/`
so the scripts can find them without a recursive search. The `.zolca` database and
LCIA results spreadsheet are not used by this workflow. The reports are optional
for running the repair and export scripts.

Keep source files unchanged and follow the [numbered reproduction steps](../../README.md#2-prepare-the-python-environment)
to prepare `bw`, validate the source count, repair the XML, and generate EcoSpold 2
under `../processed/`. Downloads and reports stay local and are ignored by Git.
