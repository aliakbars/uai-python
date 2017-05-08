from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
plt.style.use('fivethirtyeight')

df = sns.load_dataset('iris')

fig, ax = plt.subplots()
for s in df.species.unique():
	ax.scatter(df[df.species == s].petal_length, df[df.species == s].petal_width, label=s)
plt.legend()
ax.set_xlabel('petal length')
ax.set_ylabel('petal width')
# plt.savefig('iris-0.png', bbox_inches='tight')

# ax.scatter([2], [.5], marker='x')
# ax.annotate('spesies apa?', xy=(2.05, .55))
# plt.savefig('iris-1.png', bbox_inches='tight')

# ax.scatter([4.3], [1.], marker='x')
# ax.annotate('spesies apa?', xy=(4.35, 1.05))
# plt.savefig('iris-2.png', bbox_inches='tight')

# ax.scatter([4.2], [1.8], marker='x')
# ax.annotate('spesies apa?', xy=(3.05, 1.85))
# plt.savefig('iris-3.png', bbox_inches='tight')
# plt.show()

X_train = df[['petal_length', 'petal_width']]
y_train = df['species']
X_test = np.array([[2, .5],[4.3, 1.],[4.2, 1.8]])

clf = KNeighborsClassifier(3)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
ax.scatter(X_test[:,0], X_test[:,1], marker='x')
for i, (pl, pw) in enumerate(X_test[:]):
	ax.annotate(y_pred[i], xy=(pl + .05, pw + .05))
# plt.savefig('knn.png', bbox_inches='tight')
plt.show()