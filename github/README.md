# GitHub, Connect, and CodeSpaces

_[byandell.github.io/Documentation](https://byandell.github.io/Documentation)_  

- [GitHub, Connect, and CodeSpaces (Quarto Slideshow)](https://byandell.github.io/Documentation/quarto/github.html)
- [General GitHub and Git Information](#general-github-and-git-information)
- [GitHub Pages](#github-pages)
  - [My GitHub Pages](#my-github-pages)
  - [GitHub Pages References](#github-pages-references)
  - [GitHub Pages with Shinylive](#github-pages-with-shinylive)
- [Connect](#connect)
- [CodeSpaces](#codespaces)

## General GitHub and Git Information

- [GitHub Links (UW-Madison-DataScience)](https://github.com/UW-Madison-DataScience/R_for_data_sciences/blob/master/organize/github.md)
- [Get started with GitHub (Happy Git with R)](https://happygitwithr.com/usage-intro#usage-intro)
- [Git and GitHub Troubleshooting](https://happygitwithr.com/troubleshooting)
- [Install Git for Windows (Git-SCM)](https://git-scm.com/install/windows)
- [Install Git (Git Guides)](https://github.com/git-guides/install-git)

## GitHub Pages

Publishing web-based materials is easy with
[GitHub Pages](https://docs.github.com/en/pages),
a free service for hosting static websites
useful for project documentation and personal portfolios.
The personal portfolio is typically built using a repo
with the name `[username].github.io`.
Subpages are built using `[username].github.io/[reponame]`
where `[reponame]` can is the name of a repo owned by
`[username]`.
The `[username]` can also be a
[GitHub Organization](https://docs.github.com/en/organizations).

The resources below cover the basics of GitHub Pages
and provide links to my published pages and
more detailed guides and tutorials.

### My GitHub Pages

My main GitHub Page
[byandell.github.io](https://byandell.github.io),
with source at
<https://github.com/byandell/byandell.github.io>,
was modeled on (forked from)
<https://github.com/barryclark/jekyll-now>.
This has cool features like blog pages.

In addition to my main GitHub Page, I have several subpages
that are built separately in different GitHub repos.
Note that the `landmapyr` page is built within
the `byandell-envsys` GitHub organization,
which I created to organize my environment systems research projects.

- [byandell.github.io/Documentation](https://byandell.github.io/Documentation)
([source](https://github.com/byandell/Documentation)):
Documentation of Digital Tools (whole repo)
- [byandell.github.io/geyser](https://byandell.github.io/geyser/)
([source](https://github.com/byandell/geyser)):
Geyser Shiny App with Modules (`docs/` folder)
- [byandell-envsys.github.io/landmapyr](https://byandell-envsys.github.io/landmapyr/)
([source](https://github.com/byandell-envsys/landmapyr)):
Land Mapping Package (`docs/` folder)
- [byandell.github.io/esiil-stars](https://byandell.github.io/esiil-stars)
([source](https://github.com/byandell/esiil-stars)):
ESIIL Stars Training Notes (whole repo)
- [byandell.github.io/ESIIL](https://byandell.github.io/ESIIL)
([source](https://github.com/byandell/ESIIL)):
ESIIL Research (`docs/` folder using
[MkDocs](https://www.mkdocs.org/))

#### QR Codes for Github Pages

I generated a
[QR Code](https://github.com/byandell/byandell.github.io/blob/master/images/adobe-express-qr-code.png)
that points to my profile page
<https://byandell.github.io>
using
[Adobe Express](https://www.adobe.com/express/feature/image/qr-code-generator).

![](../images/adobe-express-qr-code.png)

**Warning:**
Be careful generating QR codes. Do you really need more than one?
I only have one, and make sure that relevant links to my material
are easily findable from my profile page.

You cannot add an image directly to your wallet, but you can use third party
apps to create a pass that is added to your wallet.
I used
[Pass4Wallet](https://apps.apple.com/us/app/pass4wallet-store-cards/id1423106610). 
other choices include

- [Add a QR code to Apple Wallet (QRCG)](https://www.qr-code-generator.com/blog/add-qr-code-to-apple-wallet/)
- [How to add a QR code to Apple Wallet (qrcodedynamic)](https://qrcodedynamic.com/blog/how-to-add-a-qr-code-to-apple-wallet/)

### GitHub Pages References

- [ESIIL Data Short Course: Create your own portfolio webpage](https://cu-esiil-edu.github.io/esiil-learning-portal/shortcourse/pages/03-git-github/03-github-portfolio/01-create-portfolio-website.html)
- [The Least You Need to Know About GitHub Pages](https://tomcam.github.io/least-github-pages/set-github-pages-master-branch.html)
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

### GitHub Pages with Shinylive

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

- [Prepare R app for Shinylive Export](shinylive.md)
- [Quarto Dashboard with Shinylive](quartolive.md)
- [Deploy Shinylive apps to GitHub Pages](deploy.md)

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
