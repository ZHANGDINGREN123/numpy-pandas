#coding=utf-8
import numpy as np
x = np.linspace(0,2*np.pi,10) #分成10等分
y = np.sin(x) #对每一个x中的元素求正弦值
print(y)
t = np.sin(x, x)
print(x)
print(t)

#id()返回对象的内存地址,即比较t,x,y的内存地址
print(id(t) == id(x))
print(id(t) == id(y))
print("####################################")
#add函数
a = np.arange(0,4)
print(a)
b=np.arange(1,5)
print(b)
print(np.add(a,b))
print(np.add(a,b,a))
print(a)
# 针对形状不同的俩个数组计算，进行广播处理
a =np.arange(0, 60, 10).reshape(-1,1)#-1表示系统自动匹配.
print(a)
print(a.shape)
b = np.arange(0,5)
print(b)
print(b.shape)
c = b + a
print(c)#由于a(6,1)跟b(5,)的维数不同，会直接进行广播处理，也就是要让数组b的shape属性向数组靠齐，shape属性中不足的部分通过在前面加1补齐
print(c.shape)
#进行广播运算的数组的ogrid对象
x,y=np.ogrid[0:5,0:5]#x为(5,1),y为(1,5)
print(x)
print(y)
print(x + y)
x,y=np.ogrid[0:12:4, 0:9:3j]#跟linspace很像
print(x)
print(y)
print(x + y)
