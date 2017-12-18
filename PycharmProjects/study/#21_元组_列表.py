a_tuple = (12, 3, 4, 15, 6)
another_tunple = 2, 4, 6, 7, 8

a_list = [12, 3, 67, 7, 82]

for content in a_list:
    print(content)
print('\n')
for content in a_tuple:
    print(content)
print('\n')
for index in range(len(another_tunple)):
    print('index = ', index, 'number in another_tunple = ', another_tunple[index])