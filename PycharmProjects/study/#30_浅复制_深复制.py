import copy
a = [1, 2, 3]
b = a
print(id(a), id(b))
print(a, b)
a[2] = 100
print(a, b)
print(id(a) == id(b))

c = copy.copy(a)#浅拷贝
print(a, c)
a[0] = 999
print(a, c)
print(id(a) == id(c))
print('\n##########浅拷贝##########')
d = [1, 2, [3, 4]]
e = copy.copy(d)#浅拷贝
print(id(d) == id(e))
print(id(d[2]) == id(e[2]))
print(d, e)
d[0] = 100
print(d, e)
d[2][0] = 666
print(d, e)
print('\n###########深拷贝########')
d = [1, 2, [3, 4]]
f = copy.deepcopy(d)#深拷贝,内存地址完全不同,改变其中一个变量值，另一个变量对应的值不会发生任何改变
print(id(d) == id(f))
print(id(d[2]) == id(e[2]))
print(d, f)
d[0] = 100
print(d, f)
d[2][0] = 666
print(d, f)



