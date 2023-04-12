import json
from shapely.geometry import shape
import csv

city = "chicago"
# Load the GeoJSON file into a dictionary
with open("flask/neighborhoods/"+city+'.geojson', 'r') as f:
    data = json.load(f)

# Initialize a list to store the bounding box coordinates
bbox_list = []
n_list = []
# Iterate over all features in the GeoJSON file
for feature in data['features']:
    n_list.append(feature['properties']['name'])
    
    # Extract the coordinates of the feature's geometry
    coords = feature['geometry']['coordinates']
    
    # Create a shapely object from the geometry coordinates
    geometry = shape(feature['geometry'])
    
    # Determine the bounding box of the geometry
    bounds = geometry.bounds
    
    # Add the bounding box coordinates to the list
    bbox_list.append(bounds)
    
    # Print the bounding box coordinates to the screen
    print(feature['properties']['name'], bounds)
    
# Write the bounding box coordinates to a CSV file
with open("flask/neighborhoods/"+city+'_bboxes.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Neighborhood', 'MinLon', 'MinLat', 'MaxLon', 'MaxLat'])
    for i, bbox in enumerate(bbox_list):
        writer.writerow([n_list[i], bbox[0], bbox[1], bbox[2], bbox[3]])
