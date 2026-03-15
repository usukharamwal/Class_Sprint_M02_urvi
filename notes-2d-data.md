# Notes: 2d-data.csv

## Dataset overview
- Columns: `x`, `y`
- Rows: **6000**
- Both variables are continuous and numeric.

## Before visualization

From `describe()`:
**x**
- count = 6000
- mean = 2.20, std = 0.28  
- min = 1.23, Q1 = 1.99, median = 2.20, Q3 = 2.41  
- max = 3.10

**y**
- count = 6000
- mean = 2.20, std = 0.28  
- min = 1.35, Q1 = 1.98, median = 2.19, Q3 = 2.41  
- max = 3.18

### Association checks
I computed both linear and rank-based correlation:

- **Pearson r = 0.493**
- **Spearman ρ = 0.527**

Based on correlation values, there is a moderate positive relationship between `x` and `y`. The slightly higher Spearman value suggests the relationship is monotonic and not strictly linear.

## Visualization

### Why not a simple scatter plot?
With 6000 points, a standard scatter plot can suffer from **overplotting**, where dense regions appear saturated and the true concentration structure becomes unclear.

### Final plot: Hexbin density plot
I used a **hexbin density plot**:
- Each hexagon bins points in the 2D plane.
- The color indicates the **count of points per hexagon** (shown by the colorbar).
- This makes the most common regions (high density) immediately visible without hiding points.

I also set:
- `ax.set_aspect("equal")` to avoid distorting geometry (equal scaling of x and y units).

- Brighter regions indicate where the data is most concentrated.
- The density “cloud” is elongated from lower-left to upper-right, visually reinforcing the **positive association** between `x` and `y`.
- Lower-density regions around the edges represent less frequent observations.

## Output files
- Figure: `figs/plot_2d.png`
- Script: `workflow/Final_2d.py`