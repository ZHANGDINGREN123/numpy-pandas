# 引入相关模块
# - * - coding: utf- 8- * -
from scipy import stats
import pandas as pd
import numpy as np

# 读取数据，数据保存在text文件中，就是两列数据，列之间用逗号隔开
# 参数header=None指的是数据头部没有标题，names参数制定列的名称
# 数据存放在C:\python27\python\data\目录下
fPath = 'C:\\python27\\python\\data\\单因素方差分析数据.txt'
df = pd.read_csv(fPath, header=None, names=['value', 'group'])
print(df)

# 数据分组，因为数据中group列有三个值表示数据来自不同的组
d1 = df[df['group'] == 1]['value']
d2 = df[df['group'] == 2]['value']
d3 = df[df['group'] == 3]['value']

# 使用* args参数
args = [d1, d2, d3]

# 首先进行levene test
# 如果p小于0.05，就警告方差不齐
w, p = stats.levene(*args)
if p < 0.05:
    print u'警告：Levene Test显示方差齐性假设不成立(p= % .2f)' % p

# 方差分析
f, p = stats.f_oneway(*args)
print(f, p)

# 如果不知道数据分成几组，可以自动生成
g = df['group'].unique()  # 返回唯一值
print g
args = []
for i in list(g):
    agrs.append(df[df['group'] == i]['value'])
f,p=stats.f_oneway(* args)
print(f,p)

#pandas中更好的方式
#熟悉Stasmodels的可以用它来输出更全面的结果
import statsmodels.api as sm
from statsmodels.formula.api import ols
moore=sm.datasets.get_rdataset("moore","car",cache=True)
data=moore.data
data=data.rename(columns={"partner.status":
                          "partner_status"})
moore_lm=ols('conformity~C(factegory,Sum)*C(partner_status,Sum)',data=data).fit()
table=sm.stats.anova_lm(moore_lm,typ=2)
print table











