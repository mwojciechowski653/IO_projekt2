import numpy as np
from funkcjeRobocze import wczytaniePliku 
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

all_inputs, all_classes = wczytaniePliku()

# Do badania, które PCA wybrać
results = []
for i in range(12, 1, -1):
    pca_battle = PCA(n_components=i).fit(all_inputs)
    # print(pca_battle)
    print(pca_battle.explained_variance_ratio_)
    summary = 0
    for elem in pca_battle.explained_variance_ratio_:
        summary += elem
    print(i, summary, sep=":")
    results.append([i, summary])
x, y = np.array(results).T
plt.scatter(x, y, label="PCA")
plt.title('% Wariancji a kompresja PCA')
plt.legend()
plt.xlabel('Liczba kolumn po kompresji')
plt.ylabel('% Zachowanej wariancji')
plt.grid(True)
plt.show()
