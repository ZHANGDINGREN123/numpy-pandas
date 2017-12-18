# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:53:44 2017

@author: 93138
"""

import pandas as pd
from io import StringIO
from sklearn import linear_model
import matplotlib.pyplot as plt
fpath = "2.txt"
df = pd.read_csv(fpath, header=None, names=['square_feet', 'price',])
r = df['square_feet'].corr(df['price'])#求出相关系数
print r
print(df)
regr = linear_model.LinearRegression()#建立线性回归模型
regr.fit(df['square_feet'].reshape(-1, 1), df['price'].reshape(-1, 1))#拟合数据
a,b = regr.coef_,regr.intercept_#得到直线的斜率与截距
print a, b

area = 238.5#给出待预测面积
print(regr.predict(area))#得到预测价格
plt.scatter(df['square_feet'], df['price'], color='blue')#画出真实点
plt.plot(df['square_feet'], regr.predict(df['square_feet'].reshape(-1,1)), color='red', linewidth=4)#拟合直线
plt.show()

