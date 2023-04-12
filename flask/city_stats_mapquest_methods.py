import csv
import requests
import json
from shapely.geometry import MultiPolygon, shape, Point
import pandas

def city_poi_list_mapquest(api, city):
    url = "http://www.mapquestapi.com/search/v2/radius"

    if city == "chicago":
        radius = "10"
    elif city == "washingtondc":
        radius = "5"
    with open("flask/neighborhoods/"+city+'.geojson') as f:
        neighborhoods = json.load(f)

    #use just the first 10 neighborhoods for testing purposes############################################ ONLY 10 Neighborhoods ###############
    #neighborhoods= {'type': 'FeatureCollection', 'features': neighborhoods['features'][:10]}

    for feature in neighborhoods["features"]:
        print("Working on "+city+": "+feature["properties"]["name"])
        # Convert the feature's geometry to a Shapely MultiPolygon object
        geometry = shape(feature["geometry"])

        # Calculate the center point of the MultiPolygon
        center_point = geometry.centroid
        center_point = "{},{}".format(center_point.y, center_point.x)

        params = {
        "key": api,
        "origin": center_point,
        "radius": radius,
        "ambiguities": "ignore",
        "outFormat": "json",
        "maxMatches": "500"}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            results = response.json()["searchResults"]
            with open("flask/neighborhoods/"+city+"_places_of_interest.csv", "a", newline="", encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file)
                if csv_file.tell() == 0:
                    writer.writerow(results[0]["fields"].keys())
                for result in results:
                    writer.writerow(result["fields"].values())
        else:
            print("Error:", response.status_code, response.text)


#mapquest_category_limited = [842205,599969,546103,581301,724101,594201, 581214, 799302, 866107, 565101, 541103, 531102, 581208  ] #barbers for beauty_salon, no bus stations, all places of worship,  STOPPED AT DOCTOR and adde all restaurants
# google codes from limited ["aquarium", "art_gallery", "bakery", "bar", "beauty_salon", "book_store", "bus_station", "cafe", "casino", "church", "clothing_store", "convenience_store", "department_store", "doctor", "drugstore", "electronics_store", "furniture_store", "gas_station", "gym", "hair_care", "hardware_store", "hindu_temple", "home_goods_store", "jewelry_store", "laundry", "lawyer", "library", "light_rail_station", "liquor_store", "lodging", "meal_delivery", "meal_takeaway", "mosque", "movie_theater","museum", "night_club", "park", "parking", "pet_store", "pharmacy", "police", "restaurant", "school", "shoe_store", "shopping_mall", "spa", "stadium", "store", "subway_station", "supermarket", "synagogue", "taxi_stand", "tourist_attraction", "train_station", "transit_station", "university", "veterinary_care", "zoo"]


#mapquest category codes can be fount in mapquest_codes.csv


#remove duplicates from places_of_interest.csv
def remove_poi_duplicates(file):
    try:
        df = pandas.read_csv(file, encoding='utf-8')
        df.drop_duplicates(inplace=True)
        df.to_csv(file, index=False, encoding='utf-8')
    except UnicodeDecodeError:
        print("File encoding is not utf-8, please check the file encoding")

#ID each row of the places of interest file with a neighborhood
def id_poi_with_neighborhood(file, city):
    with open("flask/neighborhoods/"+city+'.geojson') as f:
        neighborhoods = json.load(f)
    with open(file) as f:
        poi = csv.reader(f)
        poi = list(poi)
    with open("flask/neighborhoods/"+city+'_poi_with_neighborhood.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(poi[0]+['Neighborhood'])
        poi = poi[1:]
        for row in poi:
            for feature in neighborhoods["features"]:
                geometry = shape(feature["geometry"])
                # if geometry.contains(shape({"type": "Point", "coordinates": [float(row[1]), float(row[0])]})):
                if geometry.contains(Point(float(row[3]), float(row[18]))):
                    writer.writerow(row+[feature["properties"]["name"]])
                    break

#create a tally of the number of each type of place of interest in each neighborhood
def tally_occurrences(file, city):
    df = pandas.read_csv(file)

    # Group the data by Neighborhood and group_sic_code_name_ext columns
    grouped = df.groupby(['Neighborhood', 'group_sic_code_name_ext', 'group_sic_code'])

    # Count the number of occurrences of each group_sic_code_name_ext and group_sic_code per Neighborhood
    result = grouped.size().reset_index(name='count')

    # Write to CSV file
    result.to_csv("flask/neighborhoods/"+city+'_neighborhood_category_counts.csv', index=False)

    #Create a different format:
    # Group the data by "Neighborhood" and "group_sic_code_name_ext", and count the occurrences
    grouped_df = df.groupby(["Neighborhood", "group_sic_code_name_ext"])["group_sic_code_name_ext"].count().reset_index(name="count")

    # Pivot the table to have each neighborhood as a row and each group_sic_code_name_ext as a column
    pivot_df = grouped_df.pivot_table(index="Neighborhood", columns="group_sic_code_name_ext", values="count", fill_value=0)

    # Reset the index to make "Neighborhood" a regular column
    pivot_df = pivot_df.reset_index()

    # Save the pivoted table to a new CSV file
    pivot_df.to_csv("flask/neighborhoods/"+city+'_neighborhood_category_counts_transpose.csv', index=False)









    



