---
title: "Just the Docs Configuration"
parent: "Prompt Examples"
---

# Just the Docs Configuration

**Challenge**:
When setting up a documentation site using GitHub Pages, you want a clean, modern, responsive design with hierarchical navigation (headings, sub-pages) and proper SEO tags (including page names in browser tabs), without having to build a custom site from scratch.

**Use**:
Set up a standard Jekyll repository and apply the following configuration to enable the `just-the-docs` theme, customize navigation hierarchy, and configure site metadata.

**Prompt**:
"Follow the [Just the Docs Configuration Prompt](https://github.com/byandell/Documentation/blob/main/prompts/justthedocs.md) to set up and configure the `just-the-docs` remote theme, establish a site-wide navigation structure, and enable page names in browser tabs."

---

## Just the Docs Configuration Guide

### 1. Remote Theme Configuration
To run `just-the-docs` directly on GitHub Pages without installing local gems, configure `_config.yml` in the root of your repository:

```yaml
# Site branding and URLs
title: "Documentation"
description: "Documentation for Digital Tools"
url: "https://byandell.github.io"
baseurl: "/Documentation"

# Theme setup
remote_theme: just-the-docs/just-the-docs

# Plugins for remote theme and relative links
plugins:
  - jekyll-relative-links
  - jekyll-remote-theme

relative_links:
  enabled: true
  collections: true

# Apply default theme layout to all pages
defaults:
  - scope:
      path: ""
      type: pages
    values:
      layout: default
```

### 2. Page Navigation and Hierarchy
Use Jekyll front matter at the top of each Markdown (`.md`) file to configure where it appears in the navigation sidebar:

#### Homepage (`index.md` or `README.md`)
Specify `permalink: /` to render this page at the root URL.
```yaml
---
title: "Documentation for Digital Tools"
nav_order: 1
permalink: /
---
```

#### Top-level Navigation Page
Set a high-level page order using `nav_order`.
```yaml
---
title: "AI (Artificial Intelligence)"
nav_order: 5
has_children: true
---
```

#### Second-level child page
Link to a parent page by matching its exact title in `parent`.
```yaml
---
title: "AI Prompt Examples"
parent: "AI (Artificial Intelligence)"
nav_order: 1
has_children: true
---
```

#### Third-level grandchild page
Link to a parent and grandparent page.
```yaml
---
title: "Just the Docs Configuration"
parent: "AI Prompt Examples"
grand_parent: "AI (Artificial Intelligence)"
nav_order: 2
---
```

### 3. Enabling Page Names in Browser Tabs
To display tab titles in the browser as `Page Title | Site Title` (e.g. `Just the Docs Configuration | Documentation`), the site must have:
1. `title` defined in `_config.yml` (e.g., `title: "Documentation"`).
2. `title` defined in the page's YAML front matter (e.g., `title: "Just the Docs Configuration"`).
3. The `jekyll-seo-tag` plugin (which is loaded automatically by the `just-the-docs` theme through its `{% seo %}` block in `_includes/head.html`).
