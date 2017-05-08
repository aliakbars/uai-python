from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
plt.style.use('fivethirtyeight')

df = sns.load_dataset('iris')

fig, ax = plt.subplots()
ax.scatter(df.petal_length, df.petal_width)
ax.set_xlabel('petal length')
ax.set_ylabel('petal width')
# plt.savefig('kmeans-0.png', bbox_inches='tight')

X = df[['petal_length', 'petal_width']]

clf = KMeans(2)
labels = clf.fit_predict(X)
ax.scatter(X[clf.labels_ == 0].petal_length, X[clf.labels_ == 0].petal_width)
ax.scatter(X[clf.labels_ == 1].petal_length, X[clf.labels_ == 1].petal_width)
ax.scatter(clf.cluster_centers_[:,0], clf.cluster_centers_[:,1], marker='x')
centers = clf.cluster_centers_
radii = [pairwise_distances(X[labels == i], [center]).max()
         for i, center in enumerate(centers)]
for c, r in zip(centers, radii):
    ax.add_patch(plt.Circle(c, r, fc='#CCCCCC', lw=3, alpha=0.5, zorder=1))
# plt.savefig('kmeans-1.png', bbox_inches='tight')
plt.show()