a_list = (1, 2, 3, 4, 5)#列表
dic = {'apple':1, 'pear':2, 'orange':3}#字典 = {key:内容}
#dic2 = {1:'a', 'c':'b'}#格式正确
print(dic['apple'])
print(dic)
del dic['pear']
print(dic)
dic[123] = 20
print(dic)
print(dic[123])

d = {'apple':1, 'pear':{1:3,3:'a'}, 'orange':3}
print(d['pear'][3])