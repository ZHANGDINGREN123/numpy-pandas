#有错误进入except，沒有错误进入else(12行)
try:
    file = open('eeee.txt','r+')#没有名为eeee.txt的文件
except Exception as e:
    print(e)#系统显示的错误信息
    print('there is no file named as eeee.txt')
    response = input('do you want to create a new file?\n')
    if response == 'y':
        file = open('eeee.txt', 'w')#创建名为eeee.txt的文件
    else:
        pass
else:
    file.write('ssss')
file.close()
