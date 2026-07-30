---
title: "foundrShiny"
parent: "Shiny Apps"
nav_order: 3
---

# foundrShiny: pragmatic code reuse driven by collaborators

The
[foundrShiny](https://github.com/AttieLab-Systems-Genetics/foundrShiny)
repo is the basis of three tools actively used by the Attie Lab

- <https://connect.doit.wisc.edu/FounderCalciumStudy/> ⚠️
- <https://connect.doit.wisc.edu/FounderDietStudy/> ⚠️ (requires password)
- <https://connect.doit.wisc.edu/FounderLiverDietStudy/> ⚠️ (requires password)

This is an R package, which depends on another R package,
[foundr](https://github.com/AttieLab-Systems-Genetics/foundr),
that has the data analysis details.

Each code file in the
[founderShiny/R](https://github.com/AttieLab-Systems-Genetics/foundrShiny/tree/main/R)
folder itself is a shiny module with a
server function, UI functions, and an app function.
These ~30 shiny modules are interconnected in various ways as described in the
[Foundr App Developer Guide](https://docs.google.com/presentation/d/171HEopFlSTtf_AbrA28YIAJxJHvkzihB4_lcV6Ct-eI)
in order to build the tools cited above.
This was not the first, or even the second, iteration to build these tools.
It took about 1.5 years to develop this system, driven and guided by interactions
with Attie Lab members about use, function, and layout.

Some of those modules could be used (almost) directly for creating new shiny modules.
For instance, the
[download.R](https://github.com/AttieLab-Systems-Genetics/foundrShiny/blob/main/R/download.R) ⚠️
module takes a list containing filename, plot, and table objects and
arranges downloads.
There are also ideas about creating and visualizing plots and tables that could prove useful.
Further, there was a lot of work on figuring out how to organize input parameters
across shiny modules to share inputs without duplication of code.

- app infrastructure:
[about.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/about.R) ⚠️,
[foundr.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/foundr.R) ⚠️,
[entry.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/entry.R) ⚠️,
[download.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/download.R) ⚠️
- plots:
[biplot.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/biplot.R) ⚠️,
[dotplot.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/dotplot.R) ⚠️,
[volcano.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/volcano.R) ⚠️
- parameters:
[mainPar.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/mainPar.R) ⚠️,
[panelPar.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/panelPar.R) ⚠️,
[plotPar.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/plotPar.R) ⚠️
- panels:
see
[panel.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/panel.R) ⚠️
or
[foundr.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/foundr.R) ⚠️
  - trait panel:
[trait.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/trait.R) ⚠️,
[traitNames.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/traitNames.R) ⚠️,
[traitOrder.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/traitOrder.R) ⚠️,
[traitPairs.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/traitPairs.R) ⚠️,
[traitSolos.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/traitSolos.R) ⚠️,
[traitTable.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/traitTable.R) ⚠️,
[corPlot.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/corPlot.R) ⚠️,
[corTable.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/corTable.R) ⚠️
  - stats panel:
[stats.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/stats.R) ⚠️
  - time panel:
[time.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/time.R) ⚠️,
[timePlot.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/timePlot.R) ⚠️,
[timeTable.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/timeTable.R) ⚠️,
[timeTraits.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/timeTraits.R) ⚠️
  - contrast panel:
[contrast.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/contrast.R) ⚠️,
[contrastGroup.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/contrastGroup.R) ⚠️,
[contrastPlot.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/contrastPlot.R) ⚠️,
[contrastTable.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/contrastTable.R) ⚠️,
[contrastTime.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/contrastTime.R) ⚠️,
[contrastTrait.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/contrastTrait.R) ⚠️
- non-app helpers:
[foundrSetup.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/foundrSetup.R),
[foundr_helpers.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/foundr_helper.R) ⚠️

The `foundr` module draws together the other modules into the app to be deployed
through the panel modules `contrast`, `stats`, `time`, `trait`.
The `panel` module is just used for testing the panels, but is not part of the `foundr` app;
it could be modified to pull out the panel infrastructure from `foundr`.
Several of these modules are reused.
For instance,
`contrastPlot` is used in `contrastTrait` and `stats`,
`timePlot` is used in `time` and `contrast`,
`traitOrder` is used in `trait` and `time`,
and the parameter modules (`mainPar`, `panelPar`, `plotPar`) are used repeatedly.
The `traitNames` and `contrastTable` modules are used multiple times in the
`trait` and `contrast` panel modules, respectively.
The app function of each module might use other modules (notably parameter and download modules)
to test that module.
Here is the hierarchy of what modules are used directly by other modules:

- foundr: mainPar, about, download, entry, contrast, stats, time, trait
  - panel: mainPar, contrast, stats, time, trait
- contrast: panelPar, contrastGroup, contrastTime, contrastTable(3), contrastTrait, timePlot
  - contrastGroup: contrastPlot
  - contrastTable: traitOrder
  - contrastTime: timeTraits
  - contrastTrait: contrastPlot
  - contrastPlot: plotPar, biplot, dotplot, volcano
    - biplot: mainPar, panelPar, plotPar, contrastTable
- stats: panelPar, contrastPlot
- time: panelPar, timePlot, timeTable
  - timeTable: timeTraits, traitOrder
- trait: panelPar, corPlot, corTable, traitNames(2), traitOrder, traitPairs, traitSolos, traitTable

The parameter modules scope inputs at different levels of the app.
For instance, `mainPar` parameters (`dataset`, `order`, `height`) are common across many modules,
while `panelPar` parameters (`strains`, `sex`, `facet`) are localized by panel;
`plotPar` parameters are specific to plot modules.
This took some careful thinking about how information is passed among modules.

Note that for this app, input data are _not_ treated as global, but rather passed
to the `foundr` module and on to each panel.
Typically, static input data are subset to create reactive objects that are much smaller
(focused on a particular dataset and one or a few traits) based on user input.

Having this many modules was initially confusing, but they enable a developer
to concentrate app improvement on isolated parts of the app, using each module's app
function to do unit testing.

Another important aspect of this project was separating out analysis and visualization
code from the reactive (shiny) code into a separate package.
In fact, this app started with the
[foundr](https://github.com/AttieLab-Systems-Genetics/foundr)
repo, with shiny code mixed in.
The
[foundr v1.4 branch](https://github.com/byandell-sysgen/foundr/tree/v1.4)
contains the earlier version from Summer 2024,
where shiny, analysis and viz code are mixed together.
The current main branch is complicated enough without shiny code,
having ggplot2-based viz code and analytical computations.
In addition, it has utility routines;
helper routines used by `foundrShiny` modules but not needed for
`foundr` routines remain in
[foundrShiny/R/foundr_helpers.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/foundr_helpers.R)
as mentioned earlier.
Additional helpers from
[foundr](https://github.com/AttieLab-Systems-Genetics/foundr)
are organized by function

- ploting
  - ggplot_bestcor,
ggplot_conditionContrasts,
ggplot_traitPairs,
ggplot_traitSolos
ggplot_traitTimes
- utilities
  - CCcolors,
is_bestcor,
keptDatatraits,
subset_trait_names,
timetraits,
timetraitsall,
unite_datatraits
- analysis
  - bestcor,
conditionContrasts,
eigen_contrast,
eigen_traits,
traitPairs,
traitSolos,
traitTimes
- summary
  - summary_bestcor,
summary_conditionContrasts,
summary_strainstats
