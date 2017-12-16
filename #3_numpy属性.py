import numpy as np
array = np.array([[1, 2, 3],
                  [2, 3, 4]])
print(array)
print('number of dim: ', array.ndim)#几维矩阵
print('shape: ', array.shape)#几行几列
print('size: ', array.size)#总元素个数
print("############################")

a0 = np.array([1, 1, 1])
print(a0)
print(a0.shape)
print(a0.ndim)

a1 = np.array([[1, 2, 3]])
print(a1)
print(a1.shape)
print(a1.ndim)

a2 = np.zeros((2, 3))#(2, 3)形状参数
print(a2)
print(a2.shape)
print(a2.ndim)
