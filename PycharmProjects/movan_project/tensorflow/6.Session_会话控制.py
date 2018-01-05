#coding=utf-8
import tensorflow as tf

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix1,matrix2)#矩阵相乘

## method1
# sess = tf.Session()
# result = sess.run(product)
# print result
# sess.close()

# method2
#给tf.Session()起别名sess，并且可以不用执行sess.close()
with tf.Session() as sess:
    result2 = sess.run(product)
    print result2
    # sess.close()已经自动执行

