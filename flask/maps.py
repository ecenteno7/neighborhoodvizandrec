# import os
import googlemaps
import json
import neighborhood_methods as nm
from shapely.geometry import Point, shape, Polygon, MultiPolygon
import requests
import config


def get_gmaps_info(apikey, lat, lon, search_types=["restaurant", "cafe", "meal_delivery", "meal_takeaway"], debug=False):
    gmaps = googlemaps.Client(key=apikey)
    center_coords = (lat, lon)

    # with open(neighborhoods_file) as f:
    #     neighborhoods = json.load(f)

    # n_polygons = neighborhoods['coordinates']

    # search_types = ["restaurant", "cafe", "meal_delivery", "meal_takeaway"]
    restaurant_results = {'results': []}

    # place_types_all = ["accounting", "airport", "amusement_park", "aquarium", "art_gallery", "atm", "bakery", "bank", "bar", "beauty_salon", "bicycle_store", "book_store", "bowling_alley", "bus_station", "cafe", "campground", "car_dealer", "car_rental", "car_repair", "car_wash", "casino", "cemetery", "church", "city_hall", "clothing_store", "convenience_store", "courthouse", "dentist", "department_store", "doctor", "drugstore", "electrician", "electronics_store", "embassy", "fire_station", "florist", "funeral_home", "furniture_store", "gas_station", "gym", "hair_care", "hardware_store", "hindu_temple", "home_goods_store", "hospital", "insurance_agency", "jewelry_store", "laundry", "lawyer",
    #                    "library", "light_rail_station", "liquor_store", "local_government_office", "locksmith", "lodging", "meal_delivery", "meal_takeaway", "mosque", "movie_rental", "movie_theater", "moving_company", "museum", "night_club", "painter", "park", "parking", "pet_store", "pharmacy", "physiotherapist", "plumber", "police", "post_office", "primary_school", "real_estate_agency", "restaurant", "roofing_contractor", "rv_park", "school", "secondary_school", "shoe_store", "shopping_mall", "spa", "stadium", "storage", "store", "subway_station", "supermarket", "synagogue", "taxi_stand", "tourist_attraction", "train_station", "transit_station", "travel_agency", "university", "veterinary_care", "zoo"]
    # place_types_limited = ["aquarium", "art_gallery", "bakery", "bar", "beauty_salon", "book_store", "bus_station", "cafe", "casino", "church", "clothing_store", "convenience_store", "department_store", "doctor", "drugstore", "electronics_store", "furniture_store", "gas_station", "gym", "hair_care", "hardware_store", "hindu_temple", "home_goods_store", "jewelry_store", "laundry", "lawyer", "library", "light_rail_station",
    #                        "liquor_store", "lodging", "meal_delivery", "meal_takeaway", "mosque", "movie_theater", "museum", "night_club", "park", "parking", "pet_store", "pharmacy", "police", "restaurant", "school", "shoe_store", "shopping_mall", "spa", "stadium", "store", "subway_station", "supermarket", "synagogue", "taxi_stand", "tourist_attraction", "train_station", "transit_station", "university", "veterinary_care", "zoo"]

    for search_type in search_types:
        search_results = gmaps.places_nearby(
            location=(lat, lon), radius=300, type=search_type)
        restaurant_results['results'].extend(search_results['results'])

    filtered_results = []

    # for place in restaurant_results['results']:
    #     print(place['name'])
    #     print(nm.find_neighborhood(place['geometry']['location']['lat'], place['geometry']['location']['lng'], city))
    #     print()

    if debug:
        print(f"{'/'.join(search_types)} Count:",
            len(restaurant_results['results']))
    # print(restaurant_results)
    # determine if restaurant lat/lon is within the a particular neighborhood polygon, if not, then remove from list
    # Count # of restaurants
    # for place in restaurant_results['results']:
    #     print(place['name'])
    #     print(nm.find_neighborhood(place['geometry']['location']['lat'], place['geometry']['location']['lng'], city))
    #     print()

    #     point = Point(place['geometry']['location']['lng'], place['geometry']['location']['lat'])
    #     for feature in neighborhoods['features']:
    #         polygon = shape(feature['geometry'])
    #         if polygon.contains(point):
    #             filtered_results.append(place)
    #             # break

    return len(restaurant_results['results'])

# with open('../googleMapsApikey.txt') as f:
#     api_key = f.readline()
#     f.close

# print(api_key)
# results = get_gmaps_info(api_key, 40.75834719172825, -73.98543110503996, "nyc", "flask/neighborhoods/nyc.geojson")

def get_feature_by_name(neighborhood_name):
    with open(".//neighborhoods/washingtondc.geojson") as f:
        neighborhoods = json.load(f)
        for feature in neighborhoods['features']:
            if feature.get('properties').get('name') == neighborhood_name:
                return feature

def get_popular_places(neighborhood, query, type, api_key):
    
    feature = get_feature_by_name(neighborhood)
    if feature:
        n_polygon = shape(feature["geometry"])
        n_centroid = n_polygon.centroid
    
    if n_centroid:
        lat = n_centroid.y
        lon = n_centroid.x

        type = config.poi_map[type]

        # query = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?query={query}&location={lat},{lon}&radius=500&key={api_key}"
        query = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?type={type}&location={lat},{lon}&radius=500&key={api_key}"
        print(query)
        search_results = requests.get(query).json()
        search_results = search_results['results']
        print(search_results)
        search_results = [result for result in search_results if result.get('rating')]
        search_results = max(search_results, key=lambda x: x['rating'])

        return search_results

def characterize_city(city, api_key):
    # with open('../googleMapsApikey.txt') as f:
    #     api_key = f.readline()
    #     f.close()

    gmaps = googlemaps.Client(key=api_key)

    place_types_all = ["accounting", "airport", "amusement_park", "aquarium", "art_gallery", "atm", "bakery", "bank", "bar", "beauty_salon", "bicycle_store", "book_store", "bowling_alley", "bus_station", "cafe", "campground", "car_dealer", "car_rental", "car_repair", "car_wash", "casino", "cemetery", "church", "city_hall", "clothing_store", "convenience_store", "courthouse", "dentist", "department_store", "doctor", "drugstore", "electrician", "electronics_store", "embassy", "fire_station", "florist", "funeral_home", "furniture_store", "gas_station", "gym", "hair_care", "hardware_store", "hindu_temple", "home_goods_store", "hospital", "insurance_agency", "jewelry_store", "laundry", "lawyer",
                       "library", "light_rail_station", "liquor_store", "local_government_office", "locksmith", "lodging", "meal_delivery", "meal_takeaway", "mosque", "movie_rental", "movie_theater", "moving_company", "museum", "night_club", "painter", "park", "parking", "pet_store", "pharmacy", "physiotherapist", "plumber", "police", "post_office", "primary_school", "real_estate_agency", "restaurant", "roofing_contractor", "rv_park", "school", "secondary_school", "shoe_store", "shopping_mall", "spa", "stadium", "storage", "store", "subway_station", "supermarket", "synagogue", "taxi_stand", "tourist_attraction", "train_station", "transit_station", "travel_agency", "university", "veterinary_care", "zoo"]
    place_types_limited = ["aquarium", "art_gallery", "bakery", "bar", "beauty_salon", "book_store", "bus_station", "cafe", "casino", "church", "clothing_store", "convenience_store", "department_store", "doctor", "drugstore", "electronics_store", "furniture_store", "gas_station", "gym", "hair_care", "hardware_store", "hindu_temple", "home_goods_store", "jewelry_store", "laundry", "lawyer", "library", "light_rail_station",
                           "liquor_store", "lodging", "meal_delivery", "meal_takeaway", "mosque", "movie_theater", "museum", "night_club", "park", "parking", "pet_store", "pharmacy", "police", "restaurant", "school", "shoe_store", "shopping_mall", "spa", "stadium", "store", "subway_station", "supermarket", "synagogue", "taxi_stand", "tourist_attraction", "train_station", "transit_station", "university", "veterinary_care", "zoo"]

    place_types_testing1 = ["bar", "beauty_salon", "cafe", "gym", "library", "liquor_store", "lodging", "meal_delivery", "meal_takeaway", "movie_theater", "museum", "night_club",
                            "park", "restaurant", "school", "shoe_store", "shopping_mall", "spa", "store", "subway_station", "supermarket", "tourist_attraction", "train_station", "transit_station", "zoo"]
    place_types_testing2 = ["bar", "museum", "night_club", "restaurant",
                            "store", "supermarket", "tourist_attraction", "transit_station"]

    # Open Json
    with open("flask/neighborhoods/"+city+'.geojson') as f:
        neighborhoods = json.load(f)

    n_details = {}

    # loop there every feature
    for feature in neighborhoods['features']:
        n_polygon = shape(feature["geometry"])
        n_centroid = n_polygon.centroid
        n_details['name'] = {
            'name': feature['properties']['name'], "counts": {}}
        print(n_details['name'])
        max_distance = 0

        if isinstance(n_polygon, MultiPolygon):
            n_polygon = n_polygon.geoms[0].buffer(0)
        else:
            n_polygon = n_polygon.buffer(0)

        n_polygon = n_polygon.simplify(
            tolerance=0.0001, preserve_topology=True)

        for point_on_boundary in n_polygon.boundary.coords:
            point = Point(point_on_boundary)
            distance = n_centroid.distance(point)
            if distance > max_distance:
                max_distance = distance

        # use center of polygon as central lat/lon
        lat, lon = n_centroid.y, n_centroid.x

        counts = {}
        for type in place_types_testing2:
            counts[type] = 0

        # results = {'results': []}
        for search_type in place_types_testing2:
            # find places_nearby using maximum distance from center to polgon edge
            search_results = gmaps.places_nearby(
                location=(lat, lon), radius=max_distance, type=search_type)
            # results['results'].extend(search_results['results'])
            counts[search_type] = len(search_results['results'])

        # filter out places not neighborhood (not really needed?)

        n_details['name']['counts'] = counts

    # return dictionary with integer counts of each place_type
    return n_details


# nyc_details = characterize_city("nyc")
# print(nyc_details.keys())


# Google Maps API  AIzaSyAIBH2mzDjd-OGXEi4S50MmVNQw8EFyEnE
# gmaps.configure(api_key="AIzaSyAIBH2mzDjd-OGXEi4S50MmVNQw8EFyEnE")

# new_york_coordinates = (40.75, -74.00)
# gmaps.figure(center=new_york_coordinates, zoom_level=12)

# place_types = ["accounting", "airport", "amusement_park", "aquarium", "art_gallery", "atm", "bakery", "bank", "bar", "beauty_salon", "bicycle_store", "book_store", "bowling_alley", "bus_station", "cafe", "campground", "car_dealer", "car_rental", "car_repair", "car_wash", "casino", "cemetery", "church", "city_hall", "clothing_store", "convenience_store", "courthouse", "dentist", "department_store", "doctor", "drugstore", "electrician", "electronics_store", "embassy", "fire_station", "florist", "funeral_home", "furniture_store", "gas_station", "gym", "hair_care", "hardware_store", "hindu_temple", "home_goods_store", "hospital", "insurance_agency", "jewelry_store", "laundry", "lawyer", "library", "light_rail_station", "liquor_store", "local_government_office", "locksmith", "lodging", "meal_delivery", "meal_takeaway", "mosque", "movie_rental", "movie_theater", "moving_company", "museum", "night_club", "painter", "park", "parking", "pet_store", "pharmacy", "physiotherapist", "plumber", "police", "post_office", "primary_school", "real_estate_agency", "restaurant", "roofing_contractor", "rv_park", "school", "secondary_school", "shoe_store", "shopping_mall", "spa", "stadium", "storage", "store", "subway_station", "supermarket", "synagogue", "taxi_stand", "tourist_attraction", "train_station", "transit_station", "travel_agency", "university", "veterinary_care", "zoo"]

# Place types
# accounting
# airport
# amusement_park
# aquarium
# art_gallery
# atm
# bakery
# bank
# bar
# beauty_salon
# bicycle_store
# book_store
# bowling_alley
# bus_station
# cafe
# campground
# car_dealer
# car_rental
# car_repair
# car_wash
# casino
# cemetery
# church
# city_hall
# clothing_store
# convenience_store
# courthouse
# dentist
# department_store
# doctor
# drugstore
# electrician
# electronics_store
# embassy
# fire_station
# florist
# funeral_home
# furniture_store
# gas_station
# gym
# hair_care
# hardware_store
# hindu_temple
# home_goods_store
# hospital
# insurance_agency
# jewelry_store
# laundry
# lawyer
# library
# light_rail_station
# liquor_store
# local_government_office
# locksmith
# lodging
# meal_delivery
# meal_takeaway
# mosque
# movie_rental
# movie_theater
# moving_company
# museum
# night_club
# painter
# park
# parking
# pet_store
# pharmacy
# physiotherapist
# plumber
# police
# post_office
# primary_school
# real_estate_agency
# restaurant
# roofing_contractor
# rv_park
# school
# secondary_school
# shoe_store
# shopping_mall
# spa
# stadium
# storage
# store
# subway_station
# supermarket
# synagogue
# taxi_stand
# tourist_attraction
# train_station
# transit_station
# travel_agency
# university
# veterinary_care
# zoo
