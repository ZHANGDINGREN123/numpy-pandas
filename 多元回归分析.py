# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:15:48 2017

@author: 93138
"""

import numpy as np
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
xx, yy = np.meshgrid(np.linspace(0,10,10), np.linspace(0,100,10))
zz = 1.0 * xx + 3.5 * yy + np.random.randint(0,100,(10,10))#给出数据

# 将xx,yy变为列向量并合并成zz
X, Z = np.column_stack((xx.flatten(),yy.flatten())), zz.flatten()#构建特征值
regr = linear_model.LinearRegression()#建立线性回归模型
regr.fit(X,Z)#拟合
a,b = regr.coef_,regr.intercept_#平面系数，截距
print a, b
x = np.array([[5.8,78.3]])#给出待测的一个特征
print(regr.predict(x))#得到预测值
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(xx, yy, zz)#散点图
# ax.plot_wireframe(xx, yy, regr.predict(X).reshape(10,10))#线框图
ax.plot_surface(xx, yy, regr.predict(X).reshape(10,10), alpha=0.3)
plt.show()


