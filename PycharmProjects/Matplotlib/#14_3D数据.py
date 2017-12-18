import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)#添加3维坐标轴

#X,Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)#在x,y轴绘制X,Y
R = np.sqrt(X ** 2 + Y ** 2)

#height value
Z = np.sin(R)

#rstride=5, cstride=5：对应网格行密度与列密度,值越小密度越大
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))

#zdir='z',将3D图压沿z轴压;offset=-2：沿z轴压到-2处
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
ax.set_zlim(-2, 2)

plt.show()