####################################################################
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

X, y, coef = datasets.make_regression(n_samples=512, n_features=1,
                                      n_informative=1, noise=10,
                                      coef=True, random_state=0)

model = linear_model.Ridge(alpha=1.0)
model.fit(X, y)
print('coef_ = ', model.coef_)
print("score = ", model.score(X, y))

line_X = np.arange(-5, 5)
line_y = model.predict(line_X[:, np.newaxis])

plt.scatter(X, y, color='green', marker='.',
            label='Samples')
plt.plot(line_X, line_y, color='blue', linestyle='-', linewidth=2,
         label='Ridge regressor')
plt.legend(loc='lower right')
plt.show()



####################################################################
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

X, y, coef = datasets.make_regression(n_samples=512, n_features=1,
                                      n_informative=1, noise=10,
                                      coef=True, random_state=0)

n_alphas = 20
alphas = np.logspace(-10, 10, n_alphas)
coefs = []
scores = []

for alpha in alphas:
    model = linear_model.Ridge(alpha=alpha)
    model.fit(X, y)
    coefs.append(model.coef_)
    scores.append(model.score(X, y))

ax = plt.gca()
ax.plot(alphas, coefs)
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('coef')
plt.axis('tight')
plt.show()


####################################################################
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def f(x):
    """ function to approximate by polynomial interpolation"""
    return x * np.sin(x)



# generate points, use 80% to train and 20% to verify
x = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
rng.shuffle(x)
x = x[:, np.newaxis]

# alpha in log space
n_alphas = 100
alphas = np.logspace(-3, 0, n_alphas)

rcv = RidgeCV(alphas=alphas, store_cv_values=True)
model = make_pipeline(PolynomialFeatures(5), rcv)
model.fit(x, f(x))
#rcv_name, rcv = model.steps[1]
print rcv.alpha_
print rcv.coef_

means = rcv.cv_values_.mean(axis=0)
print alphas[means.argmin()]
ax = plt.gca()
ax.plot(alphas, means[0, :])
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('score')
#plt.axis('tight')
plt.show()


############################################################################
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def f(x):
    """ function to approximate by polynomial interpolation"""
    return x * np.sin(x)



# generate points, use 80% to train and 20% to verify
x = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
rng.shuffle(x)
x = x[:, np.newaxis]

# alpha in log space
n_alphas = 100
alphas = np.logspace(-10, 5, n_alphas)

ax = plt.gca()

for degree in range(2, 20):
    rcv = RidgeCV(alphas=alphas, store_cv_values=True)
    model = make_pipeline(PolynomialFeatures(degree), rcv)
    model.fit(x, f(x))
    mean = rcv.cv_values_.mean(axis=0)[0, :]
    ax.plot(alphas, mean)
    print rcv.alpha_
    
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('mean')
#plt.axis('tight')
plt.show()


##############################################################
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def f(x):
    """ function to approximate by polynomial interpolation"""
    return x * np.sin(x)


# generate points, use 80% to train and 20% to verify
x = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
rng.shuffle(x)
x = x[:, np.newaxis]

plt.figure(figsize=(12, 12))


plt.subplot(221)
# alpha in log space
n_alphas = 100
alphas = np.logspace(-3, 0.3, n_alphas)

ax = plt.gca()

for degree in range(3, 4):
    rcv = RidgeCV(alphas=alphas, store_cv_values=True)
    model = make_pipeline(PolynomialFeatures(degree), rcv)
    model.fit(x, f(x))
    mean = rcv.cv_values_.mean(axis=0)[0, :]
    ax.plot(alphas, mean)
    print rcv.alpha_
    
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('mean')
#plt.axis('tight')


plt.subplot(222)
# alpha in log space
n_alphas = 100
alphas = np.logspace(-10, 15, n_alphas)

ax = plt.gca()

for degree in range(3, 4):
    rcv = RidgeCV(alphas=alphas, store_cv_values=True)
    model = make_pipeline(PolynomialFeatures(degree), rcv)
    model.fit(x, f(x))
    mean = rcv.cv_values_.mean(axis=0)[0, :]
    ax.plot(alphas, mean)
    print rcv.alpha_
    
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('mean')



plt.subplot(223)
# alpha in log space
n_alphas = 100
alphas = np.logspace(-10, 15, n_alphas)

ax = plt.gca()

for degree in range(3, 10):
    rcv = RidgeCV(alphas=alphas, store_cv_values=True)
    model = make_pipeline(PolynomialFeatures(degree), rcv)
    model.fit(x, f(x))
    mean = rcv.cv_values_.mean(axis=0)[0, :]
    ax.plot(alphas, mean)
    print rcv.alpha_
    
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('mean')



plt.subplot(224)
# alpha in log space
n_alphas = 100
alphas = np.logspace(-4, 15, n_alphas)

ax = plt.gca()

for degree in range(2, 15):
    rcv = RidgeCV(alphas=alphas, store_cv_values=True)
    model = make_pipeline(PolynomialFeatures(degree), rcv)
    model.fit(x, f(x))
    mean = rcv.cv_values_.mean(axis=0)[0, :]
    ax.plot(alphas, mean)
    print rcv.alpha_
    
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel('alpha')
plt.ylabel('mean')
#plt.axis('tight')

plt.show()




####################################################
'
The setting of alpha value impact the performance of Ridge regressor. A too large alpha made the coefficients tend to zero, whereas a too small alpha make the effect of the regression degrade to LinearRegression. So a balance point exist between zero and infinity, where the regressor win best score.
This example illustrates how alpha impact regression performance, and how to obtain the best alpha value by using RidgeCV.
Sample data is generated with function f(x) = x*sin(x). Polynomial regressions with different degrees are tried to fit the data. Score varies as different alpha applies.
Figure 1 shows the result of 3-degree polynomial regression. In Figure 2, the alpha range is extended extremely large, an interesting locally optimal solution appears. Multipul polynomial regression results are shown in Figure 3. The performance of the models vary from each other, especially for the low-degree ones. High-degree models are almost hide on the bottom line. By using y-axis in log format we get a clear view of each model, which is shown in Figure 4.
'


#####################################################
# simplified code #
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

alpha_ranges = [(-3, 0.3), (-10, 15), (-10, 15), (-10, 15)]
degree_ranges = [(3, 4), (3, 4), (2, 15), (2, 15)]
y_scales = ['linear', 'linear', 'linear', 'log']
n_alphas = 100

plt.figure(figsize=(12, 12))

for i in range(0, 4):
    plt.subplot(221+i)
    alphas = np.logspace(alpha_ranges[i][0], alpha_ranges[i][1], n_alphas)
    ax = plt.gca()
    means = np.empty([n_alphas,0])
    for degree in range(degree_ranges[i][0], degree_ranges[i][1]):
        rcv = RidgeCV(alphas=alphas, store_cv_values=True)
        model = make_pipeline(PolynomialFeatures(degree), rcv)
        model.fit(x, y)
        mean = rcv.cv_values_.mean(axis=0)[0, :]
        means = np.c_[means, mean]
        print rcv.alpha_
    ax.plot(alphas, means)
    ax.set_xscale('log')
    ax.set_yscale(y_scales[i])
    plt.xlabel('alpha')
    plt.ylabel('mean squared errors')

plt.show()



###########################################################
# optimized #
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

plt.subplot(222)
ax = plt.gca()
ax.plot(alphas, means[:, 1], label="degree = 3")
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('mean squared errors')
plt.legend(loc='upper left')

plt.subplot(223)
ax = plt.gca()
for i in range(2, 15):
    ax.plot(alphas, means[:, i-2], label="degree="+str(i))
ax.set_xscale('log')
plt.xlabel('alpha')
plt.ylabel('mean squared errors')

plt.subplot(224)
ax = plt.gca()
for i in range(2, 15):
    ax.plot(alphas, means[:, i-2], label="degree="+str(i))
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel('alpha')
plt.ylabel('mean squared errors')
plt.legend(loc='lower right')
