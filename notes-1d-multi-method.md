# Notes: 1d-multi-method-data.csv

## Dataset overview
- Columns: `method`, `AUCROC`
- Each method (Baselines + Proposed) has **multiple AUC-ROC measurements**.

## Before final visualization
I summarized performance per method to understand the ranking before plotting:
- `groupby('method').AUCROC.mean().sort_values(ascending=False)`
- `groupby('method').AUCROC.median().sort_values(ascending=False)`

### Mean AUC-ROC (descending)
| Method      | Mean AUC-ROC |
|-------------|--------------:|
| Baseline_2  | 0.916858 |
| Baseline_1  | 0.766974 |
| Proposed    | 0.661321 |
| Baseline_9  | 0.557234 |
| Baseline_3  | 0.461854 |
| Baseline_7  | 0.388454 |
| Baseline_6  | 0.320925 |
| Baseline_5  | 0.269172 |
| Baseline_4  | 0.226200 |
| Baseline_8  | 0.192495 |

### Median AUC-ROC (descending)
| Method      | Median AUC-ROC |
|-------------|----------------:|
| Baseline_2  | 0.907718 |
| Baseline_1  | 0.767523 |
| Proposed    | 0.669363 |
| Baseline_9  | 0.572660 |
| Baseline_3  | 0.455904 |
| Baseline_7  | 0.391778 |
| Baseline_6  | 0.323728 |
| Baseline_5  | 0.266379 |
| Baseline_4  | 0.225000 |
| Baseline_8  | 0.191516 |

**Key observation:** Proposed method ranks **3rd** by both mean and median, behind **Baseline 2 and 1**.

### Final visualization: Boxplot + jittered points (sorted by median)
- Methods are **sorted by median AUC-ROC** to make ranking and gaps easy to see.

## Highlighting Proposed
To highlight Proposed clearly without distorting the data:
- Baselines are shown in **muted gray**
- Proposed is shown in a **distinct color**
- A **light vertical background band** is added behind Proposed
- The **Proposed median** is directly annotated on the plot

These cues draw attention immediately to Proposed while keeping the comparison fair.

- The y-axis is fixed to **[0, 1]**, the valid range for AUC-ROC.
- Raw points are included to avoid hiding sample size/outliers.

- Proposed performs better than most baselines (Baselines 3–9) but remains below Baseline 1 and 2 based on both central tendency and visual distribution.

## Output files
- Figure: `figs/plot_MM.png`
- Script: `workflow/Final_MM.py`