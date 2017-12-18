# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 16:12:34 2017

@author: 93138
"""
from scipy import stats
import pandas as pd
import numpy as np
fpath = r"C:\Users\93138\Desktop\1.txt"
df= pd.read_csv(fpath,header=None,names=['hs','fetus','observer'])
print(df)
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
formula='hs~C(fetus)+C(observer)+C(fetus):C(observer)'#~隔离因变量，+分隔各个自变量，:表示两个自变量交互影响 
anova_results=anova_lm(ols(formula,df).fit())
print anova_results
from statsmodels.stats.multicomp import pairwise_tukeyhsd
hsd=pairwise_tukeyhsd(df['hs'],df['fetus'])
print hsd.summary()