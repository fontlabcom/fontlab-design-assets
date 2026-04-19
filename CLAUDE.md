# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repo publishes **Fontlab Ltd. design assets** via GitHub Pages. Authoring happens in `src_docs/` (MkDocs + MaterialX theme); the rendered site lives in `docs/` with a `.nojekyll` marker so Pages serves it verbatim.

## Architecture

```
src_docs/          # source (edit here)
├── mkdocs.yml     # docs_dir: md, site_dir: ../docs, theme: materialx
├── md/            # Markdown pages (index, assets, about)
├── build.sh       # shell build via uvx
├── serve.sh       # local live-reload via uvx
└── requirements.txt

build.py           # repo-root build tool (uv inline-script, dual build/serve)
docs/              # generated output + .nojekyll (GitHub Pages root)
.github/workflows/docs.yml   # builds & deploys on v*.*.* tag
```

Key points:
- `src_docs/mkdocs.yml` writes output to `../docs` (`site_dir: ../docs`). Never change `docs_dir`/`site_dir` without updating `build.py` and `build.sh` together.
- Theme is **`materialx`** (mkdocs-materialx, the mkdocs-material 9.7.1 fork), not `material`. Do not revert — the upstream `material` project is effectively unmaintained going forward.
- `.nojekyll` in `docs/` is load-bearing: without it GitHub Pages runs Jekyll and mangles MkDocs output. Both `build.py` and `build.sh` re-`touch` it after every build.
- Builds are **`--strict`** by default; warnings fail the build. Use `--no-strict` on `build.py` only when intentionally debugging.

## Commands

Build (repo root):
```bash
python build.py             # strict build into docs/
python build.py --no-strict
python build.py serve       # live-reload preview
```

Or from `src_docs/`:
```bash
./build.sh                  # uvx-based, no venv needed
./serve.sh
```

Direct mkdocs invocation (if deps already installed):
```bash
mkdocs build -f src_docs/mkdocs.yml --clean --strict
mkdocs serve -f src_docs/mkdocs.yml --livereload
```

## Deployment

GitHub Actions (`.github/workflows/docs.yml`) triggers on push of `v[0-9]+.[0-9]+.[0-9]+` tags (and `workflow_dispatch`). It runs `python build.py build` and deploys `docs/` via `actions/deploy-pages@v4`.

Repository **Pages settings must be set to "GitHub Actions"** as the source (not a branch/folder) — the workflow uploads an artifact and `deploy-pages` serves it.

To cut a release: `git tag v0.1.0 && git push --tags`.

## Editing docs

- Pages live in `src_docs/md/`. Add new pages there and register them in the `nav:` block of `src_docs/mkdocs.yml`.
- `edit_uri` in `mkdocs.yml` points at `edit/main/src_docs/md/` — keep it consistent with the actual source path if the layout ever moves.
- Do **not** hand-edit files in `docs/` — they are regenerated on every build.
