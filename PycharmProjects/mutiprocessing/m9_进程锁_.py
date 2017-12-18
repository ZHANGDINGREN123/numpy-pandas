#coding=utf-8
#不加进程锁情况，输出结果比较混乱，两个进程抢夺cpu资源，输出结果会出现重复
import multiprocessing as mp
import time
def job(v,num,):
    for _ in range(5):
        time.sleep(0.2)
        v.value += num
        print (v.value)
def multicore():
    v =mp.Value('i',0)
    p1 =mp.Process(target=job,args=(v,1))
    p2 =mp.Process(target=job,args=(v,3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
if __name__ == '__main__':
    multicore()
