"""Small helpers for building the course notebooks from Python."""

import json
import re
from pathlib import Path

#: relative links in markdown, e.g. [`sommerhus_system.py`](sommerhus_system.py)
RELATIVE_LINK = re.compile(r"\]\((?!\.\./|https?://|#)([\w./-]+\.(?:py|ipynb|png))\)")


def load(path):
    return json.loads(Path(path).read_text())


def save(nb, path):
    strip_trailing_newline(nb)
    Path(path).write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")


def strip_trailing_newline(nb):
    """Drop the empty last line Jupyter shows when a code cell's source ends in a newline."""
    for cell in nb["cells"]:
        if cell["cell_type"] == "code" and cell["source"]:
            source = "".join(cell["source"]).rstrip("\n")
            cell["source"] = source.splitlines(keepends=True)


def _cell(cell_type, source, **meta):
    cell = {
        "cell_type": cell_type,
        "metadata": {"brightcon": meta} if meta else {},
        "source": source.splitlines(keepends=True),
    }
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    return cell


def md(source, **meta):
    return _cell("markdown", source, **meta)


def code(source, **meta):
    return _cell("code", source, **meta)


def tag(cell, **kv):
    cell.setdefault("metadata", {}).setdefault("brightcon", {}).update(kv)
    return cell


def find(nb, predicate):
    return [i for i, c in enumerate(nb["cells"]) if predicate("".join(c["source"]))]


def strip_outputs(nb):
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            cell["outputs"] = []
            cell["execution_count"] = None


def for_solutions_dir(cells, depth=2):
    """Adapt generated cells for a solved notebook saved in `solutions/<notebook>/`.

    Links in the source are written relative to the course root, so they get `depth` levels of
    `../` in front. Markdown cells are copied, so the caller's list (shared with the student
    version) is untouched.
    """
    out = []
    for cell in cells:
        if cell["cell_type"] == "markdown":
            source = RELATIVE_LINK.sub(r"](%s\1)" % ("../" * depth), "".join(cell["source"]))
            cell = dict(cell, source=source.splitlines(keepends=True))
        out.append(cell)
    return out
