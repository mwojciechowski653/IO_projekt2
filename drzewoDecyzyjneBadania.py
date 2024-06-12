import numpy as np
import matplotlib.pyplot as plt

from funkcjeRobocze import wczytaniePliku, moje_PCA, normalizacja
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import tree

# do tworzenia wykresu

results = []
mean = 0
# for i in range(50):
#     for i in range(1, 13):
#         all_inputs, all_classes = wczytaniePliku()
#         all_inputs = moje_PCA(all_inputs, i)
#         (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7)
# 
#         dtc = tree.DecisionTreeClassifier()
#         dtc.fit(train_inputs, train_classes)
#         # tree.plot_tree(dtc)
#         # plt.show()
#         predictions = dtc.predict(test_inputs)
#         # print(confusion_matrix(test_classes, predictions))
#         # print("Precyzja:")
#         # print(dtc.score(test_inputs, test_classes))
#         # mean += dtc.score(test_inputs, test_classes)
#         try:
#             results[i-1][1] += dtc.score(test_inputs, test_classes)
#         except Exception:
#             results.append([i, dtc.score(test_inputs, test_classes)])
# for i in range(12):
#     results[i][1] = results[i][1] / 50
# 
# x, y = np.array(results).T
# plt.scatter(x, y, label="Liczba kolumn a precyzja")
# plt.title('PCA - drzewo decyzyjne')
# plt.legend()
# plt.xlabel('Liczba kolumn po kompresji')
# plt.ylabel('Precyzja')
# plt.grid(True)
# plt.show()

# do schematu drzewa

# all_inputs, all_classes = wczytaniePliku()
# all_inputs = moje_PCA(all_inputs, 5)
# # all_inputs = normalizacja(all_inputs)
# (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=285779)
#
# dtc = tree.DecisionTreeClassifier()
# dtc.fit(train_inputs, train_classes)
# tree.plot_tree(dtc)
# plt.show()
# predictions = dtc.predict(test_inputs)
# print(confusion_matrix(test_classes, predictions))
# print("Precyzja:")
# print(dtc.score(test_inputs, test_classes))

# Do badania wpływu normalizacji

sum = 0
sumN = 0
for i in range(100):
    all_inputs, all_classes = wczytaniePliku()
    all_inputs = moje_PCA(all_inputs, 5)
    (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7)

    dtc = tree.DecisionTreeClassifier()
    dtc.fit(train_inputs, train_classes)
    predictions = dtc.predict(test_inputs)
    sum += dtc.score(test_inputs, test_classes)

    train_inputs = normalizacja(train_inputs)
    test_inputs = normalizacja(test_inputs)
    dtc = tree.DecisionTreeClassifier()
    dtc.fit(train_inputs, train_classes)
    predictions = dtc.predict(test_inputs)
    sumN += dtc.score(test_inputs, test_classes)
print(sum/100)
print(sumN/100)