from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "netflix_titles.csv"
OUT = ROOT / "data" / "cleaned_netflix_titles.csv"

df = pd.read_csv(RAW)
clean = df.copy()
clean["date_added"] = pd.to_datetime(clean["date_added"], errors="coerce")

for col in ["director", "cast", "country", "rating"]:
    clean[col] = clean[col].fillna("Unknown")

clean["year_added"] = clean["date_added"].dt.year
clean["month_added"] = clean["date_added"].dt.month
clean["month_name"] = clean["date_added"].dt.month_name()
clean["duration_value"] = pd.to_numeric(
    clean["duration"].str.extract(r"(\d+)")[0], errors="coerce"
)
clean["duration_unit"] = clean["duration"].str.extract(r"([A-Za-z]+)$")[0]
clean["content_age_at_addition"] = clean["year_added"] - clean["release_year"]
clean["content_age_at_addition"] = clean["content_age_at_addition"].where(
    clean["content_age_at_addition"] >= 0
)

OUT.parent.mkdir(exist_ok=True)
clean.to_csv(OUT, index=False)
print(f"Saved {len(clean):,} rows to {OUT}")
