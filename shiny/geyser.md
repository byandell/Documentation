---
title: "geyser"
parent: "Shiny Apps"
nav_order: 2
---

# geyser: modular concepts and construction

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
[hist.R](https://github.com/byandell/geyser/blob/main/R/hist.R) ⚠️,
[gghist.R](https://github.com/byandell/geyser/blob/main/R/gghist.R) ⚠️,
[ggpoint.R](https://github.com/byandell/geyser/blob/main/R/ggpoint.R) ⚠️
- data:
[data.R](https://github.com/byandell/geyser/blob/main/R/data.R) ⚠️,
[datasets.R](https://github.com/byandell/geyser/blob/main/R/datasets.R) ⚠️
- connections:
[rows.R](https://github.com/byandell/geyser/blob/main/R/rows.R) ⚠️,
[wrapper.R](https://github.com/byandell/geyser/blob/main/R/wrappeer.R) ⚠️,
[switch.R](https://github.com/byandell/geyser/blob/main/R/switch.R) ⚠️

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
[Geyser Demo](https://connect.doit.wisc.edu/geyserDemo) ⚠️)

For more information that puts these in context, see the
[Geyser Shiny Modules](https://connect.doit.wisc.edu/geyserShinyModules)
slide deck, as well as the
[11 Dec 2024 Presentation](https://drive.google.com/file/d/1BGSIhihpBc-2TfRza5RGeXBCB55EC6-l).
There are more aspects of this package, including exploration of modular apps
with Quarto and Python.
