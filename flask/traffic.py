import googlemaps
import json
import neighborhood_methods as nm
import maps
from config import *
from shapely.geometry import Point, shape, Polygon, MultiPolygon
import sqlalchemy as db
import pandas as pd

username = "postgres"
password = "bobbydodd"

engine = db.create_engine(
    f"postgresql://{username}:{password}@cse6242-useast1-f-neighborhoodvizandrec-db.chc68arzrzci.us-east-1.rds.amazonaws.com:5432/DC_2021")


def return_trips_between_times(start_time, end_time, city):
    df = pd.read_sql(f"""
            select "DESTINATION_BLOCK_LAT", "DESTINATION_BLOCK_LONG", count(*) as dropoff_count
            from public.{city}
            where "ORIGINDATETIME_TR"::TIME > '{start_time}' and "ORIGINDATETIME_TR"::TIME <= '{end_time}'
            group by "DESTINATION_BLOCK_LAT", "DESTINATION_BLOCK_LONG"
            order by dropoff_count desc
        """, engine)
    return df


def return_trips_in_neighbhorhood(all_trips, city, neighbhorhood):
    all_trips.loc[all_trips['DESTINATION_BLOCK_LAT'].isna(),
                  'DESTINATION_BLOCK_LAT'] = 0
    all_trips.loc[all_trips['DESTINATION_BLOCK_LONG'].isna(),
                  'DESTINATION_BLOCK_LONG'] = 0
    all_trips['neighborhood'] = all_trips.apply(lambda row: (nm.find_neighborhood(
        row['DESTINATION_BLOCK_LAT'], row['DESTINATION_BLOCK_LONG'], city)), axis=1)
    return all_trips.loc[all_trips['neighborhood'] == neighbhorhood, :].head(num_traffic_trips)


def refresh_knn_dataset(user_preferences):
    api_key = "INSERT API KEY HERE"

    late_am_dc_trips = return_trips_between_times(
        user_preferences['start_time'], user_preferences['end_time'], user_preferences['city'])
    late_am_dc_trips_w_neighbhoods = return_trips_in_neighbhorhood(
        late_am_dc_trips, user_preferences['city'], user_preferences['neighborhood'])

    print(late_am_dc_trips_w_neighbhoods)

    entry = {}

    for entry_type in entry_types:
        entry[entry_type] = 0

    count = 0

    for index, row in late_am_dc_trips_w_neighbhoods.iterrows():
        print(
            f'completed {count} of {late_am_dc_trips_w_neighbhoods.shape[0]}')
        if count == 2:
            break
        for entry_type in entry_types:
            print(entry_type)
            entry[entry_type] = entry[entry_type] + maps.get_gmaps_info(
                api_key, row['DESTINATION_BLOCK_LAT'], row['DESTINATION_BLOCK_LONG'], search_types=[entry_type], debug=True) * row['dropoff_count']
        count += 1

    return entry


if __name__ == "__main__":
    refresh_knn_dataset()
