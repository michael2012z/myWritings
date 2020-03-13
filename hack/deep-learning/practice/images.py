import os
import numpy as np
from PIL import Image
from tensorflow.contrib.learn.python.learn.datasets import base
from tensorflow.python.framework import dtypes
import tensorflow as tf


class DataSet(object):

  def __init__(self,
               images,
               labels,
               fake_data=False,
               one_hot=False,
               dtype=dtypes.float32,
               reshape=True):
    """Construct a DataSet.
    one_hot arg is used only if fake_data is true.  `dtype` can be either
    `uint8` to leave the input as `[0, 255]`, or `float32` to rescale into
    `[0, 1]`.
    """
    dtype = dtypes.as_dtype(dtype).base_dtype
    if dtype not in (dtypes.uint8, dtypes.float32):
      raise TypeError('Invalid image dtype %r, expected uint8 or float32' %
                      dtype)
    if fake_data:
      self._num_examples = 10000
      self.one_hot = one_hot
    else:
      assert images.shape[0] == labels.shape[0], (
          'images.shape: %s labels.shape: %s' % (images.shape, labels.shape))
      self._num_examples = images.shape[0]

      # Convert shape from [num examples, rows, columns, depth]
      # to [num examples, rows*columns] (assuming depth == 1)
      if reshape:
        assert images.shape[3] == 1
        images = images.reshape(images.shape[0],
                                images.shape[1] * images.shape[2])
      if dtype == dtypes.float32:
        # Convert from [0, 255] -> [0.0, 1.0].
        images = images.astype(np.float32)
        images = np.multiply(images, 1.0 / 255.0)
    self._images = images
    self._labels = labels
    self._epochs_completed = 0
    self._index_in_epoch = 0

  @property
  def images(self):
    return self._images

  @property
  def labels(self):
    return self._labels

  @property
  def num_examples(self):
    return self._num_examples

  @property
  def epochs_completed(self):
    return self._epochs_completed

  def next_batch(self, batch_size, fake_data=False):
    """Return the next `batch_size` examples from this data set."""
    if fake_data:
      fake_image = [1] * 784
      if self.one_hot:
        fake_label = [1] + [0] * 9
      else:
        fake_label = 0
      return [fake_image for _ in xrange(batch_size)], [
          fake_label for _ in xrange(batch_size)
      ]
    start = self._index_in_epoch
    self._index_in_epoch += batch_size
    if self._index_in_epoch > self._num_examples:
      # Finished epoch
      self._epochs_completed += 1
      # Shuffle the data
      perm = np.arange(self._num_examples)
      np.random.shuffle(perm)
      self._images = self._images[perm]
      self._labels = self._labels[perm]
      # Start next epoch
      start = 0
      self._index_in_epoch = batch_size
      assert batch_size <= self._num_examples
    end = self._index_in_epoch
    return self._images[start:end], self._labels[start:end]





def bytesToInt(bytes):
    l = np.zeros(len(bytes),  dtype=np.int8 )
    for i in range(len(bytes)):
        l[i] = int(bytes[i].encode('hex'), 16)
    return l

def imgToData(f):
    im = Image.open(f)
    imx = im.resize((280, 320))
    imy = imx.convert('L')
    return bytesToInt(imy.tobytes())





retouch_files = os.listdir(os.getcwd() + '/img/retouch')
nonretouch_files = os.listdir(os.getcwd() + '/img/non-retouch')
retouch_dataset = None
nonretouch_dataset = None

for retouch_file in retouch_files:
    print "handling file " + retouch_file
    data = imgToData(os.getcwd() + '/img/retouch/' + retouch_file)
    if retouch_dataset == None:
        retouch_dataset = data
    else:
        retouch_dataset = np.concatenate((retouch_dataset, data))
        
for nonretouch_file in nonretouch_files:
    print "handling file " + nonretouch_file
    data = imgToData(os.getcwd() + '/img/non-retouch/' + nonretouch_file)
    if nonretouch_dataset == None:
        nonretouch_dataset = data
    else:
        nonretouch_dataset = np.concatenate((nonretouch_dataset, data))

retouch_dataset = retouch_dataset.reshape((-1, 280, 320, 1))
retouch_labels = np.array([1, 0]*(len(retouch_dataset))).reshape((-1, 2))
nonretouch_dataset =  nonretouch_dataset.reshape((-1, 280, 320, 1))
nonretouch_labels = np.array([0, 1]*(len(retouch_dataset))).reshape((-1, 2))

all_images = np.concatenate((retouch_dataset, nonretouch_dataset))
all_labels = np.concatenate((retouch_labels, nonretouch_labels))

all_images = all_images.reshape((-1, 280*320))
all_labels = all_labels.reshape((-1, 2))
print all_images.shape, all_labels.shape
all_shuffle = np.column_stack((all_images, all_labels))
np.random.shuffle(all_shuffle)
all_images = all_shuffle[:,:280*320].reshape((-1, 280, 320, 1))

all_labels = all_shuffle[:,-2:].reshape((-1, 2))

validation_size = int(len(all_images)*0.15)
test_size = int(len(all_images)*0.15)
train_size = len(all_images) - validation_size - test_size

train_images = all_images[:train_size]
train_labels = all_labels[:train_size]
validation_images = all_images[train_size:train_size+validation_size]
validation_labels = all_labels[train_size:train_size+validation_size]
test_images = all_images[train_size+validation_size:]
test_labels = all_labels[train_size+validation_size:]

dtype=dtypes.float32
reshape=True

train = DataSet(train_images, train_labels, dtype=dtype, reshape=reshape)

validation = DataSet(validation_images,
                     validation_labels,
                     dtype=dtype,
                     reshape=reshape)
test = DataSet(test_images, test_labels, dtype=dtype, reshape=reshape)

datasets = base.Datasets(train=train, validation=validation, test=test)




mnist = datasets
x = tf.placeholder(tf.float32, [None, 280*320])
W = tf.Variable(tf.zeros([280*320, 2]))
b = tf.Variable(tf.zeros([2]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 2])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(mnist.train.num_examples):
  batch_xs, batch_ys = mnist.train.next_batch(1)
  #print batch_xs, batch_ys
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
accuracy_value = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
#print mnist.test.num_examples
print accuracy_value

