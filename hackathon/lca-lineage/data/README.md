# Data

The BAFU database files are not included in the current repository tree. Download
**BAFU:2026 version 1, EcoSpold 1** from
[openLCA Nexus](https://nexus.openlca.org/database/BAFU) and accept the applicable
terms before downloading or using them.

- [`raw/`](raw/README.md): original downloaded XML files and optional supporting reports.
- [`processed/`](processed/README.md): repaired copies and the locally generated EcoSpold 2 export.

Follow the [numbered reproduction steps](../README.md#1-download-the-bafu-source-files-and-accept-the-terms)
for environment setup, source placement, repairs, export, and verification. All
database payloads under these folders are ignored by Git. Only the folder
instructions are tracked; do not force-add downloads or generated inventories.
