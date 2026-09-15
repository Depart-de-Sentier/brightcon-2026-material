# Timex teaching course

This folder contains the materials for the BrightCon 2026 intermediate course on time-explicit life cycle assessment with `bw_timex`.

The Python kernel is already installed on the course server. To reproduce the environment locally, first [install `uv`](https://docs.astral.sh/uv/getting-started/installation/).

Then clone this repository to a folder of your liking, navigate there in your terminal, and run:

```sh
uv sync
```

Finally, recreate the databases we use for the course as follows, plugging in your ecoinvent 
credentials and the premise key:

```python
import bw2data as bd
from bw_timex import ensure_scenario_databases

bd.projects.set_current("timex_brightcon")

ensure_scenario_databases(
	{
		"iam_model": "remind-eu",
		"pathway": "SSP2-NDC",
		"system_model": "cutoff",
		"ecoinvent_version": "3.12",
		"years": [2020, 2030, 2040, 2050],
	},
	premise_key="dummy_premise_decryption_key",
	ecoinvent_credentials=("dummy_user", "dummy_password"),
)
```
