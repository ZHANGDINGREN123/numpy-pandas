#coding=utf-8
# import numpy
# print numpy.__version__;print numpy.__file__
import numpy as np
import tensorflow as tf

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

### create tensorflow structure start ###
# 初始化神经网络结构

#将Weights定义为变量Variable()，并设置为一个随机的一维的范围在-1~1的值
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
#将biases初始值定义为0
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

# 定义损失函数
loss = tf.reduce_mean(tf.square(y - y_data))

# 随机梯度下降法训练，学习率0.5
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
### create tensorflow structure end ###

# 激活神经网络
sess = tf.Session()
sess.run(init) #very important

for step in range(201):
    sess.run(train)
    if step%20 == 0:
        # Weights和biases是张量，不能直接输出，只能通过sess.run()输出
        print step,sess.run(Weights),sess.run(biases)

