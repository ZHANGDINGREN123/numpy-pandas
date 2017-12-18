# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 18:25:14 2017

@author: admin
"""
import numpy as np
from scipy.optimize import leastsq
import pylab as pl
def func(x,p):
    A,K,theta=p
    return A*np.sin(2*np.pi*K*x+theta)#数据拟合所用函数
def residuals(p,y,x):#实验数据下x,y和拟合函数之间的差，即残差，p为拟合需要找到的系数
    return y-func(x,p)
x=np.linspace(0,-2*np.pi,100)
A,K,theta=10,0.34,np.pi/6#真实数据的函数参数
y0=func(x,[A,K,theta])#真实数据
y1=y0+2*np.random.randn(len(x))#加入噪声之后的实验数据
p0=[7,0.2,0]#第一次猜测的函数拟合参数
plaq=leastsq(residuals,p0,args=(y1,x))#调用leastsq进行数据拟合，residuals为计算误差的函数，po为拟合参数的初始值，args为形参数据，需要拟合的实验数据
print(u"真实参数：",[A,K,theta])
print(u"拟合参数：",plaq[0])#实验数据拟合后的参数
pl.plot(x,y0,label=r"$真实数据$")
pl.plot(x,y1,label=r"$带噪声的实验数据$")
pl.plot(x,func(x,plaq[0]),label=r"$拟合数据$")
pl.legend()
pl.show()
