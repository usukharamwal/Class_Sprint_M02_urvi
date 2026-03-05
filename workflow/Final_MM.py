import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

read_MM = pd.read_csv('data/1d-multi-method-data.csv')

# create figs directory if it doesn't exist
Path("figs").mkdir(parents=True, exist_ok=True)
fig, ax = plt.subplots(figsize=(11, 5))
sns.set_theme(style="whitegrid")

# sort by median and Proposed at end
med_order = read_MM.groupby("method")["AUCROC"].median().sort_values().index.tolist()
order = [m for m in med_order if m.lower() != "proposed"] + ["Proposed"]

baselines = [m for m in order if m.lower() != "proposed"]
palette = {m: "0.75" for m in baselines}
palette["Proposed"] = "#1f77b4"

# background band 
i_prop = order.index("Proposed")
ax.axvspan(i_prop - 0.5, i_prop + 0.5, alpha=0.12, zorder=0)

sns.boxplot(
    data=read_MM, x="method", y="AUCROC",
    order=order, palette=palette,
    width=0.55, fliersize=2, linewidth=1.2, ax=ax
)

sns.stripplot(
    data=read_MM, x="method", y="AUCROC",
    order=order, color="black",
    alpha=0.18, jitter=0.22, size=2.0, ax=ax
)

prop_med = read_MM.loc[read_MM["method"] == "Proposed", "AUCROC"].median()
ax.annotate(
    f"Proposed median = {prop_med:.3f}",
    xy=(i_prop, prop_med),
    xytext=(8, 8),
    textcoords="offset points",
    fontsize=10,
    fontweight="bold",
    ha="left", va="bottom",
)

ax.set_ylim(0, 1)
ax.set_xlabel("Method")
ax.set_ylabel("AUC-ROC")
ax.set_title("AUC-ROC distributions across methods")
ax.tick_params(axis="x", rotation=25, labelsize=9)
fig.tight_layout()
fig.savefig('figs/plot_MM.png')