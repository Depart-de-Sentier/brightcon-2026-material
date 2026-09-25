"""Re-import a mapped EcoSpold 2 export without changing its inventory."""


def reimport_ecospold2(directory, database, biosphere):
    """Read this export without ecoinvent-specific inventory/uncertainty repairs.

    All matching is by UUID. The XML already contains the approved inventory;
    re-running the BAFU migrations would apply some conversions a second time.
    """
    from functools import partial
    import bw2io as bi
    from bw2io.strategies import (
        assign_single_product_as_activity,
        create_composite_code,
        es2_assign_only_product_with_amount_as_reference_product,
        link_biosphere_by_flow_uuid,
        link_internal_technosphere_by_composite_code,
    )

    importer = bi.SingleOutputEcospold2Importer(
        str(directory),
        database,
        biosphere_database_name=biosphere,
        use_mp=False,
        add_product_information=False,
    )
    importer.strategies = [
        es2_assign_only_product_with_amount_as_reference_product,
        assign_single_product_as_activity,
        create_composite_code,
        partial(link_biosphere_by_flow_uuid, biosphere=biosphere),
        link_internal_technosphere_by_composite_code,
    ]
    importer.apply_strategies()
    if len(importer.applied_strategies) != len(importer.strategies):
        raise RuntimeError("An EcoSpold 2 linking strategy failed")
    # The ES2 extractor retains the signed amount but omits stats_arrays' flag.
    for ds in importer.data:
        for exc in ds["exchanges"]:
            if exc.get("uncertainty type") == 2:
                exc["negative"] = exc["amount"] < 0
    return importer
