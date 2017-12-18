 #-*- coding: utf-8 -*-
"""
Created on Sat Oct 07 13:03:09 2017

@author: 93138
"""

import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
filefullpath = r"C:\Users\admin\Desktop\123.xlsx"
df= pd.read_excel(filefullpath)
print(df.head())
print(df[df['group']==1])
A= df[df['group']==1]['scoreA']
B= df[df['group']==2]['scoreA']
print ttest_ind(A,B)#进行t检验
from scipy.stats import levene
A=df[df['group']==1]['scoreA']
B=df[df['group']==2]['scoreA']
print levene(A,B)#检验俩组数据的方差齐性
A=df[df['group']==1][['scoreA','scoreB']]
B=df[df['group']==2][['scoreA','scoreB']]
print(A)
print(B)
print ttest_ind(A,B,equal_var=True)#方差齐次
print ttest_ind(A,B,equal_var=False)#方差非齐时

