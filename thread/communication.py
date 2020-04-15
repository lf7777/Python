from threading import Thread
import threading
import time

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