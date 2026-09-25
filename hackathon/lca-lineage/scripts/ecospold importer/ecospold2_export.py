"""Write linked BAFU inventories as EcoSpold 2, preserving numeric precision.

Elementary-flow IDs come from the selected biosphere. Other IDs belong to an
explicit, deterministic BAFU export context, not the ecoinvent master catalog.
"""

import hashlib
import json
import math
from pathlib import Path
from uuid import NAMESPACE_URL, UUID, uuid5

from lxml import etree
from pyecospold import Defaults
from tqdm import tqdm

from metadata_extractors import extract_exchange_metadata, pm_es2


NS = "http://www.EcoInvent.org/EcoSpold02"
LANG = "{http://www.w3.org/XML/1998/namespace}lang"
CONTEXT = uuid5(
    NAMESPACE_URL,
    "https://github.com/romainsacchi/lca-data-lineage-hackathon/BAFU-2026-mapped",
)
SOURCE_INDEX = "bafu source exchange index"


def uid(kind, value):
    return str(uuid5(CONTEXT, f"{kind}:{value}"))


def ids(ds):
    return uid("activity", ds["filename"]), uid("product", ds["filename"])


def dumps(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True)


def number(value):
    if not math.isfinite(float(value)):
        raise ValueError(f"Non-finite inventory quantity: {value!r}")
    return repr(float(value))


def label(value):
    """A reversible display alias; matching continues to use UUIDs, never labels."""
    if len(value) <= 120:
        return value
    return value[:107] + " [" + hashlib.sha256(value.encode()).hexdigest()[:10] + "]"


def element(parent, tag, text=None, **attrs):
    el = etree.SubElement(
        parent, f"{{{NS}}}{tag}", {k: str(v) for k, v in attrs.items()}
    )
    if text is not None:
        el.text = str(text)
    return el


def language(parent, tag, text, **kwargs):
    el = element(parent, tag, text, **kwargs)
    el.set(LANG, "en")
    return el


def paragraph(parent, tag, text):
    if text:
        wrapper = element(parent, tag)
        # Separate indexed text blocks retain arbitrarily long source comments.
        for i, start in enumerate(range(0, len(text), 32000), 1):
            el = language(wrapper, "text", text[start : start + 32000])
            el.set("index", str(i))


def add_uncertainty(parent, exc, metadata: dict | None = None):
    kind = exc.get("uncertainty type", 0)
    if kind in (0, 1, None):
        return
    unc = element(parent, "uncertainty")
    if kind in (2, 3):
        attrs = {
            "meanValue": number(exc["amount"]),
            "varianceWithPedigreeUncertainty": number(exc["scale"] ** 2),
        }
        if kind == 2:
            attrs["mu"] = number(exc["loc"])
        else:
            attrs["meanValue"] = number(exc["loc"])
        element(unc, "lognormal" if kind == 2 else "normal", **attrs)
    elif kind == 4:
        element(
            unc,
            "uniform",
            minValue=number(exc["minimum"]),
            maxValue=number(exc["maximum"]),
        )
    elif kind == 5:
        element(
            unc,
            "triangular",
            minValue=number(exc["minimum"]),
            mostLikelyValue=number(exc["loc"]),
            maxValue=number(exc["maximum"]),
        )
    else:
        raise ValueError(f"Unsupported uncertainty type {kind}")

    # add pedigree matrix if present in metadata
    pm_str = "pedigreeMatrix"

    if metadata and pm_str in metadata:
        # if values are 0 consider that it should be 5 instead (no data)
        pm = metadata[pm_str]
        element(
            unc,
            pm_str,
            **{k: min(pm.get(k, 5) or 5, 5) for k in pm_es2}
        )


def audit_and_exclude(data, source, audit_dir):
    """Save each unresolved biosphere occurrence before removing any of them.

    Indexes are attached AFTER migrations: the Pd/Rh rule intentionally requires
    its two input dictionaries to be identical before assigning pair members.
    """
    audit_dir.mkdir(parents=True, exist_ok=True)
    excluded = 0
    manifest = []
    if any(
        not e.get("input") and e["type"] != "biosphere"
        for ds in data
        for e in ds["exchanges"]
    ):
        raise ValueError("Unlinked non-biosphere exchanges cannot be excluded")
    with (audit_dir / "excluded-exchanges.jsonl").open("x", encoding="utf-8") as out, (
        audit_dir / "source-metadata.jsonl"
    ).open("x", encoding="utf-8") as meta:
        for ds in tqdm(data, desc="Audit exclusions", unit="dataset", mininterval=0.5):
            path = Path(source) / ds["filename"]
            payload = path.read_bytes()
            root = etree.fromstring(payload)
            rows = root.findall("{*}dataset/{*}flowData/{*}exchange")
            if len(rows) != len(ds["exchanges"]):
                raise ValueError(f"Source exchange count changed: {path.name}")
            checksum = hashlib.sha256(payload).hexdigest()
            manifest.append({"file": path.name, "sha256": checksum})
            meta.write(
                dumps(
                    {
                        "file": path.name,
                        "sha256": checksum,
                        "metadata_xml": etree.tostring(
                            root.find("{*}dataset/{*}metaInformation"),
                            encoding="unicode",
                        ),
                    }
                )
                + "\n"
            )
            for index, exc in enumerate(ds["exchanges"]):
                if SOURCE_INDEX in exc:
                    raise ValueError("Export source indexes already assigned")
                if not exc.get("input"):
                    out.write(
                        dumps(
                            {
                                "dataset": {
                                    k: ds.get(k)
                                    for k in (
                                        "database",
                                        "code",
                                        "filename",
                                        "name",
                                        "reference product",
                                        "location",
                                        "unit",
                                    )
                                },
                                "source_sha256": checksum,
                                "source_exchange_index": index,
                                "source_exchange_xml": etree.tostring(
                                    rows[index], encoding="unicode"
                                ),
                                "reason": "No supported biosphere 3.10 target after approved migrations",
                                "exchange": exc,
                            }
                        )
                        + "\n"
                    )
                    excluded += 1
    # Both files have been closed successfully before the exclusion takes effect.
    for ds in data:
        retained = []
        for index, exc in enumerate(ds["exchanges"]):
            if exc.get("input"):
                exc[SOURCE_INDEX] = index
                retained.append(exc)
        ds["exchanges"] = retained
    with (audit_dir / "retained-inventory.jsonl").open("x", encoding="utf-8") as out:
        for ds in data:
            out.write(dumps(ds) + "\n")
    return excluded, manifest


def dataset_xml(ds, datasets, biosphere, source):
    activity_id, product_id = ids(ds)
    tags = dict(ds["tags"])
    activity_type = int(tags.get("ecoSpold01type", 1))
    if activity_type not in (1, 2):
        raise ValueError(f"Unsupported EcoSpold 1 dataset type: {activity_type}")
    original = etree.parse(str(Path(source) / ds["filename"]))
    root = etree.Element(f"{{{NS}}}ecoSpold", nsmap={None: NS})
    dataset = element(root, "activityDataset")
    description = element(dataset, "activityDescription")
    activity = element(
        description,
        "activity",
        id=activity_id,
        activityNameId=uid("activity-name", ds["name"]),
        activityNameContextId=CONTEXT,
        type=activity_type,
        specialActivityType="0",
        energyValues=tags.get("ecoSpold01energyValues", 0),
    )
    language(activity, "activityName", label(ds["name"]))
    paragraph(
        activity,
        "generalComment",
        "Full activity name: "
        + ds["name"]
        + "\n"
        + ds.get("comment", "")
        + "\nBAFU mapped export: unsupported biosphere exchanges excluded; see audit/. "
        "Local UUIDs and generic activity classification are export conventions. "
        f"Source: {ds['filename']}",
    )
    geo = element(
        description,
        "geography",
        geographyId=uid("geography", ds["location"]),
        geographyContextId=CONTEXT,
    )
    language(geo, "shortname", ds["location"])
    paragraph(geo, "comment", ds.get("comments", {}).get("location", ""))
    tech = element(description, "technology")
    paragraph(tech, "comment", ds.get("comments", {}).get("technology", ""))
    period = element(
        description,
        "timePeriod",
        startDate=tags["ecoSpold01startDate"],
        endDate=tags["ecoSpold01endDate"],
        isDataValidForEntirePeriod=str(
            tags["ecoSpold01dataValidForEntirePeriod"]
        ).lower(),
    )
    paragraph(period, "comment", ds.get("comments", {}).get("timePeriod", ""))
    scenario = element(
        description,
        "macroEconomicScenario",
        macroEconomicScenarioId=uid("scenario", "unspecified"),
        macroEconomicScenarioContextId=CONTEXT,
    )
    language(scenario, "name", "Unspecified in BAFU source")
    flow_data = element(dataset, "flowData")
    # The XSD requires all intermediate exchanges before elementary exchanges.
    exchanges = sorted(ds["exchanges"], key=lambda e: e["type"] == "biosphere")
    for exc in exchanges:
        target_key = tuple(exc["input"])
        is_bio = exc["type"] == "biosphere"
        if exc["type"] not in {"biosphere", "production", "technosphere"}:
            raise ValueError(f"Unsupported exchange type: {exc['type']}")
        target = biosphere[target_key] if is_bio else datasets[target_key]
        if exc["unit"] != target["unit"]:
            raise ValueError(f"Exchange and supplier units differ: {exc}")
        attrs = {
            "id": uid("exchange", f"{ds['filename']}:{exc[SOURCE_INDEX]}"),
            "amount": number(exc["amount"]),
            "unitId": uid("unit", target["unit"]),
            "unitContextId": CONTEXT,
        }
        if is_bio:
            attrs["elementaryExchangeId"] = str(UUID(target_key[1]))
        else:
            attrs["activityLinkId"], attrs["intermediateExchangeId"] = ids(target)
            attrs["activityLinkContextId"] = attrs["intermediateExchangeContextId"] = (
                CONTEXT
            )

        # extracting metadata from comment
        raw_data = exc.get("comment", "")

        metadata = extract_exchange_metadata(raw_data)

        src_metadata = metadata.get("source", {})

        if src_metadata:
            # max length authorized is 40 char
            attrs.update({
                f"source{k[0].upper()}{k[1:]}": src_metadata[k][:40]
                for k in ("firstAuthor", "year")
                if k in src_metadata
            })
            # value_for_uuid = "_".join(("-".join((k, v)) for k, v in src_metadata.items())
            # comment_metadata["sourceId"] = uuid("source", value_for_uuid)

        # create element
        el = element(
            flow_data,
            "elementaryExchange" if is_bio else "intermediateExchange",
            **attrs,
        )

        full_name = target["name"] if is_bio else target["reference product"]
        language(el, "name", label(full_name))
        language(el, "unitName", target["unit"])
        details = {k: v for k, v in exc.items() if k.startswith("bafu ")}

        # comment
        comment = (
            "Full flow name: "
            + full_name
            + "\n"
            + raw_data
            + "\nBAFU mapping audit: "
            + dumps(details)
        )
        if len(comment) > 32000:
            comment = f"Full comment and audit in audit/retained-inventory.jsonl; {ds['filename']}, exchange {exc[SOURCE_INDEX]}"

        language(el, "comment", comment)

        add_uncertainty(el, exc, metadata)

        if is_bio:
            categories = target["categories"]
            comp = element(
                el,
                "compartment",
                subcompartmentId=uid("compartment", dumps(categories)),
                subcompartmentContextId=CONTEXT,
            )
            language(comp, "compartment", categories[0])
            language(
                comp,
                "subcompartment",
                categories[1] if len(categories) > 1 else "unspecified",
            )
            element(
                el,
                "inputGroup" if categories[0] == "natural resource" else "outputGroup",
                4,
            )
        else:
            element(
                el,
                "outputGroup" if exc["type"] == "production" else "inputGroup",
                0 if exc["type"] == "production" else 5,
            )
    element(dataset, "modellingAndValidation")
    admin = element(dataset, "administrativeInformation")
    source_admin = original.find(".//{*}administrativeInformation")
    people = {p.get("number"): p for p in source_admin.findall("{*}person")}
    for name in ("dataEntryBy", "dataGeneratorAndPublication"):
        source_record = source_admin.find("{*}" + name)
        person = people[source_record.get("person")]
        attrs = {
            "personId": uid("person", dumps(dict(person.attrib))),
            "personContextId": CONTEXT,
            "personName": person.get("name"),
            "personEmail": person.get("email"),
        }
        if name == "dataGeneratorAndPublication":
            attrs["isCopyrightProtected"] = source_record.get("copyright")
        element(admin, name, **attrs)
    attributes = element(
        admin,
        "fileAttributes",
        majorRelease="2026",
        minorRelease="0",
        majorRevision="1",
        minorRevision="0",
        defaultLanguage="en",
        contextId=CONTEXT,
        fileGenerator="BAFU mapped EcoSpold 2 export",
        internalSchemaVersion="2.0.14",
    )
    language(
        attributes, "contextName", "BAFU 2026 mapped export; local supporting UUIDs"
    )
    return root


def export_datasets(data, biosphere, source, destination):
    destination.mkdir(parents=True, exist_ok=True)
    by_key = {(ds["database"], ds["code"]): ds for ds in data}
    if len(by_key) != len(data):
        raise ValueError("Duplicate activity codes")
    schema = etree.XMLSchema(file=Defaults.SCHEMA_V2_FILE)
    manifest = []
    for ds in tqdm(
        data, desc="Export and validate XML", unit="dataset", mininterval=0.5
    ):
        if len([e for e in ds["exchanges"] if e["type"] == "production"]) != 1:
            raise ValueError(f"Expected one reference product in {ds['filename']}")
        root = dataset_xml(ds, by_key, biosphere, source)
        try:
            schema.assertValid(root)
        except etree.DocumentInvalid as error:
            raise ValueError(f"{ds['filename']}: {error}") from error
        activity_id, product_id = ids(ds)
        name = f"{activity_id}_{product_id}.spold"
        payload = etree.tostring(
            root, encoding="utf-8", xml_declaration=True, pretty_print=True
        )
        with (destination / name).open("xb") as out:
            out.write(payload)
        manifest.append(
            {
                "file": name,
                "source": ds["filename"],
                "code": ds["code"],
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        )
    return manifest
