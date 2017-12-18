import matplotlib.pyplot as plt
import numpy as np
n = 12#定义柱状图个数
X = np.arange(n)
Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 0.1, n)#产生值为(0.1~0.5)的n个数
Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 0.1, n)

plt.bar(X, +Y1, facecolor = '#9999ff', edgecolor = 'white')#绘制正柱状图
plt.bar(X, -Y2, facecolor = '#ff9999', edgecolor = 'white')#绘制负柱状图

for x,y in zip(X,Y1):#zip(X,Y1):把X,Y1分别赋值给x,y
    #ha:横向对齐方式. va:纵向对齐方式
    #'%.2f'% y:柱状图上显示的值
    plt.text(x + 0.4, y + 0.05, '%.2f'% y, ha='center', va='bottom')

for x,y in zip(X,Y2):#zip(X,Y2):把X,Y2分别赋值给x,y
    #ha:横向对齐方式. va:纵向对齐方式
    #(x + 0.4, y - 0.05):表示显示位置
    plt.text(x + 0.4,- y - 0.05, '-%.2f'% y, ha='center', va='top')


plt.xlim((-0.5, n))
plt.ylim((-1.25, 1.25))

#去除坐标轴上的数
plt.xticks(())
plt.yticks(())

plt.show()