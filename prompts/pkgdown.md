# Use `pkgdown` to Auto-Build GitHub Website

## Prompt

- Modify repo so that `docs/` can be used for GitHub Pages.

## What is `pkgdown`?

[pkgdown](https://pkgdown.r-lib.org/)
is an R package designed to automatically generate a complete, modern, and searchable documentation website for your R package.

Specifically, it takes your package's existing files and compiles them into a static HTML site within the `docs/` folder, featuring:

1. **Homepage**: Rendered directly from your root `README.md` (including badges, installation instructions, description, etc.).
2. **Function Reference**: Formats all your package's documentation (`.Rd` files in the `man/` directory, typically written using `roxygen2`) into beautiful, easy-to-read pages with syntax highlighting for your code examples.
3. **Articles & Vignettes**: Compiles your R Markdown and Markdown files in the `vignettes/` directory into hosted articles (like your `UserGuide.Rmd` and `DeveloperGuide.Rmd`).
4. **News**: Parses your `NEWS.md` file (if available) to show a chronological changelog of release notes.

By outputting this compiled website directly to `docs/` and committing it, **GitHub Pages** can host and serve the site automatically to the web (e.g., `https://byandell-sysgen.github.io/qtl2shiny/`).

## Walkthrough

We have successfully configured the repository to automatically build and deploy a `pkgdown` website on every push to the `main` or `master` branches using GitHub Actions, while keeping the repository clean of auto-generated HTML/JS/CSS assets.

### Configuration

1. **Created `_pkgdown.yml`**: Added standard website structure, Bootstrap 5 templates, custom navigation dropdown menus under the "Guides" section, and mapped custom articles for the user and developer documentation.
2. **Updated `.Rbuildignore`**: Configured patterns to ignore the `_pkgdown.yml` configuration, `.github/` folder, and the source `vignettes/devel_guide/` files from the R package bundle.
3. **Updated `.gitignore`**: Added `docs` to ignore the local compiled website output directory, keeping the repository git history clean.
4. **Created `.github/workflows/pkgdown.yaml`**: Set up the official `pkgdown` GitHub Action workflow to build the website and deploy it to the `gh-pages` branch on every push.

### Documentation Files

1. **Relocated Developer Guides**: Relocated files from the `docs/devel_guide/` directory to the `vignettes/devel_guide/` directory to prevent them from being deleted during site builds.
2. **Converted `.md` to `.Rmd`**: Renamed developer guide files in `vignettes/devel_guide/` from `.md` to `.Rmd` and injected standard package vignette YAML headers. This enables `pkgdown` to automatically recognize and build them as articles.
3. **Adjusted Links**:
   - Updated the relative links in `vignettes/devel_guide/index.Rmd` (formerly `README.md`) to point to `.html` destinations.
   - Updated the link in root `README.md` to point to the rendered `articles/devel_guide/index.html` file.
   - Removed the duplicate `docs/README.md`.

### Bug Fixes

- Fixed a bug in `inst/scripts/qtl2dag.Rmd` where it referred to `netModule` (which was not defined) instead of `net_server` in an `igraph` plot call. This was causing `vignettes/DeveloperGuide.Rmd` to fail rendering.

---

## Verification Results

### Automated and Manual Site Build

- Ran `Rscript -e "pkgdown::build_site()"` which built the documentation website successfully.
- Verified that all article pages, reference manual pages, and homepage index files were successfully created inside `docs/` and `docs/articles/devel_guide/`.
- Verified that relative links between the modules under `docs/articles/devel_guide/` resolve correctly.

### Package Build Check

- Ran `R CMD build . --no-build-vignettes` which completed successfully and correctly excluded the `docs/` folder and `vignettes/devel_guide/` folder from the built package tarball.

---

## GitHub Settings Configuration

To finalize the automated `pkgdown` deployment on GitHub:

1. **Push the Changes**: Commit and push the `.github/workflows/pkgdown.yaml` and other configurations to your main branch (`main` or `master`). This will run the action and automatically create the `gh-pages` branch.
2. **Configure GitHub Pages**:
   - Go to **Settings → Pages** in your repository.
   - Under **Build and deployment → Source**, select **Deploy from a branch**.
   - Under **Branch**, select **`gh-pages`** and set the folder to **`/ (root)`**.
   - Click **Save**.
3. **Allow Write Permissions** (If deployment fails):
   - Go to **Settings → Actions → General**.
   - Scroll down to **Workflow permissions** and select **Read and write permissions**.
   - Click **Save**.

