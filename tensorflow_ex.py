#from tensorflow.examples.tutorials.mnist import input_data
#mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf

#Reading the CSVs is magic
filename_queue = tf.train.string_input_producer(["data_raw/f"])
reader = tf.TextLineReader(skip_header_lines=1)
key,value = reader.read(filename_queue)




with open('data_raw/f') as f:
    feat=[l.split(',') for l in f.readlines()][1:]
    x_data = [x[:-1] for x in feat]
    y_data = [[x[-1]] for x in feat]

x = tf.placeholder(tf.float32, [None, len(feat[0])-1])
W = tf.Variable(tf.zeros([len(feat[0])-1, 1]))
b = tf.Variable(tf.zeros([1]))
y = tf.matmul(x, W) + b
y_ = tf.placeholder(tf.float32, [None, 1])
raw_error = tf.reduce_mean(tf.reduce_sum(tf.abs(y_ - y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(raw_error)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(200):
      sess.run(train_step, feed_dict={x: x_data, y_: y_data})
        
#correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(tf.abs(y-y_), tf.float32))
print(sess.run(accuracy, feed_dict={x: x_data, y_: y_data}))
print sess.run(W)

