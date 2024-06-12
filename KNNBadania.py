import numpy as np
import matplotlib.pyplot as plt

from funkcjeRobocze import wczytaniePliku, moje_PCA, normalizacja
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsRegressor


def KNN(n, train_inputs, train_classes, test_inputs, test_classes):
    regressor = KNeighborsRegressor(n_neighbors=n)
    regressor.fit(train_inputs, train_classes)

    predictions = regressor.predict(test_inputs)
    # print(predictions)

    def round_predictions(dataSet):
        for i in range(len(dataSet)):
            dataSet[i] = round(dataSet[i], 0)

    round_predictions(predictions)
    # print(predictions)
    # print(confusion_matrix(test_classes, predictions))
    # print("Precyzja:")
    # print(accuracy_score(test_classes, predictions))
    return accuracy_score(test_classes, predictions)

# Do badania wpływu PCA

# results = []
# for i in range(50):
#     for i in range(1, 13):
#         all_inputs, all_classes = wczytaniePliku()
#         all_inputs = moje_PCA(all_inputs, i)
#         (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7)
# 
#         try:
#             results[i-1][1] += KNN(5, train_inputs, train_classes, test_inputs, test_classes)
#         except Exception:
#             results.append([i, KNN(5, train_inputs, train_classes, test_inputs, test_classes)])
# for i in range(12):
#     results[i][1] = results[i][1] / 50
# 
# x, y = np.array(results).T
# plt.scatter(x, y, label="Liczba kolumn a precyzja")
# plt.title('PCA - KNN')
# plt.legend()
# plt.xlabel('Liczba kolumn po kompresji')
# plt.ylabel('Precyzja')
# plt.grid(True)
# plt.show()


# Do badania jaka ilosc najblizszych sasiadow jest najlepsza

# results = []
# for i in range(1, 101, 2):
#     mean = 0
#     for j in range(50):
#         all_inputs, all_classes = wczytaniePliku()
#         all_inputs = moje_PCA(all_inputs, 5)
#         (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7)
# 
#         mean += KNN(i, train_inputs, train_classes, test_inputs, test_classes)
# 
#     results.append([i, mean/50])
# 
# x, y = np.array(results).T
# plt.scatter(x, y, label="K najblizszych sasiadow a precyzja")
# plt.title('KNN - ustalenie K a srednia precyzja')
# plt.legend()
# plt.xlabel('K')
# plt.ylabel('Precyzja')
# plt.grid(True)
# plt.show()


# Do badania wpływu standaryzacji

sum = 0
sumN = 0
for i in range(100):
    all_inputs, all_classes = wczytaniePliku()
    all_inputs = moje_PCA(all_inputs, 5)
    (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7)
    sum += KNN(35, train_inputs, train_classes, test_inputs, test_classes)

    train_inputs = normalizacja(train_inputs)
    test_inputs = normalizacja(test_inputs)
    sumN += KNN(35, train_inputs, train_classes, test_inputs, test_classes)
print(sum/100)
print(sumN/100)
