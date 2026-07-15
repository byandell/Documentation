---
title: "Create Shiny App Gallery"
parent: "Prompt Examples"
nav_order: 8
---

# Create Shiny App Gallery

This guide explains how to display both a Shiny application and its source code side-by-side or on the same page, similar to the
[Posit Shiny Gallery](https://shiny.posit.co/r/gallery/).

We cover two main approaches: using embedded client-side **Shinylive** apps in a Quarto page (highly recommended for hosting on static sites like GitHub Pages without folder clutter), and R's built-in **Showcase Mode** (best for local R console development).
Below is a series of prompts that were used to develop this guide and add demo apps to the
[byandell/geyser](https://github.com/byandell/geyser) repo.
See also
[GitHub Actions](../github/actions.md) for information on how to deploy the app.

## Prompts

- I would like to use the machinery of <https://shiny.posit.co/r/gallery/start-simple/faithful/> to display both an app and its code. Please help me understand how that is done and how I can modify this repo to create something similar. In the end, I want to be able to use this to demo R apps in this package. See for instance `inst/build_module/4_moduleServer/app.R` and `inst/build_module/4_moduleServer/moduleServer.R` for the app components.
- Please use a `.github/deploy.yml` file for `GitHub Actions` to avoid having extraeneous folders (like `site_libs`) be part of the GitHub repo.
- Make sure `README.md` in `/docs/` folder is not ignored by using a `/docs/index.qmd` file to cite it.
- Develop a `demo_gallery.qmd` file that incorporates both the posit gallery faithful example app and my code. Make sure their files are in separate code tabs below each display.
- Propose a way to reorganize as `docs/demos/`
to accomodate multiple examples, each in its own `*.qmd` file.
That is, separate files for the Posit Gallery Example and My Source Code App. I assume this folder will need a `index.qmd` canibalized from `demo_gallery.qmd`. Please advise on how to organize for further demos.
- Is there a way I can specify order of blocks for display in docs/demos? Can I have a navigation link on those blocks to return to main demos page?
- Create `docs/demos/connect_modules.qmd` using contents of folder `inst/connect_modules/demo`
- Fix `inst/connect_modules/demo/app.R` to source all the `*.R` files in that folder. Update `docs/demos/connect_modules.qmd` accordingly.
- I want to use `inst/build_module/app_hist.py` to build `docs/demos/python_module.qmd`. Please guide me. Make sure `shinylive` and `github actions` have what they need for this `python` code.
- Create `docs/demos/quarto.qmd` using `inst/connect_modules/quarto/demo.qmd`. Since native Quarto Dashboards require a server and cannot be compiled directly in a static website project, embed the live Posit Connect app via an iframe and display the code below it.
- Why is there a gray rectangle above the name of each demo as part of the card? Can I adjust the card content and layout?

---

## Method 1: Embedded Shinylive (Recommended for Web Galleries)

By using the `{shinylive-r}` Quarto block, your app code is compiled and embedded directly inside the final HTML document. This eliminates the need for any extraneous folders or files in your git repository. It also provides an interactive, copyable, and runnable editor panel side-by-side (or stacked) with the live app.

> [!TIP]
> **Customizing the Layout Components**:
>
> - **Viewer-Only Mode (Default for Galleries)**: To hide the code editor entirely and only display the running app, set `#| components: [viewer]`. This is ideal when you want to show the code in separate static tabs below the app.
> - **Interactive Code Editor**: To allow users to modify the code and run it inside their browser, set `#| components: [editor, viewer]`.

### 1. Configure the Quarto Document

Create a `.qmd` file (like [docs/demos/build_module.qmd](demos/build_module.qmd)) that includes the `shinylive` filter in the YAML header (or share it across the directory via `_metadata.yml`):

```yaml
---
title: "Build Module (Shinylive)"
filters:
  - shinylive
---
```

### 2. Embed the App using `{shinylive-r}`

Add your self-contained app code (combining your module server and main app) in a `{shinylive-r}` code chunk, specifying the `editor` and `viewer` components:

```markdown
\`\`\`{shinylive-r}
#| standalone: true
#| viewerHeight: 500
#| components: [editor, viewer]
#| layout: vertical

library(shiny)
library(bslib)

# --- Module definitions ---
geyserServer <- function(id) { ... }
geyserInput <- function(id) { ... }
geyserOutput <- function(id) { ... }
geyserUI <- function(id) { ... }

# --- App entry point ---
ui <- bslib::page(
  geyserInput(id = "geyser"), 
  geyserOutput(id = "geyser"),
  geyserUI(id = "geyser")
)
server <- function(input, output, session) {
  geyserServer(id = "geyser")
}
shiny::shinyApp(ui, server)
\`\`\`
```

### 2b. Embed Python Apps using `{shinylive-python}`

For Python-based Shiny apps, you can use the `{shinylive-python}` code block. The Quarto Shinylive filter handles compiling and packaging the Python code just like the R version.

#### 1. Specifying Requirements

Inside browser WebAssembly (Pyodide), packages are downloaded dynamically. You must declare any package requirements by creating a virtual `requirements.txt` file within the code block using the `## file:` header syntax:

```markdown
\`\`\`{shinylive-python}
#| standalone: true
#| viewerHeight: 600
#| components: [viewer]

## file: requirements.txt
pandas
numpy
matplotlib
scipy

# Python code files here (e.g. ## file: app.py)...
\`\`\`
```

#### 2. Multi-File Apps and Local Packages

You can structure multi-file Python applications using the same `## file:` header comment syntax. For example, if you want to import from a local package folder (like `geyser/hist.py`), define `geyser/__init__.py` and the module files within the code block:

```markdown
## file: app.py
from shiny import App, ui
from geyser.hist import hist_server, hist_input, hist_output, hist_ui

app_ui = ui.page_fluid(
    hist_input("hist"),
    hist_output("hist"),
    hist_ui("hist")
)

def app_server(input, output, session):
    hist_server("hist")

app = App(app_ui, app_server)

## file: geyser/__init__.py
# empty package marker

## file: geyser/hist.py
# custom module logic goes here...
```

#### 3. WebAssembly Gotchas (CORS & C-Extensions)

When deploying Python Shinylive apps, be mindful of browser restrictions:

- **CORS Policies**: Standard python code that fetches data from online repositories (e.g. `seaborn.load_dataset("geyser")`) will fail due to browser CORS restriction blocks. Mock the dataset call to return a local static `pandas.DataFrame`.
- **C-Extensions**: Packages that compile C code locally (such as `rpy2` or custom DB connectors) are not compatible with standard Pyodide in the browser. You must mock those modules or replace them with native Python/browser equivalents.

### 3. Rendering and Local Preview

Modern web browsers block Service Workers and WebAssembly from running over the `file://` protocol. If you open the rendered `.html` page directly as a local file, the app will display as a blank page.

To preview and test the app locally, you must serve the files via a local HTTP server:

- **Quarto Preview (Easiest)**: Run this in your terminal. It will render the page, start a local server, and open your browser:

  ```bash
  quarto preview docs/demos/build_module.qmd
  ```

- **Python HTTP Server**: Serve the `docs/` folder from Python:

  ```bash
  python3 -m http.server 8000 --directory docs
  ```

  Then navigate to `http://localhost:8000/demos/build_module.html`.
- **R `servr` Package**: Serve from R console:

  ```r
  servr::httd("docs")
  ```

### 4. Deploying to GitHub Pages

To avoid committing large generated assets (like the 70MB `site_libs/` folder) to your Git repository, the website compilation and hosting are automated via a GitHub Actions pipeline.

For detailed setup instructions, troubleshooting steps, and custom configurations, see the [Quarto GitHub Actions Deployment Guide](github_actions.md).

> [!IMPORTANT]
> **GitHub Actions & Python Shinylive**:
> If your site includes `{shinylive-python}` blocks, the GitHub Actions deployment runner must have Python and the `shinylive` Python package installed to render them. Ensure your `.github/workflows/deploy.yml` includes:
>
> ```yaml
> - name: Set up Python
>   uses: actions/setup-python@v5
>   with:
>     python-version: '3.12'
> - name: Install Python dependencies
>   run: |
>     pip install shinylive
> ```
>
> Otherwise, the build will fail with the error: `Error running 'shinylive' command`.

Once set up, your live page will be automatically built and hosted at:
`https://byandell.github.io/geyser/demos/index.html` (or `demos/build_module.html` for the direct app).

---

## Organizing & Scaling Future Demos

As your project grows and you add more modules or demo applications, keeping them in a dedicated `docs/demos/` subdirectory scales much better than single files.

### 1. The Directory Layout

Organize the subdirectory with an index and shared metadata:

```
docs/
└── demos/
    ├── _metadata.yml          # Shared Quarto settings for the directory
    ├── index.qmd              # Demos landing/gallery index
    ├── posit_gallery.qmd      # Individual demo (e.g. iframe embed)
    ├── build_module.qmd       # Individual demo (e.g. Shinylive app)
    ├── connect_modules.qmd    # Connected modules demo (multi-file Shinylive)
    └── python_module.qmd      # Python module demo (Python Shinylive)
```

### 2. Sharing Configurations via `_metadata.yml`

Instead of repeating the `shinylive` filter and `knitr` engine in every new `.qmd` file, you can create a `_metadata.yml` file in the subdirectory. Quarto automatically applies these settings to all documents in that directory:

```yaml
# docs/demos/_metadata.yml
engine: knitr
filters:
  - shinylive
```

### 3. Automated Listing Galleries (`index.qmd`)

You can use Quarto's built-in **Listings** to automatically build a landing page grid. When you add a new demo `.qmd` file to the folder, Quarto will automatically detect it and render a preview card on the landing page, without requiring you to manually maintain list links.

Example `docs/demos/index.qmd`:

```yaml
---
title: "Geyser Demos Gallery"
toc: false
listing:
  contents:
    - build_module.qmd         # List files in the exact order you want them displayed
    - posit_gallery.qmd
  type: grid                   # Renders a modern grid layout of card previews
  categories: true             # Set to true to filter demos by tags (e.g., R, Python)
---

Explore the interactive geyser demos below:
```

#### Card Image Placeholders and Customization

By default, the `grid` listing type creates preview cards that expect a thumbnail image. If a page does not specify a thumbnail, Quarto will display a placeholder gray rectangle.

- **Assigning a Card Image**: To show an image on the card, add the `image` parameter to the frontmatter of that specific `.qmd` file, using a relative path to the image:

  ```yaml
  ---
  title: "Quarto Dashboard"
  image: "../images/pagesQmd.png"
  ---
  ```

* **Hiding Card Images**: If you do not want to use images, you can customize the card content in `index.qmd` by using the `fields` key and omitting `image`:

  ```yaml
  listing:
    type: grid
    fields: [title, description, author] # Hides the image placeholder
  ```

* **Card Sizing and Layout**: You can adjust columns (`grid-columns: 3`) and alignment (`grid-item-align: top`) under the `listing` block.

For a full list of card parameters and custom EJS templates, see the official [Quarto Document Listings Guide](https://quarto.org/docs/websites/website-listings.html#grid-layout).

### 4. Adding New Demos

To add a new demo:

1. Create a new `.qmd` file under `docs/demos/` (e.g. `gghist_demo.qmd`).
2. Add a simple YAML header specifying the title, description, and optional categories:

   ```yaml
   ---
   title: "ggplot2 Histogram Demo"
   description: "Interactive exploration of geyser wait times using ggplot2."
   categories: [R, ggplot2]
   ---
   ```

3. Use relative paths starting with `../../` to refer to root package assets (since files under `docs/demos/` are two levels deep relative to the project root).
4. Add a navigation link back to the gallery page at the top of your page content:

   ```markdown
   [← Back to Demos Gallery](index.qmd)
   ```

5. Update `index.qmd`'s `listing.contents` list if you want to explicitly place it in the display order.

### 5. Handling Native Quarto Dashboards (`server: shiny`)

If you want to demo a native Quarto Dashboard (`format: dashboard`, `server: shiny`), note that it cannot be compiled directly inside a static website project (such as a GitHub Pages site rendered with `quarto render docs/`). Quarto will throw an error:
`ERROR: demos/quarto.qmd uses server: shiny so cannot be included in a website project (shiny documents require a backend server and so can't be published as static web content).`

To resolve this and showcase a dashboard in your static web gallery:

1. **Deploy the Dashboard Separately**: Deploy your interactive dashboard `.qmd` to a platform that supports a live R backend (such as **Posit Connect**, **shinyapps.io**, or a self-hosted **Shiny Server**).
2. **Use Iframe Embedding in the Gallery**: Create a standard HTML page under `docs/demos/` (e.g., `docs/demos/quarto.qmd` with `format: html`) and embed the live dashboard URL via an `iframe`.
3. **Display Source Code Below**: Read and display the source code of the dashboard from its actual location (e.g., `inst/connect_modules/quarto/demo.qmd`) in a panel tabset using `readLines`.

Example `docs/demos/quarto.qmd`:

```markdown
---
title: "Quarto Dashboard"
description: "A native Quarto Dashboard layout showing Shiny module connections. Note: Runs via an embedded iframe from Posit Connect."
toc: false
---

[← Back to Demos Gallery](index.qmd)

This section displays the geyser Quarto Dashboard app hosted on Posit Connect, using an `iframe` embedding.

<div class="shiny-app-frame" style="margin-bottom: 30px;">
  <iframe src="https://connect.doit.wisc.edu/geyserQuartoDemo" style="width: 100%; height: 800px; border: 1px solid #ccc; border-radius: 4px;"></iframe>
</div>

## Source Code

Below you can view the complete source file for the Quarto dashboard.

::: {.panel-tabset}

### demo.qmd
\`\`\`{r}
#| code: !expr readLines("../../inst/connect_modules/quarto/demo.qmd")
#| eval: false
\`\`\`

:::
```

1. **Self-Contained Deployment Tip**:
   When deploying the dashboard to Posit Connect or shinyapps.io, you must either:
   - Use a `context: setup` block that installs the R package from GitHub (e.g., `pak::pak("byandell/geyser")`).
   - Or bring in copies of the supporting `.R` module files from the package directory and place them alongside the dashboard file so they are bundled during deployment.

---

## Method 2: Shiny Showcase Mode (Built-in R Shiny)

If you are developing or running the app locally, R's built-in **Showcase Mode** is the easiest option. It puts the app in a frame, shows the code next to/below the app, and highlights reactive execution in real-time.

### Running Showcase Mode

To launch the app in showcase mode from your R console:

```r
shiny::runApp("inst/build_module/4_moduleServer", display.mode = "showcase")
```

### Adding Metadata & Documentation

To configure the showcase:

1. Add a `DESCRIPTION` file to the app folder:

   ```dcf
   Title: Geyser Module Server App
   Author: Brian S. Yandell
   Description: Old Faithful geyser dataset module server demo.
   DisplayMode: Showcase
   ```

2. Add a `README.md` to the app folder. Shiny will automatically render this markdown file directly below the code panel.
