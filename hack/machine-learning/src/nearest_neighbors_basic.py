from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1, 1], [1, 3], [6, 1], [6, 3], [4, 2], [5, 2]])
C = np.array([[3, 2]])
nbrs = NearestNeighbors(n_neighbors=2).fit(X)
distances, indices = nbrs.kneighbors(C)
print indices
print distances
plt.figure(figsize=(7, 4))
plt.plot(X[:, 0], X[:, 1], 'o', markerfacecolor='b', markersize=14)
plt.plot(C[:, 0], C[:, 1], 'o', markerfacecolor='r', markersize=14)
plt.xlim(0, 7)
plt.ylim(0, 4)
plt.show()

===

[[4 5]]
[[ 1.  2.]]
