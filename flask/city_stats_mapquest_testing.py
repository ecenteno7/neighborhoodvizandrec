# city_stats_mapquest_testing
from city_stats_mapquest_methods import *
from neighborhood_methods import *


with open('../mapquestAPIkey.txt') as f:
        mq_api_key = f.readline()
        f.close()

#list_neighborhoods("washingtondc")

# city_poi_list_mapquest(mq_api_key, "chicago")
# city_poi_list_mapquest(mq_api_key, "washingtondc")


# remove_poi_duplicates("flask/neighborhoods/chicago_places_of_interest.csv")
# remove_poi_duplicates("flask/neighborhoods/washingtondc_places_of_interest.csv")

# id_poi_with_neighborhood("flask/neighborhoods/chicago_places_of_interest.csv", "chicago")
# id_poi_with_neighborhood("flask/neighborhoods/washingtondc_places_of_interest.csv", "washingtondc")

# tally_occurrences("flask/neighborhoods/chicago_poi_with_neighborhood.csv", "chicago")
tally_occurrences("flask/neighborhoods/washingtondc_poi_with_neighborhood.csv", "washingtondc")
