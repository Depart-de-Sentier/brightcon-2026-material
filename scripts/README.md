# Scripts

Add extraction, transformation, validation, and analysis scripts here.

- [Import repaired EcoSpold files (notebook)](import_fixed_ecospold.ipynb): use the `bw` kernel to create a project with biosphere 3.10, inspect the repaired-file import, and write the database if all exchanges link.
- [EcoSpold 1 import attempt](ecospold%20importer/README.md): run the standard Brightway importer on the original BAFU files using the `bw` conda environment and record the result.
- [Import with biosphere 3.10](ecospold%20importer/import_with_biosphere310.py): create a local Brightway project and try importing the repaired BAFU files against the ecoinvent 3.10 biosphere.
- [EcoSpold namespace repair](ecospold%20importer/repair_namespace.py): create modified copies with the missing namespace added and record source/output checksums.
- [EcoSpold date repair](ecospold%20importer/repair_dates.py): correct partial-date element types while preserving their values and precision.
- [EcoSpold metadata repair](ecospold%20importer/repair_metadata.py): handle publisher, company-code, and source-number constraints separately, preserving full originals in XML comments and repair logs.
- [EcoSpold administrative-order repair](ecospold%20importer/repair_administrative_order.py): reorder administrative elements while preserving their contents and attached comments.
- [EcoSpold date parser compatibility](ecospold%20importer/date_compat.py): enable optional parsing of calendar dates with timezone offsets during import, preserving the XML and stated calendar day.
- [EcoSpold exchange-number repair](ecospold%20importer/repair_exchange_numbers.py): make repeated exchange IDs unique within each dataset while retaining every inventory row and recording the original IDs.
- [Remaining EcoSpold schema repairs](ecospold%20importer/repair_schema.py): produce the final schema-valid copies with reversible edits and explicitly documented missing-field fallbacks.
- [Full collection validation](ecospold%20importer/validate_collection.py): validate every final file and compare all inventory rows with the raw release.
