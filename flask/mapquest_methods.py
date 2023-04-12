import json
import csv




with open('../mapquestAPIkey.txt') as f:
        mq_api_key = f.readline()
        f.close()


city = "chicago"
with open("flask/neighborhoods/"+city+'.geojson') as f:
        neighborhoods = json.load(f)

#use just the first 10 neighborhoods for testing purposes
neighborhoods_10 = {'type': 'FeatureCollection', 'features': neighborhoods['features'][:10]}

# Create an empty dictionary to store the bounding box information
bbox_dict = {}

# Load the BoundingBox CSV file into a list of dictionaries
with open("flask/neighborhoods/"+city+'_bboxes.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Convert the bounding box coordinates to floats
        minLon, minLat, maxLon, maxLat = map(float, [row['MinLon'], row['MinLat'], row['MaxLon'], row['MaxLat']])
        
        # Add the bounding box information to the dictionary
        bbox_dict[row['Neighborhood']] = (minLon, minLat, maxLon, maxLat)

# Print the contents of the bbox_dict to the screen
print(bbox_dict)

#bounding box for Mapquest is lowerleft corner, upper right corner
#-87.629363,41.801893,-87.606407,41.823965   upper left, lower right
#MinLon,MaxLat, MaxLon, MinLat  LL, UR
# -87.629363,41.823965,-87.606407,41.801893

mapquest_category_limited = [842205,599969,546103,581301,724101,594201, 581214, 799302, 866107, 565101, 541103, 531102, 581208  ] #barbers for beauty_salon, no bus stations, all places of worship,  STOPPED AT DOCTOR and adde all restaurants
# google codes from limited ["aquarium", "art_gallery", "bakery", "bar", "beauty_salon", "book_store", "bus_station", "cafe", "casino", "church", "clothing_store", "convenience_store", "department_store", "doctor", "drugstore", "electronics_store", "furniture_store", "gas_station", "gym", "hair_care", "hardware_store", "hindu_temple", "home_goods_store", "jewelry_store", "laundry", "lawyer", "library", "light_rail_station", "liquor_store", "lodging", "meal_delivery", "meal_takeaway", "mosque", "movie_theater","museum", "night_club", "park", "parking", "pet_store", "pharmacy", "police", "restaurant", "school", "shoe_store", "shopping_mall", "spa", "stadium", "store", "subway_station", "supermarket", "synagogue", "taxi_stand", "tourist_attraction", "train_station", "transit_station", "university", "veterinary_care", "zoo"]


#mapquest category codes can be fount in mapquest_codes.csv

