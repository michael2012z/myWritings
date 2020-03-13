## Machine Learning Bit By Bit - Ridge Regression

Comparing to Ordinary Least Squares regression, Ridge regression provide better performance by introducing a penalty item. The target function is:

min<sub>w</sub> ( || X w - y ||<sub>2</sub><sup>2</sup> + a || w ||<sub>2</sub><sup>2</sup>)

Where a is alpha.

The selection of alpha is an art. A too large alpha made the coefficients tend to zero, whereas a too small alpha make the effect of the regression degrade to LinearRegression. So a balance point exist between zero and infinity, where the regressor win the  best score.

In this article I will show an example of tuning Ridge model (find best alpha value). I reuse the data set generated in last example (Polynomial Regression) and try more degrees. I will use RidgeCV to tune. Postfix CV stands for cross-validation. This enhanced version of Redge regressor divides the data samples in subsets and apply Leave-One-Out strategy to go through all the subsets combination to achieve average and thus precise fitting result.

By going through all the alpha candidates in a rather wide range, we will finally find the best alpha value and see how alpha impact the performance of the regressor by the way.

I use mean squared errors to measure the performance of the regressor.

Here comes the code.

```
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

x = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
rng.shuffle(x)
x = x[:, np.newaxis]
y = x * np.sin(x)

alphas = np.logspace(-10, 15, 250)

means = np.empty([250,0])
for degree in range(2, 15):
    rcv = RidgeCV(alphas=alphas, store_cv_values=True)
    model = make_pipeline(PolynomialFeatures(degree), rcv)
    model.fit(x, y)
    mean = rcv.cv_values_.mean(axis=0)[0, :]
    means = np.c_[means, mean]

plt.figure(figsize=(12, 12))

plt.subplot(221)
ax = plt.gca()
ax.plot(alphas[70:105], means[70:105, 1], label="degree = 3")
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('mean squared errors')
plt.legend(loc='upper left')
plt.title('Fig. 1')

plt.subplot(222)
ax = plt.gca()
ax.plot(alphas, means[:, 1], label="degree = 3")
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('mean squared errors')
plt.legend(loc='upper left')
plt.title('Fig. 2')

plt.subplot(223)
ax = plt.gca()
for i in range(2, 15):
    ax.plot(alphas, means[:, i-2], label="degree="+str(i))
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('mean squared errors')
plt.title('Fig. 3')

plt.subplot(224)
ax = plt.gca()
for i in range(2, 15):
    ax.plot(alphas, means[:, i-2], label="degree="+str(i))
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel('alpha')
plt.ylabel('mean squared errors')
plt.legend(loc='lower right')
plt.title('Fig. 4')
```

![Fig. 1~4](https://github.com/michael2012z/myWritings/raw/master/machine-learning/img/ridge-regression.png) Fig. 1~4

Figure 1 shows the result of 3-degree polynomial regression. Optimal alpha value is found. In Figure 2, the alpha range is extended extremely large, an interesting locally optimal solution appears. Multipul polynomial regression results are shown in Figure 3. The performance of the models vary largely from each other, especially for the low-degree ones. High-degree models are almost hiden in the bottom line. By using y-axis in log format we get a clear view of each model, which is shown in Figure 4.

