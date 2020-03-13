import numpy as np
from sklearn.datasets import fetch_mldata
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier

import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

saved_mnist = fetch_mldata('MNIST original', data_home = './')
print "MNIST raw data loaded"

def get_data_set_tf():
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    training_set_x = np.array(mnist.train.images * 255, dtype=np.uint8)
    training_set_y = np.array(mnist.train.labels, dtype=np.uint8)
    testing_set_x = np.array(mnist.test.images * 255, dtype=np.uint8)
    testing_set_y = np.array(mnist.test.labels, dtype=np.uint8)
    return training_set_x, training_set_y, testing_set_x, testing_set_y

def get_data_set_sk(saved_mnist):
    mnist = saved_mnist
    training_set_x = mnist.data[:20000]
    training_set_y = mnist.target[:20000]
    testing_set_x = mnist.data[-4000:]
    testing_set_y = mnist.target[-4000:]
    return training_set_x, training_set_y, testing_set_x, testing_set_y

def rebuild_image_data(noise_coef, images, labels):
    images_x = images.copy()
    for i in range(len(images)):
        noise_dots = int(noise_coef * 784)
        noise_mask = np.zeros((784), dtype=np.uint8)
        noise_mask[:noise_dots] += np.ones((noise_dots), dtype=np.uint8)
        np.random.shuffle(noise_mask)
        image = images[i]
        image_invert = 255 - image
        noised_image = image + image_invert * noise_mask
        images_x[i] = noised_image
    return images_x, labels



shuffled_mnist = np.column_stack((saved_mnist.data, saved_mnist.target))
#print shuffled_mnist.shape
np.random.shuffle(shuffled_mnist)
saved_mnist.data = shuffled_mnist[:,:784]
saved_mnist.target = shuffled_mnist[:,-1]

f = open('accuracy_sk.txt', 'w')
for clf in [KNeighborsClassifier(), SGDClassifier(), GaussianNB()]:
    # loop through noise coef from 0 ~ 1.00
    noise_coef_list = np.arange(0.0, 1.0, 0.01)
    accuracy_list = np.empty((len(noise_coef_list)), dtype = np.float)
    for noise_coef in noise_coef_list:
        training_set_x, training_set_y, testing_set_x, testing_set_y = get_data_set_sk(saved_mnist)
        training_set_x, training_set_y = rebuild_image_data(noise_coef, training_set_x, training_set_y)
        testing_set_x, testing_set_y = rebuild_image_data(noise_coef, testing_set_x, testing_set_y)

        clf.fit(training_set_x, training_set_y)
        predicting_set_y = clf.predict(testing_set_x)
    
        # calculate accuracy
        accuracy = accuracy_score(testing_set_y, predicting_set_y)
        accuracy_list[int(noise_coef*len(noise_coef_list)+0.5)] = accuracy
        print "noise = " + str(noise_coef) + ", index = " + str(int(noise_coef*len(noise_coef_list)+0.5)) + ", accuracy = " + str(accuracy)
    f.write(str(accuracy_list))
    f.write('\n')
f.close()
