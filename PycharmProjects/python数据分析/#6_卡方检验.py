#coding=utf-8
#先引入相关模块
from pyvttbl.stats import ChiSquarelway

#实例ChiSquarelway对象
cs=ChiSquarelway()

#运行卡方检验，如果我们只输入一个参数，表示我们要检验这一列数据分布是否均匀，也就是各组频率是否相等
cs.run([1,2,3,2,2,2,2])
print(cs)

#假如我们输入两个参数，可以指定各组频数的期望值
cs.run([17,19,18,20,32,201])
expected=[10,10,10,10,10,102]
print(cs)

#对于结果，我们可以使用字典的方式读取个别值，比如卡方：
print('\nchisq')
print(cs['chisq'])


