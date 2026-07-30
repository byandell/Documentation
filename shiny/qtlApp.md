---
title: "qtlApp"
parent: "Shiny Apps"
nav_order: 1
---

# qtlApp: modular QTL visualization app

This is an ongoing project that is designed for QTL visualization and analysis at scale.
It is organized as a package with multiple small shiny modules, each with its own app.
The goal is to make this straightforward and easy enough for team members to develop
their own modules as the tools evolve.

The package has several analysis files used by shiny modules:

- [trait_scan.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/trait_scan.R)
- [QTL_plot_visualizer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/QTL_plot_visualizer.R)
- [peak_finder.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/peak_finder.R)

The shiny modules in hierarchy of calling are:

- [qtlServer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/qtlServer.R) ⚠️: QTL app
  - [mainParServer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/mainParServer.R) ⚠️: main parameters
    - [traitServer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/traitServer.R) ⚠️: break out display of `datasets` and return of `trait_list`
  - [scanServer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/scanServer.R) ⚠️: QTL scan read from file
  - [peakServer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/peakServer.R) ⚠️: QTL peaks read from file

The deployable app
[app.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/inst/shinyApp/app.R)
sources the file
[qtlSetup.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/inst/shinyApp/qtlSetup.R) ⚠️
to load data files and then calls the
[qtlServer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/qtlServer.R) ⚠️.

- [qtlSetup.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/inst/shinyApp/qtlSetup.R) ⚠️: file setup
- [app.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/inst/shinyApp/app.R): app that calls the modules
