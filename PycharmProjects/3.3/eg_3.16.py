import numpy as np
a = np.array([[8, 7, 6],
              [6, 5, 4],2012226052  730310num
              [3, 2, 1]])
print(a)
print(np.max(a,axis=0))#矩阵a每列元素最大值
print(np.max(a,axis=1))#矩阵a每行元素最大值
print(np.mean(a,axis=0))#矩阵a每列元素平均值
print(np.median(a,axis=0))#矩阵a每列中位数
print(np.min(a,axis=0))#矩阵a每列元素最小值
print(np.std(a,axis=0))#矩阵a每列元素标准差？matlab值为2.5166
print(np.prod(a,axis=0))#矩阵a每列元素的积
print(np.sum(a,axis=0))#矩阵a每列元素的和
print(np.sort(a,axis=0))#矩阵a每列元素从小到大排
print(np.sort(a,axis=1))#矩阵a每行元素从小到大排