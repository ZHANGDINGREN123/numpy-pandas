#coding uft_8
import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(b)
print(c)
print(c.shape)
c.shape=4,3 #改变数组元素个数不变改变每个轴的长度。并不是转置
print(c)
c.shape=2,-1 #设轴元素为-1，系统自动计算轴长度
print(c)
d=a.reshape((2,2)) #可以创建了一个改变了尺寸的新数组，原数据不变
print(d)
print(a)#y原数组不发生改变


