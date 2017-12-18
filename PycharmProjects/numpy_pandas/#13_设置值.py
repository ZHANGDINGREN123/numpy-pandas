import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)),
                  index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
df.iloc[2, 2] = 1111#根据位置修改值
df.loc['20130101', 'B'] = 2222#根据标签修改值
df.ix['20130106', 3] = 3333#根据位置或标签修改值
print(df)
df.A[df.A>4] = 0#'A'列大于4的值修改为0
print(df)
df[df.A==4] = 0#'A'列=4的元素所对应的行的各个元素变为0
print(df)
print("###########################")
df['F'] = np.nan#添加'F'列
#添加一个序列
df['E'] = pd.Series([1, 2, 3, 4, 5, 6],
                    index=pd.date_range('20130101',periods=6))
print(df)