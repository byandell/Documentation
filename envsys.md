# Environmental Systems References

These references were gathered while learning about environmental systems and data analytics while attending the
[CU Boulder EarthLab](https://earthlab.colorado.edu/) course
on [Earth Data Analytics](https://github.com/byandell-envsys/EarthDataAnalytics).
To help me understand and organize code and ideas, I developed the
[landmapy](https://github.com/byandell-envsys/landmapy) package.
See also
[Python Strategy](python_strategy.md).

- [Earth Data Analytics](#earth-data-analytics)
- [GitHub Pages](#github-pages)
- [Codespaces](#codespaces)
- [Python Coding](#python-coding)
- [Open Street Map](#open-street-map)
- [Google Maps Platform Access](#google-maps-platform-access)

## Earth Data Analytics

- [Fundamentals of Earth Data Analytics (EDA)](https://cu-esiil-edu.github.io/esiil-learning-portal/foundations/pages/00-course-overviews/foundations/01-fundamentals/00-home.html)
  - [1. Get started with open reproducible science](https://cu-esiil-edu.github.io/esiil-learning-portal/foundations/pages/00-course-overviews/foundations/01-fundamentals/01-portfolio.html)
  - [2. Time-series Data](https://cu-esiil-edu.github.io/esiil-learning-portal/foundations/pages/00-course-overviews/foundations/01-fundamentals/02-time-series.html)
  - [3. Geospatial Vector Data](https://cu-esiil-edu.github.io/esiil-learning-portal/foundations/pages/00-course-overviews/foundations/01-fundamentals/03-vector.html)
  - [4. Final Project](https://cu-esiil-edu.github.io/esiil-learning-portal/foundations/pages/00-course-overviews/foundations/01-fundamentals/04-raster.html)
  - [5. Fundamentals of Earth Data Analytics](https://cu-esiil-edu.github.io/esiil-learning-portal/foundations/pages/00-course-overviews/foundations/01-fundamentals/05-final.html)
- [Introduction to Earth Data Science | Earth Lab CU Boulder](https://www.earthdatascience.org/courses/intro-to-earth-data-science/)
  - [Syllabus Wiki](https://github.com/earthlab-education/Earth-Analytics-AY24/wiki)
  - [Earth Data Analytics – Foundations Textbook](https://cu-esiil-edu.github.io/esiil-learning-portal/foundations/pages/00-course-overviews/foundations/00-home.html)
  - [Earth Data Science Textbooks](https://www.earthdatascience.org/)
- [Mapping Inequality](https://dsl.richmond.edu/panorama/redlining/)
- [Geospatial Resources](https://github.com/byandell/geospatial/blob/main/README.md#geospatial-resources)

## GitHub Pages

My main GitHub Page
[byandell.github.io](https://byandell.github.io),
with source at
<https://github.com/byandell/byandell.github.io>,
was modeled on (forked from)
<https://github.com/barryclark/jekyll-now>.
This has to cool feature of blog pages.

In addition to my main GitHub Page, I have a separately generated subpage
[byandell.github.io/ESIIL](https://byandell.github.io/ESIIL),
with source at
<https://github.com/byandell/ESIIL>,
that was forked from
<https://github.com/CU-ESIIL/Postdoc_OASIS>.

- [ESIIL Data Short Course: Create your own portfolio webpage](https://cu-esiil-edu.github.io/esiil-learning-portal/shortcourse/pages/03-git-github/03-github-portfolio/01-create-portfolio-website.html)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Publish Your Project Documentation with GitHub Pages](https://github.blog/developer-skills/github/publish-your-project-documentation-with-github-pages/)
- [GitHub Page Themes](https://pages.github.com/themes/)
- [Jekyll Now](https://github.com/barryclark/jekyll-now)
  - [Build A Blog With Jekyll And GitHub Pages](https://www.smashingmagazine.com/2014/08/build-blog-jekyll-github-pages/)
  - [Other forkable themes](https://github.com/barryclark/jekyll-now/#other-forkable-themes)
- [MkDocs](https://github.com/mkdocs/mkdocs/tree/master) (advanced topic)
  - [Materials for MkDocs: Publishing your site](https://squidfunk.github.io/mkdocs-material/publishing-your-site/)
  - [Deploying your docs](https://www.mkdocs.org/user-guide/deploying-your-docs/)

## CodeSpaces

Always stop a codespace when done to save resources!

- [GitHub Codespaces overview](https://docs.github.com/en/codespaces/overview),
[QuickStart](https://docs.github.com/en/codespaces/getting-started/quickstart) &
[Documentation](https://docs.github.com/en/codespaces)
- [GitHub Codespaces (Visual Studio Code)](https://code.visualstudio.com/docs/remote/codespaces)
- [Stopping and starting a codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace#stopping-a-codespace)
  
## Home Computer Visual Studio Code & GitBash

[Lesson 2. Setup Git, Bash, and Conda on Your Computer Setup earth analytics environment](https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-git-bash-conda/)

- [Visual Studio Code](https://code.visualstudio.com/download)
- [git](https://git-scm.com/downloads)
  - `git` is already installed if using it within `Rstudio`.
  - Install `git`, maybe `git-gui`.
  - Start `git-gui` from shell.
- [miniconda](https://docs.anaconda.com/miniconda/)
  - Install `bash`, not `pkg`.
  - [Miniconda3 macOS Apple M1 64-bit bash](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh)

Command line entries to install `miniconda` via bash:

```
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

### Set up SSH key in GitHub account

[Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

```
ssh-keygen -t ed25519 -C "byandell@wisc.edu"
```

Default storage is in
`~/.ssh/id_ed25519`.

Can use `pbcopy` to copy public key to clipboard for
subsequent paste to GitHub SSH key generation (2 ways).

```
cat ~/.ssh/id_ed25519.pub | pbcopy
pbcopy < ~/.ssh/id_ed25519.pub
```

## Python Coding

- [Pandas Library](https://pandas.pydata.org/docs/)
  - [Pandas Tutorial](https://pandas.pydata.org/docs/user_guide/10min.html)
  - [Pandas API Reference](https://pandas.pydata.org/docs/reference/)
- [EDA Scientific Data Structures in Python](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/)
  - [EDA 6.15. Intro to Pandas Dataframes](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/)

 <https://github.com/earthlab/earth-analytics-python-env>

## Open Street Map

[OpenStreetMap (OSM)](https://www.openstreetmap.org/).
Data can be accessed via `osmdata`.
Static maps are plotted using `ggplot2` with `sf` bridging via `geom_sf` for polygon and point layers.
OSM base map layer is added with `annotation_map_tile` from `ggspatial` package.
Interactive maps can be produces with package `tmap`.

OSM is a free resource with maps and features (but should be cited).
Most people seem to use Python to work with such maps, but there
are some tools in R.

- [OSM Wiki](https://wiki.openstreetmap.org/wiki/How_to_contribute)
- [Making Maps with R](https://bookdown.org/nicohahn/making_maps_with_r5/docs/introduction.html)
- [Quantitative Analysis with R by Brian Wood](https://bookdown.org/brianwood1/QDASS/)
- [Automating Map generation from Multi-polygon shapefiles using Python with GeoPandas and Matplotlib](https://medium.com/@sooryanarayan_5231/automating-map-generation-from-multi-polygon-shapefiles-using-python-with-geopandas-and-matplotlib-aad4c79f8d5e)

### osmdata package

- [osmdata Vignette](https://cran.r-project.org/web/packages/osmdata/vignettes/osmdata.html)
- [Mapping with Open Street Maps in R](https://jcoliver.github.io/learn-r/017-open-street-map.html)
- [Open Street Map data (RSpatialData)](https://rspatialdata.github.io/osm.html)

### ggspatial package

- [ggspatialto overlay OSM or other maps using R](https://paleolimbot.github.io/ggspatial/)
- [Spatial objects using ggspatial and ggplot2](https://paleolimbot.github.io/ggspatial/articles/ggspatial.html)

### tmap package

- [Quickstart Guide - Shapefiles and R(tmap)](https://www.kaggle.com/code/umeshnarayanappa/quickstart-guide-shapefiles-and-r-tmap)
- [tmap: thematic maps in R](https://r-tmap.github.io/tmap/)
- [tmap](https://cran.r-project.org/web/packages/tmap/vignettes/tmap-getstarted.html) interactive maps
- [tmap book](https://r-tmap.github.io/tmap-book/)
- [tmap: using make-valid for multipolygons](https://stackoverflow.com/questions/76455486/impossible-to-plot-osm-multipolygons-in-tmap-and-leaflet)

## Google Maps Platform Access

Google maps can be used via `ggmap` but require a Google Map Key, which requires CC and payment.

- <https://mapsplatform.google.com/>
  - [ggmap::register_google](https://rdrr.io/cran/ggmap/man/register_google.html)
  - [Get API Key](https://developers.google.com/maps/documentation/maps-static/get-api-key/)
  - [Securing an API Key](https://cloud.google.com/docs/authentication/api-keys#securing_an_api_key)
  - [usage and billing](https://developers.google.com/maps/documentation/maps-static/usage-and-billing/)
  - [UW Guidelines on Google Maps API Key](https://wiscweb.wisc.edu/2018/11/30/events-calendar-embedded-map-display-changes/)
