import json
from shapely.geometry import Point, shape
import csv


def find_neighborhood(lat, lon, city):

    if city in ['nyc', 'atlanta', 'chicago', 'washingtondc']:
        neighborhood = 'NONE FOUND'

        with open("neighborhoods/"+city+'.geojson') as f:
            geojson_data = json.load(f)

        point = Point(lon, lat)  # replace with your actual lat/lon values

        for feature in geojson_data['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                # point is within this feature's geometry
                neighborhood = feature['properties']['name']  # replace with the actual name key in your GeoJSON file
                break  # stop checking other features

        return neighborhood
    
    else:
        return "CITY NOT FOUND"
    
def list_neighborhoods(city):
    with open("flask/neighborhoods/"+city+'.geojson') as f:
        geojson_data = json.load(f)

    neighborhoods_list = []
    for feature in geojson_data['features']:
        name = feature['properties']['name']
        neighborhoods_list.append(name)

    with open("flask/neighborhoods/"+city+'_neighborhood_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Neighborhood'])
        for neighborhood in neighborhoods_list:
            writer.writerow([neighborhood])

    return neighborhoods_list


# print(find_neighborhood(40.69407098028509, -73.99551310312538, 'nyc'))
# print(find_neighborhood(41.708209818630316, -87.62425062144386, 'chicago'))
# print(find_neighborhood(33.73756864954531, -84.42450107648365, 'atlanta'))

# nyc = list_neighborhoods('nyc')
# print(len(nyc))
# print(list_neighborhoods('chicago'))
# print(list_neighborhoods('atlanta'))