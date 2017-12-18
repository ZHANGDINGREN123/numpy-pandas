#coding=utf-8
import multiprocessing as mp
import threading as td
def job(a, b):
    print ('aaaaa')

t1 = td.Thread(target=job, args=(2, 1))#job 输入参数添加载args后面，job后没有括号，有括号是调用）
p1 = mp.Process(target=job,args=(1, 1))
t1.start()#Process 和Thread 要大写
p1.start()#p1 开始只是定义完成，还没有开始 启动线程

#阻塞当前线程，即使得当前线程结束时，不会退出。
