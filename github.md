# GitHub, Connect, and CodeSpaces

_[byandell.github.io/Documentation](https://byandell.github.io/Documentation)_  

- [GitHub, Connect, and CodeSpaces (Quarto Slideshow)](https://byandell.github.io/Documentation/quarto/github.html)
- [My GitHub Pages](#my-github-pages)
- [General GitHub and Git Information](#general-github-and-git-information)
- [GitHub Pages](#github-pages)
- [Shinylive](#shinylive)
- [Connect](#connect)
- [CodeSpaces](#codespaces)

## My GitHub Pages

My main GitHub Page
[byandell.github.io](https://byandell.github.io),
with source at
<https://github.com/byandell/byandell.github.io>,
was modeled on (forked from)
<https://github.com/barryclark/jekyll-now>.
This has cool features like blog pages.

In addition to my main GitHub Page, I have a subpages
that are built separately in different GitHub repos:

- [byandell.github.io/Documentation](https://byandell.github.io/Documentation):
Documentation of Digital Tools (whole repo)
- [byandell.github.io/geyser](https://byandell.github.io/geyser/):
Geyser Shiny App with Modules (`docs/` folder)  
- [byandell-envsys.github.io/landmapyr](https://byandell-envsys.github.io/landmapyr/):
Land Mapping Package (`docs/` folder)
- [byandell.github.io/esiil-stars](https://byandell.github.io/esiil-stars):
ESIIL Stars Training Notes (whole repo)
- [byandell.github.io/ESIIL](https://byandell.github.io/ESIIL),
([GitHub](https://github.com/byandell/ESIIL)):
ESIIL Research (`docs/` folder using
[MkDocs](https://www.mkdocs.org/))

## General GitHub and Git Information

- [GitHub Links (UW-Madison-DataScience)](https://github.com/UW-Madison-DataScience/R_for_data_sciences/blob/master/organize/github.md)
- [Get started with GitHub (Happy Git with R)](https://happygitwithr.com/usage-intro#usage-intro)
- [Git and GitHub Troubleshooting](https://happygitwithr.com/troubleshooting)
- [Install Git for Windows (Git-SCM)](https://git-scm.com/install/windows)
- [Install Git (Git Guides)](https://github.com/git-guides/install-git)

## GitHub Pages

- [ESIIL Data Short Course: Create your own portfolio webpage](https://cu-esiil-edu.github.io/esiil-learning-portal/shortcourse/pages/03-git-github/03-github-portfolio/01-create-portfolio-website.html)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Publish Your Project Documentation with GitHub Pages](https://github.blog/developer-skills/github/publish-your-project-documentation-with-github-pages/)
- [GitHub Page Themes](https://pages.github.com/themes/)
- [Jekyll Now](https://github.com/barryclark/jekyll-now)
  - [Build A Blog With Jekyll And GitHub Pages](https://www.smashingmagazine.com/2014/08/build-blog-jekyll-github-pages/)
  - [Other forkable themes](https://github.com/barryclark/jekyll-now/#other-forkable-themes)
- [GitHub Actions](https://docs.github.com/en/actions)
- [MkDocs](https://github.com/mkdocs/mkdocs/tree/master) (advanced topic)
  - [Materials for MkDocs: Publishing your site](https://squidfunk.github.io/mkdocs-material/publishing-your-site/)
  - [Deploying your docs](https://www.mkdocs.org/user-guide/deploying-your-docs/)
- [Resolving Git Push for CI/CD Workflows (TutorialPedia)](https://www.tutorialpedia.org/blog/how-to-resolve-refusing-to-allow-an-oauth-app-to-create-or-update-workflow-on-git-push/)

## Shinylive

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
- [Using Shinylive to host Shiny app on GitHub Pages (HBC Training)](https://hbctraining.github.io/Training-modules/RShiny/lessons/shinylive.html).

## Connect

Posit's Connect is a platform for sharing resources such as R shiny apps, Quarto documents,
and python apps.

- [Posit Connect](https://posit.co/products/enterprise/connect/)

Deployment of apps using GitHub repos to a Connect server can be tricky, as Connect relies on the
`renv` package to create reproducible environments for your R projects.
A message like
**Deployment error: unknown package source**
indicates that the `renv` package does not recognize where a package was installed,
for instance if one uses `devtools::install_github()`.
`renv` cannot track the source well enough to reproduce it, and it refuses to bundle the app as a result.
The fix is to reinstall the package using `renv::install()` instead, which records the GitHub source in a way that `renv` can reproduce:

```r
renv::install("github_user/package_name")
renv::snapshot()
```

After running those two lines, retry the deployment. The snapshot validator should pass and the bundle should reach the server cleanly.
If for any reason that does not work, you can also try explicitly recording the source before deploying:

```r
renv::record("github_user/package_name")
```

- [renv](https://rstudio.github.io/renv/)
- [Manage dependencies with renv](https://www.r-bloggers.com/2021/03/new-on-techguides-manage-dependencies-with-renv/)
- [Using renv with Posit Connect](https://pkgs.rstudio.com/renv/articles/rsconnect.html)
- [R Package Management](https://docs.posit.co/connect/admin/r/package-management/)

## CodeSpaces

Always stop a codespace when done to save resources!

- [GitHub Codespaces overview](https://docs.github.com/en/codespaces/overview),
[QuickStart](https://docs.github.com/en/codespaces/getting-started/quickstart) &
[Documentation](https://docs.github.com/en/codespaces)
- [GitHub Codespaces (Visual Studio Code)](https://code.visualstudio.com/docs/remote/codespaces)
- [Stopping and starting a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#stopping-a-codespace)
