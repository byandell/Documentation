---
title: "Global Agents Template"
parent: "Prompt Examples"
nav_order: 9
---

# Global Agents Template (`~/.agents/AGENTS.md`)

This file defines the universal system instructions, safety boundaries, coding standards, and response preferences for AI assistants working across Brian Yandell's (`byandell`) repositories.

---

## 1. Global System Instructions & Context

- **Developer Context**: Data scientist and researcher working across R packages, Python tools, geospatial/environmental analysis, Shiny applications, Quarto documentation, and academic writing.
- **Language Baselines**:
  - **R**: Use `tidyverse`; document all functions with `roxygen2`; build packages with `devtools`; use `bslib` for Shiny apps.
  - **Python**: Use `pandas`, `scikit-learn`; use modern type annotations and complete docstrings.
  - **Documentation & Publishing**: Prefer Quarto (`.qmd`) and Markdown (`.md`) with Just-the-Docs Jekyll themes.

---

## 2. Version Control & Execution Governance

- **No Automatic Git Commit/Push**: Prepare all file edits and run local tests/checks, but **NEVER** execute `git commit` or `git push`. Leave all staging, committing, and pushing for the user to execute manually.
- **Empirical Local Verification**: Never declare a task complete without running concrete verification commands (`quarto render`, `pytest`, `devtools::check()`, etc.) unless the user requests otherwise.
- **Preserve Codebase Conventions**: Maintain existing docstrings, variable naming styles, architectural patterns, and legacy version workflows (`prompts/file_versions.md`).

---

## 3. R Language Quality & Safety Guidelines

- **Vector Subsetting Safety**: When filtering vectors in R, ALWAYS use `grepl("^\\s*#'", lines)` with `!grepl(...)` or `grep(..., invert = TRUE)`. NEVER use `!grep(...)` (which evaluates `!2` -> `FALSE` in R and wipes out the entire vector).
- **Explicit Package Namespacing**: Use explicit package prefixes (`pkg::func()`) in exported functions and Shiny modules to avoid namespace collisions.
- **Roxygen Stripping in WASM**: Inlining R code into WebAssembly blocks (`{shinylive-r}`) requires stripping roxygen comments (`^#'`) to prevent Pandoc JSON serialization errors.
- **Vectorized Logic**: Prefer vectorized operations (`ifelse()`, `lapply()`, `map()`) over explicit `for` loops when manipulating data frames or atomic vectors.

---

## 4. Python Language Guidelines

- **Modern Type Annotations**: Use modern Python type hints (`str | None`, `list[int]`, `dict[str, Any]`) and explicit return type declarations for functions.
- **Immutable Default Arguments**: Never use mutable default arguments (`def func(items=[])`). Use explicit `None` guards (`def func(items: list | None = None): items = items or []`).
- **Environment & Dependency Hygiene**: Respect active virtual environments (`.venv`, `conda`, `uv`). Avoid modifying system Python packages directly.
- **Explicit Exception Handling**: Avoid silent `except Exception: pass` blocks. Catch specific exceptions (`ValueError`, `FileNotFoundError`) and log or re-raise with clear context.

---

## 5. Quarto, Markdown & Technical Writing

- **Single H1 Title Tag**: Ensure each markdown or Quarto document has exactly one `# Title` tag at the top, followed by structured `##` and `###` heading hierarchy.
- **Relative Path Hygiene**: Verify that file links use valid relative paths (`../index.html`, `vignettes/`) and valid markdown link syntax.
- **Explicit Code Chunk Tagging**: Always tag code blocks with appropriate language identifiers (`{shinylive-r}`, `python`, `bash`, `r`, `json`, `yaml`).
- **GitHub Pages Security (`.nojekyll`)**: When deploying Quarto or static web assets to GitHub Pages (`gh-pages`), ensure `docs/.nojekyll` exists.

---

## 6. Response Preferences & Collaboration (CRAFT Alignment)

- **Concise & Direct**: Keep responses focused on actionable solutions. Provide high-level summaries highlighting key decisions or open questions.
- **Complete Drop-in Replacements**: Provide complete replacement code blocks or diffs rather than truncated snippets or `// TODO` placeholders.
- **Empirical Evidence Base**: Base technical diagnoses strictly on actual terminal command output, logs, and empirical test traces.
