# -*- coding: utf-8 -*-
"""
Created on Sat Oct 07 20:05:09 2017

@author: 93138
"""

from scipy import stats
import pandas as pd
import numpy as np
#fpath = r"C:\Users\93138\Desktop\1234.txt"
# 路径中不能有中文？??
#fpath = r'C:/Users/hzy/Desktop/PythonL/大数据项目组/数据分析篇/1234.txt'
fpath = r'C:/Users/hzy/Desktop/1234.txt'
df= pd.read_csv(fpath,header=None,names=['value','group'])
print(df)
d1=df[df['group']==1]['value']
d2=df[df['group']==2]['value']
d3=df[df['group']==3]['value']
args=[d1,d2,d3]
#函数levene判断方差是否是齐性的（即判断方差是否相等）
w,p=stats.levene(*args)
print(w,p)
if p<0.05:
    print u'警告：Levene Test显示方差齐性假设不成立'
f,p=stats.f_oneway(*args)
print(f,p)
g=df['group'].unique()
print(g)
args=[]
for i in list(g):
    args.append(df[df['group']==i]['value'])
f,p=stats.f_oneway(*args)
print f,p
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
anova_results=anova_lm(ols('value~C(group)',df).fit())#~隔离因变量，根据公式数据建模，拟合，计算p，f
print anova_results
    
