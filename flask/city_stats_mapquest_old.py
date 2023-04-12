import csv
import requests
import json
from shapely.geometry import MultiPolygon

def city_stats_mapquest(api, city):
    url = "http://www.mapquestapi.com/search/v2/radius"

    if city == "Chicago":
        radius = "10"
    elif city == "DC":
        radius = "5"
    with open("flask/neighborhoods/"+city+'.geojson') as f:
        neighborhoods = json.load(f)

    #use just the first 10 neighborhoods for testing purposes
    neighborhoods= {'type': 'FeatureCollection', 'features': neighborhoods['features'][:10]}    #don't bother?

    for feature in neighborhoods["features"]:
        # Convert the feature's geometry to a Shapely MultiPolygon object
        geometry = MultiPolygon(feature["geometry"]["coordinates"])

        # Calculate the center point of the MultiPolygon
        center_point = geometry.centroid

        params = {
        "key": mq_api_key,
        "origin": center_point,
        "radius": radius,
        "ambiguities": "ignore",
        "outFormat": "json",
        "maxMatches": "500"}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            results = response.json()["searchResults"]
            with open("flask/neighborhoods/"+city+"_places_of_interest.csv", "a", newline="") as csv_file:
                writer = csv.writer(csv_file)
                if csv_file.tell() == 0:
                    writer.writerow(results[0]["fields"].keys())
                for result in results:
                    writer.writerow(result["fields"].values())
        else:
            print("Error:", response.status_code, response.text)









    



