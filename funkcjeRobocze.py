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


def moje_PCA(all_inputs, n):
    pca_battle = PCA(n_components=n).fit(all_inputs)
    # print(pca_battle)
    # print(pca_battle.explained_variance_ratio_)
    # print(pca_battle.components_)
    return pca_battle.transform(all_inputs)


def normalizacja(all_inputs):
    if len(all_inputs[0]) != 5:
        print("Standaryzacja jest przygotowana dla 5 kolumnowych danych")
        return

    x1, x2, x3, x4, x5 = [], [], [], [], []
    x = [x1, x2, x3, x4, x5]
    results = []
    for i in range(5):
        column = x[i]
        for record in all_inputs:
            column.append(record[i])

        sdX = statistics.stdev(column)
        meanX = sum(column) / len(column)

        resultX = []
        for j in range(0, len(column)):
            resultX.append((column[j] - meanX) / sdX)
        results.append(resultX)

    standarizedData = []
    for i in range(len(results[0])):
        standarizedData.append([])
        for j in range(5):
            standarizedData[i].append(results[j][i])

    return standarizedData