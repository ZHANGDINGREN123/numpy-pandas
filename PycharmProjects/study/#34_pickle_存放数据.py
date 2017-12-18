import pickle
a_dict = {'da':111, 2:[23, 1, 4], '23':{1:2, 'd':'sad'}}
file = open('pickle_example.pickle', 'wb')
pickle.dump(a_dict,file)#将a_dict中内容dump到file指向的文件pickle_example.pickle
file.close()

#############################
#方法1 = 方法2

#方法1
file = open('pickle_example.pickle', 'rb')
b_dict = pickle.load(file)#将文件中的内容load到b_dic字典当中
file.close()

#方法2
with open('pickle_example.pickle', 'rb') as file:#将文件中的内容load到b_dic字典当中
    b_dict = pickle.load(file)


print(b_dict)