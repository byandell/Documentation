# Shiny Apps

Shiny apps are cool, but they can get complicated, and frustrating to debug.
Complicated apps--longer than 500 lines of code--can
have subtle paradoxes caused by reactive elements.
It is helpful to think carefully about how to modularize apps,
much as we do with functions, so that we can debug piece by piece.

R language apps developed with collaborators by [Brian Yandell](https://github.com/byandell)
using the
[Shiny](https://shiny.posit.co/)
package
illustrate in various ways an evoling design over time,
which made the apps easier
to use, understand and debug.
These repos include some lessons learned that hopefully will
help others as they design and evolve apps for this project.
For those interested in comparing shiny apps built in R vs. python,
there is a useful development in the
[Shiny Geyser App](https://github.com/byandell/geyser)
repo.

The best reference for building shiny apps is
[Mastering Shiny](https://mastering-shiny.org),
with particular attention to Ch 19 on
[Shiny modules](https://mastering-shiny.org/scaling-modules.html).
See also
[Modularizing Shiny app code](https://shiny.rstudio.com/articles/modules.html).
Yandell's key working repos that inform this document are

- [Helper Apps](https://github.com/byandell/helperApps)
- [Shiny app for QTL visualization](https://github.com/AttieLab-Systems-Genetics/qtlApp)
- [Shiny Geyser App with and without Modules](https://github.com/byandell/geyser)
- [Founder Shiny App](https://github.com/AttieLab-Systems-Genetics/foundrShiny)
- [Shiny app for R/qtl2](https://github.com/byandell-sysgen/qtl2shiny)
- [Learning about Shiny Modules](https://github.com/byandell/shiny_module)

Below are discussions in reverse chronological order of these repos:

- [helperApps: modules for reuse in other Shiny Apps](https://github.com/byandell/helperApps/blob/main/README.md)
- [qtlApp: modular QTL visualization app](#qtlapp-modular-qtl-visualization-app)
- [geyser: modular concepts and construction](#geyser-modular-concepts-and-construction)
- [foundrShiny: pragmatic code reuse driven by collaborators](#foundrshiny-pragmatic-code-reuse-driven-by-collaborators)
- [qtl2shiny: localized QTL analysis and visualization](#qtl2shiny-localized-qtl-analysis-and-visualization)
- [shiny_module: learning about reactivity](#shiny_module-learning-about-reactivity)

Additional links on R in general can be found at
[R for Data Sciences](https://github.com/UW-Madison-DataScience/R_for_data_sciences).

<hr>

## qtlApp: modular QTL visualization app

This is an ongoing project that is designed for QTL visualization and analysis at scale.
It is organized as a package with multiple small shiny modules, each with its own app.
The goal is to make this straightforward and easy enough for team members to develop
their own modules as the tools evolve.

The package has several analysis files used by shiny modules:

- [trait_scan.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/trait_scan.R)
- [QTL_plot_visualizer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/QTL_plot_visualizer.R)
- [peak_finder.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/peak_finder.R)

The shiny modules in hierarchy of calling are:

- [qtlServer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/qtlServer.R): QTL app
  - [mainParServer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/mainParServer.R): main parameters
    - [traitServer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/traitServer.R): break out display of `datasets` and return of `trait_list`
  - [scanServer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/scanServer.R): QTL scan read from file
  - [peakServer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/peakServer.R): QTL peaks read from file

The deployable app
[app.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/inst/shinyApp/app.R)
sources the file
[qtlSetup.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/inst/shinyApp/qtlSetup.R)
to load data files and then calls the
[qtlServer.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/R/qtlServer.R).

- [qtlSetup.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/inst/shinyApp/qtlSetup.R): file setup
- [app.R](https://github.com/AttieLab-Systems-Genetics/qtlApp/blob/main/inst/shinyApp/app.R): app that calls the modules

## geyser: modular concepts and construction

The
[geyser](https://github.com/byandell/geyser)
repo studies a simple app
([Faithful](https://shiny.posit.co/r/gallery/start-simple/faithful))
to illustrate the components of a shiny app,
and how to develop more complicated apps using shiny modules.
It starts with
[building one shiny module](https://github.com/byandell/geyser/tree/main/inst/build_module)
around this classic example,
and then
[connects multiple modules](https://github.com/byandell/geyser/tree/main/inst/connect_modules)
that organize the logic (server) and app view (ui) in various ways.
About a half-dozen shiny modules in
[geyser/R](https://github.com/byandell/geyser/tree/main/R)
comprise the geyser R package, or library. These are of three types:

- plots:
[hist.R](https://github.com/byandell/geyser/blob/main/R/hist.R),
[gghist.R](https://github.com/byandell/geyser/blob/main/R/gghist.R),
[ggpoint.R](https://github.com/byandell/geyser/blob/main/R/ggpoint.R)
- data:
data.R, datasets.R
[data.R](https://github.com/byandell/geyser/blob/main/R/data.R),
[datasets.R](https://github.com/byandell/geyser/blob/main/R/datasets.R)
- connections:
rows.R, wrapper.R, switch.R
[rows.R](https://github.com/byandell/geyser/blob/main/R/rows.R),
[wrapper.R](https://github.com/byandell/geyser/blob/main/R/wrappeer.R),
[switch.R](https://github.com/byandell/geyser/blob/main/R/switch.R)

In addition, in the
[connects_modules](https://github.com/byandell/geyser/tree/main/inst/connect_modules)
folder, there are multiple apps that illustrate different concepts of connecting modules:

- modules over pages:
[appPages.R](https://github.com/byandell/geyser/blob/main/inst/connect_modules/appPages.R)
- modules in rows and columns:
[appRows.R](https://github.com/byandell/geyser/blob/main/inst/connect_modules/appRows.R),
[appRowsModule.R](https://github.com/byandell/geyser/blob/main/inst/connect_modules/appRowsModule.R)
- reuse of one module:
[appTwin.R](https://github.com/byandell/geyser/blob/main/inst/connect_modules/appTwin.R),
[appDupe.R](https://github.com/byandell/geyser/blob/main/inst/connect_modules/appDupe.R),
[appFlip.R](https://github.com/byandell/geyser/blob/main/inst/connect_modules/appFlip.R)
- modules within modules:
[app.R](https://github.com/byandell/geyser/blob/main/inst/connect_modules/app.R)
(see deployed
[Geyser Demo](https://connect.doit.wisc.edu/geyserDemo))

For more information that puts these in context, see the
[Geyser Shiny Modules](https://connect.doit.wisc.edu/geyserShinyModules)
slide deck, as well as the
[11 Dec 2024 Presentation](https://drive.google.com/file/d/1BGSIhihpBc-2TfRza5RGeXBCB55EC6-l).
There are more aspects of this package, including exploration of modular apps
with Quarto and Python.

## foundrShiny: pragmatic code reuse driven by collaborators

The
[foundrShiny](https://github.com/AttieLab-Systems-Genetics/foundrShiny)
repo is the basis of three tools actively used by the Attie Lab

- <https://connect.doit.wisc.edu/FounderCalciumStudy/>
- <https://connect.doit.wisc.edu/FounderDietStudy/> (requires password)
- <https://connect.doit.wisc.edu/FounderLiverDietStudy/> (requires password)

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
[download.R](https://github.com/AttieLab-Systems-Genetics/foundrShiny/blob/main/R/download.R)
module takes a list containing filename, plot, and table objects and
arranges downloads.
There are also ideas about creating and visualizing plots and tables that could prove useful.
Further, there was a lot of work on figuring out how to organize input parameters
across shiny modules to share inputs without duplication of code.

- app infrastructure:
[about.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/about.R),
[foundr.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/foundr.R),
[entry.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/entry.R),
[download.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/download.R)
- plots:
[biplot.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/biplot.R),
[dotplot.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/dotplot.R),
[volcano.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/volcano.R)
- parameters:
[mainPar.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/mainPar.R),
[panelPar.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/panelPar.R),
[plotPar.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/plotPar.R)
- panels:
see
[panel.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/panel.R)
or
[foundr.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/foundr.R)
  - trait panel:
[trait.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/trait.R),
[traitNames.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/traitNames.R),
[traitOrder.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/traitOrder.R),
[traitPairs.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/traitPairs.R),
[traitSolos.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/traitSolos.R),
[traitTable.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/traitTable.R),
[corPlot.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/corPlot.R),
[corTable.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/corTable.R)
  - stats panel:
[stats.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/stats.R)
  - time panel:
[time.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/time.R),
[timePlot.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/timePlot.R),
[timeTable.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/timeTable.R),
[timeTraits.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/timeTraits.R)
  - contrast panel:
[contrast.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/contrast.R),
[contrastGroup.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/contrastGroup.R),
[contrastPlot.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/contrastPlot.R),
[contrastTable.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/contrastTable.R),
[contrastTime.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/contrastTime.R),
[contrastTrait.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/contrastTrait.R)
- non-app helpers:
[foundrSetup.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/foundrSetup.R),
[foundr_helpers.R](https://github.com/byandell-sysgen/foundrShiny/blob/main/R/foundr_helper.R)

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

## qtl2shiny: localized QTL analysis and visualization

The
[qtl2shiny](https://github.com/byandell-sysgen/qtl2shiny)
app was designed to investigate local QTL, within a small (1-4Mb) region of a peak.
It performs allele-based LOD scans, SNP-based association mapping,
[SNP distribution pattern](https://smcclatchy.github.io/mapping/12-snp-assoc/)
analysis,
and mediation.
This work was never published in a peer-reviewed journal, only as a set of packages
in CRAN and GitHub.
It is in the process of major redesign, which is documented in
[Shiny Module Organization](https://github.com/byandell-sysgen/qtl2shiny/blob/master/inst/doc/module.md).

The
[qtl2shiny](https://github.com/byandell-sysgen/qtl2shiny)
repo was designed about a decade ago.
It is currently working on a laptop with data organized in a particular fashion.
However, one can view screenshots and the User's Guide.
This repo has ~25 shiny modules in
[qtl2shiny/R](https://github.com/byandell-sysgen/qtl2shiny/tree/main/R),
although they do not (yet) follow the conventional naming of
server and UI functions, and they do not have app functions.
Nevertheless, they have many features that are being considered in current development;
these could be usefully retooled for a modernized qtl2 shiny app.

The hierarchy of module calling is approximately shown in the following figure
(with some missing links) and file layout here:

![](images/qtl2shiny.png)

- [Main](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyMain.R):
[Dash](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyDash.R),
  - [Dash](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyDash.R):
[Setup](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySetup.R),
[Haplo](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyHaplo.R),
[Diplo](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyDiplo.R)
- [Setup](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySetup.R):
[Project](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyProject.R),
[Phenos](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPhenos.R),
[Peaks](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPeaks.R)
  - [Phenos](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPhenos.R):
[PhenoPlot](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPhenoPlot.R)
  - [Peaks](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPeaks.R):
[Hotspot](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyHotspot.R)
- [Haplo](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyHaplo.R):
[Probs](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyProbs.R),
[SNPSetup](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPSetup.R),
[ScanCoef](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyScanCoef.R),
[Mediate](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyMediate.R)
  - [Mediate](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyMediate.R):
[Triad](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyTriad.R)
- [Diplo](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyDiplo.R):
[PairProbs](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPairProbs.R),
[SNPSetup](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPSetup.R),
[Pattern](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPattern.R)
  - [SNPSetup](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPSetup.R):
[SNPProbs](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPProbs.R),
[SNPPattern](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPPattern.R),
[SNPGene](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPGene.R)
    - [SNPPattern](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPPattern.R):
[SNPFeature](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPFeature.R)
    - [SNPGene](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPGene.R):
[SNPSum](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPSum.R),
[SNPPlot](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPPlot.R),
[GeneRegion](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyGeneRegion.R),
[GeneExon](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyGeneExon.R)
  - [Pattern](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPattern.R):
[Allele](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyAllele.R)

The above table is based on the `master` branch;
the `byandell-refactor` branch is modernizing this code.
Below are the branch links:

- [main](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/mainServer.R):
[dash](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/dashServer.R)
  - [dash](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/dashServer.R):
[setup](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/setupServer.R),
[haplo](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/haploServer.R),
[diplo](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/diploServer.R)
- [setup](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/setupServer.R):
[project](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/projectServer.R),
[pheno](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/phenoServer.R),
[peaks](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/peaksServer.R)
  - [pheno](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/phenoServer.R):
[phenoPlot](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/phenoPlotServer.R)
  - [peaks](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/peaksServer.R):
[hotspot](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/hotspotServer.R)
- [haplo](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/haploServer.R):
[probs](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/probsServer.R),
[snpSetup](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpSetupServer.R),
[scanCoef](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/scanCoefServer.R),
[mediate](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/mediateServer.R)
  - [mediate](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/mediateServer.R):
[triad](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/triadServer.R)
- [diplo](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/diploServer.R):
[pairProbs](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/probsServer.R),
[snpSetup](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpSetupServer.R),
[pattern](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/patternServer.R)
  - [snpSetup](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpSetupServer.R):
[snpProbs](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/probsServer.R),
[snpPattern](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpPatternServer.R),
[snpGene](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpGeneServer.R)
    - [snpPattern](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpPatternServer.R):
[snpFeature](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpFeatureServer.R)
    - [snpGene](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpGeneServer.R):
[snpSum](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpSumServer.R),
[snpPlot](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpPlotServer.R),
[geneRegion](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/geneRegionServer.R),
[geneExon](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/geneExonServer.R)
  - [pattern](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/patternServer.R):
[allele](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/alleleServer.R)

The `main` module calls `dash`, which then invokes `setup`
and the two primary modules,
`haplo` and `diplo`, for haplotype and diplotype analyses.
Each of those call multiple other modules.
The app has a side panel where switches among different types of analyses and plots are performed.
Some shiny technology is older--would be good to switch from
[shinydashboard to bslib](https://shiny.posit.co/blog/posts/bslib-dashboards/)--and
more modularity is possible.
Download operations are currently duplicated in multiple modules,
but should be pulled out as was done for `foundShiny`,
ideally using that same
[download.R](https://github.com/AttieLab-Systems-Genetics/foundrShiny/blob/main/R/download.R)
module.
See screenshots and guides:

- [Screen Shots](http://pages.stat.wisc.edu/~yandell/software/qtl2shiny/screenshots.html)
- [User Guide](https://github.com/byandell/qtl2shiny/blob/master/vignettes/UserGuide.Rmd)
- [Developer Guide](https://github.com/byandell/qtl2shiny/blob/master/vignettes/DeveloperGuide.Rmd)
- [Data Preparation](https://github.com/byandell/qtl2shiny/blob/master/vignettes/qtl2shinyData.Rmd)

Finally, `qtl2shiny` depends on several other R packages
(some in CRAN, all in GitHub):

- [qtl2](https://cran.r-project.org/package=qtl2)
- [qtl2ggplot2](https://cran.r-project.org/package=qtl2ggplot)
- [qtl2fst](https://cran.r-project.org/package=qtl2fst)
- [qtl2pattern](https://cran.r-project.org/package=qtl2pattern)
- [qtl2mediate](https://github.com/byandell/qtl2mediate)
- [intermediate](https://github.com/byandell/intermediate)

## shiny_module: learning about reactivity

Finally, the
[shiny_module](https://github.com/byandell/shiny_module)
repo has some early learnings about reactivity.
It is perhaps useful as a reference when trying to figure out
why reactive code is not working.
However, it is rather dated at this point.
