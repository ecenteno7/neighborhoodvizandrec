import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

def run_knn(input_neighborhood = 'input.csv', filename = 'knn_data.csv'):
    data = pd.read_csv(filename)
    input_neighborhood = pd.read_csv(input_neighborhood)
    y = data.iloc[:, -1:]
    x = data.iloc[:, :-1]
    min_max_scaler = preprocessing.MinMaxScaler()
    combined_for_normalization = pd.concat([input_neighborhood, x], ignore_index = True, sort = False)

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(x, y)
    knn_indices = knn.kneighbors(input_neighborhood, return_distance = False)[0]
    return_list = []
    for i in knn_indices:
        return_list.append(y.values[i][0])
    return return_list

print(run_knn(input_neighborhood='input_data.csv', filename='knn_dataset.csv'))