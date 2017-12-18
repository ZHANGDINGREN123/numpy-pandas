#coding=utf-8
import multiprocessing as mp

def job(q):
    res = 0
    for i in range(800):
        res += i + i**2 + i**3
    q.put(res)#queue

if __name__ == '__main__':
    q = mp.Queue()#定义queue
    p1 = mp.Process(target=job, args=(q,))#如果是一个参数，参数后要加，说明可以迭代或者说后面还有数值进来，
    p2 = mp.Process(target=job, args=(q,))#不加会报错
    p2.start()
    p1.start()
    p1.join()
    p2.join()
    res1 = q.get()#上面是分两批处理，所以这里分两批保存
    res2 = q.get()
    print(res1+res2)
    #Queue的功能是将每个核和线程的运算结果放在队列中，等到每个线程或核运行完毕再从队列中取出结果，继续加载运算
    #原因在于，多线程调用的函数不能有返回值，所以用Queue存储多个线程运算的结果