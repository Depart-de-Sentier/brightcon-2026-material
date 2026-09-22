# Getting Started with OpenLineage

Here you can find some notes about getting the [OpenLineage quickstart](https://openlineage.io/getting-started/) running, plus the extra steps we needed that weren't in the official docs.

## Environment setup

WSL2 wouldn't install on the work laptop, so we used [GitHub Codespaces](https://github.com/features/codespaces) instead — it ships with Docker pre-installed, which is all the quickstart really needs.

### Extra steps required inside the Codespace

The default Codespace environment needs two adjustments before `docker compose up` runs cleanly:

1. **Raise the max map count** (Elasticsearch/OpenSearch-backed services need this):
   ```bash
   sudo sysctl -w vm.max_map_count=262144
   ```

2. **Switch iptables to legacy mode** (the Codespace default `nftables` backend can break Docker's networking rules):
   ```bash
   sudo update-alternatives --config iptables
   sudo update-alternatives --config ip6tables
   ```
   Select the `iptables-legacy` / `ip6tables-legacy` option when prompted.

> **Note:** neither setting persists across Codespace rebuilds — redo both after a rebuild.

## Sending lineage events

Once the instance is up, you can POST `RunEvent`s directly to the API. A `START` event, followed by a matching `COMPLETE` event for the same `runId`:

```bash
curl -sS -X POST http://localhost:5000/api/v1/lineage \
  -H 'Content-Type: application/json' \
  -d '{
    "eventTime": "2026-09-22T14:21:21Z",
    "eventType": "START",
    "producer": "https://github.com/sentier-dev/sentier-importers",
    "schemaURL": "https://openlineage.io/spec/2-0-2/OpenLineage.json#/$defs/RunEvent",
    "run": { "runId": "run-1" },
    "job": {
      "namespace": "sentier-importers",
      "name": "bafu.parse",
      "facets": {
        "documentation": {
          "_producer": "https://github.com/sentier-dev/sentier-importers",
          "_schemaURL": "https://openlineage.io/spec/facets/1-0-0/DocumentationJobFacet.json",
          "description": "Parse BAFU EcoSpold XML export into flat records."
        }
      }
    },
    "inputs": [{
      "namespace": "file:///home/laurenz/dds/sources/bafu-2026",
      "name": "BAFU-2026 v1_ecoSpold v1.zip",
      "facets": {
        "dataSource": {
          "_producer": "https://github.com/sentier-dev/sentier-importers",
          "_schemaURL": "https://openlineage.io/spec/facets/1-0-0/DatasourceDatasetFacet.json",
          "name": "BAFU",
          "uri": "https://www.bafu.admin.ch"
        }
      }
    }],
    "outputs": []
  }'

curl -sS -X POST http://localhost:5000/api/v1/lineage \
  -H 'Content-Type: application/json' \
  -d '{
    "eventTime": "2026-09-22T14:21:22Z",
    "eventType": "COMPLETE",
    "producer": "https://github.com/sentier-dev/sentier-importers",
    "schemaURL": "https://openlineage.io/spec/2-0-2/OpenLineage.json#/$defs/RunEvent",
    "run": { "runId": "run-1" },
    "job": {
      "namespace": "sentier-importers",
      "name": "bafu.parse",
      "facets": {
        "documentation": {
          "_producer": "https://github.com/sentier-dev/sentier-importers",
          "_schemaURL": "https://openlineage.io/spec/facets/1-0-0/DocumentationJobFacet.json",
          "description": "Parse BAFU EcoSpold XML export into flat records."
        }
      }
    },
    "inputs": [{
      "namespace": "file:///home/laurenz/dds/sources/bafu-2026",
      "name": "BAFU-2026 v1_ecoSpold v1.zip",
      "facets": {
        "dataSource": {
          "_producer": "https://github.com/sentier-dev/sentier-importers",
          "_schemaURL": "https://openlineage.io/spec/facets/1-0-0/DatasourceDatasetFacet.json",
          "name": "BAFU",
          "uri": "https://www.bafu.admin.ch"
        }
      }
    }],
    "outputs": [{
      "namespace": "sentier-importers",
      "name": "parsed",
      "facets": {
        "dataSource": {
          "_producer": "https://github.com/sentier-dev/sentier-importers",
          "_schemaURL": "https://openlineage.io/spec/facets/1-0-0/DatasourceDatasetFacet.json",
          "name": "BAFU",
          "uri": "https://www.bafu.admin.ch"
        }
      }
    }]
  }'
```

Fields that must stay consistent between the two calls:

| Field | Why it matters |
|---|---|
| `run.runId` | Links `START` and `COMPLETE` as the same run |
| `job.namespace` + `job.name` | Identifies the job across runs |
| `eventTime` | Must be valid ISO 8601 UTC; `COMPLETE` time should be ≥ `START` time |

## Viewing results

By default: UI on `http://localhost:3000`, API on `http://localhost:5000` (check `docker-compose.yml` if ports were changed).

Example:
<img width="1906" height="937" alt="Screenshot 2026-09-22 173740" src="https://github.com/user-attachments/assets/5a668646-4e4c-409d-85e1-7799dead49ab" />


## Long-term Vision

Goal: have `sentier-importers` log every transformation as `.jsonl` (for offline/audit purposes) **and** emit the same events live to a running OpenLineage instance.

## References

- [OpenLineage getting started guide](https://openlineage.io/getting-started/)
- [OpenLineage Python client docs](https://openlineage.io/docs/client/python/)
- [GitHub Codespaces](https://github.com/features/codespaces)
