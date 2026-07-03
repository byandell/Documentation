---
title: "Automate with GitHub Actions"
parent: "Publish GitHub Pages"
nav_order: 2
---

# Automate with GitHub Actions

This at present illustrates a way to
[Publish Apps with Shinylive](#publish-apps-with-shinylive).
While this may be of limited utility at this time,
it does illustrate how one might use
[GitHub Actions](https://github.com/features/actions)
to automate a workflow.
More to come.

- [Publish Apps with Shinylive](#publish-apps-with-shinylive)
  - [Prepare Shinylive Apps](shinylive.md)
  - [Publish Quarto Dashboard](quartolive.md)
  - [Deploy Shinylive Apps](deploy.md)

## Publish Apps with Shinylive

It is possible to host a client-side (browser run)
Shiny app provided it is fairly simple.
The tool to do this is
[Shinylive](https://shiny.posit.co/py/get-started/shinylive.html),
which was probably originally developed for `Python`
and is now available for `R` as
[r-shinylive](https://posit-dev.github.io/r-shinylive/).
It has some challenges as all material must
be self-contained in the app, including data.

- [Python Shinylive: Shiny + WebAssembly (Posit)](https://shiny.posit.co/py/get-started/shinylive.html)
- [r-shinylive](https://posit-dev.github.io/r-shinylive/)
- [py-shinylive](https://github.com/posit-dev/py-shinylive)
- [Using Shinylive to host Shiny app on GitHub Pages (HBC Training)](https://hbctraining.github.io/Training-modules/RShiny/lessons/shinylive.html)
- [Prepare R app for Shinylive Export](shinylive.md)
- [Quarto Dashboard Shinylive](quartolive.md)

See AI prompts used for creating shinylive apps:

- [Prepare Shinylive Apps](shinylive.md)
- [Publish Quarto Dashboard](quartolive.md)
- [Deploy Shinylive Apps](deploy.md)
