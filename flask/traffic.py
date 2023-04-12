import googlemaps
import json
import neighborhood_methods as nm
from shapely.geometry import Point, shape, Polygon, MultiPolygon
import sqlalchemy as db
import pandas as pd

username = "postgres"
password = "bobbydodd"

engine = db.create_engine(f"postgresql://{username}:{password}@cse6242-useast1-f-neighborhoodvizandrec-db.chc68arzrzci.us-east-1.rds.amazonaws.com:5432/DC_2021")

def return_trips_between_times(start_time, end_time, city):
    df = pd.read_sql(f"""
            select * from public.{city}
            where "ORIGINDATETIME_TR"::TIME > '{start_time}' and "ORIGINDATETIME_TR"::TIME <= '{end_time}'
        """, engine)

    return df


def return_trips_in_neighbhorhood(all_trips, city, neighbhorhood):
    all_trips.loc[all_trips['DESTINATION_BLOCK_LAT'].isna(),'DESTINATION_BLOCK_LAT'] = 0
    all_trips.loc[all_trips['DESTINATION_BLOCK_LONG'].isna(),'DESTINATION_BLOCK_LONG'] = 0
    all_trips['neighborhood'] = all_trips.apply(lambda row: (nm.find_neighborhood(row['DESTINATION_BLOCK_LAT'], row['DESTINATION_BLOCK_LONG'], city)), axis=1)
    return all_trips.loc[all_trips['neighborhood'] == neighbhorhood, :]


if __name__ == "__main__":
    user_preferences = {
        "city": "washingtondc",
        "neighborhood": "Columbia Heights",
        "start_time": "05:59",
        "end_time": "11:59"
    }

    late_am_dc_trips = return_trips_between_times(user_preferences['start_time'], user_preferences['end_time'], user_preferences['city'])
    late_am_dc_trips_w_neighbhoods = return_trips_in_neighbhorhood(late_am_dc_trips, user_preferences['city'], user_preferences['neighborhood'])

    print(late_am_dc_trips_w_neighbhoods)


