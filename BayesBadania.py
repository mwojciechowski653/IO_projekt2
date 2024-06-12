import numpy as np

from funkcjeRobocze import wczytaniePliku, moje_PCA, normalizacja
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def Bayes(train_inputs, train_classes, test_inputs, test_classes):
    model = GaussianNB()
    model.fit(train_inputs, train_classes)
    predictions = model.predict(test_inputs)
    # print(confusion_matrix(test_classes, predictions))
    # print(model.score(test_inputs, test_classes))
    return model.score(test_inputs, test_classes)

# Do badania wpływu PCA

# results = []
# for i in range(50):
#     for i in range(1, 13):
#         all_inputs, all_classes = wczytaniePliku()
#         all_inputs = moje_PCA(all_inputs, i)
#         (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7)
# 
#         try:
#             results[i-1][1] += Bayes(train_inputs, train_classes, test_inputs, test_classes)
#         except Exception:
#             results.append([i, Bayes(train_inputs, train_classes, test_inputs, test_classes)])
# for i in range(12):
#     results[i][1] = results[i][1] / 50
# 
# x, y = np.array(results).T
# plt.scatter(x, y, label="Liczba kolumn a precyzja")
# plt.title('PCA - Bayes')
# plt.legend()
# plt.xlabel('Liczba kolumn po kompresji')
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
    sum += Bayes(train_inputs, train_classes, test_inputs, test_classes)

    train_inputs = normalizacja(train_inputs)
    test_inputs = normalizacja(test_inputs)
    sumN += Bayes(train_inputs, train_classes, test_inputs, test_classes)
print(sum/100)
print(sumN/100)
