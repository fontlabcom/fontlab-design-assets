# fontlab-design-assets

Design assets by **Fontlab Ltd.**, published via GitHub Pages.

- **Published site:** https://fontlabcom.github.io/fontlab-design-assets/
- **Source pages:** [`src_docs/md/`](src_docs/md/)
- **Asset packs:** [`src_docs/assets/`](src_docs/assets/)
- **Built site (served by Pages):** [`docs/`](docs/)

## What's inside

169 files across four packs — logos, banners, app icons, and marketing screenshots:

- **`fontlab-marketingpack-company`** — the FontLab Ltd. wordmark: logo font (OTF + VFJ source), Illustrator/PDF vectors, and PNGs from 50px to 1024px in black and gray tints.
- **`fontlab-banners`** — 728×90 web banners in four themes (dark, graydark, graylight, light), PDF and PNG.
- **`fontlab-marketingpack-fontlab-8`** — FontLab 8 app icons, headers, screenshots, and store copy.
- **`fontlab-marketingpack-transtype-4`** — TransType 4 app icon and screenshots.

The [Assets page](https://fontlabcom.github.io/fontlab-design-assets/assets/) links each pack in the repo.

## Layout

```
docs/          # built site, served by GitHub Pages (contains .nojekyll)
src_docs/      # MkDocs MaterialX source
├── mkdocs.yml
├── md/        # Markdown pages
├── assets/    # the design asset packs
├── build.sh   # build into ../docs
└── serve.sh   # local live-reload preview
```

## Build

```bash
cd src_docs
./build.sh     # or: uvx --with mkdocs-materialx --with pymdown-extensions mkdocs build
```

The build writes to `../docs/` and refreshes `.nojekyll` so GitHub Pages serves the site as-is (no Jekyll processing). From the repo root, `python build.py` does the same in `--strict` mode.

## Preview locally

```bash
cd src_docs
./serve.sh     # http://127.0.0.1:8000
```

## GitHub Pages

Pages is served by **GitHub Actions**, not a branch/folder. The
[`docs.yml`](.github/workflows/docs.yml) workflow builds the site and deploys it
with `actions/deploy-pages` on every `vX.Y.Z` tag (and on manual dispatch). In
repository settings, set **Pages → Source → GitHub Actions**.

To cut a release: `uvx gitnextver@latest` (tags the next `vX.Y.Z` and pushes),
or `git tag v1.0.4 && git push --tags`.
