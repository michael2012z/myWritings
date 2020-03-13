import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
from tensorflow.python.framework import dtypes

def rebuild_image_data(noise_coef, mnist):
    images_sets = [mnist.train.images, mnist.test.images]
    for images in images_sets:        
        for i in range(len(images)):
            noise_dots = int(noise_coef * 784)
            noise_mask = np.zeros((784), dtype=np.float32)
            noise_mask[:noise_dots] += np.ones((noise_dots), dtype=np.float32)
            np.random.shuffle(noise_mask)
            image = images[i]
            image_invert = 1.0 - image
            noised_image = image + image_invert * noise_mask
            images[i] = noised_image
    return mnist

def mnist_noise_tf_single_layer():
    noise_coef_list = np.arange(0.0, 1.0, 0.01)
    accuracy_list = np.empty((len(noise_coef_list)), dtype = np.float)
    for noise_coef in noise_coef_list:
        mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
        mnist = rebuild_image_data(noise_coef, mnist)
        x = tf.placeholder(tf.float32, [None, 784])
        W = tf.Variable(tf.zeros([784, 10]))
        b = tf.Variable(tf.zeros([10]))
        y = tf.nn.softmax(tf.matmul(x, W) + b)
        y_ = tf.placeholder(tf.float32, [None, 10])
        cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
        train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
        init = tf.global_variables_initializer()
        sess = tf.Session()
        sess.run(init)
        for i in range(1000):
            batch_xs, batch_ys = mnist.train.next_batch(100)
            sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        accuracy_value = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
        accuracy_list[int(noise_coef*len(noise_coef_list)+0.5)] = accuracy_value
        print accuracy_value

    print noise_coef_list
    print accuracy_list
    plt.figure(figsize=(12, 6))
    plt.plot(noise_coef_list, accuracy_list, color='blue', linestyle='-', linewidth=2, label='Accuracy')
    plt.legend(loc='upper right')
    plt.savefig('img/mnist_noise_accuracy_tf_single_layer.png')
    f = open('accuracy_tf.txt', 'w')
    f.write('mnist_noise_tf_single_layer:\n')
    f.write(str(accuracy_list))
    f.write('\n')
    f.close()



#####################################################################

def init_weights(shape, name):
    return tf.Variable(tf.random_normal(shape, stddev=0.01), name=name)

# This network is the same as the previous one except with an extra hidden layer + dropout
def model(X, w_h, w_h2, w_o, p_keep_input, p_keep_hidden):
    # Add layer name scopes for better graph visualization
    with tf.name_scope("layer1"):
        X = tf.nn.dropout(X, p_keep_input)
        h = tf.nn.relu(tf.matmul(X, w_h))
    with tf.name_scope("layer2"):
        h = tf.nn.dropout(h, p_keep_hidden)
        h2 = tf.nn.relu(tf.matmul(h, w_h2))
    with tf.name_scope("layer3"):
        h2 = tf.nn.dropout(h2, p_keep_hidden)
        return tf.matmul(h2, w_o)

def mnist_noise_tf_multi_layers():
    noise_coef_list = np.arange(0.0, 1.0, 0.01)
    accuracy_list = np.empty((len(noise_coef_list)), dtype = np.float)
    for noise_coef in noise_coef_list:
        mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
        mnist = rebuild_image_data(noise_coef, mnist)
        trX, trY, teX, teY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels

        X = tf.placeholder("float", [None, 784], name="X")
        Y = tf.placeholder("float", [None, 10], name="Y")

        w_h = init_weights([784, 400], "w_h")
        w_h2 = init_weights([400, 100], "w_h2")
        w_o = init_weights([100, 10], "w_o")

        p_keep_input = tf.placeholder("float", name="p_keep_input")
        p_keep_hidden = tf.placeholder("float", name="p_keep_hidden")
        py_x = model(X, w_h, w_h2, w_o, p_keep_input, p_keep_hidden)

        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=py_x, labels=Y))
        train_op = tf.train.RMSPropOptimizer(0.001, 0.9).minimize(cost)

        correct_pred = tf.equal(tf.argmax(Y, 1), tf.argmax(py_x, 1)) # Count correct predictions
        acc_op = tf.reduce_mean(tf.cast(correct_pred, "float")) # Cast boolean to float to average

        init = tf.global_variables_initializer()
        sess = tf.Session()
        sess.run(init)

        for i in range(100):
            for start, end in zip(range(0, len(trX), 128), range(128, len(trX)+1, 128)):
                sess.run(train_op, feed_dict={X: trX[start:end], Y: trY[start:end], p_keep_input: 0.8, p_keep_hidden: 0.5})
        accuracy_value = sess.run(acc_op, feed_dict={X: teX, Y: teY, p_keep_input: 1.0, p_keep_hidden: 1.0})
        accuracy_list[int(noise_coef*len(noise_coef_list)+0.5)] = accuracy_value

    print noise_coef_list
    print accuracy_list
    plt.figure(figsize=(12, 6))
    plt.plot(noise_coef_list, accuracy_list, color='blue', linestyle='-', linewidth=2, label='Accuracy')
    plt.legend(loc='upper right')
    plt.savefig('img/mnist_noise_accuracy_tf_single_layer.png')
    f = open('accuracy_tf.txt', 'a')
    f.write('mnist_noise_tf_multi_layers:\n')
    f.write(str(accuracy_list))
    f.write('\n')
    f.close()



#############################################################

def init_weights_m(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))

def model_m(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden):
    l1a = tf.nn.relu(tf.nn.conv2d(X, w,                       # l1a shape=(?, 28, 28, 32)
                        strides=[1, 1, 1, 1], padding='SAME'))
    l1 = tf.nn.max_pool(l1a, ksize=[1, 2, 2, 1],              # l1 shape=(?, 14, 14, 32)
                        strides=[1, 2, 2, 1], padding='SAME')
    l1 = tf.nn.dropout(l1, p_keep_conv)

    l2a = tf.nn.relu(tf.nn.conv2d(l1, w2,                     # l2a shape=(?, 14, 14, 64)
                        strides=[1, 1, 1, 1], padding='SAME'))
    l2 = tf.nn.max_pool(l2a, ksize=[1, 2, 2, 1],              # l2 shape=(?, 7, 7, 64)
                        strides=[1, 2, 2, 1], padding='SAME')
    l2 = tf.nn.dropout(l2, p_keep_conv)

    l3a = tf.nn.relu(tf.nn.conv2d(l2, w3,                     # l3a shape=(?, 7, 7, 128)
                        strides=[1, 1, 1, 1], padding='SAME'))
    l3 = tf.nn.max_pool(l3a, ksize=[1, 2, 2, 1],              # l3 shape=(?, 4, 4, 128)
                        strides=[1, 2, 2, 1], padding='SAME')
    l3 = tf.reshape(l3, [-1, w4.get_shape().as_list()[0]])    # reshape to (?, 2048)
    l3 = tf.nn.dropout(l3, p_keep_conv)

    l4 = tf.nn.relu(tf.matmul(l3, w4))
    l4 = tf.nn.dropout(l4, p_keep_hidden)

    pyx = tf.matmul(l4, w_o)
    return pyx


def mnist_noise_tf_conv_networks():
    batch_size = 128
    test_size = 256
    noise_coef_list = np.arange(0.45, 1.0, 0.05)
    accuracy_list = np.empty((len(noise_coef_list)), dtype = np.float)
    for noise_coef in noise_coef_list:
        mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
        mnist = rebuild_image_data(noise_coef, mnist)
        trX, trY, teX, teY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels
        trX = trX.reshape(-1, 28, 28, 1)  # 28x28x1 input img
        teX = teX.reshape(-1, 28, 28, 1)  # 28x28x1 input img

        X = tf.placeholder("float", [None, 28, 28, 1])
        Y = tf.placeholder("float", [None, 10])

        w = init_weights_m([3, 3, 1, 32])       # 3x3x1 conv, 32 outputs
        w2 = init_weights_m([3, 3, 32, 64])     # 3x3x32 conv, 64 outputs
        w3 = init_weights_m([3, 3, 64, 128])    # 3x3x32 conv, 128 outputs
        w4 = init_weights_m([128 * 4 * 4, 625]) # FC 128 * 4 * 4 inputs, 625 outputs
        w_o = init_weights_m([625, 10])         # FC 625 inputs, 10 outputs (labels)

        p_keep_conv = tf.placeholder("float")
        p_keep_hidden = tf.placeholder("float")
        py_x = model_m(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden)

        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=py_x, labels=Y))
        train_op = tf.train.RMSPropOptimizer(0.001, 0.9).minimize(cost)
        correct_pred = tf.equal(tf.argmax(Y, 1), tf.argmax(py_x, 1)) # Count correct predictions
        acc_op = tf.reduce_mean(tf.cast(correct_pred, "float")) # Cast boolean to float to average

        # Launch the graph in a session
        with tf.Session() as sess:
            # you need to initialize all variables
            tf.global_variables_initializer().run()
            accuracy_value = 0.0
            accuracy_array = []
            for i in range(100):
                print("noise_coef = " + str(noise_coef) + ", " + str(i) + " of 100 batches")
                training_batch = zip(range(0, len(trX), batch_size), range(batch_size, len(trX)+1, batch_size))
                for start, end in training_batch:
                    sess.run(train_op, feed_dict={X: trX[start:end], Y: trY[start:end], p_keep_conv: 0.8, p_keep_hidden: 0.5})


                test_indices = np.arange(len(teX)) # Get A Test Batch
                np.random.shuffle(test_indices)
                test_indices = test_indices[0:test_size]

                accuracy_value = sess.run(acc_op, feed_dict={X: teX[test_indices], Y: teY[test_indices], p_keep_conv: 1.0, p_keep_hidden: 1.0})
                accuracy_array.append(accuracy_value)
            f = open('accuracy_tf_a.txt', 'a')
            f.write('mnist_noise_tf_conv_networks:\n')
            f.write("noise_coef = " + str(noise_coef) + ", " + "accuracy_array = " + str(accuracy_array) + ", last = " + str(accuracy_value))
            f.write('\n')
            f.close()

            accuracy_list[int(noise_coef*len(noise_coef_list)+0.5)] = accuracy_value

    print noise_coef_list
    print accuracy_list
    plt.figure(figsize=(12, 6))
    plt.plot(noise_coef_list, accuracy_list, color='blue', linestyle='-', linewidth=2, label='Accuracy')
    plt.legend(loc='upper right')
    plt.savefig('img/mnist_noise_accuracy_tf_conv_networks.png')
    f = open('accuracy_tf_a.txt', 'a')
    f.write('mnist_noise_tf_conv_networks:\n')
    f.write(str(accuracy_list))
    f.write('\n')
    f.close()


        
#mnist_noise_tf_single_layer()
#mnist_noise_tf_multi_layers()
mnist_noise_tf_conv_networks()
