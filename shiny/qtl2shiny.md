---
title: "qtl2shiny"
parent: "Shiny Apps"
nav_order: 4
---

# qtl2shiny: localized QTL analysis and visualization

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
[qtl2shiny/R](https://github.com/byandell-sysgen/qtl2shiny/tree/main/R) ⚠️,
although they do not (yet) follow the conventional naming of
server and UI functions, and they do not have app functions.
Nevertheless, they have many features that are being considered in current development;
these could be usefully retooled for a modernized qtl2 shiny app.

The hierarchy of module calling is approximately shown in the following figure
(with some missing links) and file layout here:

![](../images/qtl2shiny.png)

- [Main](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyMain.R) ⚠️:
[Dash](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyDash.R) ⚠️,
  - [Dash](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyDash.R) ⚠️:
[Setup](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySetup.R) ⚠️,
[Haplo](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyHaplo.R) ⚠️,
[Diplo](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyDiplo.R) ⚠️
- [Setup](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySetup.R) ⚠️:
[Project](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyProject.R) ⚠️,
[Phenos](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPhenos.R) ⚠️,
[Peaks](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPeaks.R) ⚠️
  - [Phenos](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPhenos.R) ⚠️:
[PhenoPlot](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPhenoPlot.R) ⚠️
  - [Peaks](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPeaks.R) ⚠️:
[Hotspot](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyHotspot.R) ⚠️
- [Haplo](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyHaplo.R) ⚠️:
[Probs](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyProbs.R) ⚠️,
[SNPSetup](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPSetup.R) ⚠️,
[ScanCoef](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyScanCoef.R) ⚠️,
[Mediate](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyMediate.R) ⚠️
  - [Mediate](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyMediate.R) ⚠️:
[Triad](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyTriad.R) ⚠️
- [Diplo](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyDiplo.R) ⚠️:
[PairProbs](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPairProbs.R) ⚠️,
[SNPSetup](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPSetup.R) ⚠️,
[Pattern](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPattern.R) ⚠️
  - [SNPSetup](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPSetup.R) ⚠️:
[SNPProbs](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPProbs.R) ⚠️,
[SNPPattern](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPPattern.R) ⚠️,
[SNPGene](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPGene.R) ⚠️
    - [SNPPattern](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPPattern.R) ⚠️:
[SNPFeature](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPFeature.R) ⚠️
    - [SNPGene](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPGene.R) ⚠️:
[SNPSum](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPSum.R) ⚠️,
[SNPPlot](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinySNPPlot.R) ⚠️,
[GeneRegion](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyGeneRegion.R) ⚠️,
[GeneExon](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyGeneExon.R) ⚠️
  - [Pattern](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyPattern.R) ⚠️:
[Allele](https://github.com/byandell-sysgen/qtl2shiny/blob/master/R/shinyAllele.R) ⚠️

The above table is based on the `master` branch;
the `byandell-refactor` branch is modernizing this code.
Below are the branch links:

- [main](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/mainServer.R) ⚠️:
[dash](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/dashServer.R) ⚠️
  - [dash](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/dashServer.R) ⚠️:
[setup](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/setupServer.R) ⚠️,
[haplo](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/haploServer.R) ⚠️,
[diplo](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/diploServer.R) ⚠️
- [setup](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/setupServer.R) ⚠️:
[project](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/projectServer.R) ⚠️,
[pheno](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/phenoServer.R) ⚠️,
[peaks](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/peaksServer.R) ⚠️
  - [pheno](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/phenoServer.R) ⚠️:
[phenoPlot](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/phenoPlotServer.R) ⚠️
  - [peaks](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/peaksServer.R) ⚠️:
[hotspot](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/hotspotServer.R) ⚠️
- [haplo](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/haploServer.R) ⚠️:
[probs](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/probsServer.R) ⚠️,
[snpSetup](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpSetupServer.R) ⚠️,
[scanCoef](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/scanCoefServer.R) ⚠️,
[mediate](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/mediateServer.R) ⚠️
  - [mediate](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/mediateServer.R) ⚠️:
[triad](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/triadServer.R) ⚠️
- [diplo](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/diploServer.R) ⚠️:
[pairProbs](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/probsServer.R) ⚠️,
[snpSetup](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpSetupServer.R) ⚠️,
[pattern](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/patternServer.R) ⚠️
  - [snpSetup](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpSetupServer.R) ⚠️:
[snpProbs](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/probsServer.R) ⚠️,
[snpPattern](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpPatternServer.R) ⚠️,
[snpGene](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpGeneServer.R) ⚠️
    - [snpPattern](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpPatternServer.R) ⚠️:
[snpFeature](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpFeatureServer.R) ⚠️
    - [snpGene](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpGeneServer.R) ⚠️:
[snpSum](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpSumServer.R) ⚠️,
[snpPlot](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/snpPlotServer.R) ⚠️,
[geneRegion](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/geneRegionServer.R) ⚠️,
[geneExon](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/geneExonServer.R) ⚠️
  - [pattern](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/patternServer.R) ⚠️:
[allele](https://github.com/byandell-sysgen/qtl2shiny/blob/byandell-refactor/R/alleleServer.R) ⚠️

The `main` module calls `dash`, which then invokes `setup`
and the two primary modules,
`haplo` and `diplo`, for haplotype and diplotype analyses.
Each of those call multiple other modules.
The app has a side panel where switches among different types of analyses and plots are performed.
Some shiny technology is older--would be good to switch from
[shinydashboard to bslib](https://shiny.posit.co/blog/posts/bslib-dashboards/) ⚠️--and
more modularity is possible.
Download operations are currently duplicated in multiple modules,
but should be pulled out as was done for `foundShiny`,
ideally using that same
[download.R](https://github.com/AttieLab-Systems-Genetics/foundrShiny/blob/main/R/download.R) ⚠️
module.
See screenshots and guides:

- [Screen Shots](http://pages.stat.wisc.edu/~yandell/software/qtl2shiny/screenshots.html)
- [User Guide](https://github.com/byandell/qtl2shiny/blob/master/vignettes/UserGuide.Rmd) ⚠️
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
