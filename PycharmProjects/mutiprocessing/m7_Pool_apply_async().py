#coding=utf-8
import  multiprocessing as mp

def job(x):
    return x*x
def multicore():
    pool = mp.Pool()
    res = pool.apply_async(job, (2,))#一次只能输入一个值,输出多个回报错
    print(res.get())#用get获得结果
if __name__ == '__main__':
    multicore()
