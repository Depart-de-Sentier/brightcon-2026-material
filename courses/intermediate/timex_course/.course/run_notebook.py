"""Execute a notebook's code cells in one namespace. Exit non-zero on the first error.

Usage:
    python .course/run_notebook.py solutions/3_sommerhus_SOLVED.ipynb
    python .course/run_notebook.py 3_sommerhus.ipynb --as-student
    python .course/run_notebook.py 5_sommerhus_dynamic.ipynb --after 3_sommerhus.ipynb

`--as-student` replaces every `# %load solutions/x.py` escape hatch with that file's
contents, i.e. simulates a student who solved nothing and used every hatch.
`--after` runs another notebook first, in the same namespace (for notebooks that start
with a `%run` magic we cannot execute here).
"""

import json
import os
import re
import sys
import time
from pathlib import Path

HATCH = re.compile(r"^\s*#\s*%load\s+(\S+)", re.MULTILINE)
#: `obj?` / `obj??` opens the help in Jupyter and is a SyntaxError everywhere else
HELP = re.compile(r"^\s*[\w\.]+\?\??\s*$", re.MULTILINE)


def run(path, ns, as_student=False):
    path = Path(path).resolve()
    nb = json.loads(path.read_text())
    started = time.time()

    # run it the way a student would: from the notebook's own directory
    os.chdir(path.parent)
    if str(path.parent) not in sys.path:
        sys.path.insert(0, str(path.parent))

    for n, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
        src = "".join(cell["source"])
        hatch = HATCH.search(src)
        if hatch and as_student:
            src = (path.parent / hatch.group(1)).read_text()
        elif src.lstrip().startswith("%"):
            continue  # IPython magic, not executable here
        elif "FILL YOURSELF" in src:
            continue  # an exercise skeleton: not valid Python until the student fills it
        src = HELP.sub("", src)
        try:
            exec(compile(src, f"{path.name}:cell{n}", "exec"), ns)
        except Exception:
            print(f"\nFAILED in cell {n} of {path}:\n{src}", file=sys.stderr)
            raise

    print(f"\nOK: {path} ran {len(nb['cells'])} cells in {time.time() - started:.1f} s")


def main():
    args = sys.argv[1:]
    as_student = "--as-student" in args
    args = [a for a in args if a != "--as-student"]

    before = []
    while "--after" in args:
        i = args.index("--after")
        before.append(args[i + 1])
        del args[i : i + 2]

    # resolve up front: run() chdirs into each notebook's directory
    before = [Path(p).resolve() for p in before]
    target = Path(args[0]).resolve()

    ns = {"__name__": "__main__"}
    for path in before:
        run(path, ns)
    run(target, ns, as_student=as_student)


if __name__ == "__main__":
    main()
