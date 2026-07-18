---
title: "Interactive and Dynamic Plots"
parent: "Python Language"
nav_order: 2
---

# Interactive and Dynamic Plots

When visualizing spatial data over time, we often want sliders, multiple plots arranged in a grid, or other dynamic elements. This page describes approaches for creating static multi-panel maps and interactive map sliders using packages like `matplotlib`, `hvplot` (HoloViews), `Panel`, and `geemap` (Google Earth Engine).

For reference implementations, see the
[landmapyr](https://byandell-envsys.github.io/landmapyr/)
package, which contains utilities for environmental mapping and species occurrence visualization.

---

## 1. Static Multi-Panel Maps (Matplotlib & Contextily)

For presenting temporal changes (e.g., species occurrence by month or decade) in reports, static grids of maps are often preferred. They are lightweight, render quickly in Markdown and Quarto, and display directly on GitHub.

The utility function [plot_occurrence](https://github.com/byandell-envsys/landmapyr/blob/main/landmapyr/plots.py#L383) in [plots.py](https://github.com/byandell-envsys/landmapyr/blob/main/landmapyr/plots.py) demonstrates how to cleanly set up a multi-panel grid of maps:

### Key Design Principles

1. **Consistent Extent**: Calculate `total_bounds` from the entire GeoDataFrame beforehand to set identical limits (`xlim`, `ylim`) for all subplots. This ensures that the map zoom level and centering do not change between panels.
2. **Consistent Color Scaling**: Pre-calculate `vmin` and `vmax` across the entire dataset so the color scale represents values consistently across panels.
3. **Axis Limits before Basemap**: Set axis limits *before* calling `contextily.add_basemap`. This ensures that `contextily` fetches the correct map tiles for the exact bounding box and avoids rendering errors.
4. **Clean Layout**: Hide axes labels and ticks using `ax.set_axis_off()`, and turn off any unused axes in the grid.

### Implementation Example

```python
import matplotlib.pyplot as plt
import contextily as ctx
import calendar
import math

def plot_occurrence(occurrence_gdf, unit="month", ncols=None):
    # 1. Get unique time units (e.g., month names or years)
    units = sorted(occurrence_gdf[unit].unique())
    n_units = len(units)
    
    # 2. Determine grid size
    ncols = min(4, n_units) if ncols is None else min(ncols, n_units)
    nrows = math.ceil(n_units / ncols)
    
    # 3. Get bounds for consistent extent
    xmin, ymin, xmax, ymax = occurrence_gdf.total_bounds
    
    fig, axes = plt.subplots(nrows, ncols, figsize=(ncols * 5.0, nrows * 5.0))
    axes = axes.flatten() if n_units > 1 else [axes]
    
    # 4. Get consistent colorbar limits
    vmin = occurrence_gdf["norm_occurrences"].min()
    vmax = occurrence_gdf["norm_occurrences"].max()
    
    for i, u in enumerate(units):
        ax = axes[i]
        subset = occurrence_gdf[occurrence_gdf[unit] == u]
        
        # Plot data
        subset.plot(
            column="norm_occurrences",
            ax=ax,
            cmap="viridis",
            vmin=vmin,
            vmax=vmax,
            edgecolor="none"
        )
        
        # Set limits BEFORE adding basemap
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
        
        # Add basemap (e.g., CartoDB Positron)
        try:
            ctx.add_basemap(
                ax,
                source=ctx.providers.CartoDB.Positron,
                crs=occurrence_gdf.crs.to_string(),
            )
        except Exception:
            pass
            
        ax.set_axis_off()
        if unit == "month":
            ax.set_title(calendar.month_name[int(u)])
            
    # Hide any unused axes
    for j in range(i + 1, len(axes)):
        axes[j].axis("off")
        
    plt.tight_layout()
    plt.show()
```

---

## 2. Interactive Map Sliders (hvPlot & Panel)

Interactive plots allow users to explore data dynamically. The `hvplot` library provides a high-level API built on HoloViews, and `Panel` handles dashboard components like sliders.

> [!WARNING]
> HoloViews and GeoViews objects generate very large files (often several Megabytes) when embedded directly in HTML or Quarto files. To keep your main documents light and displayable on platforms like GitHub, save the interactive plots as standalone HTML files and link to them.

### Approach A: Custom Slider and `hvplot` (inline widgets)

You can define a discrete slider widget using `Panel` and link it to an `hvplot` object through the `groupby` parameter. This approach is illustrated in [Marsha's migration-mj notebook](https://github.com/cu-esiil-edu/03-migration-MarshaJ24/blob/main/notebooks/migration-mj.ipynb):

```python
import panel as pn
import hvplot.pandas
import calendar
import cartopy.crs as ccrs

# Get bounds to lock the map view during transitions
xmin, ymin, xmax, ymax = occurrence_gdf.total_bounds

# Define discrete slider widget
slider = pn.widgets.DiscreteSlider(
    name='month',
    options={calendar.month_name[i]: i for i in range(1, 13)}
)

# Generate interactive map with slider widget
migration_plot = (
    occurrence_gdf
    .hvplot(
        c='norm_occurrences',
        groupby='month',
        geo=True,
        crs=ccrs.Mercator(),
        tiles='CartoLight',
        title="Crane migration",
        xlim=(xmin, xmax), 
        ylim=(ymin, ymax),
        frame_width=500,
        widgets={'month': slider},
        widget_location='bottom'
    )
)

# Save to standalone HTML file to keep notebooks/pages lightweight
migration_plot.save('migration_map.html', embed=True)
```

### Approach B: Packaged `hvplot_occurrence` Utility

The function [hvplot_occurrence](https://github.com/byandell-envsys/landmapyr/blob/main/landmapyr/hv_plots.py#L222) in [hv_plots.py](https://github.com/byandell-envsys/landmapyr/blob/main/landmapyr/hv_plots.py) generalizes this pattern, handling different temporal units (e.g. `month`, `decade`, `year`) and automatically generating appropriate slider options.

```python
def hvplot_occurrence(occurrence_gdf, unit="month"):
    import panel as pn
    import calendar
    import hvplot.pandas

    # Lock bounding box
    xmin, ymin, xmax, ymax = occurrence_gdf.total_bounds
    pn.extension()

    # Determine slider options dynamically based on unit
    if unit == "month":
        options = {calendar.month_name[i]: i for i in range(1, 13)}
    elif unit == "decade":
        decades = occurrence_gdf.index.get_level_values("decade").dropna().unique()
        options = {f"{int(d)}s": int(d) for d in sorted(decades)}
    elif unit == "year":
        years = occurrence_gdf.index.get_level_values("year").dropna().unique()
        options = sorted([int(y) for y in years])
    else:
        levels = occurrence_gdf.index.get_level_values(unit).dropna().unique()
        options = sorted(list(levels))

    # Initialize slider and plot
    slider = pn.widgets.DiscreteSlider(name=unit, options=options)
    
    occurrence_hvplot = occurrence_gdf.hvplot(
        c="norm_occurrences",
        groupby=unit,
        tiles="CartoLight",
        xlim=(xmin, xmax),
        ylim=(ymin, ymax),
        frame_height=600,
        frame_width=1400,
        colorbar=False,
        widgets={unit: slider},
        widget_location="bottom",
        width=500,
        height=500,
    )
    return occurrence_hvplot
```

For illustration, see
[sandhill_crane.qmd](https://byandell-envsys.github.io/landmapyr/sandhill_crane.html)
([source](https://github.com/byandell-envsys/landmapyr/blob/main/docs/sandhill_crane.qmd))
where it is used to output a dynamic HTML map:

```python
from landmapyr.hv_plots import hvplot_occurrence

occurrence_hvplot = hvplot_occurrence(occurrence_gdf)
# Save the plot externally
occurrence_hvplot.save('sandhill-crane-migration.html', embed=True)
```

### Rendering Interactive Sliders on Static Websites (Quarto / GitHub Pages)

When rendering `.qmd` files to static HTML sites (such as GitHub Pages), there is no active Python kernel in the background to handle the slider callbacks. Simply outputting the `occurrence_hvplot` object in a cell will result in a static plot with a non-functional slider.

To solve this, the most robust and conflict-free approach is to:

1. Save the plot to a standalone HTML file with `embed=True`.
2. Disable evaluation for the cell displaying the plot (`eval: false`).
3. Embed the generated HTML file using a standard HTML
[`<iframe>` tags](https://www.w3schools.com/tags/tag_iframe.asp).

This isolates the
[Bokeh](https://docs.bokeh.org/en/latest/)
and
[Panel](https://panel.holoviz.org/)
JavaScript contexts, avoiding version clashes or double-loading conflicts
on the parent page (which otherwise often cause the plot to render as a blank space).
This may still not work smoothly as all these
tools may clash with each other;
consider putting the plot in a separate web page
as I did with
[Dynamic Images from EDA Projects](https://byandell-envsys.github.io/landmapyr/images.html)
([source](https://github.com/byandell-envsys/landmapyr/blob/main/docs/images.md)).

#### Step 1: Save the plot with embedded states

```python
# Save the plot with all slider states pre-computed
occurrence_hvplot.save('sandhill-crane-migration.html', embed=True)
```

#### Step 2: Display via iframe in your Markdown

```python
#| eval: false
#| label: fig-monthly-occurrence
# Shown as code reference but not evaluated to avoid duplication
occurrence_hvplot
```

#### Step 3: Embed HTML file using an iframe

```html
<iframe src="sandhill-crane-migration.html" width="100%" height="650px"
        style="border: none;"></iframe>
```

---

## 3. Google Earth Engine (geemap) Time Slider

For high-resolution Earth Engine imagery collections, [Google Earth Engine Map (geemap)](https://geemap.org/) provides a native time slider widget.

See [72 time slider gui](https://geemap.org/notebooks/72_time_slider_gui/) for details:

```python
import ee
import geemap

# Initialize map
Map = geemap.Map(center=[37.75, -122.45], zoom=12)

# Load Copernicus Sentinel-2 image collection
S2 = (
    ee.ImageCollection("COPERNICUS/S2_SR")
    .filterBounds(ee.Geometry.Point([-122.45, 37.75]))
    .filterMetadata("CLOUDY_PIXEL_PERCENTAGE", "less_than", 10)
)

vis_params = {"min": 0, "max": 4000, "bands": ["B8", "B4", "B3"]}

# Add Sentinel-2 layer and interactive time slider GUI
Map.addLayer(S2, {}, "Sentinel-2", False)
Map.add_time_slider(S2, vis_params)
Map
```

---

## 4. Notebook Integration & Interactive Widgets

To render interactive plots (especially standard matplotlib ones) inside Jupyter notebooks rather than outputting static inline images, use the `ipympl` backend.

- **Enable Widgets Backend**:

  ```python
  %matplotlib widget
  ```

  This command activates `ipympl`, turning static matplotlib figures into interactive widgets where you can zoom, pan, and resize within VS Code or Jupyter.
- **Reference**: See [Using `%matplotlib` widget in Jupyter](https://github.com/microsoft/vscode-jupyter/wiki/Using-%25matplotlib-widget-instead-of-%25matplotlib-notebook,tk,etc) and [ipympl documentation](https://matplotlib.org/ipympl/).

---

## 5. Creating Animated GIFs

If interactive controls are not necessary, you can compile a sequence of static maps into an animated GIF. Here is a curated list of tutorials and libraries:

- [Creating an Animated GIF with Python (Pillow)](https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/)
  - [How to create animated GIF with Pillow in Python](https://note.nkmk.me/en/python-pillow-gif/)
- [Create an Animated GIF Using Python Matplotlib](https://www.geeksforgeeks.org/create-an-animated-gif-using-python-matplotlib/)
  - [Create a GIF with Python](https://www.codedex.io/projects/create-a-gif-with-python)
- [How to make a gif map using Python, Geopandas and Matplotlib](https://towardsdatascience.com/how-to-make-a-gif-map-using-python-geopandas-and-matplotlib-cd8827cefbc8) ⚠️
- [Using Python to make an animated gif out of a collection of images](https://propolis.io/articles/make-animated-gif-using-python.html) ⚠️
