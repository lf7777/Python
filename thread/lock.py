from threading import Thread,Lock
# 再导一次为了调用其本身的 threading.current_thread().name
import threading
import time

'''
锁的作用: 防止多线程线程间通信造成数据数据混乱
确保一个时间内指定区间的代码只能由一个线程执行
from threading import Lock
创建锁 : lock = threading.Lock()
上锁 : lock.acquire() 在需要的位置添加 acquire : 获得
解锁 :  lock.release() 在需要的位置添加 release : 释放
上锁之后,第二个线程看到锁,进入阻塞状态,等待解锁,后再执行
'''

'''
上锁后 : 阻止了线程的并发执行,只能以单线程执行,效率指数级的降低了
死锁概念 : 锁上了没释放锁
'''

num = 10

lock = threading.Lock()
def run(n):
    global num
    for i in range(10000000):
        lock.acquire()
        try:    # 如果程序比较复杂,程序本身可能会出问题,加上了锁之后,执行代码出错,无法执行到解锁,需要加try
            num = num + n
            num = num - n
        finally: # 表示最后始终会执行的步骤
            lock.release()

        ''' 与lock.acquire() lock.release() 作用相同,自动上锁解锁 (降低些死锁的几率)
        with lock:
            num = num+n
            num = num -n
        '''

if __name__ == "__main__":
    print('主进程开启')
    print('%s开启'%(threading.current_thread().name))

    t1 = Thread(target=run,args=(6,))
    t2 = Thread(target=run,args=(6,))

    t1.start()
    t2.start()

    global num
    t1.join()
    t2.join()

    print('num的值是:',num)

    print('%s结束'%(threading.current_thread().name))