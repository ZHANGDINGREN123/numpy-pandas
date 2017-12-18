#coding=utf-8
import threading
import time

def thread_job():
    print ("T1 START\n")
    for i in range(10):
        time.sleep(0.1)#任务间隔0.1秒
    print ("T1 finish\n")

def main():
    added_thread = threading.Thread(target=thread_job)  # 定义线程
    added_thread.start()  # 线程开始工作
    added_thread.join()
    print ("all done")

if __name__ == '__main__':
    main()
    #join对控制多个线程的执行顺序非常关键