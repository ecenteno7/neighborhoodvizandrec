api_key_mq = "hn3cnNt2TJoLZTi2yNUY3oxe2LK0pE0w"

neighborhoods_dc = [
    "Takoma Park",
    "Catholic University-Brookland",
    "Anacostia",
    "Shaw",
    "Stadium-Armory",
    "Logan Circle",
    "Ledroit Park",
    "Chevy Chase",
    "Barnaby Woods",
    "Capitol Hill",
    "Friendship Heights",
    "Au-Tenleytown",
    "The Palisades",
    "Cleveland Park",
    "Downtown",
    "Columbia Heights",
    "Fort Totten-Upper Northeast",
    "Deanwood",
    "Adams Morgan",
    "Petworth",
    "Foxhall Village",
    "Glover Park",
    "Kalorama",
    "Brentwood",
    "Mount Vernon Square",
    "Woodley Park",
    "Georgetown",
    "Foggy Bottom",
    "Berkley",
    "Mount Pleasant",
    "U Street Corridor",
    "South West",
    "Brightwood",
    "Dupont Circle"
]

num_traffic_trips = 2000
restrict_traffic_trips = 10000000000000

poi_categories = [
    "Wineries",
    "Transportation Services",
    "Taxis",
    "Food Markets",
    "Convenience Stores",
    "Grocery Stores",
    "Grocers Health Foods",
    "Seafood Markets",
    "Farm Markets",
    "Bakers Cake & Pie",
    "Doughnuts",
    "Miscellaneous Food Stores",
    "Electric Charging Station",
    "Children's Clothing",
    "Clothing Retail",
    "Sportswear",
    "Ice Cream Parlors",
    "Foods Carry Out",
    "(All) Restaurants",
    "Delicatessens",
    "Cafeterias",
    "Cafes",
    "Appetizers & Snacks Etc",
    "Subs & Sandwiches",
    "Theatres Dinner",
    "Coffee Shops",
    "Tea Rooms",
    "Juice Bars",
    "Restaurants Cyber Cafes",
    "Bars",
    "Discotheques",
    "Cocktail Lounges",
    "Pubs",
    "Comedy Clubs",
    "Karaoke Clubs",
    "Pharmacies",
    "Wines Retail",
    "Flea Markets",
    "Book Stores",
    "Toy Stores",
    "Gift Shops",
    "Art Galleries & Dealers",
    "Monuments",
    "Shopping Centers & Malls",
    "Hotels & Motels",
    "Cottages & Cabins",
    "Bed & Breakfasts",
    "Chalet & Cabin Rentals",
    "Skiing Centers & Resorts",
    "Resorts",
    "Villas",
    "Hostels",
    "Adventure Games & Activities",
    "Campgrounds",
    "Manicurists",
    "Barbers",
    "Movie Theatres",
    "Movie Theatres (drive-Ins)",
    "Theatres Live",
    "Concert Venues",
    "Entertainment Bureaus",
    "Bowling Centers",
    "Stadiums Arenas & Athletic Fields",
    "Race Tracks",
    "Horse Racing",
    "Health Clubs & Gyms",
    "Golf Courses-Public Or Private",
    "Casinos",
    "Arcades",
    "Amusement Places",
    "Water Parks",
    "Amusement Parks",
    "Recreation Centers",
    "Hockey Clubs",
    "Flying Clubs",
    "Beach & Cabana Clubs",
    "Sports Recreational",
    "Skating Rinks",
    "Bicycles Renting",
    "Baths Bath Houses Spas & Saunas",
    "Billiard Parlors",
    "Fairgrounds",
    "Historical Places",
    "Parks",
    "Picnic Grounds",
    "Horseback Riding",
    "Swimming Pools Public",
    "Tennis Courts Public",
    "Squash Courts Public",
    "Colleges & Universities",
    "Hiking Backpacking & Mountaineering Service",
    "Museums",
    "Planetariums",
    "Cultural Centres",
    "National Monuments",
    "Zoos",
    "Arboretums",
    "Aquariums Public",
    "Motoring Organisations",
    "Clubs",
    "Community Organizations",
    "(All) Places Of Worship",
    "Dance Clubs",
    "Beach",
    "Cave",
    "Forest",
    "Ridge",
    "Valley",
    "Bay",
    "Rapids",
    "Reservoir",
    "Swamp",
    "Bridge",
    "Building",
    "Dam",
    "Tower",
    "Tourist Attractions"
]

# categories = [
#     "bar", "book_store", "cafe", "casino", "clothing_store", "convenience_store", "movie_theater", "museum", "night_club", "park", "restaurant", "shopping_mall", "spa", "stadium", "store", "supermarket", "tourist_attraction", "university"
# ]
#
# ]

categories = [

]

google_pois = [
    "accounting",
    "airport",
    "amusement_park",
    "aquarium",
    "art_gallery",
    "atm",
    "bakery",
    "bank",
    "bar",
    "beauty_salon",
    "bicycle_store",
    "book_store",
    "bowling_alley",
    "bus_station",
    "cafe",
    "campground",
    "car_dealer",
    "car_rental",
    "car_repair",
    "car_wash",
    "casino",
    "cemetery",
    "church",
    "city_hall",
    "clothing_store",
    "convenience_store",
    "courthouse",
    "dentist",
    "department_store",
    "doctor",
    "drugstore",
    "electrician",
    "electronics_store",
    "embassy",
    "fire_station",
    "florist",
    "funeral_home",
    "furniture_store",
    "gas_station",
    "gym",
    "hair_care",
    "hardware_store",
    "hindu_temple",
    "home_goods_store",
    "hospital",
    "insurance_agency",
    "jewelry_store",
    "laundry",
    "lawyer",
    "library",
    "light_rail_station",
    "liquor_store",
    "local_government_office",
    "locksmith",
    "lodging",
    "meal_delivery",
    "meal_takeaway",
    "mosque",
    "movie_rental",
    "movie_theater",
    "moving_company",
    "museum",
    "night_club",
    "painter",
    "park",
    "parking",
    "pet_store",
    "pharmacy",
    "physiotherapist",
    "plumber",
    "police",
    "post_office",
    "primary_school",
    "real_estate_agency",
    "restaurant",
    "roofing_contractor",
    "rv_park",
    "school",
    "secondary_school",
    "shoe_store",
    "shopping_mall",
    "spa",
    "stadium",
    "storage",
    "store",
    "subway_station",
    "supermarket",
    "synagogue",
    "taxi_stand",
    "tourist_attraction",
    "train_station",
    "transit_station",
    "travel_agency",
    "university",
    "veterinary_care",
    "zoo",
]

# map from poi_categories to google_pois
poi_map = {
    "Wineries": "liquor_store",
    "Transportation Services": "light_rail_station",
    "Taxis": "taxi_stand",
    "Food Markets": "supermarket",
    "Convenience Stores": "convenience_store",
    "Grocery Stores": "supermarket",
    "Grocers Health Foods": "supermarket",
    "Seafood Markets": "supermarket",
    "Farm Markets": "supermarket",
    "Bakers Cake & Pie": "bakery",
    "Doughnuts": "bakery",
    "Miscellaneous Food Stores": "supermarket",
    "Electric Charging Station": "parking",
    "Children's Clothing": "clothing_store",
    "Clothing Retail": "clothing_store",
    "Sportswear": "clothing_store",
    "Ice Cream Parlors": "restaurant",
    "Foods Carry Out": "restaurant",
    "(All) Restaurants": "restaurant",
    "Delicatessens": "restaurant",
    "Cafeterias": "restaurant",
    "Cafes": "cafe",
    "Appetizers & Snacks Etc": "restaurant",
    "Subs & Sandwiches": "restaurant",
    "Theatres Dinner": "restaurant",
    "Coffee Shops": "cafe",
    "Tea Rooms": "cafe",
    "Juice Bars": "cafe",
    "Restaurants Cyber Cafes": "restaurant",
    "Bars": "bar",
    "Discotheques": "night_club",
    "Cocktail Lounges": "bar",
    "Pubs": "bar",
    "Comedy Clubs": "night_club",
    "Karaoke Clubs": "night_club",
    "Pharmacies": "pharmacy",
    "Wines Retail": "liquor_store",
    "Flea Markets": "supermarket",
    "Book Stores": "book_store",
    "Toy Stores": "store",
    "Gift Shops": "store",
    "Art Galleries & Dealers": "art_gallery",
    "Monuments": "tourist_attraction",
    "Shopping Centers & Malls": "shopping_mall",
    "Hotels & Motels": "lodging",
    "Cottages & Cabins": "lodging",
    "Bed & Breakfasts": "lodging",
    "Chalet & Cabin Rentals": "lodging",
    "Skiing Centers & Resorts": "lodging",
    "Resorts": "lodging",
    "Villas": "lodging",
    "Hostels": "lodging",
    "Adventure Games & Activities": "tourist_attraction",
    "Campgrounds": "campground",
    "Manicurists": "beauty_salon",
    "Barbers": "beauty_salon",
    "Movie Theatres": "movie_theater",
    "Movie Theatres (drive-Ins)": "movie_theater",
    "Theatres Live": "movie_theater",
    "Concert Venues": "movie_theater",
    "Entertainment Bureaus": "movie_theater",
    "Bowling Centers": "bowling_alley",
    "Stadiums Arenas & Athletic Fields": "stadium",
    "Race Tracks": "stadium",
    "Horse Racing": "stadium",
    "Health Clubs & Gyms": "gym",
    "Golf Courses-Public Or Private": "golf_course",
    "Casinos": "casino",
    "Arcades": "amusement_park",
    "Amusement Places": "amusement_park",
    "Water Parks": "amusement_park",
    "Amusement Parks": "amusement_park",
    "Recreation Centers": "amusement_park",
    "Hockey Clubs": "amusement_park",
    "Flying Clubs": "amusement_park",
    "Beach & Cabana Clubs": "amusement_park",
    "Sports Recreational": "amusement_park",
    "Skating Rinks": "amusement_park",
    "Bicycles Renting": "transit_station",
    "Baths Bath Houses Spas & Saunas": "spa",
    "Billiard Parlors": "amusement_park",
    "Fairgrounds": "amusement_park",
    "Historical Places": "tourist_attraction",
    "Parks": "park",
    "Picnic Grounds": "park",
    "Horseback Riding": "tourist_attraction",
    "Swimming Pools Public": "tourist_attraction",
    "Tennis Courts Public": "tourist_attraction",
    "Squash Courts Public": "tourist_attraction",
    "Colleges & Universities": "university",
    "Hiking Backpacking & Mountaineering Service": "tourist_attraction",
    "Museums": "museum",
    "Planetariums": "museum",
    "Cultural Centres": "museum",
    "National Monuments": "museum",
    "Zoos": "zoo",
    "Arboretums": "park",
    "Aquariums Public": "aquarium",
    "Motoring Organisations": "tourist_attraction",
    "Clubs": "night_club",
    "Community Organizations": "tourist_attraction",
    "(All) Places Of Worship": "church",
    "Dance Clubs": "night_club",
    "Beach": "park",
    "Cave": "park",
    "Forest": "park",
    "Ridge": "park",
    "Valley": "park",
    "Bay": "park",
    "Rapids": "park",
    "Reservoir": "park",
    "Swamp": "park",
    "Bridge": "park",
    "Building": "park",
    "Dam": "park",
    "Tower": "park",
    "Tourist Attractions": "tourist_attraction",
}

