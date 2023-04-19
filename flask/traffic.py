import googlemaps
import json
import neighborhood_methods as nm
import maps
from config import *
from shapely.geometry import Point, shape, Polygon, MultiPolygon
import sqlalchemy as db
import pandas as pd
import requests
import csv

username = "postgres"
password = "bobbydodd"

engine = db.create_engine(f"postgresql://{username}:{password}@localhost:5432/traffic")


def return_trips_between_times(start_time, end_time, city):
    if city == 'washingtondc':
        df = pd.read_sql(f"""
            select "DESTINATION_BLOCK_LAT", "DESTINATION_BLOCK_LONG", count(*) as dropoff_count
            from public.{city}
            where "DESTINATIONDATETIME_TR"::TIME > '{start_time}' and "DESTINATIONDATETIME_TR"::TIME <= '{end_time}'
            group by "DESTINATION_BLOCK_LAT", "DESTINATION_BLOCK_LONG"
            order by dropoff_count desc
        """, engine)
    else:
        df = pd.read_sql(f"""
                select "dropoff_latitude", "dropoff_longitude", count(*) as dropoff_count
                from public.{city}
                where "end_timestamp"::TIME > '{start_time}' and "end_timestamp"::TIME <= '{end_time}'
                group by "dropoff_latitude", "dropoff_longitude"
                order by dropoff_count desc
            """, engine)
    return df


def return_trips_in_neighbhorhood(all_trips, city, neighbhorhood):
    if city == 'washingtondc':
        all_trips.loc[all_trips['DESTINATION_BLOCK_LAT'].isna(),
                    'DESTINATION_BLOCK_LAT'] = 0
        all_trips.loc[all_trips['DESTINATION_BLOCK_LONG'].isna(),
                    'DESTINATION_BLOCK_LONG'] = 0
        all_trips['neighborhood'] = all_trips.apply(lambda row: (nm.find_neighborhood(
            row['DESTINATION_BLOCK_LAT'], row['DESTINATION_BLOCK_LONG'], city)), axis=1)
    else:
        all_trips.loc[all_trips['dropoff_latitude'].isna(),
                    'dropoff_latitude'] = 0
        all_trips.loc[all_trips['dropoff_longitude'].isna(),
                    'dropoff_longitude'] = 0
        all_trips['neighborhood'] = all_trips.apply(lambda row: (nm.find_neighborhood(
            row['dropoff_latitude'], row['dropoff_longitude'], city)), axis=1)
    return all_trips.loc[all_trips['neighborhood'] == neighbhorhood, :].head(num_traffic_trips)


def refresh_knn_dataset(user_preferences):
    api_key = api_key_mq

    print(f"processing user preferences: {user_preferences}")

    late_am_dc_trips = return_trips_between_times(
        user_preferences['start_time'], user_preferences['end_time'], user_preferences['city'])
    late_am_dc_trips_w_neighbhoods = return_trips_in_neighbhorhood(
        late_am_dc_trips, user_preferences['city'], user_preferences['neighborhood'])

    # print(late_am_dc_trips_w_neighbhoods)

    entry = {}

    for category in poi_categories:
        entry[str(category)] = 0

    count = 0

    for index, row in late_am_dc_trips_w_neighbhoods.iterrows():
        # print(
        #     f'completed {count} of {late_am_dc_trips_w_neighbhoods.shape[0]}')
        if count == restrict_traffic_trips:
            break

        if user_preferences['city'] == 'washingtondc':
            center_point = "{},{}".format(row['DESTINATION_BLOCK_LAT'], row['DESTINATION_BLOCK_LONG'])
        else:
            center_point = "{},{}".format(row['dropoff_latitude'], row['dropoff_longitude'])
        
        poi_df = tag_poi_in_at_location_mapquest(api_key_mq, center_point)

        if poi_df is None:
            continue
        
        for idx, poi in poi_df.iterrows():
            # print(poi['group_sic_code_name_ext'], poi['group_sic_code'])
            if poi['group_sic_code_name_ext'] != '' and poi['group_sic_code_name_ext'] in poi_categories:
                # print(row['dropoff_count'])
                entry[poi['group_sic_code_name_ext']] = entry[poi['group_sic_code_name_ext']] + row['dropoff_count']
            
            # Using Google Maps Places API
            # entry[entry_type] = entry[entry_type] + maps.get_gmaps_info(
            #     api_key, row['DESTINATION_BLOCK_LAT'], row['DESTINATION_BLOCK_LONG'], search_types=[entry_type], debug=True) * row['dropoff_count']
        
        count += 1

    # print(entry)

    return entry


def test_chicago():
    # api_key = api_key_mq

    # user_preferences = {
    #     "city": "chicago",
    #     "neighborhood": "Wicker Park",
    #     "start_time": "05:59",
    #     "end_time": "11:59"
    # }

    # late_am_chi_trips = return_trips_between_times(
    #     user_preferences['start_time'], user_preferences['end_time'], user_preferences['city'])
    # late_am_chi_trips_w_neighbhoods = return_trips_in_neighbhorhood(
    #     late_am_chi_trips, user_preferences['city'], user_preferences['neighborhood'])

    # entry = {}

    # for category in poi_categories:
    #     entry[str(category)] = 0

    # count = 0

    # for index, row in late_am_chi_trips_w_neighbhoods.iterrows():
    #     print(
    #         f'completed {count} of {late_am_chi_trips_w_neighbhoods.shape[0]}')
    #     if count == restrict_traffic_trips:
    #         break
    #     center_point = "{},{}".format(row['dropoff_latitude'], row['dropoff_longitude'])
    #     poi_df = tag_poi_in_at_location_mapquest(api_key_mq, center_point)

    #     if poi_df is None:
    #         continue
        
    #     for idx, poi in poi_df.iterrows():
    #         print(poi['group_sic_code_name_ext'], poi['group_sic_code'])
    #         if poi['group_sic_code_name_ext'] != '' and poi['group_sic_code_name_ext'] in poi_categories:
    #             print(row['dropoff_count'])
    #             entry[poi['group_sic_code_name_ext']] = entry[poi['group_sic_code_name_ext']] + row['dropoff_count']
            
    #         # Using Google Maps Places API
    #         # entry[entry_type] = entry[entry_type] + maps.get_gmaps_info(
    #         #     api_key, row['DESTINATION_BLOCK_LAT'], row['DESTINATION_BLOCK_LONG'], search_types=[entry_type], debug=True) * row['dropoff_count']
        
    #     count += 1

    # print(entry)

    entry = {'Wineries': 0, 'Transportation Services': 22, 'Taxis': 442, 'Food Markets': 897, 'Convenience Stores': 2003, 'Grocery Stores': 1406, 'Grocers Health Foods': 0, 'Seafood Markets': 0, 'Farm Markets': 0, 'Bakers Cake & Pie': 1527, 'Doughnuts': 0, 'Miscellaneous Food Stores': 0, 'Electric Charging Station': 0, "Children's Clothing": 955, 'Clothing Retail': 8083, 'Rubber & Plastic Footwear Retail': 1649, 'Sportswear': 230, 'Ice Cream Parlors': 201, 'Foods Carry Out': 0, 'All) Restaurants': 0, 'Delicatessens': 115, 'Cafeterias': 0, 'Cafes': 1328, 'Appetizers & Snacks Etc': 0, 'Subs & Sandwiches': 115, 'Theatres Dinner': 0, 'Coffee Shops': 316, 'Tea Rooms': 0, 'Juice Bars': 115, 'Restaurants Cyber Cafes': 0, 'Bars': 1938, 'Discotheques': 0, 'Cocktail Lounges': 3033, 'Pubs': 0, 'Comedy Clubs': 0, 'Karaoke Clubs': 0, 'Pharmacies': 2886, 'Wines Retail': 552, 'Flea Markets': 0, 'Book Stores': 418, 'Toy Stores': 223, 'Gift Shops': 37, 'Art Galleries & Dealers': 1264, 'Monuments': 0, 'Shopping Centers & Malls': 0, 'Hotels & Motels': 1151, 'Cottages & Cabins': 0, 'Bed & Breakfasts': 0, 'Chalet & Cabin Rentals': 0, 'Skiing Centers & Resorts': 115, 'Resorts': 0, 'Villas': 0, 'Hostels': 0, 'Adventure Games & Activities': 0, 'Campgrounds': 0, 'Manicurists': 468, 'Barbers': 1272, 'Movie Theatres': 0, 'Movie Theatres (drive-Ins)': 0, 'Theatres Live': 731, 'Concert Venues': 0, 'Entertainment Bureaus': 0, 'Bowling Centers': 0, 'Stadiums Arenas & Athletic Fields': 0, 'Race Tracks': 0, 'Horse Racing': 0, 'Health Clubs & Gyms': 3437, 'Golf Courses-Public Or Private': 0, 'Casinos': 0, 'Arcades': 1151, 'Amusement Places': 0, 'Water Parks': 0, 'Amusement Parks': 0, 'Recreation Centers': 0, 'Hockey Clubs': 0, 'Flying Clubs': 0, 'Beach & Cabana Clubs': 0, 'Sports Recreational': 0, 'Skating Rinks': 0, 'Bicycles Renting': 0, 'Baths Bath Houses Spas & Saunas': 0, 'Billiard Parlors': 0, 'Fairgrounds': 0, 'Historical Places': 0, 'Parks': 1411, 'Picnic Grounds': 0, 'Horseback Riding': 0, 'Swimming Pools Public': 0, 'Tennis Courts Public': 0, 'Squash Courts Public': 0, 'Colleges & Universities': 0, 'Hiking Backpacking & Mountaineering Service': 0, 'Museums': 2582, 'Planetariums': 0, 'Cultural Centres': 0, 'National Monuments': 0, 'Zoos': 0, 'Arboretums': 0, 'Aquariums Public': 0, 'Motoring Organisations': 0, 'Clubs': 0, 'Community Organizations': 84, 'All) Places Of Worship': 0, 'Dance Clubs': 0, 'Beach': 0, 'Cave': 0, 'Forest': 0, 'Ridge': 0, 'Valley': 0, 'Bay': 0, 'Rapids': 0, 'Reservoir': 0, 'Swamp': 0, 'Bridge': 0, 'Building': 0, 'Dam': 0, 'Tower': 0, 'Tourist Attra': 0}

    keys = entry.keys()

    with open('chi_input.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerow(entry)


def tag_poi_in_at_location_mapquest(api, location):
    url = "http://www.mapquestapi.com/search/v2/radius"

    radius = 0.300

    params = {
        "key": api,
        "origin": location,
        "radius": radius,
        "units": "k",
        "ambiguities": "ignore",
        "outFormat": "json",
        "maxMatches": "1000"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        records = []
        try: 
            for result in response.json()['searchResults']:
                records.append(result['fields'])
            # print(pd.DataFrame(records))
            res = pd.DataFrame(records)
            # print(res[['group_sic_code_name_ext', 'name']])
            return res
        except Exception as e:
            print(e)
            return None
    else:
        print("Error:", response.status_code, response.text)
        return None




if __name__ == "__main__":
    # refresh_knn_dataset(user_preferences = {
    #     "city": "washingtondc",
    #     "neighborhood": "Columbia Heights",
    #     "start_time": "05:59",
    #     "end_time": "11:59"
    # })
    test_chicago()
