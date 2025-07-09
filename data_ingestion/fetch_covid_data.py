import requests

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
filename = "owid_covid_data.csv"

response = requests.get(url)

if response.status_code == 200:
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"✅ File downloaded and saved as {filename}")
else:
    print(f"❌ Failed to fetch data: {response.status_code}")
