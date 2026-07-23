---
title: "Significance and Importance"
parent: "Data Sciences"
nav_order: 1
---

# Significance and Importance

The challenge of looking at many things is that patterns emerge
even when there are no actual relationships.
The observed effect, picked out of a vast array of things examined,
may be just a chance event.

When examining natural processes, such as building overlays of
geospatial maps, we want to find relationships.
However, it is tricky to do this in a way that is rigorous
and defensible.

Plots of data relationships are helpful, even crucial,
to understanding complicated data.
Environmental data scientists are facile at developing maps,
but less familiar with plotting relationships.
Below are some thoughts that hopefully will be useful
in developing a detailed study of natural processes.

The word "significance" often implies some sort of formal
statistical test.
On the other hand, the importance of a finding relates to
whether the result is meaningful and useful
to the problem at hand.
Statistical significance does not imply importance, and
importance does not imply statistical significance.
Further, large amounts of data can lead to highly significant
relationships that are practically meaningless.

- [Measures over Time and Space](#measures-over-time-and-space)
- [Test or Plot?](#test-or-plot)
- [Scatter Plots to Relate Measurements](#scatter-plots-to-relate-measurements)
- [Spurious Association](#spurious-association)
- [Multiple Testing](#multiple-testing)
- [`p`-hacking and Data Dredging](#p-hacking-and-data-dredging)

## Measures over Time and Space

There are further issues in that measurements over time and space
are inherently correlated (autocorrelated).
Two measures of rainfall in the same valley would likely be
similar, and over time would be (auto)correlated.
Over space, multiple locations in that valley would have similar
values, with correlation decaying with distance.
This means that comparing such measures will take some care.

A further challenge is that the time or spatial resolution
of measurements is often somewhat arbitrary.
A day makes sense for time measurements, but a drought may
last for weeks or months, and rainfall may be over in minutes.
Spatial resolution is even trickier, and may be driven by
geographic factors (land cover) and/or administrative
boundaries (different management in different states or
counties).

In addition, the effects may be cumulative, such as rainfall
and drought over time.
For an example of plotting rainfall and drought cumulatively, see
[South Dakota Rain and Drought (Brian Yandell)](https://byandell.github.io/rainDrought/).

## Test or Plot?

It is tempting to jump quickly to tests of significance.
Often it is more useful to plot the data first
to get a sense of what is going on.
We used to teach to first develop an hypothesis,
then design an experiment to collect data,
then analyze (test) the data.
In natural setting, the "experiment" is beyond our control,
but we can still use scientific reasoning to ideate plausible
relationships.
Plotting data in a variety of
ways helps us explore relationships and potential models.
Statistical tests can then be used to formally evaluate discovered
relationships, with the caveat that the journey to fixing
on the tested relationships needs to be documented.

Usually, plots are more effective, and more pleasing to the eye,
than tables of numbers from tests.

## Scatter Plots to Relate Measurements

A scatter plot is an XY-plot of two measurements, ideally augmented with color and trend lines and maybe even facets.
Data scientists do this all the time in `R` with the
[ggplot2](https://ggplot2.tidyverse.org/) package,
which has a `Python` version called
[plotnine](https://plotnine.readthedocs.io/).

A question came up of how to relate rain and drought (or any other measures over time and space).
I figured out how to create the plot I suggested from cumulative rain and drought.
I used an example of two counties in SD, which are homes to Oglala Lakota (Pine Ridge in Oglala Lakota County)
and Sicangu (Rosebud in Todd County).
Here are links to the published reports and the GitHub repo.
The code uses `plotnine` in python.

- <https://byandell.github.io/rainDrought/> (published report)
- <https://github.com/byandell/rainDrought> (GitHub repo)

I think it is much better to show data explicitly (and do it early in a report) rather than talk about the concept.
I also do not think correlation works well when considering processes over time and space,
where there is substantial auto-correlation built in and variability due to the scale of measures.
Cumulative measures are much better behaved for a variety of reasons.

I have another example using `plotnine` in the section
[Scatter Plots with GGplot](https://byandell-envsys.github.io/landmapyr/climate.html#scatter-plots-with-ggplot)
of an EDA report
[Habitat suitability under climate change](https://byandell-envsys.github.io/landmapyr/climate.html).

## Spurious Association

Association among measurements may be spurious rather than
meaningful or causative.
Here are some examples.

- [Spurious Associations (Alexander Pastukhov)](https://alexander-pastukhov.github.io/notes-on-statistics/multiple-regression-01-spurious-association.html)
- [5 Examples of Spurious Correlation in Real Life (Statology)](https://www.statology.org/spurious-correlation-examples/)
- [Understanding Spurious Correlations (keydifferences)](https://keydifferences.com/spurious-correlation-vs-causation.html)
- [Spurious Correlation Explained with 7 Examples (Datanizant)](https://datanizant.com/spurious-correlation-examples/)

## Multiple Testing

Multiple testing involves conducting multiple (hundreds, thousands or millions) of statistical tests on the same data.
Often this involves picking out different types of responses to
look for relationships.

The problem is that even if all tests are conducted at a significance (alpha) level of 0.05,
we still expect 5% of tests to be statistically significant by chance alone.
So, if we conduct 100 tests, we expect 5 to be statistically significant by
chance alone, even if there are no real relationships.

Instead, it is useful to think of test summaries, such as `p`-values,
as measures of "evidence" to support relationships.
In this sense, ordered tables (from smallest to largest `p`)
provide a rank ordered presentation of evidence.
Think of this as a way to prioritize likely relationships,
giving one insights that might be useful in designing future
investigations.

Below are some references, but **beware of simply how to**.
Don't get lost in the mechanics.
And remember that all approaches to multiple testing are imperfect
approximations.
Judgement and external knowledge of a system are paramount.

- [Multiple Comparisons Problem (Wikipedia)](https://en.wikipedia.org/wiki/Multiple_comparisons_problem)
- [Multiple Testing Problem (Statistics How To)](https://www.statisticshowto.com/multiple-testing-problem/)
- [Use and misuse of corrections for multiple testing (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2590260123000115)
- [When to Adjust for Multiple Testing: A Unifying Guiding Principle (Biometrical Journal)](https://onlinelibrary.wiley.com/doi/10.1002/bimj.70148)

## `p`-hacking and Data Dredging

- [What Is P-Hacking and How Does It Affect Science?](https://scienceinsights.org/what-is-p-hacking-and-how-does-it-affect-science/)
- [Data Dredging (Wikipedia)](https://en.wikipedia.org/wiki/Data_dredging)
- [What is P Hacking: Methods & Best Practices (Jim Frost)](https://statisticsbyjim.com/hypothesis-testing/p-hacking/)
- [Ethics of P-hacking: How to Avoid P-Hacking in Research (Statology)](https://www.statology.org/ethics-p-hacking-avoid-research/)
