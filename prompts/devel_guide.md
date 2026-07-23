---
title: "Create Developer Guides (Blueprint)"
parent: "Prompt Examples"
nav_order: 6
---

# Create Developer Guides (Blueprint)

This document serves as a general blueprint for creating developer guides across different project structures: **R Packages**, **Python Projects**, **Documentation Projects**, and **Hybrid R/Python Projects**.

A developer guide clarifies codebase structure, module boundaries, data routing, reactivity flow, and custom design patterns. It helps human maintainers and AI pair-programming agents understand how to extend and debug the system without introducing architectural drift.

In addition to a Developer Guide, a project would benefit from the following
complementary files:

- [R Package Developer Guide](./R_package_developer_guide.md)
- [Python Developer Guide](./python_developer_guide.md)
- [Documentation Developer Guide](./documentation_developer_guide.md)
- [Hybrid R & Python Developer Guide](./hybrid_r_python_developer_guide.md)
- Additional Pages
  - [`AGENTS.md`](../AI/agents.md): Repository-level systems instructions and agent skills
  - `README.md`: Repository overview and quick start
  - `DEVELOPER.md`: Developer-facing architecture notes and whole-repo guidance

> [!TIP]
> For a concrete case study of this blueprint applied to a mature R Shiny package, see the [qtl2shiny Developer Guide Reference](./devel_guide_qtl2shiny.md). For a hybrid R/Python package case study, see the [`geyser` developer documentation](https://byandell.github.io/geyser/DEVELOPER.html).

---

## R Package Developer Guides (Vignette-Based)

In mature R packages, developer guides are best placed as package vignettes (e.g., `vignettes/DeveloperGuide.Rmd`) so they render as part of the official package documentation (e.g., via `pkgdown`).

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

## Python Project Developer Guides

Python developer guides are typically placed in `docs/devel/` (e.g., `docs/devel/python.md` for website rendering via Quarto/MkDocs) or inside the Python package source directory (`my_module/README.md`) for package developers, anchored by a root `DEVELOPER.md`.

### Directory Layout

```text
my_project/
├── DEVELOPER.md                    # Root architecture & developer guide entrypoint
├── docs/
│   └── devel/
│       ├── python.md               # Detailed Python Developer Guide (rendered on site)
│       └── environment_setup.md    # Python environment & dependencies
├── tests/                          # Test suite (pytest)
├── pyproject.toml / setup.py       # Configuration and dependencies
└── my_module/                      # Python package source code
    └── README.md                   # Sub-directory developer reference inside Python package source
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

## Documentation Projects

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

## Hybrid R & Python Projects

In research repositories (like
[`geyser`](https://byandell.github.io/geyser/)
or
[landmapyr](https://byandell.github.io/landmapyr/)),
R and Python code often sit side-by-side. The developer guide must
reconcile both ecosystems, outlining boundaries and interfaces.

### Dual-Housing Documentation Strategy

Based on experience with the `geyser` package, hybrid repositories succeed by adopting a **three-tier documentation strategy**:

1. **Root Repository Guide (`DEVELOPER.md`)**:
   - Primary entry point for developers of the overall project.
   - Documents shared architecture, cross-language module mappings (e.g., R 5-function modules vs Python `@module.ui` / `@module.server`), execution entry points, setup commands (`devtools::load_all()` and `pip install -e .`), port discovery, and reserved file patterns.
   - Links out to ecosystem-specific sub-guides.
2. **R Package Sub-Guide (`vignettes/DeveloperGuide.Rmd`)**:
   - Master vignette for R package compilation (`devtools::build_vignettes()`) and `pkgdown` articles rendering.
   - Focuses on R reactive flow, S3/S4 object structures, and R Shiny module patterns.
3. **Python Package Sub-Guide (`docs/devel/python.md` & `my_module/README.md`)**:
   - Housed in `docs/devel/python.md` for web/Quarto site rendering (`byandell.github.io/<project>`).
   - Housed in `my_module/README.md` as an in-source developer reference for Python package developers.
   - Focuses on Python reactivity, async loops, Shinylive WebAssembly build flows, and `rpy2` / dataframe data exchange.
4. **Planning & Execution Record (`guides.md`)**:
   - Consolidates initial blueprint prompts, the implementation plan, and the execution walkthrough for auditability and pair-programming context.

### Directory Layout

```text
hybrid_project/
├── DEVELOPER.md                    # Root architecture index & hybrid guide (both R & Python)
├── README.md                       # Repository overview & quickstart (links to DEVELOPER.md)
├── guides.md                       # Consolidated blueprint prompts, plan, and walkthrough
├── R/                              # R package source code
├── vignettes/                      # R-centric Vignettes
│   └── DeveloperGuide.Rmd          # Master R developer guide vignette
├── my_module/                      # Python package source code
│   ├── README.md                   # Python package sub-directory developer reference
│   └── io.py, hist.py, etc.        # Python package modules
└── docs/                           # Documentation & Quarto / MkDocs Website
    └── devel/                      # Extended sub-guides directory
        └── python.md               # Detailed Python Developer Guide (rendered on site)
```

### Actionable Prompts

1. **Bridge Architecture Map**:
   > "Create a root `DEVELOPER.md` describing how the R and Python components cooperate. Trace the communication boundaries (e.g.,
   [`reticulate`](https://rstudio.github.io/reticulate/),
   [`rpy2`](https://rpy2.readthedocs.io/en/latest/),
   subprocess calls, REST APIs, or shared SQLite/Parquet files). Provide a side-by-side R and Python module cross-reference table mapping equivalent features across ecosystems."
2. **Dual-Environment Configuration**:
   > "Create environment guides mapping out how to bootstrap both R and Python environments on a local machine. Document installation commands (`devtools::load_all()` for R and `pip install -e .` for Python) and dependency declarations."
3. **Shared Data & API Schemas**:
   > "Document data structures shared between R and Python code. Define SQLite database schemas, HDF5 hierarchies, or Parquet column schemas, detailing validation checks on both sides (e.g., `pandas.DataFrame` and R `data.frame` conversion rules)."

### Steps to Perform

1. **Establish Root Entry Point**: Create `DEVELOPER.md` in the repository root as the master developer guide indexing both R and Python architectures.
2. **Implement R Vignette Guide**: Draft `vignettes/DeveloperGuide.Rmd` to document R package modules and integration with `pkgdown`.
3. **Implement Python Sub-Guides**:
   - Create `docs/devel/python.md` for site documentation (e.g., Quarto).
   - Create `my_module/README.md` within the Python source folder for direct developer reference.
4. **Define Dual-Testing Workflows**: Outline execution scripts that run both
[`pytest`](https://pytest.org/)
and
[`devtools::test`](https://testthat.r-lib.org/reference/test_package.html)
as part of verification.
5. **Coordinate Shared Data Schemas & Planning**: Formulate explicit specifications for exchange file formats
([CSV](https://allthings.how/what-is-a-csv-file-and-how-to-open-or-create-it/),
[Parquet](https://parquet.apache.org/),
[SQLite](https://www.sqlite.org/))
and maintain a `guides.md` file recording initial prompts, implementation plan, and completion walkthrough.
