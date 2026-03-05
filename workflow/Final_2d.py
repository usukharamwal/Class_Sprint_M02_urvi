import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

read_2d = pd.read_csv('data/2d-data.csv')

# create figs directory if it doesn't exist
Path("figs").mkdir(parents=True, exist_ok=True)

df = read_2d.copy()
df["x"] = pd.to_numeric(df["x"], errors="coerce")
df["y"] = pd.to_numeric(df["y"], errors="coerce")
df = df.dropna(subset=["x", "y"])

# --- Density Plot ---
plt.close("all")
fig, ax = plt.subplots(figsize=(6.5, 5))

hb = ax.hexbin(df["x"], df["y"], gridsize=40, mincnt=1)
cb = fig.colorbar(hb, ax=ax)
cb.set_label("Count per hexagon")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("2D sample density")
ax.set_aspect("equal", adjustable="box")
fig.tight_layout()
fig.savefig('figs/plot_2d.png')
