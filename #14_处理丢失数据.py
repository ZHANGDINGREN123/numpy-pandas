import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)),
                  index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)

#how={'any','all'}:默认为any；若设置为all，则只有该行(axis=0)或该列(axis=1)全部为NAN才删除该行或列
print(df.dropna(axis=0, how='any'))#若某一行含有NAN，则丢弃该行
print(df.dropna(axis=1, how='any'))#若某一列含有NAN，则丢弃该列

print(df.fillna(value=0))#若df含有NAN，则填充为0
print(np.any(df.isnull()) == True)#若至少有一个(np.any())数据为NAN,则返回True
