import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os

src_dir = Path.cwd() / "src"

DATA_PATH = src_dir / "data" / "processed" / "cluster_summary.csv"
OUT_PATH = src_dir / "visualizations" / "cluster_summary_table.png"
df = pd.read_csv(DATA_PATH)

fig, ax = plt.subplots(figsize=(4, 2))
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns,
                 cellLoc='center', loc='center')
table.auto_set_font_size(False)   # disable automatic font sizing
table.set_fontsize(3)            # set your preferred font size
plt.savefig(OUT_PATH, bbox_inches='tight', dpi=300)
