---
title: "GitHub"
parent: "Document Digital Tools"
nav_order: 3
permalink: /github/
---

# GitHub

- [View GitHub Slides](https://byandell.github.io/Documentation/quarto/github.html)
- [General GitHub and Git Information](#general-github-and-git-information)
- [Collaborate with GitHub Organizations](#collaborate-with-github-organizations)
- [Connect with GitHub](#connect-with-github)
- [CodeSpaces within GitHub](#codespaces-within-github)
- [GitHub Pages](pages.md)

## General GitHub and Git Information

- [GitHub Links (UW-Madison-DataScience)](https://github.com/UW-Madison-DataScience/R_for_data_sciences/blob/master/organize/github.md)
- [Get started with GitHub (Happy Git with R)](https://happygitwithr.com/usage-intro#usage-intro)
- [Git and GitHub Troubleshooting](https://happygitwithr.com/troubleshooting)
- [Install Git for Windows (Git-SCM)](https://git-scm.com/install/windows)
- [Install Git (Git Guides)](https://github.com/git-guides/install-git)

## Collaborate with GitHub Organizations

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
