import statistics

import pandas as pd
from sklearn.decomposition import PCA


def wczytaniePliku():
    df = pd.read_csv("./rozgrywki.txt")
    # print(df)

    all_inputs = df[['typL', 'liczbaL', 'typS', 'liczbS', 'typP', 'liczbaP', 'typWrogaL', 'liczbaWrogaL', 'typWrogaS',
                     'liczbWrogaS', 'typWrogaP', 'liczbaWrogaP']].values
    all_classes = df['wygrana'].values

    for i in range(len(all_inputs)):
        for j in range(len(all_inputs[i])):
            elem = all_inputs[i][j]
            if elem == "artylerzysci":
                all_inputs[i][j] = 3
            elif elem == "konnica":
                all_inputs[i][j] = 2
            elif elem == "piechurzy":
                all_inputs[i][j] = 1
    return all_inputs, all_classes