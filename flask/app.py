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