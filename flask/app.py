from flask import Flask, request, Response
from config import *
import traffic
import pandas as pd
from flask import request
from knn import run_knn

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


@app.route('/get-knn-result', methods=['POST'])
@cross_origin()
def get_knn_result():
    print(request.json['region'])
    user_preferences = {
        "city": "chicago",
        "neighborhood": request.json['region'],
        "start_time": request.json['startTime'],
        "end_time": request.json['endTime']
    }

    res = []

    neighborhood_data = traffic.refresh_knn_dataset(user_preferences)
    res.append(neighborhood_data)
    print(res)

    convert_list_to_csv(res, fn='knn_input.csv')

    res = calculate_knn('knn_input.csv', 'knn_dataset.csv',
                        user_preferences['city'])

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

    return {
        'message': 'Input data received! KNN Calculated',
        'body': neighborhood_res
    }


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

@app.route('/get-pie-chart-data')
def get_pie_chart_data():
    neighborhood = request.args.get('neighborhood')
    df = pd.read_csv('knn_dataset.csv')
    df = df[df.neighborhood == neighborhood]
    df = df.drop(['neighborhood'], axis=1)
    df = df.T
    column = df.columns.values.tolist()[0]
    print(df)
    print(column)
    df = df.sort_values(by=[column], ascending=False)
    df = df.head(5)
    df = df.T
    response = Response(df.to_json())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run(host='0.0.0.0', port=81)
