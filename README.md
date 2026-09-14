# Brightcon 2026 Material

This repository holds the material used during brightcon 2026.

## Repository structure

```
.
├── conference/            # Material for the main conference days
│   ├── wednesday/
│   ├── thursday/
│   └── friday/
├── courses/                # Material for pre-conference courses
│   ├── beginners/
│   └── intermediate/
└── hackathon:input-data/  # Input data for the hackathon
```

`conference/` and `courses/` are organized by day / level respectively — add a new subfolder for your own session
under whichever matches (e.g. `courses/intermediate/<your-session>/` or `conference/friday/<your-session>/`), then
follow the steps below. Each session folder is self-contained: it holds your notebooks/slides alongside its own
environment file (see `courses/intermediate/bw_timex/` for an example).

## Presenters / Instructors

If you are not an instructor, or are not planning on running your notebooks live during the conference, you only
need to fork this repository and add your material via a pull request.

If you are an instructor, or plan to present and run notebooks live, follow the steps below so that your Python
environment appears automatically in the JupyterHub that participants will use. No manual setup is needed on the
DdS side.

### Step 1 — Fork the repository and add your material

Fork this repository to your own GitHub account, then create a folder for your session inside your fork and drop
your notebooks, slides, or whatever you want participants to have. The folder name and location are up to you —
keep it self-explanatory and follow the existing structure (courses, conference, dates, etc.).

### Step 2 — Add an environment file

Inside your session folder, add a file that tells the server which Python packages to install for your kernel. Pick
one of the three depending on what you normally use:

+ **conda / mamba** (recommended): `environment-<yourname>.yml`
+ **pip**: `requirements-<yourname>.txt`
+ **pyproject.toml**: `pyproject-<yourname>.toml`

The `<yourname>` part becomes the internal kernel name — keep it short, lowercase, no spaces (e.g.
`requirements-lca-basics.txt` or `environment-premise.yml`).

Two things to be careful about:

1. **Always add a display name** at the top of your file, otherwise your kernel shows up with an ugly label like
   "Display label [conda:base]":

   ```
   # display-name: LCA Basics BC26
   ```

2. If you use conda/mamba, **do not** just run `conda env export` and paste the result — it dumps every transitive
   dependency with platform-specific build strings (`osx-arm64`, `win-64`, etc.) that will likely fail on the Linux
   server. Instead, hand-write your YAML with just the packages you actually need, or export only what you
   explicitly installed:

   ```
   conda env export --from-history > environment-<yourname>.yml
   ```

   Also remove any `prefix:` line at the bottom if it appears (it's just a local path, meaningless on the server),
   and pin versions where it makes sense (`numpy=2.0`, `brightway2=2.4`, etc.) to keep things reproducible.

Full details and examples are in the documentation:
[https://brightcon-environ.readthedocs.io/en/latest/for-contributors.html](https://brightcon-environ.readthedocs.io/en/latest/for-contributors.html)

### Step 3 — Open a pull request

Once your material and environment file are in your fork, open a pull request back to the `main` branch of this
repository. An automated check will run and validate that your environment actually builds on the conference Linux
server (green checkmark, or red with a log if something needs fixing). A green check does not change the live
JupyterHub yet — it just means everything is good to go.

Someone from the DdS team will then review and merge your PR, and from that point on your kernel appears
automatically in the JupyterHub. Please tag `@tngTUDOR`, `@lbougan`, `@xiaoshir` in the PR so we notice it and do
the formal merge.

### Step 4 — Test it yourself

Once your PR is merged, log in to [https://summer.brightcon.link](https://summer.brightcon.link) (default password
`"2026bc"`; credentials from past years are no longer valid), click "Get the materials" to pull the latest version of
the repository, and check that your kernel appears in the launcher with the display name you set. If it doesn't
show up right away, try restarting your server from the JupyterHub control panel.

If anything goes wrong, or the automated check turns red and you're not sure why, send an email or ping us with
your PR link.

## Participants

This repository is meant to be automatically pulled by nbgitpuller in our servers ;)
