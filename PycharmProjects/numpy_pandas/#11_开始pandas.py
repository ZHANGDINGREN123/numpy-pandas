import pandas as pd
import numpy as np
from pandas import DataFrame
#左边自动生成index,右边对应value
s = pd.Series([1, 3, 4, np.nan, 44, 1])#np.nan：none

print(s)
dates = pd.date_range('20160101', periods=6)#日期函数
print(dates)

#数据为np.random(6, 4),行索引为dates,列索引为['a', 'b', 'c', 'd']
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)

#以字典形式写入DataFrame():'A'~'F'(key)表示列名,value表示列中的值
df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
print(df2)
print(df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)
print("##############################")
print(df2.describe())#只能运算数字，所以忽略了'B''E''F'列
print(df2.T)#转置
print(df2.sort_index(axis=1,ascending=False))#按照列标签/索引(axis=1),进行倒序排序(ascending=False)
print(df2.sort_index(axis=0,ascending=True))#按照行标签/索引(axis=0),进行倒序排序(ascending=False)
print("##############################")
print(df2.sort_values(by='E'))#按照表中内容eg:by='E'(列'E')中内容进行排序