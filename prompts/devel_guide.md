---
title: "Create Developer Guides (Blueprint)"
parent: "Prompt Examples"
nav_order: 6
---

# Create Developer Guides (Blueprint)

This document serves as a general blueprint for creating developer guides across different project structures: **R Packages**, **Python Projects**, **Documentation Projects**, and **Hybrid R/Python Projects**.

A developer guide clarifies codebase structure, module boundaries, data routing, reactivity flow, and custom design patterns. It helps human maintainers and AI pair-programming agents understand how to extend and debug the system without introducing architectural drift.

In addition to a Developer Guide, a project would benefit from the flowing
complementary files:

- [`AGENTS.md`](../AI/agents.md): Repository-level systems instructions and agent skills
- `README.md`: Repository overview and quick start
- `DEVELOPER.md`: Developer-facing notes and guidance

> [!TIP]
> For a concrete, real-world case study of this blueprint applied to a mature R Shiny package, see the [qtl2shiny Developer Guide Reference](./devel_guide_qtl2shiny.md).

---

## 1. R Package Developer Guides (Vignette-Based)

In mature R packages, developer guides are best placed as package vignettes so they render as part of the official package documentation (e.g., via `pkgdown`).

### Directory Layout

```text
my_package/
├── vignettes/
│   ├── DeveloperGuide.Rmd          # Master developer guide index
│   └── devel/
│       ├── data_flow.Rmd           # Detailed submodule guide
│       └── custom_plots.Rmd        # Detailed plotting guide
├── _pkgdown.yml                    # Configures navigation bar
└── R/                              # Package source code
```

### Actionable Prompts

1. **Directory & Index Setup**:
   > "Create a master developer guide vignette `vignettes/DeveloperGuide.Rmd` (or `.qmd`). The guide should detail the high-level architecture of the package, including execution entrypoints and core dependencies. Provide an index of all `.R` source files and group them by function category (e.g., DB querying, data loading, plotting, UI panels). Document this creation process in `prompts/devel_guide.md`."
2. **Sub-module/Panel Details**:
   > "Develop a detailed developer sub-guide in `vignettes/devel/module_name.Rmd` describing `module_name`. Document the inputs and outputs, reactive logic, data dependencies, and custom defensive checks. Include a Mermaid reactivity flow diagram if applicable."
3. **Internal Linking**:
   > "Update `vignettes/DeveloperGuide.Rmd` to link to the new sub-guide `vignettes/devel/module_name.Rmd` and ensure all file links are relative. Register the vignettes in the `_pkgdown.yml` site config so they are visible under the articles tab."

### Steps to Perform

1. **Analyze File Structure**: Identify all source files in the `R/` directory. Trace their dependencies and namespace exports.
2. **Create Vignettes Directory**: Ensure `vignettes/` (and subdirectories like `vignettes/devel/`) exists.
3. **Build the Prototype**: Create a single sub-module guide (e.g., `vignettes/devel/geno_module.Rmd`) to serve as a format prototype.
4. **Draft the Master Vignette**: Create `vignettes/DeveloperGuide.Rmd` with high-level architecture, module categorization, layout descriptions, and utility mappings.
5. **Add Sub-module Guides**: Flesh out guides for remaining sub-modules, using the prototype as a blueprint.
6. **Compile and Verify**: Run `devtools::build_vignettes()` to compile and `pkgdown::build_site()` to verify website navigation and layout.

---

## 2. Python Project Developer Guides

Python developer guides are typically placed in a root-level `docs/` folder or formatted directly in a `DEVELOPER.md` or `AGENTS.md` (to serve as workspace instructions for AI coding assistants).

### Directory Layout

```text
my_project/
├── docs/
│   ├── developer_guide.md          # Core architecture document
│   ├── environment_setup.md        # Python environment & dependencies
│   └── api/                        # API detail documents
├── tests/                          # Test suite (pytest)
├── pyproject.toml / setup.py       # Configuration and dependencies
└── my_module/                      # Python package source code
```

### Actionable Prompts

1. **Initial Architecture Map**:
   > "Inspect the python package `my_module/` and map out the directory layout and core execution pathways (e.g., entrypoint `__main__.py` or class interfaces). Create a developer guide in `docs/developer_guide.md` detailing how classes interact and outline data processing pipelines."
2. **Setup and Testing Instructions**:
   > "Draft `docs/environment_setup.md` containing detailed commands to configure the python virtual environment (using venv, conda, or poetry), install developer dependencies, and execute the test suite via pytest. Note how code linting (ruff, black, flake8) is configured."
3. **API & Extension Guide**:
   > "Write documentation on how to extend the module. Outline class hierarchy interfaces (e.g., adding a new database engine or plot format) and define rules for code standards (e.g., docstrings style, type hints)."

### Steps to Perform

1. **Source Discovery**: Run `find my_module -name "*.py"` to map out files and subdirectories.
2. **Trace Class Interfaces**: Inspect imports and inheritance relationships to map out object-oriented structures.
3. **Create Environment Reference**: Document dependencies defined in `pyproject.toml`, `setup.py`, or `requirements.txt`.
4. **Draft the Developer Guide**: Structure the files into Overview, Class/Module Architecture, Testing Workflows, and Extension Guidelines.
5. **Code Style Definitions**: Detail constraints around docstring formats (Google, NumPy, Sphinx style) and type hinting protocols.

---

## 3. Documentation Projects

For projects whose main deliverable is documentation (such as a Quarto book, Jupyter Book, or Just-the-Docs Jekyll site), the developer guide details site layout, configuration variables, page metadata, navigation structures, and automated checks.

### Directory Layout

```text
documentation_site/
├── guides.md                       # Navigation to user and developer guides
├── AGENTS.md                       # Project-level constraints for AI agents
├── _config.yml / _quarto.yml       # Site config files
├── index.md / README.md            # Landing / index page
└── scripts/
    └── check_links.py              # Automated link-validation scripts
```

### Actionable Prompts

1. **Site Layout Documentation**:
   > "Map out the site's folder hierarchy and page navigation in a root `guides.md` file. Explain the purpose of key configuration files like `_config.yml` or `_quarto.yml` and how the side navigation menu is generated."
2. **Metadata & Writing Conventions**:
   > "Add rules to the top-level developer index or `AGENTS.md` specifying frontmatter metadata standards (e.g., `title`, `parent`, `nav_order`, and `permalink`). Establish conventions for markdown headers, cross-references, and slide inclusions."
3. **Automation & Link Validation**:
   > "Create documentation in `prompts/check_links.md` on how to run automated link verification scripts. Outline how to identify and prune broken internal relative links and external web URLs before publishing."

### Steps to Perform

1. **Identify Configuration Entrypoints**: Map YAML configuration properties to the resulting website structure (navigation menus, page hierarchies).
2. **Define Frontmatter Conventions**: List required frontmatter elements for new pages to ensure correct layout and theme mapping.
3. **Setup Link-Check Tools**: Implement automated checks (e.g., python or bash scripts) to parse markdown links and identify 404s.
4. **Write guides.md / AGENTS.md**: Combine rules, templates, and procedures into readable documents for future editors and AI agents.

---

## 4. Hybrid R & Python Projects

In research repositories (like
[]`geyser`](<https://byandell.github.io/geyser/>)
or
[landmapyr](https://byandell.github.io/landmapyr/)),
R and Python code often sit side-by-side. The developer guide must
reconcile both ecosystems, outlining boundaries and interfaces.

### Directory Layout

```text
hybrid_project/
├── DEVELOPER.md                    # Root architecture index for both languages
├── r/                              # R package sub-project
│   ├── R/
│   └── vignettes/
├── python/                         # Python package sub-project
│   ├── pyproject.toml
│   └── docs/
└── data/                           # Shared raw / processed data artifacts
```

### Actionable Prompts

1. **Bridge Architecture Map**:
   > "Create a root `DEVELOPER.md` describing how the R and Python components cooperate. Trace the communication boundaries (e.g.,
   [`reticulate`](https://rstudio.github.io/reticulate/),
   [`rpy2`](https://rpy2.readthedocs.io/en/latest/),
   subprocess calls, REST APIs, or shared SQLite/Parquet files). Group files by language and function."
2. **Dual-Environment Configuration**:
   > "Create environment guides mapping out how to bootstrap both R and Python environments on a local machine. Document dependencies (e.g., a shared conda `environment.yml` or installation scripts)."
3. **Shared Data & API Schemas**:
   > "Document data structures shared between R and Python code. Define SQLite database schemas, HDF5 hierarchies, or Parquet column schemas, detailing validation checks on both sides."

### Steps to Perform

1. **Map Cross-Language Boundary**: Determine if languages communicate at runtime (e.g., via `reticulate` in R, web sockets, or system APIs) or offline (e.g., Python pre-processes data, R Shiny visualizes it).
2. **Create Combined Root Guide**: Write a root `DEVELOPER.md` detailing directory splits, shared folder layouts, and build steps.
3. **Draft Language-Specific Sub-Guides**:
   - For R: Link to `r/vignettes/` developer docs.
   - For Python: Link to `python/docs/` developer docs.
4. **Define Dual-Testing Workflows**: Outline execution scripts that run both
[`pytest`](https://pytest.org/)
and
[`devtools::test`](https://testthat.r-lib.org/reference/test_package.html)
as part of verification.
5. **Coordinate Shared Data Schemas**: Formulate explicit specifications for exchange file formats
([CSV](https://allthings.how/what-is-a-csv-file-and-how-to-open-or-create-it/),
[Parquet](https://parquet.apache.org/),
[SQLite](https://www.sqlite.org/))
to avoid data drift.
