#coding=utf-8
import tensorflow as tf

# input1 = tf.placeholder(tf.float32,[2,2])如需定义两行两列的input1则用改句
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)

with tf.Session() as sess:
    # 使用placeholder则要在sess.run()时使用feed_dict(通过字典为input1和input2赋值)
    print sess.run(output,feed_dict={input1:[7.],input2:[2.]})