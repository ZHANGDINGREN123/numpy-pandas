#coding=utf-8
import  multiprocessing as mp

def job(x):
    return x*x
def multicore():
    pool = mp.Pool() #定义Pool,也可以自行分配几个进程（如pool=mp.Pool（2）分配成两个核
    res = pool.map(job, range(10))#用map（）获取结果，在map（）中需要放入函数和需要迭代运算的值，然后会自
    print(res)#行分配给cpu核，返回结果
if __name__ == '__main__':
    multicore()
    #进程池Pool，进程池是将我们所要运行的东西，放到池子里，Python会自行解决多进程问题