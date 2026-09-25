"""Apply BAFU migrations, including exchange mappings scoped to a source file."""

import json
from pathlib import Path

from bw2io import Migration
from bw2io.utils import activity_hash

CONTEXT_FIELD = "_migration_source_file"


def apply_technosphere_migrations(importer, mapping_dir):
    """Read the current JSON files, migrate fresh importer data, and relink.

    The temporary source-file field distinguishes otherwise identical exchanges
    in different consuming datasets. It is removed before returning, even on error.
    Dataset codes stay stable so existing input references remain valid.
    """
    files = [
        Path(mapping_dir) / "bafu-2026-technosphere.json",
        Path(mapping_dir) / "bafu-2026-technosphere-context.json",
    ]
    mappings = []
    for path in files:
        mapping = json.loads(path.read_text(encoding="utf-8"))
        keys = []
        for source, replacement in mapping["data"]:
            if len(source) != len(mapping["fields"]) or not isinstance(replacement, dict):
                raise ValueError(f"Invalid migration row in {path.name}")
            keys.append(
                activity_hash(
                    dict(zip(mapping["fields"], source)), fields=mapping["fields"]
                )
            )
        if len(keys) != len(set(keys)):
            raise ValueError(f"Duplicate matching rules in {path.name}")
        mappings.append((path, mapping))

    if any(CONTEXT_FIELD in exc for ds in importer.data for exc in ds["exchanges"]):
        raise ValueError(f"Reserved migration field already present: {CONTEXT_FIELD}")
    if not all(ds.get("filename") for ds in importer.data):
        raise ValueError("Source filenames are required for contextual migrations")

    for path, mapping in mappings:
        Migration(path.stem).write(mapping, "BAFU 2026 documented technosphere mappings")
        contextual = CONTEXT_FIELD in mapping["fields"]
        if contextual:
            for ds in importer.data:
                for exc in ds["exchanges"]:
                    exc[CONTEXT_FIELD] = Path(ds["filename"]).name
        try:
            before = len(importer.applied_strategies)
            importer.migrate(path.stem)
            if len(importer.applied_strategies) != before + 2:
                raise RuntimeError(f"Migration failed: {path.stem}")
        finally:
            if contextual:
                for ds in importer.data:
                    for exc in ds["exchanges"]:
                        exc.pop(CONTEXT_FIELD, None)
        print(f"Applied {len(mapping['data'])} rules from {path.name}")

    before = len(importer.applied_strategies)
    importer.match_database(
        fields=["name", "categories", "unit", "location"],
        edge_kinds=["technosphere"],
    )
    if len(importer.applied_strategies) != before + 1:
        raise RuntimeError("Technosphere linking failed")
