## Machine Learning Bit By Bit - Polynomial Regression

Is Linear Regression too simple to resolve your problem, especially when the data dots didn't seem to be around a line? If your data is distributed in a "curve" pattern, it's possible that a polynomial regression apply.

Polynomial regression sound complex, because it involes multiple degrees, and the degree can be any number. But in fact it's not complicated at all, a multi-degree regression can be transformed into linear regression with degree 1.

See a target polinomial with 2 degree and 2 features:

y = w<sub>0</sub> + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + w<sub>3</sub>x<sub>1</sub>x<sub>2</sub> + w<sub>4</sub>x<sub>1</sub><sup>2</sup> + w<sub>5</sub>x<sub>2</sub><sup>2</sup>

Create a new vector z with:

z = [x<sub>1</sub>, x<sub>2</sub>, x<sub>1</sub>x<sub>2</sub>, x<sub>1</sub><sup>2</sup>, x<sub>2</sub><sup>2</sup>]

And notate it as:

z = [z<sub>1</sub>, z<sub>2</sub>, z<sub>3</sub>, z<sub>4</sub>, z<sub>5</sub>]

So the original question become a new one which is a linear regression:

y = w<sub>0</sub> + w<sub>1</sub>z<sub>1</sub> + w<sub>2</sub>z<sub>2</sub> + w<sub>3</sub>z<sub>3</sub> + w<sub>4</sub>z<sub>4</sub> + w<sub>5</sub>z<sub>5</sub>

Scikit provides a utilizing class to help you in translating you data set. Here is a example:
```
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
x = np.arange(4).reshape(2, 2)
poly = PolynomialFeatures(degree=2)
poly.fit_transform(x)

[output] 
array([[ 1.,  0.,  1.,  0.,  0.,  1.],
       [ 1.,  2.,  3.,  4.,  6.,  9.]])
```

The data set x you got is:
[[0 1]
 [2 3]]
 
In each data sample there are 2 number, x<sub>1</sub> and x<sub>2</sub>.
Converting it to z, you got the data in output. Note, w<sub>0</sub> is always 1.

Let's try some fittings with polynomial regression of diffent degrees (Scikit examples with tiny modification):

```
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def f(x):
    return x * np.sin(x)

# generate points used to plot
x_plot = np.linspace(0, 10, 100)

# generate points and keep a subset of them
x = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
rng.shuffle(x)
x = np.sort(x[:20])
y = f(x)

# create matrix versions of these arrays
X = x[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]

colors = ['teal', 'yellowgreen', 'gold']
lw = 2
plt.plot(x_plot, f(x_plot), color='cornflowerblue', linewidth=lw, label="ground truth")
plt.scatter(x, y, color='navy', s=30, marker='o', label="training points")

for count, degree in enumerate([3, 4, 5]):
    model = make_pipeline(PolynomialFeatures(degree), Ridge())
    model.fit(X, y)
    y_plot = model.predict(X_plot)
    plt.plot(x_plot, y_plot, color=colors[count], linewidth=lw, label="degree %d" % degree)

plt.legend(loc='lower left')

plt.show()
```
![Fig. 1](https://github.com/michael2012z/myWritings/raw/master/machine-learning/img/polynomial-regression.png) Fig. 1

The fitting result of different degree is shown in the figure. Not surprisingly, the model with degree 5 is most close to the actual data set.
