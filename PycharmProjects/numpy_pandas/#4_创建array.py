import numpy as np
a = np.array([[2, 23, 4],
              [2, 3, 4]], dtype=np.float)
print(a)
print(a.dtype)

b = np.zeros((3, 4), dtype=np.int)
print(b)

c = np.ones((4, 3), dtype=np.int)
print(c)

d = np.empty((4, 3))#认为np.empty()会返回全0数组的想法是不安全的，它返回的是为初始化的无用值
#eg:d = np.empty((4, 1))
print(d)

e = np.arange(10, 20, 2)#10~19,步长为2
print(e)

f = np.arange(12).reshape((3,4))#将1*12改为3*4
print(f)

g = np.linspace(1,10,20)#生成20段1~10的数列
print(g)

g1 = np.linspace(1,10,6).reshape((2,3))
print(g1)
