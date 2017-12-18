import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    # the height function(计算(x,y)点对应的高度)
    return (1 - x/2 + x**5 + y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)#定义(x,y)网格为网格输入值

# use plt.contourf to filling contours
#X, Y and value for (X, Y) point
#cmap=plt.hot():热度. 8:分成10(8+2)个圈。若将8换成0则有2个圈. plt.hot():可以换成plt.cool()
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.hot())#前三个参数为x,y,z;x,y表示网格坐标表,z表示高度

#use plt.contour to add contour lines
#等高线颜色：colors='black',宽度linewidth=0.5
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=0.5)

# adding label
# 在C上面添加数字,是否在线内=True,字体大小10
plt.clabel(C, inline=True, fontsize=10)

#去除坐标轴上的数
plt.xticks(())
plt.yticks(())

plt.show()