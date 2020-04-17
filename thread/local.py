from threading import Thread
import threading
import time

'''
创建一个全局的local对象
每个线程都可以对local对象读写,操作的是线程本地的变量,和其他线程互不影响
作用 : 1.让每个线程有独立的存储空间
       2.为每个线程绑定一个数据库,HTTP请求,用户身份信息等
'''

num = 10

local = threading.local()

def run(x,n):
    x = x + n
    x = x - n

def func(n):
    local.x = num
    for i in range(10000):
        run(local.x,n)
    print('%s-%d'%(threading.current_thread().name,local.x))

if __name__ == "__main__":
    print('主进程开启')
    print('%s开启'%(threading.current_thread().name))

    t1 = Thread(target=func,args=(6,))
    t2 = Thread(target=func,args=(9,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('num的值是:',num)

    print('%s结束'%(threading.current_thread().name))
