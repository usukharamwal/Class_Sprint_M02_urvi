import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

read_1d = pd.read_csv('data/1d-data.csv')

# create figs directory if it doesn't exist
Path("figs").mkdir(parents=True, exist_ok=True)

df = read_1d.copy()
df["group"] = df["group"].astype(str).str.strip()
df["value"] = pd.to_numeric(df["value"], errors="coerce")

plt.close("all")
fig, ax = plt.subplots(figsize=(7, 4.5))
sns.set_theme(style="whitegrid")
sns.boxplot(
    data=df,
    x="group",
    y="value",
    ax=ax,
    showfliers=True,
    width=0.5,
)

sns.stripplot(
    data=df,
    x="group",
    y="value",
    ax=ax,
    jitter=0.18,
    size=6,
    alpha=0.8,
    linewidth=0.5,
    edgecolor="black",
)

# Log scale to avoid misleading compression given extreme skew
ax.set_yscale("log")

ax.set_xlabel("Group")
ax.set_ylabel("Value (log scale)")
ax.set_title("Distribution by group")

fig.tight_layout()
fig.savefig('figs/plot_1d.png')