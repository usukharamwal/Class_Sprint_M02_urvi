# Notes: 1d-data.csv (Cases vs Control)

## Dataset overview
- Columns: `value`, `group`
- Groups: **cases** and **control**
- Sample size: **n = 10 per group** (20 total)
- `value` is positive and highly variable.

## Before final visualization
I first reviewed the dataset using:
- `groupby('group').describe()` to compare summary statistics per group

## Summary statistics

| group   | count | mean       | std        | min      | 25%      | 50% (median) | 75%      | max        |
|---------|------:|-----------:|-----------:|---------:|---------:|-------------:|---------:|-----------:|
| cases   | 10.0  | 8536.68 | 12638.71 | 4.56 | 407.29 | 2589.40  | 9046.85 | 35764.91 |
| control | 10.0  | 2802.91 | 2815.49  | 20.80 | 204.46 | 2351.10   | 5384.06 | 6432.62 |

- `sort_values(['group','value'])` to inspect the smallest and largest values in each group
- `groupby('group').hist()` to check the distribution shape by group

### Key observations from review
- The data is **heavily right-skewed** in both groups with gaps/empty in between.
- The range spans **multiple orders of magnitude** (small values vs very large values).
- A simple linear-scale plot makes small values hard to see because large values dominate.

## Visualization attempts and iteration
### Attempt 1: Box plot (linear scale)
- I plotted a **boxplot + stripplot** by `group` using Seaborn.
- This correctly shows outliers and individual observations, but the linear y-axis still makes the lower range difficult to interpret due to extreme values.

### Final choice: Box + log-scaled y-axis
- I kept the same chart type (box + jittered points) but set:
  - `ax.set_yscale("log")`
- This makes the visualization **non-misleading** for skewed data because:
  - it preserves all observations,
  - it avoids compressing most points near zero,
  - it supports fair visual comparison across groups despite extreme values.

## How to interpret the final figure
- Each dot represents one observation.
- The box shows the middle 50% (IQR) and the median.
- On a **log scale**, equal vertical distances correspond to multiplicative differences (e.g., ~10×), which is appropriate given the data’s spread.

## Output files
- Figure: `figs/plot_1d.png`
- Script: `workflow/Final_1d.py`