#coding=utf-8
import tensorflow as tf

#设定state为变量，初始值为0,名字为counter
state = tf.Variable(0, name='counter')
# print state.name
one = tf.constant(1)

new_value = tf.add(state, one)

#更新state的值为new_value
update = tf.assign(state,new_value)

init = tf.initialize_all_variables()#must hace if define variable

with tf.Session() as sess:
    sess.run(init)#must hace if define variable
    for _ in range(3):
        sess.run(update)
        print sess.run(state)