import statistics

import pandas
import seaborn as sns
from matplotlib import pyplot as plt

from funkcjeRobocze import wczytaniePliku, moje_PCA


all_inputs, all_classes = wczytaniePliku()
all_inputs = moje_PCA(all_inputs, 5)
maxX = 0
minX = 0
for x in all_inputs:
    for elem in x:
        if elem > maxX:
            maxX = elem
        if elem < minX:
            minX = elem

# print(minX, maxX)
# print(all_inputs)

x = []
for record in all_inputs:
    x.append(record[0])
sdX = statistics.stdev(x)
meanX = sum(x)/len(x)
print(meanX)
print(sdX)

resultY = x
resultX = []
for i in range(0, len(x)):
    resultX.append((x[i]-meanX)/sdX)

# Tworzenie wykresu
plt.scatter(resultX, resultY)
plt.title('Z-score dla pierwszej kolumny')
plt.legend()
plt.xlabel('Po przeprowadzeniu standaryzacji')
plt.ylabel('Przed standaryzacją')
plt.grid(True)
plt.show()

dataBefore = pandas.DataFrame(data=resultY)
dataAfter = pandas.DataFrame(data=resultX)
sns.displot(data=dataBefore, kde=True)
plt.show()
sns.displot(data=dataAfter, kde=True)
plt.show()
