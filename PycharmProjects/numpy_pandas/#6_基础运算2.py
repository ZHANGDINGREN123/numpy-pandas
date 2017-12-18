import numpy as np
A = np.arange(2,14).reshape((3, 4))
print(A)
print(np.argmin(A))#当前矩阵最小值对应下标,即索引
print(np.argmax(A))#当前矩阵最大值对应下标,即索引

#以下两个输出皆为矩阵A所有元素的平均值
print(np.mean(A))
print(A.mean())
print(np.cumsum(A))#矩阵A累加并显示累加结果
print(np.diff(A))#矩阵A每行累差并显示累差结果
print(np.nonzero(A))#输出对应每一个下标是否为0,本例中皆为非0元素,
# (array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]), array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]))
#前一个array表示行下标,后一个array表示列下标,它们所对应元素皆为非0.

print(np.clip(A, 5, 9))#将矩阵A中所有小于5的都变成5,大于9的都变成9,其余不变

print('#################################')
a = np.array([[8, 7, 6],
              [6, 5, 4],
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
print(np.transpose(a))#矩阵a的转置
print(a.T)#矩阵a的转置
print((a.T).dot(a))#a的转置乘a
print(np.dot(a,a.T))#a乘a的转置