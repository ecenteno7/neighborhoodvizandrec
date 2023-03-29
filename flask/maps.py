import os
import googlemaps
import json
import neighborhood_methods as nm


def get_gmaps_info(lat, lon, city, neighborhoods_file):
    gmaps = googlemaps.Client(key="AIzaSyAIBH2mzDjd-OGXEi4S50MmVNQw8EFyEnE")
    center_coords = (lat, lon)
    
    with open(neighborhoods_file) as f:
        neighborhoods = json.load(f)
    
    # n_polygons = neighborhoods['coordinates']

    search_types = ["restaurant", "cafe", "meal_delivery", "meal_takeaway"]
    restaurant_results = {'results': []}

    for search_type in search_types:
        search_results = gmaps.places_nearby(location=(lat, lon), radius=5000, type=search_type)
        restaurant_results['results'].extend(search_results['results'])

    for place in restaurant_results['results']:
        print(place['name'])
        print(nm.find_neighborhood(place['geometry']['location']['lat'], place['geometry']['location']['lng'], city))
        print()
    
    print("Restaurant/Cafe/Takeaway/Delivery Count:", len(restaurant_results['results']))
    #determine if restaurant lat/lon is within the a particular neighborhood polygon, if not, then remove from list
    #Count # of restaurants

    return restaurant_results

    

results = get_gmaps_info(40.75834719172825, -73.98543110503996, "nyc", "flask/neighborhoods/nyc.geojson")



#Google Maps API  AIzaSyAIBH2mzDjd-OGXEi4S50MmVNQw8EFyEnE
# gmaps.configure(api_key="AIzaSyAIBH2mzDjd-OGXEi4S50MmVNQw8EFyEnE")

# new_york_coordinates = (40.75, -74.00)
# gmaps.figure(center=new_york_coordinates, zoom_level=12)

place_types = ["accounting", "airport", "amusement_park", "aquarium", "art_gallery", "atm", "bakery", "bank", "bar", "beauty_salon", "bicycle_store", "book_store", "bowling_alley", "bus_station", "cafe", "campground", "car_dealer", "car_rental", "car_repair", "car_wash", "casino", "cemetery", "church", "city_hall", "clothing_store", "convenience_store", "courthouse", "dentist", "department_store", "doctor", "drugstore", "electrician", "electronics_store", "embassy", "fire_station", "florist", "funeral_home", "furniture_store", "gas_station", "gym", "hair_care", "hardware_store", "hindu_temple", "home_goods_store", "hospital", "insurance_agency", "jewelry_store", "laundry", "lawyer", "library", "light_rail_station", "liquor_store", "local_government_office", "locksmith", "lodging", "meal_delivery", "meal_takeaway", "mosque", "movie_rental", "movie_theater", "moving_company", "museum", "night_club", "painter", "park", "parking", "pet_store", "pharmacy", "physiotherapist", "plumber", "police", "post_office", "primary_school", "real_estate_agency", "restaurant", "roofing_contractor", "rv_park", "school", "secondary_school", "shoe_store", "shopping_mall", "spa", "stadium", "storage", "store", "subway_station", "supermarket", "synagogue", "taxi_stand", "tourist_attraction", "train_station", "transit_station", "travel_agency", "university", "veterinary_care", "zoo"]

#Place types
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