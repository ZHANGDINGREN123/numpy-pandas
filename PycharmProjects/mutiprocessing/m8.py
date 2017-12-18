#coding=utf-8
import multiprocessing as mp
value1 = mp.Value('i',1)#i是int型
value2 = mp.Value('d',3,14)#d是double型
array =mp.Array('i',[1,2,3,4])
#在python的multiprocessing中的Array，可以实现共享内存交互，以此来实现进程之间的共享数据，这里Array与numpy
#中不同，只能是一维数组，value一样需要定义数据形式