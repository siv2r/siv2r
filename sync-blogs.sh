#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if ! python3 -c "import feedparser, json" 2>/dev/null; then
    echo "Error: required Python modules 'feedparser' and 'json' must be importable." >&2
    echo "Activate the project venv first:  source .venv/bin/activate" >&2
    exit 1
fi

./update_readme.py
