## Nearest Neighbors Optimization

This article records 2 methods to speed up the calculation of Nearest Neighbors (classification).

#### Locality Sensitive Hashing

By applying hashing techniques, Locality Sensitive Hashing (LSH) divide data samples into a number of small collections. The aim of doing this is to reduce the amount of calculation, as the samples in each collection are close to each other.

The main concept behind LSH is to hash each data point in the database using multiple (often simple) hash functions to form a digest (also called a hash). At this point the probability of collision - where two objects have similar digests - is much higher for the points which are close to each other than that of the distant points.

The hash function family to be locality sensitive is defined as follows.

A family H of functions from a domain S to a range U is called (r, e , p<sub>1</sub> , p<sub>2</sub> )-sensitive, with r, e > 0, p<sub>1</sub> > p<sub>2</sub> > 0, if for any p, q \in S, the following conditions hold (D is the distance function):

* If D(p,q) <= r then P<sub>H</sub>[h(p) = h(q)] >= p<sub>1</sub>,
* If D(p,q) > r(1 + e) then P<sub>H</sub>[h(p) = h(q)] <= p<sub>2</sub>.

As defined, nearby points within a distance of r to each other are likely to collide with probability p<sub>1</sub>. In contrast, distant points which are located with the distance more than r(1 + e) have a small probability of p<sub>2</sub> of collision. Suppose there is a family of LSH function H. An LSH index is built as follows:

* Choose k functions h<sub>1</sub>, h<sub>2</sub>, … h<sub>k</sub> uniformly at random (with replacement) from H. For any p in S, place p in the bucket with label g(p) = (h<sub>1</sub>(p), h<sub>2</sub>(p), … h<sub>k</sub>(p)). Observe that if each h<sub>i</sub> outputs one “digit”, each bucket has a k-digit label.

* Independently perform step 1 l times to construct l separate estimators, with hash functions g<sub>1</sub>, g<sub>2</sub>, … g<sub>l</sub>.

The reason to concatenate hash functions in the step 1 is to decrease the probability of the collision of distant points as much as possible. The probability drops from p<sub>2</sub> to p<sub>2</sub><sup>k</sup> which is negligibly small for large k. The choice of k is strongly dependent on the data set size and structure and is therefore hard to tune in practice. There is a side effect of having a large k; it has the potential of decreasing the chance of nearby points getting collided. To address this issue, multiple estimators are constructed in step 2.

The requirement to tune k for a given dataset makes classical LSH cumbersome to use in practice. The LSH Forest variant has benn designed to alleviate this requirement by automatically adjusting the number of digits used to hash the samples.


#### Data reduction

Data reduction is one of the most important problems for work with huge data sets. Usually, only some of the data points are needed for accurate classification. Those data are called the prototypes and can be found as follows:

* Select the class-outliers, that is, training data that are classified incorrectly by k-NN (for a given k)
* Separate the rest of the data into two sets: (i) the prototypes that are used for the classification decisions and (ii) the absorbed points that can be correctly classified by k-NN using prototypes. The absorbed points can then be removed from the training set.

Selection of class-outliers

A training example surrounded by examples of other classes is called a class outlier. Causes of class outliers include:

1. random error
1. insufficient training examples of this class (an isolated example appears instead of a cluster)
1. missing important features (the classes are separated in other dimensions which we do not know)
1. too many training examples of other classes (unbalanced classes) that create a "hostile" background for the given small class

Class outliers with k-NN produce noise. They can be detected and separated for future analysis. Given two natural numbers, k>r>0, a training example is called a (k,r)NN class-outlier if its k nearest neighbors include more than r examples of other classes.

##### CNN for data reduction

Condensed nearest neighbor (CNN, the Hart algorithm) is an algorithm designed to reduce the data set for k-NN classification. It selects the set of prototypes U from the training data, such that 1NN with U can classify the examples almost as accurately as 1NN does with the whole data set.

Given a training set X, CNN works iteratively:

1. Scan all elements of X, looking for an element x whose nearest prototype from U has a different label than x.
1. Remove x from X and add it to U
1. Repeat the scan until no more prototypes are added to U.

Use U instead of X for classification. The examples that are not prototypes are called "absorbed" points.

The figures below compare the classification based on original dataset and that on reduced dataset.

![Fig. 1](https://upload.wikimedia.org/wikipedia/commons/c/cc/Data3classes.png)Figure 1. Dataset
![Fig. 2](https://upload.wikimedia.org/wikipedia/commons/8/8c/Map5NN.png)Figure 2. 5-NN Classification Map
![Fig. 3](https://upload.wikimedia.org/wikipedia/commons/b/b3/ReducedDataSet.png)Figure 3. Reduced Dataset
![Fig. 4](https://upload.wikimedia.org/wikipedia/commons/e/e9/Map1NNReducedDataSet.png)Figure 4. 1-NN Classification Map Based on Reduced Dataset
