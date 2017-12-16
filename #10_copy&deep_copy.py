import numpy as np
a = np.arange(4)
print(a)
b = a#浅拷贝
c = a
d = b
a[0] = 11
print(a, b, c, d)#b,c,d is a
d[1:3] = [22, 33]
print(a, b, c, d)#b,c,d is a
print('#################')
b = a.copy()#深拷贝
a[3] = 44
print(a, b)