#coding=utf-8
#加入进程锁之后，保证运行时一个进程的对锁内内容的独占
import multiprocessing as mp
import time
def job(v,num,l):
    l.acquire()#锁住
    for _ in range(5):
        time.sleep(0.2)
        v.value += num
        print (v.value)
    l.release()#释放
def multicore():
    l =mp.Lock()#定义一个进程锁
    v =mp.Value('i',0)
    p1 =mp.Process(target=job,args=(v,1,l))#将进程锁传入进程
    p2 =mp.Process(target=job,args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
if __name__ == '__main__':
    multicore()
