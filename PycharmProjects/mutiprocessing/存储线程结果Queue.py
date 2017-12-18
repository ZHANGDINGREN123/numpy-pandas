#coding=utf-8
import threading
import time
from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i] =l[i]**2
    q.put(l)#多线程调用的函数不能使用return返回值

def multithreading(data):
    q = Queue() #q中存放返回值，代替return的返回值
    threads =[]
    data=[[1,2,3],[2,2,3][3,3,3][4,4,4]]
    for i in range(4):#定义四个线程
        t=threading.Thread(target=job,args=(data[i],q))#Thread首字母大写，
        t.start()
        threads.append(t)#把每个线程append到线程表中
    for thread in threads:
        thread.join()
    results =[]
    for _ in range(4):
        results.append(q.get())#q.get（）按顺序从q中拿出一个值
    print (results)
if __name__ == '__main__':
   multithreading()