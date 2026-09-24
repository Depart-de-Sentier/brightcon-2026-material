# Using Edges in BONSAI: Spatializing Water Scarcity Impacts of French Consumption

Brightcon 2026 · Denise Almeida, Fan Yang, Mathieu Delpierre, Miguel Fernández Astudillo,
Stefano Merciai, Valentin Starlinger (2-0 LCA)

We use the `edges` library on the BONSAI database to calculate the water scarcity footprint
(AWARE 2.0) of French household consumption, with characterisation factors that depend on where
the water is used. Everything the notebook needs is in this folder.

## Contents

| path | what |
|---|---|
| `brightcon_water_edges_bonsai.ipynb` | the notebook |
| `requirements-bonsai-edges.txt` | Python packages; this is also the JupyterHub kernel |
| `conda-environment.yml` | the same packages for running locally with conda |
| `data/bonsai/` | BONSAI v2.4.0 export (~31 MB), imported on the first run |
| `data/coicop/` | BONSAI → COICOP 2018 correspondence, for the footprint per COICOP division |

## Running it

On the Brightcon JupyterHub, open the notebook and select the kernel **Edges in BONSAI BC26**.

Locally, install the packages with pip (Python 3.12):

```bash
pip install -r requirements-bonsai-edges.txt
```

or with conda:

```bash
conda env create -f conda-environment.yml
conda activate brightcon-edges
```

and start the notebook from this folder:

```bash
jupyter lab brightcon_water_edges_bonsai.ipynb
```

The first run creates a Brightway project called `french_water`, downloads the ecoinvent 3.12
biosphere, imports BONSAI and the COICOP divisions, and gets the product classification from the
BONSAI API (<https://lca.aau.dk/api/>, no account needed). This takes about three minutes. After that the
whole notebook runs in about 90 seconds. You can change the project name with `BONSAI_PROJECT` in the setup.

## Links

* Analysis code: <https://github.com/20lca/ademe_fr_cons> (ADEME *Impacts de la consommation* project)
* `edges`: <https://github.com/romainsacchi/edges>
* BONSAI: <https://bonsai.uno/>
* AWARE: <https://wulca-waterlca.org/aware/>
