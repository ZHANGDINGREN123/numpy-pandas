char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
print(set(char_list))#去除重复的元素
print(type(set(char_list)))
print(type({1:2}))


print('##########################')
sentence = 'Welcome Back to This Tutirial'
print(set(sentence))
#print(set(char_list, sentence))#只能传单个列表

unique_char = set(char_list)

set1 = unique_char
set2 = {'a', 'e', 'i'}
print(set1.difference(set2))#在set2中找到与set1不同的元素并输出
print(set1.intersection(set2))#在set2中找到与set1相同同的元素并输出

unique_char.add('x')
#unique_char.add('a', 'd')#只能加单个元素
print(unique_char)
unique_char.remove('x')
print(unique_char)
unique_char.clear()
print(unique_char)#输出set()，表示列表为空（已经清空）
