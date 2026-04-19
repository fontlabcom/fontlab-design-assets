# fontlab-design-assets

Design assets by **Fontlab Ltd.**, published via GitHub Pages.

- **Published site:** https://fontlabcom.github.io/fontlab-design-assets/
- **Source pages:** [`src_docs/md/`](src_docs/md/)
- **Built site (served by Pages):** [`docs/`](docs/)

## Layout

```
docs/          # built site, served by GitHub Pages (contains .nojekyll)
src_docs/      # MkDocs (Material) source
├── mkdocs.yml
├── md/        # Markdown pages
├── build.sh   # build into ../docs
└── serve.sh   # local live-reload preview
```

## Build

```bash
cd src_docs
./build.sh     # or: uvx --with mkdocs-material mkdocs build
```

The build writes to `../docs/` and refreshes `.nojekyll` so GitHub Pages serves the site as-is (no Jekyll processing).

## Preview locally

```bash
cd src_docs
./serve.sh     # http://127.0.0.1:8000
```

## GitHub Pages

Configure Pages to serve from the `main` branch, `/docs` folder.
