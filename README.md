# LCA data lineage hackathon

Private workspace for the Brightcon 2026 hackathon on traceable datapoints and lineage in life cycle assessment (LCA) databases.

The hackathon will explore a proposed traceability standard, establish data lineage, and assess the BAFU LCA database against the requirements developed by participants.

Project context: [Brightcon 2026 hackathon issue #42](https://github.com/Depart-de-Sentier/brightcon-2026-material/issues/42).

## Repository structure

| Folder | Purpose |
| --- | --- |
| [schemas/candidates/](schemas/candidates/) | Candidate schemas |
| [schemas/mappings/](schemas/mappings/) | Mappings between schemas and data formats |
| [scripts/](scripts/) | Extraction, transformation, validation, and analysis scripts |
| [prototypes/](prototypes/) | Experiments and proof-of-concept implementations |
| [examples/](examples/) | Example datapoints and lineage records |
| [assessment/bafu/](assessment/bafu/) | BAFU assessment materials and findings |
| [data/raw/](data/raw/) | Original database files and source documents |
| [data/processed/](data/processed/) | Derived data and metadata extracts |
| [docs/](docs/) | Project documentation and notes |
| [docs/decisions/](docs/decisions/) | Agreed scope and design decisions |
| [reports/](reports/) | Hackathon reports and presentations |

This repository contains only the initial structure and READMEs. Participants will add the schemas, code, assessment criteria, and database themselves.

Data files under `data/` are ignored by Git by default; the folder READMEs are tracked.
