---
title: "Deploy with GitHub Actions"
parent: "Publish GitHub Pages"
nav_order: 2
---

# Deploy with GitHub Actions

This guide explains how to set up a
[GitHub Actions](https://github.com/features/actions)
 workflow to build and deploy a Quarto website directly to
 [GitHub Pages](pages.md).
 This setup allows you to keep your Git repository clean and lightweight by avoiding checking in large generated directories
 (like `site_libs/`, which is over 70MB) or generated HTML files.

This shows how to host a client-side (browser run)
Shiny app provided it is fairly simple.
The tool to do this is
[Shinylive](https://shiny.posit.co/py/get-started/shinylive.html),
which was probably originally developed for `Python`
and is now available for `R` as
[r-shinylive](https://posit-dev.github.io/r-shinylive/).
All material must be self-contained in the app, including data.

- [Python Shinylive: Shiny + WebAssembly (Posit)](https://shiny.posit.co/py/get-started/shinylive.html)
- [r-shinylive](https://posit-dev.github.io/r-shinylive/)
- [py-shinylive](https://github.com/posit-dev/py-shinylive)
- [Using Shinylive to host Shiny app on GitHub Pages (HBC Training)](https://hbctraining.github.io/Training-modules/RShiny/lessons/shinylive.html)

## Table of Contents

- [GitHub Actions Workflow](#github-actions-workflow)
- [Key Architecture Decisions & Gotchas](#key-architecture-decisions--gotchas)
  - [Subfolder Project Roots & Extension Paths](#subfolder-project-roots--extension-paths)
  - [Jupyter/Python Kernel Fallbacks](#jupyterpython-kernel-fallbacks)
  - [Jekyll Bypassing & Homepage (`index.html`) Missing](#jekyll-bypassing--homepage-indexhtml-missing)
  - [Clean Git Repository & Local `.gitignore`](#clean-git-repository--local-gitignore)
- [GitHub Pages Repository Settings](#github-pages-repository-settings)
- Additional Pages
  - [Shinylive Performance Tradeoffs](shinylive.md)
  - [Use `pkgdown` to Auto-Build GitHub Website](pkgdown.md)

---

## GitHub Actions Workflow

Create a file named `.github/workflows/deploy.yml` in your repository. This file automates checking out the repository, installing R and system dependencies, setting up Quarto, rendering the website, and deploying the compiled files.

Here is the robust workflow used in this repository:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

# Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Allow only one concurrent deployment
concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up R
        uses: r-lib/actions/setup-r@v2
        with:
          use-public-rspm: true

      - name: Install R package dependencies
        run: |
          install.packages(c("rmarkdown", "knitr", "shinylive", "bslib", "shiny", "ggplot2", "dplyr", "DT", "rlang", "stringr", "tibble"))
        shell: Rscript {0}

      - name: Install local package (if site depends on it)
        run: |
          R CMD INSTALL .

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Install Quarto Shinylive Extension
        working-directory: docs
        run: |
          quarto add --no-prompt quarto-ext/shinylive

      - name: Render Website
        run: |
          quarto render docs/

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: 'docs/'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

---

## Key Architecture Decisions & Gotchas

When migrating a Quarto site to build on a GitHub Actions runner, keep these common issues in mind:

### Subfolder Project Roots & Extension Paths

If your Quarto project is located in a subdirectory (like `/docs`), Quarto treats that subdirectory as the root of the project (looking for `_quarto.yml` there).

- **The Issue**: Installing an extension in the main root folder will place it in `/_extensions`, but Quarto will only look inside `/docs/_extensions`.
- **The Fix**: Add `working-directory: docs` (or equivalent subfolder path) to the extension installation step:

  ```yaml
  - name: Install Quarto Shinylive Extension
    working-directory: docs
    run: quarto add --no-prompt quarto-ext/shinylive
  ```

### Jupyter/Python Kernel Fallbacks

When Quarto renders `.qmd` files containing code blocks, it evaluates which rendering engine to use. If it cannot resolve the Knitr package config, or if a Python/Jupyter syntax cell is detected, it will try to start a Python 3 Jupyter kernel. This will crash on a clean CI runner unless Jupyter and all package dependencies are pre-installed.

- **The Fix**: Always explicitly declare the engine in the YAML header of your `.qmd` documents to avoid automatic fallback search:

  ```yaml
  engine: knitr
  ```

### Jekyll Bypassing & Homepage (`index.html`) Missing

Historically, if you pushed a markdown file named `README.md` to GitHub Pages, the default Jekyll server automatically translated it to `index.html` to serve as the homepage.
Because our Actions runner deploys pre-rendered HTML directly (bypassing Jekyll), **Quarto does not translate `README.md` to `index.html` by default**.

- **The Fix**: Create a file named `index.qmd` in your project folder, and use Quarto's built-in include directive to dynamically copy your `README` during compile-time:

  ```markdown
  ---
  title: "Homepage"
  engine: knitr
  ---

  {{< include README.md >}}
  ```

### Clean Git Repository & Local `.gitignore`

Since GitHub Actions compiles the site on every push, you should configure Git to ignore all locally generated HTML files and libraries so that your Git commits remain lightweight.

Add the following to your `.gitignore` to keep your workspace clean:

```gitignore
# Quarto generated website assets (built and deployed dynamically by GitHub Actions)
/docs/*.html
/docs/site_libs/
/docs/_extensions/
/docs/shinylive-sw.js
/docs/app.json
```

If you previously committed these generated files to Git, remove them from tracking (while keeping your local files) using:

```bash
git rm --cached docs/demos/*.html
git rm -r --cached docs/site_libs/ docs/_extensions/ docs/app.json
git commit -m "Untrack generated files"
```

---

## GitHub Pages Repository Settings

After pushing your workflow file to GitHub:

1. Go to your repository on GitHub.
2. Click on **Settings** > **Pages** (in the left sidebar).
3. Under **Build and deployment** > **Source**, switch the dropdown from **"Deploy from a branch"** to **"GitHub Actions"**.

Now, every push to `main` will run the workflow and deploy the latest build automatically.
