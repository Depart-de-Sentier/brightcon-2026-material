#!/usr/bin/env bash
# Install BAFU-2026 v1 + EF 3.1 into the Brightway 2.5 project "bafu-2026". See README.md.
set -euo pipefail
cd "$(dirname "$0")"

uv sync
uv run sentier-brightway coverage
uv run sentier-brightway db --project bafu-2026 "$@"   # pass --overwrite to replace a previous install
