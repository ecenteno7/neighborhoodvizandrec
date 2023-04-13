from flask import Flask
from config import *
import traffic

import csv


app = Flask(__name__)


def convert_list_to_csv(list):
    keys = list[0].keys()

    with open('knn_dataset.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list)


@app.route('/refresh-knn-dataset')
def backend():
    user_preferences = {
        "city": "washingtondc",
        "neighborhood": "",
        "start_time": "05:59",
        "end_time": "11:59"
    }

    res = []
    # res = [{'842205': 0, '599969': 94, '546103': 654, '581301': 696, '724101': 969, '594201': 502, '581214': 1875, '799302': 0, '866107': 434, '565101': 684, '541103': 1005, '531102': 752, '581208': 9144, 'neighborhood': 'Columbia Heights'}, {'842205': 0, '599969': 162, '546103': 3681, '581301': 3564, '724101': 1140, '594201': 2483, '581214': 6393, '799302': 0, '866107': 1767, '565101': 10919, '541103': 1338, '531102': 549, '581208': 29458, 'neighborhood': 'Capitol Hill'}, {'842205': 0, '599969': 0, '546103': 0, '581301': 0, '724101': 0, '594201': 0, '581214': 0, '799302': 0, '866107': 0, '565101': 0, '541103': 0, '531102': 0, '581208': 0, 'neighborhood': 'Navy YardFoggy Bottom'}, {'842205': 0, '599969': 1307, '546103': 2144, '581301': 4026, '724101': 1765, '594201': 3246, '581214': 5687, '799302': 0, '866107': 213, '565101': 5045, '541103': 414, '531102': 2560, '581208': 25488, 'neighborhood': 'Dupont Circle'}, {'842205': 0, '599969': 485, '546103': 241, '581301': 1522, '724101': 145, '594201': 301, '581214': 1639, '799302': 0, '866107': 237, '565101': 662, '541103': 315, '531102': 180, '581208': 8224, 'neighborhood': 'U Street Corridor'}, {'842205': 0, '599969': 1535, '546103': 425, '581301': 643, '724101': 550, '594201': 781, '581214': 1666, '799302': 0, '866107': 130, '565101': 8470, '541103': 340, '531102': 285, '581208': 5783, 'neighborhood': 'Georgetown'}, {'842205': 0, '599969': 6, '546103': 0, '581301': 121, '724101': 43, '594201': 6, '581214': 163, '799302': 0, '866107': 47, '565101': 0, '541103': 0, '531102': 64, '581208': 665, 'neighborhood': 'Cleveland Park'}, {'842205': 0, '599969': 151, '546103': 139, '581301': 127, '724101': 216, '594201': 0, '581214': 707, '799302': 0, '866107': 147, '565101': 135, '541103': 307, '531102': 151, '581208': 1314, 'neighborhood': 'Mount Pleasant'}, {'842205': 0, '599969': 28, '546103': 37, '581301': 90, '724101': 195, '594201': 188, '581214': 183, '799302': 0, '866107': 38, '565101': 270, '541103': 205, '531102': 155, '581208': 1453, 'neighborhood': 'Chevy Chase'}]

    for neighborhood in neighborhoods_dc:
        user_preferences['neighborhood'] = neighborhood
        neighborhood_data = traffic.refresh_knn_dataset(user_preferences)
        neighborhood_data['neighborhood'] = neighborhood
        res.append(neighborhood_data)
        print(res)

    convert_list_to_csv(res)

    return {
        'message': 'Dataset refreshed!',
        'body': res
    }

app.run(host='0.0.0.0', port=81)