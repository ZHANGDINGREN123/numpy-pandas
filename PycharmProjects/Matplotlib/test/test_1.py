a = [1, 2, 3, 4, 3, 2, 1, 1]
a.append(0)#追加0
a.insert(2,100)
a.remove(1)
print(a[len(a) - 2])
print ("数组a的长度：",len(a))
print(a)
print(a[-1])

print("返回4的下标",a.index(4))
print("出现一的次数",a.count(1))
a.sort()#从小到大排序
print("从小到大排序",a)