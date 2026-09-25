
# Hackathon project: Add additional data to the Sentier platform

# Main reflections

- In order to add new data and __fully embed them__ into an existing database, one must be able to link to processes already existing into that database. This is not a neutral approach as the linking implies modelling choices (selecting the best matching process for a linkage). One could also upload unlinked data and then a second user might do the linking in a later stage. However, due to time constraints this case is not considered here.

- Users might want to upload just a handful of datasets, this might be the case for non-expert users that upload occasionally. Or users might want to upload them in bulk, which requires automation and more coding expertise. 

- There has to be a validation step either by humans or machines. If human-made, it has to be done on files that are human-readable. Validation is intended as a review by an external party, followed by a revision by the user. The processes should be traceabkle (logs). 

## Authoring workflow

1) User creates three files `processes.csv`, `exchanges.csv`, `metadata.json` (examples below)
2) Validation is performed
3) `processes.parquet` and `exchanges.parquet` files are created, that are added ot the Sentier platform (BOFU-compliant format).

__Rationale:__ CSV files are used as data source because they are easy to edit, review, and version-control. Before publishing, the CSV files are validated and converted to Parquet, which provides efficient storage, strong data typing, and fast downstream processing.

# Suggested upload workflow

1. Define processes in `processes.csv` (one row per process, IDs should be __unique__).
2. Define exchanges in `exchanges.csv` (one row per input/output flow).
3. Link exchanges to processes using `process_id`.
4. Use consistent identifiers:
   - `reference_product` in `processes.csv`
   - `flow` in `exchanges.csv`
5. Convert CSV files to Parquet using PyArrow.
6. Store the generated files together with `metadata.json`.

## Structure

```text
sector/
├── processes.csv
├── exchanges.csv
├── metadata.json
├── processes.parquet
└── exchanges.parquet
```

## Generate Parquet

```python
import pyarrow.csv as csv
import pyarrow.parquet as pq

pq.write_table(
    csv.read_csv("processes.csv"),
    "processes.parquet"
)

pq.write_table(
    csv.read_csv("exchanges.csv"),
    "exchanges.parquet"
)
```

## Schema Rules

See also here: [https://github.com/sentier-dev/sentier-inventory/tree/main/schema](https://github.com/sentier-dev/sentier-inventory/tree/main/schema)

- `processes.parquet`: one row per process.
- `exchanges.parquet`: one row per exchange.
- `process_id` links exchanges to processes.
- Allowed `process_type`: `unit`, `system`, `lci_result`.
- Allowed `flow_type`: `production`, `technosphere`, `biosphere`.
- Allowed `direction`: `input`, `output`.

## SINGLE UPLOAD (1-10 processes, non-expert user)

The suggestion is to use a graphical interface (opline page or simlar) that guides the human user, similarly to what existing LCA software does. Once a new process is created, an unique ID is automatically assigned, and each exchange can be linked by using drop-down menus, choosing the most representative process ID to be linked. The Validation is performed within the same interface, e.g. by a third party, using verison control. The interace then exports the `processes.csv`, `exchanges.csv`, `metadata.json` files for the record and for conversion into parquet. 

## BULK UPLOAD (10-1000 processes, expert user)

The single upload approach would become excessively time-consuming for uploading many new processes. In that case, the worflow above can be used as well (larger files, more rows) skipping the graphical interface. 
What is needed, however, is fast access to a full list of datasets (and their unique identifiers) already existing in the database or platform, so that linking can be done at scale.

# Open issues and possible solutions

- Documentation. It is recommended that documentation such as background reports on the data are made available open source in other repositories (e.g. Zenodo or similar) __with citable doi__. and then referred to. The reference could be added in the `metadata.json` file using a dedicated `documentation` section. For bulk upload, multiple references could be added and ideally one should be able to refer to the single processes using their unique IDs. Below an example with structure that supports multiple references, such as methodology documents, source datasets, reports, publications, or GitHub repositories.

```json
{
"...",
"process_count": 2,
"exchange_count": 15,
  "documentation": [
    {
      "title": "Background report for process ID12345",
      "url": "https://docs.myrepowebpage/ID12345"
    },
    {
      "title": "Background report for process ID12346",
      "doi": "10.1234/sentier.2026.001"
    }
  ]
}
```


- Interface is mentioned but not developed. The approach above can be used, non-expert users can be facilitated by  providing temlapte/examples that can be modified manually (or with AI).

- Governanece is not adddressed. This is specifically important for the validation step. Who reviews and how? To be defined. A recommendation is to use version control for validation so that history is maintained. This also influenced the suggestion of using .csv format.

- Updated liks of unique id of each database records needs to be produced. 

# Files in this folder

- Examples of data
- - `processes.csv`
- - `exchanges.csv`
- - `metadata.json`
- Converter to parquet
- - `csv_to_parquet.py`
- Parquet files
- -`exchanges.parquet`
- -`processes.parquet`
- Validator for parquet
- - `check_parquet.py`