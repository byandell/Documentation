---
title: "Create Developer Guide to `qtl2shiny`"
parent: "Prompt Examples"
nav_order: 7
---

# Create Developer Guide to `qtl2shiny` (Reference Case Study)

> [!NOTE]
> This document serves as a concrete reference case study for creating a developer guide for a mature R package. For a general blueprint and template covering R, Python, Documentation, and hybrid projects, see the general [Developer Guide Blueprint](devel_guide.md).

This file documents the prompts, process and design decisions made while building the developer's guide for the `qtl2shiny` package,
which resides as [qtl2shiny Developer Guide](https://byandell-sysgen.github.io/qtl2shiny/articles/DeveloperGuide.html)
([source](https://github.com/byandell-sysgen/qtl2shiny/blob/master/vignettes/DeveloperGuide.Rmd)).
See also
[Use `pkgdown` to Auto-Build GitHub Website](../github/pkgdown.md).

## Prompts

The developer's guide structure and content were developed interactively using the following prompts:

1. **Initial Setup**: "Create a developer guide to `qtl2shiny` package in `inst/doc/devel_guide/` folder. This will have a high-level guide to the panels used in `R/qtl2shinyApp.R` and major sections for each of those panels. It should focus on `R/*App.R` files, noting how some are integral to a panel and other are more generic. Consider the `doc/genoDataApp.md` as a model, which should be moved into the folder. Include a `README.md` in that folder. Use this file `inst/doc/devel_guide.md` to document the process of creating this guide."
2. **Relative Links Conversion**: "Make links in `inst/doc/devel_guide/README.md` relative."
3. **Table of Contents**: "Provide a TOC to `inst/doc/devel_guide/README.md`. After internal TOC, include a link to `./genoDataApp.md` in anticipation of more guide detail pages like this."
4. **Genotypes Panel Expansion**: "Develop detailed guides for `genoApp`, `genoPlotApp` and `genoEffectApp`. Make this an expansion (and renaming) of `genoDataApp.md`, reusing material as possible."
5. **Remaining Panel Guides**: "Using `genoApp.md` as a model, create developer guides for the other panels, including a link back to the developer's guide main page (`README.md`)."
6. **Prototype History**: "Add to `inst/doc/devel_guide.md` documentation of creating the initial `inst/doc/genoDataApp.md` as a prototype/model for the full developer's guide."
7. **Prompts Documentation**: "Add a front section on `## Prompts` used to develop this process."

## Prototype Development

Prior to launching the full developer's guide, a single-module documentation prototype was created: `inst/doc/genoDataApp.md` (which documented the genotype data submodule `genoDataApp`). This prototype served as a model for the entire developer's guide, establishing standard headings and design representations:

- **Module Hierarchy and Entrypoints**: Detailing the standalone entrypoint, the server module, and UI inputs/outputs.
- **Data Dependencies**: Clarifying what RDS and SQLite files the module reads.
- **Workflow Reactivity Diagrams**: Utilizing Mermaid flowcharts to visualize reactive logic.
- **Defensive Design Patterns**: Explaining code defensive checks (e.g. updating sliders reactively to prevent out-of-bounds errors when chromosome coordinates reset).

The success of the `genoDataApp.md` prototype in clarifying module logic led to the decision to expand it into a unified Genotypes guide (`genoApp.md`) and reproduce the same structured format for all other major panels.

## Steps Performed

1. **Analysis of File Structure**:
   - Identified all 41 `R/*App.R` files on the filesystem.
   - Traced their loading and execution hierarchy within [R/qtl2shinyApp.R](../R/qtl2shinyApp.R) and `inst/qtl2shinyApp/app.R`.

2. **Creation of Guide Directory**:
   - Created the directory `inst/doc/devel_guide/` to house developer documentation.

3. **Relocation & Expansion of Genotypes Guide (`genoApp.md`)**:
   - Relocated and renamed `inst/doc/genoDataApp.md` to [inst/doc/devel_guide/genoApp.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/genoApp.md).
   - Expanded the document to provide detailed developer guides for `genoApp` (the container panel), `genoPlotApp` (genotype probability plotter), and `genoEffectApp` (phenotype association effect calculator), reusing the original `genoDataApp` documentation.

4. **Creation of the Master Guide (`README.md`)**:
   - Created [inst/doc/devel_guide/README.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/README.md) as the high-level entrypoint.
   - Documented:
     - **UI Layout & Navigation**: The Bootstrap 5 layout, reactive linking across tabs, and standardizing panel names.
     - **Data Routing & Downloader Integration**: How active tabs route plot/table outputs to the external `downr` downloader module.
     - **Tab Panels & Submodules**: Divided into Hotspots & Phenotypes, Scans, Patterns, Genotypes, and Mediation.
     - **Utility Classification**: Grouped global controls like `projectApp.R`, `setParApp.R`, `winParApp.R`, `dipParApp.R`, `snpListApp.R`, and data loaders like `probsApp.R` and `kinshipApp.R`.
     - **Complete File Index**: Indexed and linked every `R/*App.R` file to its corresponding module type (Entrypoint, Integral Submodule, Data Loader, Normalizer, Selector, DB Query, and Generic Utility).

5. **Creation of Detailed Guides for Remaining Panels**:
   - Created the detailed guides for remaining panels, each including a link back to the developer's guide main page ([README.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/README.md)):
     - [inst/doc/devel_guide/hotspotApp.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/hotspotApp.md) for the Hotspots & Phenotypes panel.
     - [inst/doc/devel_guide/scanApp.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/scanApp.md) for the Allele & SNP Scans panel.
     - [inst/doc/devel_guide/patternApp.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/patternApp.md) for the SDP Pattern Analysis panel.
     - [inst/doc/devel_guide/mediateApp.md](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/devel_guide/mediateApp.md) for the Mediation panel.

## Rationale for Module Categorization

To maintain a clean separation of concerns, the 41 files were categorized based on whether their lifecycle and data scope are self-contained within an analysis tab, or whether they serve coordinates and global states across multiple tabs:

- **Integral Panel Modules**: Highly specific to a particular mathematical analysis (e.g. mediation computations, SDP pattern scans, LOD genome curves). They consume global reactives but do not mutate state consumed by other panels.
- **Generic/Utility Modules**: Mutate global states (e.g., changing the chromosome or peak coordinate region via `winPar` / `snpList`) or load large disk-backed data objects (e.g., genotype probabilities via `probs` / `kinship`) that are consumed globally by all panels.
