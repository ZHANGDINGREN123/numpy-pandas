a = [1, 2, 3]
b = [4, 5, 6]
print(zip(a, b))
print(list(zip(a, b)))#可视化观察zip(a, b)
for i,j in zip(a, b):
    print(i/2, j*2)

print('################')
print(list(zip(a,b,a)))#zip可以合并多个

def fun1(x,y):
    return (x + y)
print(fun1(5, 6))

fun2 = lambda x,y:x + y#lambda
print(fun2(2, 3))

print('################')
print(map(fun1, [1], [2]))
print(list(map(fun1, [10], [34])))#可视化观察map(fun1, [1], [2]),map:用fun1运算参数[x = 10][y = 34]

print(list(map(fun1, [10, 1, 999], [34, 11, 1])))#多个参数也可以

