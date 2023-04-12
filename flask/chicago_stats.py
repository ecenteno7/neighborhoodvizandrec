import csv
import requests

with open('../mapquestAPIkey.txt') as f:
        mq_api_key = f.readline()
        f.close()


url = "http://www.mapquestapi.com/search/v2/radius"

params = {
    "key": mq_api_key,
    "origin": "Chicago, IL",
    "radius": "35",
    "ambiguities": "ignore",
    "outFormat": "json",
    "maxMatches": "500"}

response = requests.get(url, params=params)

if response.status_code == 200:
    results = response.json()["searchResults"]
    with open("flask/neighborhoods/chicago_places_of_interest.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(results[0]["fields"].keys())
        for result in results:
            writer.writerow(result["fields"].values())
else:
    print("Error:", response.status_code, response.text)

