import numpy as np
A = np.arange(3, 15)
print(A)
print(A[3])#输出一维向量A下标3的对应值

a = np.arange(3, 15).reshape((3, 4))
print(a)
print(a[2][2])#输出矩阵A下标[2][2]的对应值
print(a[2, 2])#输出矩阵A下标[2][2]的对应值
print(a[:, 1])#输出矩阵A第一列所有元素
print(a[1, 1:3])#输出矩阵A第一行的一到三列的元素（即第一列和第二列）
print('#################\n')
for row in a:#逐行输出矩阵a
    print(row)
for column in a.T:#逐列输出矩阵a
    print(column)

print(a.flatten())#将矩阵a变成1*12向量
for item in a.flat:#将矩阵a变成1*12向量,并逐个输出
    print(item)
