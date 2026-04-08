import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# kagglehub.dataset_download("alitaqishah/global-mental-health-crisis-index-2026", output_dir="datasets", force_download=True)
df = pd.read_csv("datasets/Global_Mental_Health_Crisis_Index_2026.csv")
# # print(df.head())
#
# # depression = df[["depression_pct", "country"]]
#
#
# # mask = (df["region"] == "Europe") & (df["depression_pct"] > 5)
# # europe_depression = df[mask]
# # print(europe_depression[["country", "depression_pct"]])
#
#
# # df["millions * rate"] = df["suicide_rate_per100k"] * df["population_millions"] * 10
# # print(df[["country","millions * rate"]])
#
# mask = (df["gdp_per_capita_usd"] <= 10000) & (df["mh_system_score"]< 5)
# rich_countries = df[mask]
# rich_countries["lack_of_care_mln"] = (rich_countries["population_millions"] * rich_countries["treatment_gap_pct"]/100)
# print(rich_countries[['country', "gdp_per_capita_usd", "mh_system_score", "lack_of_care_mln"]])

# top_5 = df.nlargest(5, "depression_pct")
#
# plt.figure(figsize = (8,4))
#
# plt.plot(top_5["country"], top_5["depression_pct"],
#          marker = 'o')
# plt.plot(top_5["country"], top_5["anxiety_pct"],
#          marker = 's')
# plt.title("Anxiety vs Depression (%)")
# plt.xlabel("Countries")
# plt.ylabel("Percents")
# plt.show()

plt.figure(figsize = (8,4))

plt.title("Hours in social media vs crisis")
plt.xlabel("Hours")
plt.ylabel("Crisis")
plt.scatter(df["social_media_hours_daily"], df["youth_mh_crisis_score"],
            s=100, alpha = 0.5, color='red')

x,y = np.polyfit(df["social_media_hours_daily"], df["youth_mh_crisis_score"], 1)
plt.plot(df["social_media_hours_daily"], x*df["youth_mh_crisis_score"]+y, color='blue')
plt.grid(True, linestyle = '--', linewidth = 0.5)
plt.show()