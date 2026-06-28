# Deploy Shinylive apps to GitHub Pages

The following prompts are modified from the original conversation in the
[geyser](https://github.com/byandell/geyser) repo with Gemini.
The reconstructed deploy YAML file, which should go in
`.github/workflows/deploy.yml`
is saved here as
[deploy.yml](deploy.yml).

## Prompts

- What files in docs/shiny can I ignore with .gitignore but make sure the shiny app will function when pushed to GitHub?
- Proceed with Option 1.
- Is .github/workflows/deploy.yml set up to publish the rest of material in the docs/ folder? Notably the html and qmd documents are not shown.

## Response

If you are deploying a Shinylive app to GitHub Pages, you have two different strategies depending on how you want to handle the deployment.

---

### Option 1: Using GitHub Actions (Recommended & Best Practice)

The standard and cleanest way to deploy a Shinylive app is to **never commit the build directory to Git**. This avoids bloating your repository with the large WebAssembly runtime (currently ~76MB).

Instead, you let GitHub Actions build the Shinylive export on-the-fly and deploy it.

1. **Add this to your `.gitignore`:**

   ```text
   # Ignore all generated shinylive app files
   docs/shiny/
   ```

2. **Setup a GitHub Action Workflow:**
   Create a file at `.github/workflows/deploy.yml` with the following contents:

   ```yaml
   name: Deploy Shinylive App
   on:
     push:
       branches: [main] # or master
   jobs:
     build-and-deploy:
       runs-on: ubuntu-latest
       permissions:
         contents: read
         pages: write
         id-token: write
       steps:
         - uses: actions/checkout@v4
         - uses: r-lib/actions/setup-r@v2
         - name: Install Shinylive
           run: Rscript -e "install.packages('shinylive')"
         - name: Export App
           # Copies R files to inst/connect_modules/R/ first if not in git
           run: |
             cp -r R inst/connect_modules/
             Rscript -e "shinylive::export('inst/connect_modules', 'docs/shiny', wasm_packages = FALSE)"
         - name: Upload Pages artifact
           uses: actions/upload-pages-artifact@v3
           with:
             path: 'docs/shiny'
         - name: Deploy to GitHub Pages
           uses: actions/deploy-pages@v4
   ```

#### Modify `deploy.yml` to publish the entire `docs/` folder

In the previous version, only `docs/shiny` was uploaded.

I have updated `.github/workflows/deploy.yml` so that the **entire `docs/` directory** is uploaded and published to GitHub Pages:

```yaml
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: 'docs'  # Changed from 'docs/shiny' to publish the whole folder
```

#### Modify `deploy.yml` to install knitr and rmarkdown

```yaml
      - name: Install Shinylive, Knitr, and Rmarkdown
        run: |
          Rscript -e "install.packages(c('shinylive', 'knitr', 'rmarkdown'))"
```

1. In your GitHub Repository settings, go to **Settings** > **Pages** and under **Build and deployment** > **Source**, change the setting to **GitHub Actions**.

---

### Option 2: Committing the Export Directly (Local Build)

If you prefer not to use GitHub Actions and want to commit the build outputs directly to Git so GitHub Pages can serve them:

**You cannot ignore any files inside `docs/shiny`** (except for the 278-byte redirect page at `docs/shiny/edit/index.html`).

- `index.html` is the launcher.
- `app.json` contains your actual code.
- `shinylive-sw.js` is the service worker.
- `shinylive/` contains the essential `webR` WebAssembly binaries (`R.wasm`, virtual filesystem, etc.) required to run R inside the browser.

#### How to optimize the file size for this option

To save 53MB of space in your Git history, you should export the app with `wasm_packages = FALSE`:

```R
shinylive::export(
  appdir = "inst/connect_modules", 
  destdir = "docs/shiny", 
  wasm_packages = FALSE
)
```

This tells Shinylive not to download the package binaries (like `ggplot2`, `dplyr`, `bslib`) locally. Instead, the browser will dynamically fetch them from `repo.r-wasm.org` when a user opens the page. This reduces the folder size from **129MB** to **76MB**.

### Set up Option 1

I have successfully set up **Option 1 (GitHub Actions / CI-CD Deployment)** for you:

1. **Ignored Local Build Outputs**: Added `/docs/shiny/` to your `.gitignore` file. This ensures you won't accidentally commit the large locally-generated Shinylive WebAssembly folder (76MB+) to your Git history.
2. **Created GitHub Actions Workflow**: Created the deployment workflow at `.github/workflows/deploy.yml`.

#### What happens now?

Whenever you push to the `main` or `master` branch:

1. GitHub will spin up an environment, install `shinylive` and other setup tools.
2. It will copy the root `R/` package scripts dynamically into `inst/connect_modules/R/`.
3. It will export the Shinylive application with `wasm_packages = FALSE` directly into `docs/shiny`.
4. It will publish `docs/shiny` directly to your GitHub Pages hosting.

### ⚠️ Final Step Required by You

Please go to your repository on GitHub, navigate to **Settings** > **Pages**, and under **Build and deployment** > **Source**, make sure it is changed to **GitHub Actions** instead of "Deploy from a branch".

### What this means for your site structure

- The rest of your files in `docs/` (such as `docs/geyserShinyPython.html` and `docs/geyserShinyR.html`) will be served at the root of your GitHub Pages site (e.g., `https://username.github.io/geyser/geyserShinyR.html`).

- The Shinylive app will be built and served inside the `/shiny/` subfolder (e.g., `https://username.github.io/geyser/shiny/`).
