# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:22:05 2017

@author: 93138
"""

from scipy import stats
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

treatment = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]    #处理 变量 
gender    = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]    #性别
loss      = [76,78,76,76,76,74,74,76,76,55,65,90,65,90,65,90,90,79,70,90, 88,76,76,76,56,76,76,98,88,78,65,67,67,87,78,56,54,56,54,56]  #体重减少 

data = {'T':treatment, 'G':gender, 'L':loss}
df = pd.DataFrame(data)
formula = 'L~T+G+T:G'                           #~ 隔离因变量和自变量 (左边因变量，右边自变量 )
                                                #+ 分隔各个自变量， :表示两个自变量交互影响 
model = ols(formula,df).fit()                   # 根据公式数据建模，拟合
results = anova_lm(model)                       # 计算F和P
print results