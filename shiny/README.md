---
title: "Shiny Apps"
parent: "Document Digital Tools"
nav_order: 5
permalink: /shiny/
---

# Shiny Apps

Shiny apps are cool, but they can get complicated, and frustrating to debug.
Complicated apps--longer than 500 lines of code--can
have subtle paradoxes caused by reactive elements.
It is helpful to think carefully about how to modularize apps,
much as we do with functions, so that we can debug piece by piece.

- [View Shiny Apps Slides](https://byandell.github.io/Documentation/quarto/ShinyApps.html)

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
<!-- - [qtlApp: modular QTL visualization app](qtlApp.md) -->
- [geyser: modular concepts and construction](geyser.md)
- [foundrShiny: pragmatic code reuse driven by collaborators](foundrShiny.md)
- [qtl2shiny: localized QTL analysis and visualization](qtl2shiny.md)
- [shiny_module: learning about reactivity](shiny_module.md)

Additional links on R in general can be found at
[R for Data Sciences](https://github.com/UW-Madison-DataScience/R_for_data_sciences).

_[byandell.github.io/Documentation](https://byandell.github.io/Documentation)_
