---
title: "Curate R Data"
parent: "R Language"
author: "Brian S. Yandell"
date: "6/29/2017"
nav_order: 2
permalink: /R/curate/
---

# Curate R Data

This and other lessons assume users already have some experience with R, for instance through a [Data Carpentry](http://kbroman.org/datacarpentry_R_2017-01-10/) workshop. See [References](reference.md) for useful introductory and advanced material.

> ## Learning Objectives
>
> After completing this section, an individual will be able to curate data in `R`.
>
> * read, manipulate and display data summaries in concise tables
> * work with data frames using [tidyverse](http://tidyverse.org/) tools
> * use character string operations to clean data
> * create functions to collapse repeated steps into one-line "verbs"
> * save cleaned up data tables in external files

------------

## Read, Manipulate and Display Data

* [Working with data tables in R](curate/data_tables.Rmd)
* [Examples using `for` and `apply`](curate/applyExample.Rmd)

## Work with Data Frames using Tidyverse tools

* [sub_lesson recasting data.frame examples](curate/intro_dplyr.Rmd)
* [Tidyverse split-apply-combine example](curate/tidyverse.Rmd)
* [purrr example using `map` & `transpose`](curate/purrr.Rmd)
* [more tidyverse on `portal_mammals` data](curate/species.Rmd)

## Character String Operations to Clean Cata

* [characters and strings](curate/string.Rmd)
* [regular expressions (regex)](curate/regex.Rmd)

## Create Functions to Collapse Steps

[examples of functions](curate/function.Rmd)

## Save Cleaned up Data to External Files

[read and write files](curate/file.Rmd)

---

## Condensed Format

**Learning Objectives:** After completing this material, an individual will be able to
curate data in `R`.

* read, manipulate and display data summaries in concise tables
* work with data frames using [tidyverse](http://tidyverse.org/) tools
* write cleaned up data table out in CSV format

file | contents
---- | --------
[data_tables](data_tables.Rmd) | Working with data tables in R
[applyExample](applyExample.Rmd) | Examples using `for` and `apply`
[intro_dplyr](intro_dplyr.Rmd) | sub_lesson recasting data.frame examples
[tidyverse](tidyverse.Rmd) | Tidyverse split-apply-combine example
[purrr](purrr.Rmd) | another example using `map` & `transpose`
[species](species.Rmd) | `dplyr`, `tidyr` and `purrr` ideas with `portal_mammals` data
[string](string.Rmd) | characters and strings
[regex](regex.Rmd) | regular expressions
[file](file.Rmd) | read and write files
