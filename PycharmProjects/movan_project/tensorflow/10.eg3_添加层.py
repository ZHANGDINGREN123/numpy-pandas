#coding=utf-8
import tensorflow as tf

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