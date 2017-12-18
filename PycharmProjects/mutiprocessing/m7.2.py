#coding=utf-8
import multiprocessing as mp

def job(x):
    return x*x
def multicore():
    pool = mp.Pool()
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    print(res.get())
    #用get得到结果
    multi_res = [pool.apply_async(job, (i,))for i in range(10)]#从迭代器中取出
    print([res.get() for res in multi_res])
if __name__ == '__main__':
    multicore()
