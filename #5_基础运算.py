import numpy as np
a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(a, b)
c = a - b
print(c)
d = a + b
print(d)
print('##################\n')
e = a**2#a的平方
print(e)

f = 10*np.sin(a)
print(f)
print(f < 0)

g = np.array([[1, 1],
              [0, 1]])
h = np.arange(4).reshape((2, 2))
print(g)
print(h)

i = g * h#矩阵对应A元素相乘

#矩阵乘法1 = 矩阵乘法2 即 j == j_2
j = np.dot(g, h)#矩阵乘法1
j_2 = g.dot(h)#矩阵乘法2
print(i)
print(j)
print(j_2)
print(np.sum(j_2))#矩阵j_2各个元素之和
print(np.min(j_2))#矩阵j_2各个元素最小值
print(np.max(j_2))#矩阵j_2各个元素最大值
print(np.sum(j_2,axis=1))#矩阵j_2每行元素之和
print(np.min(j_2,axis=0))#矩阵j_2每列元素最小值
print(np.max(j_2,axis=1))#矩阵j_2每行元素最大值


k = np.random.random((2, 4))#随机生成0~1的2*4矩阵
print(k)
