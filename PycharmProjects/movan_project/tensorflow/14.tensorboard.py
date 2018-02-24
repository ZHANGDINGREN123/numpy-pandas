#coding=utf-8

import tensorflow as tf
import numpy as np
# import matplotlib.pyplot as plt

def add_layer(inputs, in_size, out_size, activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('Weight'):
            # Weights为随机生成in_size行，out_size列的随机矩阵
            Weights = tf.Variable(tf.random_normal([in_size,out_size]), name='W')
        with tf.name_scope('biases'):
            # biases定义为1行，out_size列的矩阵(向量)
            biases = tf.Variable(tf.zeros([1,out_size]) + 0.1, name='b')
        with tf.name_scope('Wx_plus_b'):
            # wx + b
            Wx_plus_b = tf.matmul(inputs,Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs

# 创建数据
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
#添加均值为0，方差为0.05,形状与x_data相同的噪声
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

#定义NONE行，1列的xs,ys  NONE表示样本数木无所谓
with tf.name_scope('inputs'):#Tensorboard中大框架名
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
predition = add_layer(l1, 10, 1, activation_function=None)


# 损失函数
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - predition),
                         reduction_indices=[1]))

with tf.name_scope('train'):
    # 梯度下降:学习率:0.1
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()
# terminal进入.py文件的路径输入:tensorboard --logdir='logs/'
writer = tf.summary.FileWriter("logs/", sess.graph)#必须有此步才有效
sess.run(init)




