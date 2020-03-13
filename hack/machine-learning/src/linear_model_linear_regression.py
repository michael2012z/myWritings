import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

X, y, coef = datasets.make_regression(n_samples=512, n_features=1,
                                      n_informative=1, noise=10,
                                      coef=True, random_state=0)

model = linear_model.LinearRegression()
model.fit(X, y)
print('coef_ = ', model.coef_)

line_X = np.arange(-5, 5)
line_y = model.predict(line_X[:, np.newaxis])

plt.scatter(X, y, color='green', marker='.',
            label='Samples')
plt.plot(line_X, line_y, color='blue', linestyle='-', linewidth=2,
         label='Linear regressor')
plt.legend(loc='lower right')
plt.show()
