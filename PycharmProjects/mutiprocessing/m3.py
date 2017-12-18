#coding=utf-8
import multiprocessing as mp
def job(a, b):
    print('aaaa')
if __name__ == '__main__':#定义主函数的语句 == 与c语言int main()一致
    q = mp.Queue()#队列
    p1 = mp.Process(target=job, args=(1, 2))#只是定义好进程
    p1.start()#有start()才开始
    p1.join()
