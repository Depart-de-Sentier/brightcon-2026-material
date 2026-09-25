"""The reviewed notebook migration sequence, reusable from command-line scripts."""

from collections import Counter
from pathlib import Path

from tqdm import tqdm

# Explicit order: candidate mappings must never be discovered automatically.
BIOSPHERE_STAGES = (
    "categories",
    "flows",
    "catalog",
    "resources",
    "reviewed",
    "water-context",
    "chemistry",
    "gas-units",
    "land-resources",
    "followup",
    "compartments",
    "source-review",
    "context",
    "plastics-source-review",
    "eps-metals",
    "plastics-conversions",
    "plastics-chemicals",
    "historical-names",
    "nitrogen-dioxide",
    "land-mosaic",
    "diesel-carbon",
    "uranium-convention",
    "wood-density",
    "pm10-metals",
)


def counts(data):
    result = Counter(datasets=len(data))
    for ds in data:
        for exc in ds["exchanges"]:
            result["exchanges"] += 1
            result[exc["type"]] += 1
            if not exc.get("input"):
                result["unlinked_" + exc["type"]] += 1
    return dict(result)


def import_mapped(source, database, biosphere, mapping_dir, reports):
    """Extract unchanged XML, apply standard ES1 strategies, then all approved rules."""
    import bw2data as bd
    import bw2io as bi
    from biosphere_migrations import (
        apply_biosphere_category_migration,
        apply_biosphere_flow_migration,
    )
    from date_compat import xml_date_parser
    from technosphere_migrations import apply_technosphere_migrations
    from timestamp_compat import iso_timestamp_parser

    if bd.config.biosphere != biosphere:
        raise ValueError(f"Project default biosphere must be {biosphere!r}")
    with iso_timestamp_parser(), xml_date_parser():
        importer = bi.SingleOutputEcospold1Importer(str(source), database, use_mp=False)
    importer.apply_strategies()
    if len(importer.applied_strategies) != len(importer.strategies):
        raise RuntimeError("An EcoSpold 1 importer strategy failed")
    apply_technosphere_migrations(importer, mapping_dir)
    before = len(importer.applied_strategies)
    importer.match_database(
        fields=["name", "reference product", "location"], edge_kinds=["technosphere"]
    )
    if len(importer.applied_strategies) != before + 1:
        raise RuntimeError("Final technosphere matching failed")
    for stage in tqdm(BIOSPHERE_STAGES, desc="Biosphere mappings", unit="stage"):
        apply = (
            apply_biosphere_category_migration
            if stage == "categories"
            else apply_biosphere_flow_migration
        )
        apply(
            importer,
            Path(mapping_dir) / f"bafu-2026-biosphere-{stage}.json",
            biosphere,
            Path(reports) / f"after-{stage}.json",
        )
    return importer
