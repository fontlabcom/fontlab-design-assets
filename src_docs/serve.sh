#!/usr/bin/env bash
# this_file: src_docs/serve.sh
# Serve the MkDocs MaterialX site locally with live reload.
set -euo pipefail
cd "$(dirname "$0")"
uvx --with mkdocs-materialx --with pymdown-extensions mkdocs serve --livereload
