# AGENTS.md — Documentation Repository

This is Brian Yandell's (`byandell`) personal documentation site, published at
[byandell.github.io/Documentation](https://byandell.github.io/Documentation)
and versioned at [GitHub](https://github.com/byandell/Documentation).

## Purpose

A consolidated reference for digital tools and workflows spanning R, Python,
GitHub, environmental data science, Shiny apps, AI, and Quarto. The site is
rendered as GitHub Pages using the `just-the-docs` theme configured in
[`_config.yml`](_config.yml) and [`_quarto.yml`](_quarto.yml).

## Repository Structure

| Path | Contents |
|---|---|
| `R/` | R language notes and tutorials |
| `python/` | Python language notes and tutorials |
| `github/` | Git and GitHub references |
| `envsys/` | Environmental systems / earth data science |
| `AI/` | Notes on AI tools and concepts |
| `prompts/` | AI prompt examples and walkthroughs |
| `quarto/` | Quarto slides and references |
| `datasci/` | Data science topics |
| `images/` | Images used across pages |
| `AI_prompts.md` | Detailed AI prompt examples (actively edited) |
| `ShinyApps.md` | Notes on Shiny app development |
| `README.md` | Top-level site index / landing page |

## Key Files

- **`README.md`** — Main site index; keep in sync with `_quarto.yml` nav.
- **`AI_prompts.md`** — Living document of AI prompt examples; update when
  new prompts are added.
- **`prompts/`** — Individual saved prompt files (e.g., `powerpoint.md`,
  `workflow.md`, `file_versions.md`).

## Conventions

- All prose documents are Markdown (`.md`) or Quarto (`.qmd`).
- Quarto slides are rendered to HTML in `quarto/`.
- Do **not** overwrite versioned files (e.g., `*_v1.R`) when committing
  version histories — follow the multi-version commit workflow in
  [`prompts/file_versions.md`](prompts/file_versions.md).
- Respect `.gitignore` when updating `README.md` or adding new files.
- When creating or updating `README.md` files for sub-folders, keep summaries
  concise and high-level, with links to relevant files.

## Related Organizations & Repositories

- [`byandell-sysgen`](https://github.com/byandell-sysgen) — Systems genetics code
- [`byandell-envsys`](https://github.com/byandell-envsys) — Environmental systems code
- [`AttieLab-Systems-Genetics`](https://github.com/AttieLab-Systems-Genetics) — Collaborative lab repos
- [`byandell/geyser`](https://github.com/byandell/geyser) — Shiny app examples (R and Python)

## Code Preferences

- **R**: use `tidyverse`; document functions with `roxygen2`; build packages with `devtools`.
- **Python**: use `pandas`, `scikit-learn`; document with docstrings and type hints.
- **Reports/Slides**: prefer Quarto (`.qmd`) over R Markdown (`.Rmd`).
- **Shiny**: use `bslib` for UI layout and theming.
