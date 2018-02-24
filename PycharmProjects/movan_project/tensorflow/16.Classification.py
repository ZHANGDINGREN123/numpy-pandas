#coding=utf-8
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# number 1 to 10 data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

def add_layer(inputs, in_size, out_size, activation_function=None):
    # Weights为随机生成in_size行，out_size列的随机矩阵
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    # biases定义为1行，out_size列的矩阵(向量)
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    # wx + b
    Wx_plus_b = tf.matmul(inputs,Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

def compute_accuracy(v_xs,v_ys):
    global prediction#定义prediction为全局变量
    y_pre = sess.run(prediction, feed_dict={xs:v_xs})

    # 判断：预测的数组中概率最大的位置的数组下标(即1的位置)是否与真实值对应的位置相等
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    # 计算准确率：值为一个百分比
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    # 计算准确率使用的数据是xs:v_xs, ys:v_ys
    result = sess.run(accuracy, feed_dict={xs:v_xs, ys:v_ys})
    return result


# define placeholder for inputs to network
# 每张图片28*28=784个点
xs = tf.placeholder(tf.float32, [None,784])
# 0~9共10个输出
ys = tf.placeholder(tf.float32, [None,10])

# add output layer
prediction = add_layer(xs, 784, 10, activation_function=tf.nn.softmax)

# the error between prediction and rel data
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),
                                              reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.Session()
sess.run(tf.initialize_all_variables())


for i in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100)#分块训练：效率比整体训练高，并且结果不表
    sess.run(train_step,feed_dict={xs:batch_xs, ys:batch_ys})
    if i%50 == 0:
        print compute_accuracy(mnist.test.images,mnist.test.labels)


# 展示lines变化过程

