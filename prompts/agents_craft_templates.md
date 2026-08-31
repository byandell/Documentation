---
title: "AGENTS.md CRAFT Templates"
parent: "Prompt Examples"
---

# AGENTS.md CRAFT Templates by Repository Archetype

This catalog provides concise, drop-in [CRAFT](https://tyson-swetnam.github.io/intro-gpt/prompts/#the-craft-framework) (**Context, Role, Action, Format, Tone**) templates for `AGENTS.md` across Brian Yandell's repository ecosystem.

Because universal rules (no automatic git commit/push, empirical local verification, tidyverse/roxygen2, python typing, etc.) live in global System Instructions (`~/.agents/AGENTS.md`), these project-level files remain token-efficient (20–35 lines) for small and large models alike.
See
[../AI/agents.md](../AI/agents.md)
for a more complete discussion of AGENTS.md files.

---

## 1. Pure R Package / Shiny App

*Applicable Repos*: `qtl2shiny`, `foundr`, `foundrShiny`, `foundrHarmony`, `qtl2pattern`, `rainDrought`, `downr`

```markdown
# AGENTS.md — [PackageName]

## Context
- **Repository**: [PackageName] — [One-line description of package functionality]
- **Key Directories**: `R/` (functions and Shiny modules), `man/` (roxygen documentation), `tests/testthat/`, `inst/` (Shiny apps / vignettes / data)

## Role
Act as an expert R package developer, bioinformatician, and Shiny systems architect.

## Action & Verification
- Run local check: `devtools::document()`, `devtools::test()`, `devtools::check()`.
- Shiny reactivity: Test server logic modularly or with `shiny::testServer()`.
- Never edit files in `man/` directly; always update roxygen tags in `R/`.

## Format & Conventions
- Modular Shiny structure (`bslib` for UI, `moduleServer` for server logic).
- Explicit package namespacing (`pkg::func()`) across all exported and internal functions.

## Tone & Collaboration
- Concise, precise, complete drop-in replacement code. Run tests before declaring complete.
```

---

## 2. Pure Python / Geospatial Package

*Applicable Repos*: `landmapyr`, `ESIIL`

```markdown
# AGENTS.md — [PackageName]

## Context
- **Repository**: [PackageName] — Python library and workflows for [geospatial/data science]
- **Key Directories**: `src/` (or `[pkg]/`), `tests/`, `notebooks/`, `docs/`
- **Environment**: Active Python virtual environment (`.venv` / `conda` / `uv`)

## Role
Act as a scientific Python developer and geospatial data engineer.

## Action & Verification
- Run tests: `pytest`
- Run linting/formatting: `ruff check` / `mypy`
- Ensure notebooks execute cleanly from top to bottom with relative data paths.

## Format & Conventions
- Modern Python type hints (`str | None`, `list[int]`, `dict[str, Any]`).
- NumPy or Google-style docstrings on all exported functions/classes.

## Tone & Collaboration
- Concise, clear, and actionable. Provide verified diffs.
```

---

## 3. Dual R + Python Polyglot Repos

*Applicable Repos*: `geyser`, `hexmap`, `watershed`, `ewing`

```markdown
# AGENTS.md — [ProjectName]

## Context
- **Repository**: [ProjectName] — Polyglot R and Python project for [domain]
- **Layout**: `R/` (R functions and Shiny apps), `python/` (Python modules and Shiny for Python), `data/`, `docs/`

## Role
Act as a polyglot scientific software engineer proficient in both R and Python data ecosystems.

## Action & Verification
- **R Verification**: `devtools::test()` or `Rscript -e "source('...')"`
- **Python Verification**: `pytest python/tests`
- Maintain clean modular separation between R and Python submodules.

## Format & Conventions
- Apply global R guidelines to `R/` and global Python guidelines to `python/`.
- Cross-language data exchanges must use open standard formats (Parquet, CSV, GeoJSON).

## Tone & Collaboration
- Direct and concise. Verify both language pipelines when modifying shared data workflows.
```

---

## 4. Documentation & Web Publishing

*Applicable Repos*: `Documentation`, `byandell.github.io`

```markdown
# AGENTS.md — [Documentation / Site]

## Context
- **Repository**: Documentation site published via GitHub Pages
- **Key Directories**: `R/`, `python/`, `AI/`, `prompts/`, `quarto/`, `envsys/`, `datasci/`
- **Configuration**: `_quarto.yml`, `_config.yml` (Just-the-Docs theme)

## Role
Act as a technical documentation architect and digital tools writer.

## Action & Verification
- Build verification: `quarto render` or `bundle exec jekyll build`
- Ensure `docs/.nojekyll` exists on published GitHub Pages branches.
- Never overwrite versioned files (e.g. `*_v1.R`) — follow `prompts/file_versions.md`.

## Format & Conventions
- Single `# H1` tag per `.md`/`.qmd` file with strict `##` and `###` hierarchy.
- Clickable relative markdown file links. Keep subfolder `README.md` files concise.

## Tone & Collaboration
- Concise, organized, and focused on documentation usability.
```

---

## 5. Technical & Discursive / Academic Writing

*Applicable Repos*: Research notes, grant proposals, manuscripts (e.g. `mkeller3Projects2`, ESIIL reports)

```markdown
# AGENTS.md — [Project Title]

## Context
- **Repository**: [Project Title] — Scientific research notes, analysis workflows, and manuscript drafts
- **Key Directories**: `notes/`, `manuscript/`, `figures/`, `data/`

## Role
Act as an academic co-author, grant writer, and scientific research reviewer.

## Action & Verification
- Verify logical narrative progression, clarity of methodology, and complete citations.
- Validate that empirical claims align with data outputs and figure references.
- Preserve draft version histories without destructive overwriting.

## Format & Conventions
- Scholarly, constructive, and precise tone.
- Use tracked revision blocks when modifying drafts; maintain structured section headings.

## Tone & Collaboration
- Collaborative and rigorous. Highlight key decisions and open conceptual questions.
```

---

## 6. Duplicate `docs/AGENTS.md` Handling

For repositories with nested `docs/` folders (`hexmap`, `watershed`, `ewing`, `qtl2shiny`, `foundrShiny`, `foundrHarmony`, `foundr`):

Either delete `docs/AGENTS.md` (if the root `AGENTS.md` is sufficient), or replace `docs/AGENTS.md` with this 2-line pointer:

```markdown
# Documentation Guidelines
See root [AGENTS.md](../AGENTS.md).
```
