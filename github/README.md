---
title: "GitHub"
nav_order: 3
permalink: /github/
---

# GitHub

_[byandell.github.io/Documentation](https://byandell.github.io/Documentation)_  

- [View GitHub Slides](https://byandell.github.io/Documentation/quarto/github.html)
- [General GitHub and Git Information](#general-github-and-git-information)
- [GitHub Pages](#github-pages)
  - [My GitHub Pages](#my-github-pages)
    - [My Documentation GitHub Pages](#my-documentation-github-pages)
    - [QR Codes for Github Pages](#qr-codes-for-github-pages)
  - [GitHub Pages References](#github-pages-references)
  - [GitHub Pages with Shinylive](shinylive.md)
- [Collaborating with GitHub Organizations](#collaborating-with-github-organizations)
- [Connect with GitHub](#connect-with-github)
- [CodeSpaces within GitHub](#codespaces-within-github)

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
[GitHub Organization](#collaborating-with-github-organizations).

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
the `byandell-envsys`
[GitHub organization](#collaborating-with-github-organizations),
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

#### My Documentation GitHub Pages

I developed my
[Documentation GitHub Pages](https://byandell.github.io/Documentation)
to serve as a reference for the Digital Tools I use.
In the process, I learned how to use
[Just-the-Docs](https://just-the-docs.com/)
as the theme, which includes many useful navigation features.
It interprets `README.md` files in folders
as top-level pages, with the `README.md` in the top-most
folder displayed as the homepage.
One mistake I made was that putting YAML front matter
in a `README.md`
such as for navigation order (`nav_order`),
requires adding a `permalink`,
which forces Jekyll to use that page as the top-level `index` page.
The corrected front matter, say for the top
[README.md](https://github.com/byandell/Documentation/blob/main/README.md):

```
---
title: "Documentation for Digital Tools"
nav_order: 0
permalink: /
---
```

I also learned that using `title:` and `parent:`
was a useful way to create a navigation hierarchy.

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

## Collaborating with GitHub Organizations

A GitHub organization allows a team (or an individual like me)
to collaborate on related repositories.
The organization `owner`(s) manage `member`(s) and repositories (repos).
Each repo can be `public` or `private`, and members can have one of 5 `permission` levels
with increasing level of control/danger: read, triage, write, maintain or admin.
Organization and repo membership are managed, respectively,
with the `Settings` menu in the upper right-hand corner.

- [How to Create a GitHub Organization From Scratch (GeeksforGeeks)](https://www.geeksforgeeks.org/git/how-to-create-github-organization-from-scratch/)
- [What Are GitHub Organizations and Should You Use One? (How-To Geek)](https://www.howtogeek.com/devops/what-are-github-organizations-and-should-you-use-one/)
- [GitHub Organizations and Teams Documentation (GitHub)](https://docs.github.com/organizations)
- [Managing an organization (git-scm.com)](https://git-scm.com/book/en/v2/GitHub-Managing-an-organization.html)

I belong to a variety of
[GitHub Organizations](https://github.com/settings/organizations):

- My Organizations
  - [byandell-envsys](https://github.com/byandell-envsys)
  - [byandell-sysgen](https://github.com/byandell-sysgen)
- UW-Madison Organizations:
  - [UW-Madison Data Science Institut (DSI](https://github.com/UW-Madison-DSI)
  - [UW-Madison Data Science Hub](https://github.com/UW-Madison-DataScience)
- CU-Boulder Environmental Organizations:
  - [Environmental Data Science Innovation and Impact Lab (ESIIL)](https://github.com/cu-esiil)
  - [ESIIL Education](https://github.com/cu-esiil-edu)
  - [Earth Analytics Education Program (Earth Lab)](https://github.com/earthlab-education)
- Oglala Lakota College (OLC)
  - [OLC Geospatial Data Science Hub](https://github.com/olc-techsupport)

An optional special repo in an organization, `.github`, can be used to provide an organization-level README and default settings.
I use mine to provide a brief introduction to an organization and links to its resources.
For instance, see the
`.github/README.md`
file in my
[byandell-envsys](https://github.com/byandell-envsys)
and
[byandell-sysgen](https://github.com/byandell-sysgen)
repositories.
The
[`envsys` README.md](https://github.com/byandell-envsys/.github/blob/main/profile/README.md)
is very simple, providing a one-paragraph intro and links to resources.
In contrast, the
[`sysgen` README.md](https://github.com/byandell-sysgen/.github/blob/main/profile/README.md)
has dropdown sections to help
organize multiple repos.
This is done with old style HTML code:

```
<details>
<summary>QTL Repos</summary>
<br>
...
</details>
```

## Connect with GitHub

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

## CodeSpaces within GitHub

Always stop a codespace when done to save resources!

- [GitHub Codespaces overview](https://docs.github.com/en/codespaces/overview),
[QuickStart](https://docs.github.com/en/codespaces/getting-started/quickstart) &
[Documentation](https://docs.github.com/en/codespaces)
- [GitHub Codespaces (Visual Studio Code)](https://code.visualstudio.com/docs/remote/codespaces)
- [Stopping and starting a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#stopping-a-codespace)
