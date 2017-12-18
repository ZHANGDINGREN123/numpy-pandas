import threading

def job1():
    Lock.acquire()
    global A,Lock
    for i in range(10):
        A +=1
    print ('job1',A)
    Lock.release()
def job2():
    Lock.acquire()
    global A,Lock
    for i in range(10):
        A += 10
    print ('job2',A)
    Lock.release()
if __name__ == '__main__':
    Lock =threading.Lock()
    A =0
    t1 =threading.Thread(target=job1)
    t2 =threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()