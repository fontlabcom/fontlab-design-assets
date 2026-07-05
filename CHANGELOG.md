# Changelog

All notable changes to this repository are recorded here. Versions are git tags
(`vX.Y.Z`); the site redeploys on each tag.

## [Unreleased]

### Added
- `CHANGELOG.md` — this file.
- Asset inventory on the **Assets** page: every pack described and linked to its
  folder in the repo, so consumers can find and download assets.
- Usage and licensing guidance on the **About** page.
- Asset-inventory sanity check in the `docs.yml` workflow: the build fails fast
  if any of the four asset packs goes missing.

### Changed
- README rewritten: added a "What's inside" summary of the four packs, corrected
  the GitHub Pages setup (served by **GitHub Actions**, not a branch/folder), and
  fixed the build command to use `mkdocs-materialx`.

## [1.0.3] — 2026-04-19

- Published release of the FontLab Ltd. design-asset site (MkDocs MaterialX),
  deployed to GitHub Pages on `vX.Y.Z` tags.
