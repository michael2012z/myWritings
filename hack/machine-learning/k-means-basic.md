## Machine Learning Bit by Bit - K-Means Clustering Basic

The KMeans algorithm clusters data by trying to separate samples in n groups of equal variance. This algorithm requires the number of clusters to be specified.

The k-means algorithm divides a set of N samples X into K disjoint clusters C, each described by the mean u<sub>j</sub> of the samples in the cluster. The means are commonly called the cluster “centroids”; note that they are not, in general, points from X, although they live in the same space.

The K-means algorithm aims to choose centroids that minimise the inertia, or within-cluster sum of squared criterion:

∑ min( || x<sub>j</sub> - u<sub>i</sub> ||<sup>2</sup> )

In general, the algorithm operates in 3 steps:
1. The first step chooses the initial centroids, with the most basic method being to choose k samples from the dataset X.
1. The second step assigns each sample to its nearest centroid.
1. The third step creates new centroids by taking the mean value of all of the samples assigned to each previous centroid. The difference between the old and the new centroids are computed. Loop in step 2 and 3 until the difference is less than a threshold.

The figure below shows some examples of clustering.

![Fig. 1](http://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_assumptions_001.png)