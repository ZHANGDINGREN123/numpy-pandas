a = [1, 2, 3, 4, 3, 2, 1, 1]
a.append(0)#追加0
a.insert(2, 100)
print(a)
a.remove(1)#删除第一个1
print(a)
#print(a[len(a) - 1])
#print(a[-1])
print(a.index(4))#返回第一个值为4的下标
print(a.count(1))#出现1的次数

a.sort()#从小到大排序
print(a)

a.sort(reverse= True)#从大到小排序
print(a)

