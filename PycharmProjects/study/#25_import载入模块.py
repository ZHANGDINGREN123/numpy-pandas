#调用方式1
# import time as t#调用time包,简写为t
# print(t.localtime())

#调用方式2
# from time import time,localtime #仅从time包中调用time,localtime.
# print(localtime())
# print(time())

#调用方式3
from time import *#从time包中调用所有功能.
print(timezone)
print(time())
