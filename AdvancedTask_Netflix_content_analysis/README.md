# Netflix Content Analysis — Advanced EDA

An advanced, reproducible Jupyter Notebook project for analyzing the supplied Netflix Movies and TV Shows catalog dataset.

## Research Problem

Netflix's catalog contains movies and TV shows from many countries, genres, release periods, and rating categories. This project investigates the structure and patterns represented in the dataset using data cleaning, feature engineering, exploratory data analysis, and visualization.

### Main Research Question

> **What patterns and trends can be identified in the Netflix catalog based on content type, release year, genres, countries, ratings, duration, and the timing of content addition?**

## Project Objectives

- Compare Movies and TV Shows.
- Examine content additions over time.
- Identify dominant genres/categories.
- Analyze geographic representation.
- Compare content ratings.
- Study movie duration and TV-show season structure.
- Examine the relationship between original release year and Netflix addition year.

## Repository Structure

```text
netflix-content-analysis/
├── data/
│   ├── netflix_titles.csv
│   ├── netflix_titles.txt
│   └── cleaned_netflix_titles.csv
├── notebooks/
│   └── Netflix_Content_Analysis.ipynb
├── outputs/
│   ├── 01_content_type_distribution.png
│   ├── 02_content_additions_by_year.png
│   ├── 03_top_genres.png
│   ├── 04_top_countries.png
│   ├── 05_ratings_by_type.png
│   ├── 06_movie_duration_distribution.png
│   ├── 07_tv_season_distribution.png
│   ├── 08_release_year_vs_added_year.png
│   ├── 09_addition_heatmap.png
│   ├── content_type_summary.csv
│   ├── genre_summary.csv
│   └── country_summary.csv
├── src/
│   └── clean_data.py
├── docs/
│   └── dataset_summary.json
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset

The project uses the Netflix titles dataset supplied for this project. The raw file is preserved unchanged in `data/netflix_titles.txt` and a CSV copy is provided as `data/netflix_titles.csv`.

The source contains fields including:

`show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, and `description`.

## Methodology

1. Load and inspect the raw data.
2. Measure missing values and duplicates.
3. Convert dates and extract temporal features.
4. Handle missing categorical metadata.
5. Extract numeric duration/season values.
6. Explode multi-valued genre and country fields.
7. Analyze content type, temporal trends, genres, countries, ratings, duration, and release/addition timing.
8. Generate visual evidence.
9. Summarize findings and limitations.

## Advanced Analysis Features

- Temporal feature engineering
- Multi-value categorical decomposition
- Type-specific analysis
- Cross-tabulation
- Distribution analysis
- Scatter analysis
- Heatmap analysis
- Reproducible preprocessing script
- Exported analysis artifacts

## Installation

```bash
git clone <your-repository-url>
cd netflix-content-analysis
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

## Run the Project

Open:

```text
notebooks/Netflix_Content_Analysis.ipynb
```

Run all cells from top to bottom.

Or regenerate the cleaned dataset with:

```bash
python src/clean_data.py
```

## Important Interpretation Note

This is a historical dataset snapshot. Results describe the titles represented in the supplied dataset and should not be presented as a live description of Netflix's 2026 catalog.

Also, country and genre counts are association counts because a single title can have multiple countries and categories.

## Skills Demonstrated

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Statistical Summaries
- Data Visualization
- Research Question Formulation
- Reproducible Data Analysis
- Git/GitHub project organization

## License / Dataset Attribution

Use the dataset according to the license and attribution requirements of the original public dataset source. The repository does not claim ownership of the underlying Netflix metadata.
