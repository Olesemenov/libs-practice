import kagglehub
import pandas as pd

# kagglehub.dataset_download("alitaqishah/global-mental-health-crisis-index-2026", output_dir="datasets", force_download=True)
df = pd.read_csv("datasets/Global_Mental_Health_Crisis_Index_2026.csv")
# print(df.head())

# depression = df[["depression_pct", "country"]]


# mask = (df["region"] == "Europe") & (df["depression_pct"] > 5)
# europe_depression = df[mask]
# print(europe_depression[["country", "depression_pct"]])


# df["millions * rate"] = df["suicide_rate_per100k"] * df["population_millions"] * 10
# print(df[["country","millions * rate"]])

mask = (df["gdp_per_capita_usd"] <= 10000) & (df["mh_system_score"]< 5)
rich_countries = df[mask]
rich_countries["lack_of_care_mln"] = (rich_countries["population_millions"] * rich_countries["treatment_gap_pct"]/100)
print(rich_countries[['country', "gdp_per_capita_usd", "mh_system_score", "lack_of_care_mln"]])

