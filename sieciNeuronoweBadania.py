import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier

from funkcjeRobocze import wczytaniePliku, moje_PCA, normalizacja
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder


# def neuronNetwork(hidden_layers):
#     mlp = MLPClassifier(hidden_layer_sizes=hidden_layers, max_iter=1_000_000, random_state=1, alpha=1e-5)
#     mlp.fit(train_data, train_labels)
# 
#     predictions_train = mlp.predict(train_data)
#     predictions_test = mlp.predict(test_data)
#     # print(accuracy_score(predictions_test, test_labels))
#     # print(confusion_matrix(test_labels, predictions_test))
#     return accuracy_score(predictions_test, test_labels)


# Wykres dla PCA

# results = []
# for j in range(10):
#     for i in range(1, 13):
#         all_inputs, all_classes = wczytaniePliku()
#         all_inputs = moje_PCA(all_inputs, i)
#         (train_data, test_data, train_labels, test_labels) = train_test_split(all_inputs, all_classes, train_size=0.7)
# 
#         train_labels, test_labels = list(train_labels), list(test_labels)
#         try:
#             results[i-1][1] += neuronNetwork([64, 64])
#         except Exception:
#             results.append([i, neuronNetwork([64, 64])])
# for i in range(12):
#     results[i][1] = results[i][1] / 10
# 
# x, y = np.array(results).T
# plt.scatter(x, y, label="Liczba kolumn a precyzja")
# plt.title('PCA - Sieci Neuronowe')
# plt.legend()
# plt.xlabel('Liczba kolumn po kompresji')
# plt.ylabel('Precyzja')
# plt.grid(True)
# plt.show()


# Do badania wpływu standaryzacji

# sum = 0
# sumN = 0
# for i in range(10):
#     all_inputs, all_classes = wczytaniePliku()
#     all_inputs = moje_PCA(all_inputs, 5)
#     (train_data, test_data, train_labels, test_labels) = train_test_split(all_inputs, all_classes, train_size=0.7)
#     train_labels, test_labels = list(train_labels), list(test_labels)
#     sum += neuronNetwork([64, 64])
# 
#     train_data = normalizacja(train_data)
#     test_data = normalizacja(test_data)
#     sumN += neuronNetwork([64, 64])
# print(sum/10)
# print(sumN/10)


# Badania batch size
# 
# def neuronNetworkZBatchSize(hidden_layers, batch):
#     mlp = MLPClassifier(hidden_layer_sizes=hidden_layers, max_iter=10_000, random_state=1, alpha=1e-5, batch_size=batch)
#     mlp.fit(train_data, train_labels)
# 
#     predictions_train = mlp.predict(train_data)
#     predictions_test = mlp.predict(test_data)
#     # print(accuracy_score(predictions_test, test_labels))
#     # print(confusion_matrix(test_labels, predictions_test))
#     return accuracy_score(predictions_test, test_labels)
# 
# 
# results = []
# for j in range(10):
#     for i in range(4, 68, 4):
#         all_inputs, all_classes = wczytaniePliku()
#         all_inputs = moje_PCA(all_inputs, 5)
#         (train_data, test_data, train_labels, test_labels) = train_test_split(all_inputs, all_classes, train_size=0.7)
# 
#         train_labels, test_labels = list(train_labels), list(test_labels)
#         try:
#             results[(i-4)//4][1] += neuronNetworkZBatchSize([64, 64], i)
#         except Exception:
#             results.append([i, neuronNetworkZBatchSize([64, 64], i)])
# for i in range(16):
#     results[i][1] = results[i][1] / 1
# 
# x, y = np.array(results).T
# plt.scatter(x, y, label="Batch size a precyzja")
# plt.title('Sieci neuronowe - wplyw batch size')
# plt.legend()
# plt.xlabel('Batch size')
# plt.ylabel('Precyzja')
# plt.grid(True)
# plt.show()


# Badanie learning rate

# def neuronNetworkZLearningRate(hidden_layers, lr):
#     mlp = MLPClassifier(hidden_layer_sizes=hidden_layers, max_iter=10_000, random_state=1, alpha=1e-5, learning_rate_init=lr)
#     mlp.fit(train_data, train_labels)
# 
#     predictions_train = mlp.predict(train_data)
#     predictions_test = mlp.predict(test_data)
#     # print(accuracy_score(predictions_test, test_labels))
#     # print(confusion_matrix(test_labels, predictions_test))
#     return accuracy_score(predictions_test, test_labels)


# results = []
# for j in range(10):
#     for i in range(1, 101, 5):
#         x = i / 1000
#         all_inputs, all_classes = wczytaniePliku()
#         all_inputs = moje_PCA(all_inputs, 5)
#         (train_data, test_data, train_labels, test_labels) = train_test_split(all_inputs, all_classes, train_size=0.7)
# 
#         train_labels, test_labels = list(train_labels), list(test_labels)
#         try:
#             results[i//5][1] += neuronNetworkZLearningRate([64, 64], x)
#         except Exception:
#             results.append([i / 1000, neuronNetworkZLearningRate([64, 64], x)])
# for i in range(20):
#     results[i][1] = results[i][1] / 10
# 
# x, y = np.array(results).T
# plt.scatter(x, y, label="Learning rate a precyzja")
# plt.title('Sieci neuronowe - wplyw learning rate')
# plt.legend()
# plt.xlabel('Learning rate')
# plt.ylabel('Precyzja')
# plt.grid(True)
# plt.show()


# Do sprawdzenia najlepszej sieci neuronowej


def neuronNetworkBest(hidden_layers):
    mlp = MLPClassifier(hidden_layer_sizes=hidden_layers, max_iter=1_000_000, random_state=1, alpha=1e-5, batch_size=16, learning_rate_init=0.0425)
    mlp.fit(train_data, train_labels)

    predictions_train = mlp.predict(train_data)
    predictions_test = mlp.predict(test_data)
    print(accuracy_score(predictions_test, test_labels))
    print(confusion_matrix(test_labels, predictions_test))
    return accuracy_score(predictions_test, test_labels)


sum = 0
for i in range(10):
    all_inputs, all_classes = wczytaniePliku()
    all_inputs = moje_PCA(all_inputs, 5)
    (train_data, test_data, train_labels, test_labels) = train_test_split(all_inputs, all_classes, train_size=0.7)
    train_data = normalizacja(train_data)
    test_data = normalizacja(test_data)
    train_labels, test_labels = list(train_labels), list(test_labels)
    sum += neuronNetworkBest([64, 64])

print(sum/10)