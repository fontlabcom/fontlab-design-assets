#!/usr/bin/env -S uv run -s
# /// script
# requires-python = ">=3.10"
# dependencies = ["mkdocs>=1.6", "mkdocs-materialx>=10", "pymdown-extensions>=10.7"]
# ///
# this_file: build.py
"""Build the MkDocs MaterialX site from src_docs/ into docs/ for GitHub Pages."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src_docs"
OUT = ROOT / "docs"


def run(cmd: list[str], cwd: Path) -> None:
    print(f"$ {' '.join(cmd)}  (cwd={cwd})", flush=True)
    subprocess.run(cmd, cwd=cwd, check=True)


def build(strict: bool) -> None:
    cmd = [sys.executable, "-m", "mkdocs", "build", "--clean"]
    if strict:
        cmd.append("--strict")
    run(cmd, SRC)
    (OUT / ".nojekyll").touch()
    print(f"Built -> {OUT}")


def serve() -> None:
    run([sys.executable, "-m", "mkdocs", "serve", "--livereload"], SRC)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", nargs="?", default="build", choices=["build", "serve"])
    p.add_argument("--no-strict", action="store_true", help="Disable --strict mode")
    args = p.parse_args()

    if args.command == "serve":
        serve()
    else:
        build(strict=not args.no_strict)


if __name__ == "__main__":
    main()
