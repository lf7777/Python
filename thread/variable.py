from threading import Thread
import threading
import time

'''
所有线程都可对全局变量做修改,容易造成变量值混乱
在多线程中任何一个变量都可以被任意一个线程修改,因此,线程之间共享进程的数据段最大的危险在于多个线程同时修改一个变量,容易把内容改乱
'''

num = 10

def run(n):
    global num
    for i in range(10000000):
        num = num + n
        num = num - n

if __name__ == "__main__":
    print('主进程开启')
    print('%s开启'%(threading.current_thread().name))

    t1 = Thread(target=run,args=(6,))
    t2 = Thread(target=run,args=(6,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('num的值是:',num)

    print('%s结束'%(threading.current_thread().name))
