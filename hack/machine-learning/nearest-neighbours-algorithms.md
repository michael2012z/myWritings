## Nearest Neighbor Algorithms

The concept of Nearest Neighbors model is simple, but there is huge space in designing and optimizing the implementation algorithms.

#### Brute Force
The most naive neighbor search algorithm is named Brute Force, which go through all samples and calculate its distance from every other samples. for N samples in D dimensions, this approach scales as O(D N<sup>2</sup>).

Brute-force neighbors searches for small data set can be easy. However, as the number of samples N grows, the brute-force approach quickly becomes infeasible (so-called “curse of dimensionality”).

To address the computational inefficiencies of the brute-force approach, a variety of tree-based data structures have been invented.

#### K-D Tree

The k-d tree is a binary tree in which every node is a k-dimensional point. Every non-leaf node can be thought of as implicitly generating a splitting hyperplane that divides the space into two parts, known as half-spaces. Points to the left of this hyperplane are represented by the left subtree of that node and points right of the hyperplane are represented by the right subtree. The hyperplane direction is chosen in the following way: every node in the tree is associated with one of the k-dimensions, with the hyperplane perpendicular to that dimension's axis. So, for example, if for a particular split the "x" axis is chosen, all points in the subtree with a smaller "x" value than the node will appear in the left subtree and all points with larger "x" value will be in the right subtree. In such a case, the hyperplane would be set by the x-value of the point, and its normal would be the unit x-axis.

An example of dimension divistion by K-D Tree is illustrated by the figure below (from Wikipedia).

![Fig. 1](https://upload.wikimedia.org/wikipedia/commons/b/b6/3dtree.png)

[Wikipedia](https://en.wikipedia.org/wiki/K-d_tree) also provide a demo Python code for constructing K-D Tree in 2-D plane.

Searching process is omitted here. Check wiki page for all the details.

#### Ball Tree

A ball tree is a binary tree in which every node defines a D-dimensional hypersphere, or ball, containing a subset of the points to be searched. Each internal node of the tree partitions the data points into two disjoint sets which are associated with different balls.

The balls themselves may intersect, each point is assigned to one or the other ball in the partition according to its distance from the ball's center. Each leaf node in the tree defines a ball and enumerates all data points inside that ball.

The most important property is that each node in the tree defines the smallest ball that contains all data points in its subtree.

Variant algorithms exist in building Ball Tree data structure. The paper [Five Balltree Construction Algorithms](ftp://ftp.icsi.berkeley.edu/pub/techreports/1989/tr-89-063.pdf) compares the performance of different algorhtms.

The figure below isslustrates how a set of sample divided into balls.

![Fig. 2](https://raw.githubusercontent.com/michael2012z/myWritings/master/machine-learning/img/nearest-neighbors-balltree.png)

#### Choice of "leaf_size"

Both algorithm K-D Tree and Ball Tree use a critical parameter "leaf_size", which determine how many samples are contained in the lowest level node of the tree. The choice of the parameter is an art of balance, as it has many effects:

- **Construction Time.** A larger leaf_size leads to a faster tree construction time, because fewer nodes need to be created.
- **Query Time.** Both a large or small leaf_size can lead to suboptimal query cost. For leaf_size approaching 1, the overhead involved in traversing nodes can significantly slow query times. For leaf_size approaching the size of the training set, queries become essentially brute force. 
- **Memory.** As leaf_size increases, the memory required to store a tree structure decreases. 

