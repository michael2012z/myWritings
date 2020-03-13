import numpy as np
from sklearn.datasets import fetch_mldata
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
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

# loop through noise coef from 0 ~ 1.00
noise_coef_list = np.arange(0.0, 1.0, 0.01)
accuracy_list = np.empty((len(noise_coef_list)), dtype = np.float)
for noise_coef in noise_coef_list:

    training_set_x, training_set_y, testing_set_x, testing_set_y = get_data_set_sk(saved_mnist)

    training_set_x, training_set_y = rebuild_image_data(noise_coef, training_set_x, training_set_y)
    testing_set_x, testing_set_y = rebuild_image_data(noise_coef, testing_set_x, testing_set_y)

    # print training_set_x.shape
    # print training_set_y.shape
    # fit and predict
    # clf = svm.SVC()
    clf = KNeighborsClassifier()
    clf.fit(training_set_x, training_set_y)
    predicting_set_y = clf.predict(testing_set_x)
    #predicting_set_y = testing_set_y
    
    # calculate accuracy
    accuracy = accuracy_score(testing_set_y, predicting_set_y)
    accuracy_list[int(noise_coef*len(noise_coef_list)+0.5)] = accuracy
    print "noise = " + str(noise_coef) + ", index = " + str(int(noise_coef*len(noise_coef_list)+0.5)) + ", accuracy = " + str(accuracy)
    
    # show
    if (noise_coef * 100) % 10 == 0:
        plt.figure(figsize=(12, 6))
        plt.title('noise coneficient = ' + str(noise_coef))
        for i in range(2):
            for j in range(4):
                plt.subplot(240 + i * 4 + j + 1)
                ax = plt.gca()
                ax.matshow(testing_set_x[i*4+j].reshape((28, 28)), cmap='gray')
        fname = "img/mnist_noise_coef_" + str(int(noise_coef * 100)).zfill(2) + '.png'
        plt.savefig(fname)
        plt.close(0)
    #plt.imsave(fname=fname)
    # plt.imsave(fname=fname, arr=testing_set_x[0].reshape((28, 28)))

print noise_coef_list
print accuracy_list
plt.figure(figsize=(12, 6))
plt.plot(noise_coef_list, accuracy_list, color='blue', linestyle='-', linewidth=2,
         label='Accuracy')
plt.legend(loc='upper right')
plt.savefig('img/mnist_noise_accuracy.png')
