#coding=utf-8
import threading

def thread_job():
    print ('this is an added thread ,name is %s'%threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job)#定义线程
    added_thread.start()#线程开始工作
    print (threading.active_count())#获取已激活的线程数
    print (threading.enumerate())#查看所有线程消息，输出结果是一个<_MainThread带多个<Thread
    print (threading.current_thread())#查看现在正在运行的线程
if __name__ == '__main__':
    main()
