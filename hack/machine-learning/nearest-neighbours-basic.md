## Nearest Neighbours Basic

The principle behind nearest neighbor methods is to find a predefined number of training samples closest in distance to the new point, and predict the label from these. The number of samples can be a user-defined constant (k-nearest neighbor learning), or vary based on the local density of points (radius-based neighbor learning). The distance can, in general, be any metric measure: standard Euclidean distance is the most common choice.

k-NN is a type of instance-based learning, or lazy learning, where the function is only approximated locally and all computation is deferred until classification.

Nearest Neighbours is one of the simplest machine learning algorithms.

#### Finding Nearest Neighbours

sklearn.neighbors provides functionality for neighbors-based learning methods.

The basis of all neighors-based methods is the calculation of neighbors.

Here is an example of getting neighbors of a 2-dimension dot.

```
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

===>

[[4 5]]
[[ 1.  2.]]

```
![Fig. 1](https://raw.githubusercontent.com/michael2012z/myWritings/master/machine-learning/img/nearest-neighbors-concept.png)


#### Nearest Neighbours Classification

Neighbors-based classification is a type of instance-based learning or non-generalizing learning: it does not attempt to construct a general internal model, but simply stores instances of the training data. Classification is computed from a simple majority vote of the nearest neighbors of each point: a query point is assigned the data class which has the most representatives within the nearest neighbors of the point.


```
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets.samples_generator import make_blobs
from matplotlib.colors import ListedColormap

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
centers = np.array([[-1.5, 0], [1.5, 0], [0, 1]])
X, y = make_blobs(n_samples=4000, centers=centers, cluster_std=0.6)

clf = KNeighborsClassifier(15)
clf.fit(X, y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
zz = clf.predict(np.c_[xx.ravel(), yy.ravel()])
zz = zz.reshape(xx.shape)
    
plt.figure(figsize=(12, 9))
plt.pcolormesh(xx, yy, zz, cmap=cmap_light)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.show()
```

![Fig. 2](https://raw.githubusercontent.com/michael2012z/myWritings/master/machine-learning/img/nearest-neighbors-classification.png)

In the demo above, 4000 dots were generated on random. They were located in 3 different blobs, to each of which a label applied.
Then we trained a Nearest Neighbors Classifier with the blobs data and predicted each dot of the plain and marked different classification area with different color.

The value of parameter 'k' impact the performance of the classifier. If the value of k is too small, the classification result can be seriously affected by noise.

The figure below illustrates the effect while applying different parameters.

![Fig. 3](https://github.com/michael2012z/myWritings/raw/master/machine-learning/img/nearest-neighbors-classification_k.png)
