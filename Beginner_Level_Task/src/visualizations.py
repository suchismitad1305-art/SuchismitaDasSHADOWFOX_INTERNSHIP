"""
Beginner Data Visualization Project
Student: Suchismita Das
ShadowFox Internship | September 2026

Run:
    python src/visualizations.py
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
sns.set_theme(style="whitegrid")

# 1. Matplotlib Line Chart
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]
plt.figure(figsize=(7, 4))
plt.plot(x, y, marker="o")
plt.title("Matplotlib Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.tight_layout()
plt.savefig(OUT / "matplotlib_line_chart.png", dpi=160)
plt.close()

# 2. Matplotlib Bar Chart
plt.figure(figsize=(7, 4))
plt.bar(df["Student"][:4], df["Marks"][:4])
plt.title("Matplotlib Bar Chart - Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(OUT / "matplotlib_bar_chart.png", dpi=160)
plt.close()

# 3. Matplotlib Histogram
rng = np.random.default_rng(42)
data = rng.normal(size=100)
plt.figure(figsize=(7, 4))
plt.hist(data, bins=10)
plt.title("Matplotlib Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(OUT / "matplotlib_histogram.png", dpi=160)
plt.close()

# 4. Matplotlib Scatter Plot
scatter_x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
scatter_y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
plt.figure(figsize=(7, 4))
plt.scatter(scatter_x, scatter_y)
plt.title("Matplotlib Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.tight_layout()
plt.savefig(OUT / "matplotlib_scatter_plot.png", dpi=160)
plt.close()

# 5. Matplotlib Pie Chart
labels = ["A", "B", "C", "D"]
sizes = [25, 35, 20, 20]
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Matplotlib Pie Chart")
plt.tight_layout()
plt.savefig(OUT / "matplotlib_pie_chart.png", dpi=160)
plt.close()

# 6. Seaborn Line Plot
line_data = [2, 4, 7, 11, 16]
plt.figure(figsize=(7, 4))
sns.lineplot(x=[1,2,3,4,5], y=line_data, marker="o")
plt.title("Seaborn Line Plot")
plt.tight_layout()
plt.savefig(OUT / "seaborn_line_plot.png", dpi=160)
plt.close()

# 7. Seaborn Bar Plot
plt.figure(figsize=(7, 4))
sns.barplot(x=df["Student"][:4], y=df["Marks"][:4], color="steelblue")
plt.title("Seaborn Bar Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(OUT / "seaborn_bar_plot.png", dpi=160)
plt.close()

# 8. Seaborn Histogram
plt.figure(figsize=(7, 4))
sns.histplot(data, bins=10, kde=True, color="steelblue")
plt.title("Seaborn Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(OUT / "seaborn_histogram.png", dpi=160)
plt.close()

# 9. Seaborn Scatter Plot
plt.figure(figsize=(7, 4))
sns.scatterplot(x=scatter_x, y=scatter_y, color="steelblue")
plt.title("Seaborn Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.tight_layout()
plt.savefig(OUT / "seaborn_scatter_plot.png", dpi=160)
plt.close()

# 10. Seaborn Box Plot
box_data = [[1, 2, 5, 6, 7, 9], [3, 4, 5, 7, 8, 10]]
plt.figure(figsize=(7, 4))
sns.boxplot(data=box_data, color="steelblue")
plt.title("Seaborn Box Plot")
plt.xlabel("Dataset")
plt.ylabel("Values")
plt.tight_layout()
plt.savefig(OUT / "seaborn_box_plot.png", dpi=160)
plt.close()

# 11. Seaborn Count Plot
count_data = pd.DataFrame({"Category": ["A","B","A","C","B","A"]})
plt.figure(figsize=(7, 4))
sns.countplot(data=count_data, x="Category", color="steelblue")
plt.title("Seaborn Count Plot")
plt.xlabel("Category")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(OUT / "seaborn_count_plot.png", dpi=160)
plt.close()

print(f"Created {len(list(OUT.glob('*.png')))} visualization files in: {OUT}")
