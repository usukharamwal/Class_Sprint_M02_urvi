from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('data/digits-data.csv')

pixel_cols = [c for c in df.columns if c.startswith("pixel_")]
X = df[pixel_cols].to_numpy(dtype=float)
y = df["digit"].to_numpy()

# Standardize features for better t-SNE performance
X_scaled = StandardScaler().fit_transform(X)

# PCA for dimensionality reduction before t-SNE (speeds it up and can improve results)
X_pca = PCA(n_components=30, random_state=42).fit_transform(X_scaled)

# t-SNE embedding
tsne = TSNE(
    n_components=2,
    perplexity=30,    
    learning_rate="auto",
    init="pca",
    random_state=42
)
X_2d = tsne.fit_transform(X_pca)

plt.close("all")
fig, ax = plt.subplots(figsize=(8, 6))

# Plot each digit separately
for d in range(10):
    mask = (y == d)
    ax.scatter(
        X_2d[mask, 0],
        X_2d[mask, 1],
        s=12,
        alpha=0.8,
        label=str(d),
    )

ax.set_title("t-SNE visualization of handwritten digits (8×8)")
ax.set_xlabel("t-SNE 1")
ax.set_ylabel("t-SNE 2")

# Place the legend outside the plot to avoid overlap
ax.legend(
    title="Digit",
    ncol=4,
    fontsize=12,
    title_fontsize=14,
    frameon=True,
    loc="upper left",
    bbox_to_anchor=(1.02, 1),
    markerscale=2.0,
)

# Make room for the legend on the right and save including the outside legend
fig.subplots_adjust(right=0.78)
fig.savefig('figs/plot_DD.png', bbox_inches='tight')
