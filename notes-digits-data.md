# Notes: digits-data.csv

## Dataset overview
- Columns: `pixel_0` … `pixel_63`, `digit`
- Rows: **1797**
- Each row represents an **8×8** grayscale handwritten digit image flattened into **64 pixel-intensity features**.
- `digit` is the provided class label (0–9). No clustering is performed; labels are used only for coloring.

## Preprocessing and dimensionality reduction
### (1) Standardization
- Applied `StandardScaler()` to pixel features:
  - Many embedding methods (including t-SNE) behave more consistently when features are on comparable scales.
  
### (2) PCA before t-SNE
- Applied `PCA(n_components=30, random_state=42)` before t-SNE:
  - Speeds up t-SNE by reducing dimensionality from 64 → 30.
  - Keeps results reproducible with a fixed random seed.

## 2D embedding method (t-SNE)
- Used `TSNE(n_components=2, perplexity=30, learning_rate="auto", init="pca", random_state=42)`
- Rationale:
  - t-SNE is designed to preserve **local neighborhoods**, making it suitable for visualizing high-dimensional similarity structure.
  
## Visualization design choices
- Scatter plot in 2D:
  - Each point = one digit image.
  - Points are colored by the known `digit` label (0–9).

## Output files
- Figure: `figs/plot_DD.png`
- Script: `workflow/Final_DD.py`