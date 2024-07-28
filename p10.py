from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = load_iris()
# print(dataset)
X = pd.DataFrame(dataset.data)
X.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
y = pd.DataFrame(dataset.target)
y.columns = ['Targets']
# print(X)
plt.figure(figsize=(14, 7))
colormap = np.array(['red', 'lime', 'black'])
# REAL PLOT.
plt.subplot(1, 3, 1)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[y.Targets])
plt.title('Real')
# K-PLOT
plt.subplot(1, 3, 2)
model = KMeans(n_clusters=3)
model.fit(X)
predY = np.choose(model.labels_, [0, 1, 2])
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[predY])
plt.title('KMeans')
# GMM PLOT
scaler = StandardScaler()
scaler.fit(X)
xsa = scaler.transform(X)
xs = pd.DataFrame(xsa, columns=X.columns)
gmm = GaussianMixture(n_components=3)
gmm.fit(xs)
y_cluster_gmm = gmm.predict(xs)
plt.subplot(1, 3, 3)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[y_cluster_gmm])
plt.title('GMM Classification')
plt.show()