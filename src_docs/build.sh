#!/usr/bin/env bash
# this_file: src_docs/build.sh
# Build the MkDocs MaterialX site into ../docs for GitHub Pages.
set -euo pipefail
cd "$(dirname "$0")/.."
exec uv run build.py build
