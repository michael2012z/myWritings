## Machine Learning Bit By Bit - Linear Regression

### General 

Regression, according to Wikipedia, is a statistical process for estimating the relationships among variables. Regression analysis helps one understand how the typical value of the dependent variable changes when any one of the independent variables is varied, while the other independent variables are held fixed.

The term "regression" was first used in the nineteenth century to describe a biological phenomenon. The phenomenon was that the heights of descendants of tall ancestors tend to regress down towards a normal average.

Nowadays, regression analysis is widely used for prediction and forecasting.

Linear Regression is the sort of regression in which the target value is expected to be a linear combination of the input variables.

It is notated as:
y(w, x) = w<sub>0</sub> + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + ... + w<sub>p</sub>x<sub>p</sub>
where y is the predicted value. w = (w<sub>0</sub>, w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>p</sub>) is called weight or coef_ in the model which will be shown below, w~0~ is intercept.

### Ordinary Least Squares

Ordinary Least Squares Regression is the simplest regression. The target function is notated as:
min<sub>w</sub> || X w - y ||<sub>2</sub><sup>2</sup>

The following code shows an example of OLS regression.
```
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

X, y, coef = datasets.make_regression(n_samples=512, n_features=1, n_informative=1, noise=10, coef=True, random_state=0)

model = linear_model.LinearRegression()
model.fit(X, y)
print('coef_ = ', model.coef_)

line_X = np.arange(-5, 5)
line_y = model.predict(line_X[:, np.newaxis])

plt.scatter(X, y, color='green', marker='.', label='Samples')
plt.plot(line_X, line_y, color='blue', linestyle='-', linewidth=2, label='Linear regressor')
plt.legend(loc='lower right')
plt.show()

```

![Fig. 1](https://github.com/michael2012z/myWritings/raw/master/machine-learning/img/linear-regression.png) Fig. 1

With datasets.make_regression(), we generate a sample set containing 512 point. The value "number of feature (n_features)" is set to 1, so vector x contains one variable (x<sub>1</sub>) only. Sample data is shown with dots in Figure 1.

Regressor LinearRegression implements OLS, we will use it to predict. But before that we need to calculate the coeficient by fitting the model with samples.

After fitting, the model is ready to predict. You feed a x value, the model will predict the corresponding y value. Prediction data of the similar range is drawn with a line in the figure.
