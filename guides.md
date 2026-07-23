---
title: "Create User and Developer Guides"
parent: "Document Digital Tools"
nav_order: 6
---

# Create User and Developer Guides

User and Developer Guides are handy to provide overviews of projects
by highlighting useful functions and approaches.
In addition, `README.md` and `AGENTS.md` files are handy for overiews.
Here are some examples:

## Table of Contents

- [Digital Tool Guides & Prompts](#digital-tools-guides--prompts)
  - [Prompts](#prompts)
  - [Guides and Overviews](#guides-and-overviews)
- [Documentation Repo Developer Guide](#documentation-repo-developer-guide)
  - [1. Site Layout & Directory Map](#1-site-layout--directory-map)
  - [2. Page Metadata & Frontmatter Standards](#2-page-metadata--frontmatter-standards)
  - [3. Automation & Link Checking](#3-automation--link-checking)

---

## Digital Tool Guides & Prompts

### Prompts

- [Create Developer Guides (Blueprint)](prompts/devel_guide.md)
- [Create Developer Guide to `qtl2shiny` (Reference Case Study)](prompts/devel_guide_qtl2shiny.md)
- [Use `pkgdown` to Auto-Build GitHub Website](github/pkgdown.md)

### Guides and Overviews

- [this repo](https://byandell.github.io/Documentation)
  - [Developer Guide](#documentation-repo-developer-guide)
  - [AGENTS.md](AGENTS.md)
- [`qtl2shiny`](https://byandell-sysgen.github.io/qtl2shiny/)
  - [Articles](https://byandell-sysgen.github.io/qtl2shiny/articles/)
  - [Developer Guide](https://byandell-sysgen.github.io/qtl2shiny/articles/devel_guide/index.html)
  - [DEVELOPER.md](https://github.com/byandell-sysgen/qtl2shiny/blob/main/DEVELOPER.md)
  - [AGENTS.md](https://github.com/byandell-sysgen/qtl2shiny/blob/main/AGENTS.md)
- [`geyser`](https://byandell.github.io/geyser/)
  - [Architectural Overview (DEVELOPER.md)](https://byandell.github.io/geyser/DEVELOPER.html)
  - [R Developer Guide (DeveloperGuide.Rmd)](https://byandell.github.io/geyser/vignettes/DeveloperGuide.html)
  - [Python Developer Guide (python.md)](https://byandell.github.io/geyser/docs/devel/python.html)
  - [AGENTS.md](https://github.com/byandell/geyser/blob/main/AGENTS.md)
- [`landmapyr`](https://byandell-envsys=.github.io/landmapyr/)
  - [AGENTS.md](https://github.com/byandell-envsys/landmapyr/blob/main/AGENTS.md)

---

## Documentation Repo Developer Guide

This section serves as the developer guide for managing, editing, and checking the integrity of this `Documentation` repository.

### 1. Site Layout & Directory Map

The repository is built as a Jekyll static site using the `just-the-docs` theme, compiled automatically on GitHub Pages. Quarto is used to build slides.

```text
Documentation/
├── _config.yml                     # Jekyll configuration (remote theme, plugins)
├── _quarto.yml                     # Quarto website output options
├── README.md                       # Main site landing page (index)
├── guides.md                       # Main guides index & repo developer guide (this page)
├── AGENTS.md                       # Workspace conventions and rules for AI agents
├── R/                              # R language tutorials and notebooks
├── python/                         # Python language tutorials and notebooks
├── github/                         # Git and GitHub publishing workflows
├── envsys/                         # Environmental systems data notes
├── datasci/                        # Data science resources
├── AI/                             # AI tool summaries and agents research
├── prompts/                        # System prompts and case studies
├── quarto/                         # Quarto source slides and compiled slide decks
└── scripts/                        # Repository helper scripts
    ├── check_links.py              # Automated link checking script
    └── add_glyphs.py               # Glyphs addition helper
```

### Configuration Files

- **`_config.yml`**: Uses the `remote_theme: just-the-docs/just-the-docs`. It enables `jekyll-relative-links` (allowing markdown files to reference each other with standard relative links like `[text](folder/file.md)`) and auto-generates the side navigation tree based on metadata.
- **`_quarto.yml`**: Configures Quarto slide projects to compile `.qmd` files in place (`output-dir: .`) so they can be processed and served alongside Jekyll markdown files.

---

### 2. Page Metadata & Frontmatter Standards

To ensure Jekyll organizes the navigation sidebar and breadcrumbs correctly, every markdown and Quarto file must begin with standard YAML frontmatter:

```yaml
---
title: "The Page Title"                # Shows in navigation menu and page title
parent: "Parent Page Title"           # MUST match the exact title of the parent page (optional)
nav_order: 3                           # Determines layout order under parent (optional)
permalink: /optional/custom/path/      # Absolute URL path override (optional)
---
```

### Folder Conventions

- Save general conceptual notes as markdown files (`.md`) inside their respective folders (e.g. `github/`, `AI/`, `python/`).
- Save slides as Quarto slides (`.qmd`) under `quarto/`.
- Ensure all relative link paths to other documents do not include leading slashes or absolute domain prefixes, so that they render correctly in local previews and on the published GitHub Pages site.

---

### 3. Automation & Link Checking

To prevent dead references and broken links as external websites change, use the automated script in `scripts/check_links.py` to scan the repository.

### Running the Link Checker

Run the script from the repository root:

```bash
python3 scripts/check_links.py
```

### Features

- Scans all `.md`, `.qmd`, and `.Rmd` files in the repository.
- Extracts and checks all `http://` and `https://` URLs in parallel using threaded execution.
- If broken links are found, generates a detailed markdown report (`link_check_report.md` in the root) listing the file, line number, URL, and HTTP status code or connection error.

For more details on link checking parameters (ignoring SSL errors, checking a single file, fetching historical Wayback Machine snapshots), see the [Check External Links Guide](prompts/check_links.md).
