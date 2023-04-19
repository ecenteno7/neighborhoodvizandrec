from flask import Flask, Response
from config import *
import traffic
from flask import request
from knn import run_knn
import threading

import csv

from flask_cors import CORS, cross_origin


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def convert_list_to_csv(list, fn='knn_dataset.csv'):
    keys = list[0].keys()

    with open(fn, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list)

def bgrd_proc(user_preferences):
    res = []

    neighborhood_data = traffic.refresh_knn_dataset(user_preferences)
    res.append(neighborhood_data)
    print(res)

    convert_list_to_csv(res, fn='knn_input.csv')

    return res
    
download_thread = None

@app.route('/get-knn-result', methods=['POST'])
# @cross_origin()
def get_knn_result():
    global download_thread
    print(request.json['region'])
    user_preferences = {
        "city": "chicago",
        "neighborhood": request.json['region'],
        "start_time": request.json['startTime'],
        "end_time": request.json['endTime']
    }

    download_thread = threading.Thread(target=bgrd_proc, name="running_proc", args=(user_preferences, ))
    download_thread.start()

    return {
        'message': 'Input data received! KNN calculating...',
    }


@app.route('/poll-knn-proc', methods=['GET'])
# @cross_origin()
def poll_knn_proc():
    global download_thread
    res = {
        'message': 'KNN still calculating...',
    }

    if not download_thread.is_alive():
        res = calculate_knn('knn_input.csv', 'knn_dataset.csv',
                        'chicago')

        neighborhood_res = {
            "neighborhoods": []
        }

        for neighborhood in res:
            neighborhood_res['neighborhoods'].append({
                'key': neighborhood,
                'description': "Lorem ipsum dolor",
                'pointsOfInterest': [
                    "Ormsby's",
                    "Puttshack",
                    "Fire Maker Brewing Company",
                ],
            })


        res = {
            'message': 'KNN Calculated!',
            'body': neighborhood_res
        }

    return res


def calculate_knn(input_file, knn_data_file, city):
    res = run_knn(input_file, knn_data_file)

    return res


@app.route('/refresh-knn-dataset', methods=['GET'])
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

# context = ('local.crt', 'local.key')
app.run(host='0.0.0.0', port=80)
