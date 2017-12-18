import pandas as pd
import numpy as np

#concatenating
df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])
print(df1)
print(df2)
print(df3)
res = pd.concat([df1, df2, df3], axis=0)
print(res)

#ignore_index=True：忽略以前的行标签,重新定义
res1 = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res1)

# print("1.##################################")
#join,['inner','outer']
# df4 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'],
#                    index=[1, 2, 3])
# df5 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'],
#                    index=[2, 3, 4])
# print(df4)
# print(df5)
# res2 = pd.concat([df4, df5], join='outer')#默认join='outer'
# print(res2)

#inner：显示df4.df5共有的列标签,其余裁减掉
# res3 = pd.concat([df4, df5], join='inner', ignore_index=True)
# print(res3)


# print("2.##################################")
# #join_axes
# df6 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'],
#                    index=[1, 2, 3])
# df7 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'],
#                    index=[2, 3, 4])
#
# #进行across合并
# res4 = pd.concat([df6, df7], axis=1)
# print(res4)
#
# #按照df6的index进行across合并
# res5 = pd.concat([df6, df7], axis=1, join_axes=[df6.index])
# print(res5)


print("3.##################################")
df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'],
                   index=[2, 3, 4])
res6 = df1.append(df2, ignore_index=True)
print(res6)
res7 = df1.append([df2, df3])
print(res7)

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res8 = df1.append(s1, ignore_index=True)
print(res8)


