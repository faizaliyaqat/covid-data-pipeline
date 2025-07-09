# clean_transform.py

import pandas as pd
df = pd.read_csv("C:/covid_free_tier_pipeline/data_ingestion/owid_covid_data.csv")

df = df[[
    'iso_code', 'continent', 'location', 'date',
    'total_cases', 'new_cases', 'total_deaths', 'new_deaths',
    'population', 'people_fully_vaccinated'
]]

df = df.dropna(subset=['location', 'date'])
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

df.to_csv("cleaned_owid_covid_data.csv", index=False)
# or df.to_parquet("cleaned_owid_covid_data.parquet")
print("✅ Transformation complete!")
