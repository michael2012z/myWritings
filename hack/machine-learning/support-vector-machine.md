## Machine Learning Bit by Bit - Support Vector Machine

#### Overview

Support Vector Machine classifier applies yet another classification streatgy go divide training samples and predict.

The concept of Support Vector Machine classifier is to find the best border of samples in two categories, and predict the category of new data according to which side of the border the data is located on. Whereas "best" mean that the border is as far from both  categories as possible.

#### Basic

An SVM model is a representation of the examples as points in space, mapped so that the examples of the separate categories are divided by a clear gap that is as wide as possible. New examples are then mapped into that same space and predicted to belong to a category based on which side of the gap they fall.

![Fig. 1](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Svm_separating_hyperplanes_%28SVG%29.svg/277px-Svm_separating_hyperplanes_%28SVG%29.svg.png)
Figure 1. H1 does not separate the classes. H2 does, but only with a small margin. H3 separates them with the maximum margin.

In the case of support vector machines, a data point is viewed as a p-dimensional vector (a list of p numbers), and we want to know whether we can separate such points with a (p-1)-dimensional hyperplane. This is called a linear classifier.

There are many hyperplanes that might classify the data. One reasonable choice as the best hyperplane is the one that represents the largest separation, or margin, between the two classes. So we choose the hyperplane so that the distance from it to the nearest data point on each side is maximized. If such a hyperplane exists, it is known as the maximum-margin hyperplane and the linear classifier it defines is known as a maximum margin classifier; or equivalently, the perceptron of optimal stability.

#### Support Vectors

To Support Vector Machine classifier, the samples to the border is very important, they determine the position of hyperplane.

Maximum-margin hyperplane and margins for an SVM trained with samples from two classes. Samples on the margin are called the support vectors.

![Fig. 2](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Svm_max_sep_hyperplane_with_margin.png/445px-Svm_max_sep_hyperplane_with_margin.png)


#### Kernal function

Whereas the original problem may be stated in a finite dimensional space, it often happens that the sets to discriminate are not linearly separable in that space. For this reason, it was proposed that the original finite-dimensional space be mapped into a much higher-dimensional space, presumably making the separation easier in that space.

To keep the computational load reasonable, the mappings used by SVM schemes are designed to ensure that dot products may be computed easily in terms of the variables in the original space, by defining them in terms of a kernel function k(x,y) selected to suit the problem.

![Fig. 3](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Kernel_Machine.svg/640px-Kernel_Machine.svg.png)


