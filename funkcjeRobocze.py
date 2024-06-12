import pandas as pd

def wczytaniePlikuDoAlgGen():
    df = pd.read_csv("./rozgrywkiSamWrog.txt")
    # print(df)

    all_inputs = df[['typL', 'liczbaL', 'typS', 'liczbS', 'typP', 'liczbaP']].values

    for i in range(len(all_inputs)):
        for j in range(len(all_inputs[i])):
            elem = all_inputs[i][j]
            if elem == "artylerzysci":
                all_inputs[i][j] = 3
            elif elem == "konnica":
                all_inputs[i][j] = 2
            elif elem == "piechurzy":
                all_inputs[i][j] = 1
    return all_inputs

