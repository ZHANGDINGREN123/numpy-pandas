import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)),
                  index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
print(df['A'], df.A)#df['A']与df.A功能相同

#df[0:3]输出0~3行(不包括第三行),输出'20130102'到'20130104'
print(df[0:3], df['20130102':'20130104'])

print("1.###########################")
#select by label:loc(标签筛选)
print(df.loc['20130102'])
#保留所有行信息筛选'A''B'列.
print(df.loc[:, ['A', 'B']])
#输出20130103及其之后行的'A''B'列.
print(df.loc['20130103':],['A', 'B'])

#select by position:iloc(数字筛选)
print(df.iloc[3])#输出第三行
print(df.iloc[3:5, 1:3])#输出第三行到第五行(不包括第五行)的第一列到第三列(不包括第三列)
print(df.iloc[[1,3,5], 1:3])#输出第一,三,五行的第一列到第三列(不包括第三列)

print("2.###########################")
#mixed selection:ix(标签与数字混合筛选)
print(df.ix[:3, ['A', 'C']])

#Boolean indexing
print(df)
print(df[df.A>8])#筛选A列中>8的行并显示出来.
