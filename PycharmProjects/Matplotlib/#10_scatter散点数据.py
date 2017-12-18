import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)#生成n个平均值为0，方差为1的数据
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)#装饰颜色
#大小：s = 75,颜色：c = T
plt.scatter(X, Y, s = 75, c = T, alpha = 0.5)
#plt.scatter(np.arange(5), np.arange(5))
plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))

#去除坐标轴上的数
plt.xticks(())
plt.yticks(())

plt.show()