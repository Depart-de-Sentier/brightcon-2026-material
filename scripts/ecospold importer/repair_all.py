#!/usr/bin/env python3
"""Run all BAFU EcoSpold 1 repairs from raw files, then validate the result."""

from pathlib import Path
import subprocess
import sys

SCRIPTS = Path(__file__).resolve().parent
STEPS = (
    ("repair_namespace.py",),
    ("repair_dates.py",),
    ("repair_metadata.py", "publisher"),
    ("repair_metadata.py", "company-code"),
    ("repair_metadata.py", "source-number"),
    ("repair_administrative_order.py",),
    ("repair_exchange_numbers.py",),
    ("repair_schema.py",),
    ("validate_collection.py",),
)


def main():
    for number, (script, *args) in enumerate(STEPS, start=1):
        print(f"[{number}/{len(STEPS)}] {script} {' '.join(args)}", flush=True)
        try:
            subprocess.run(
                [sys.executable, str(SCRIPTS / script), *args], check=True
            )
        except subprocess.CalledProcessError as exc:
            print(f"Stopped: {script} failed with exit code {exc.returncode}.")
            return exc.returncode
    print("Repaired and validated XML: data/processed/ecospold1-schema-fixed/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
