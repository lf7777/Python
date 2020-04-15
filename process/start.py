from time import sleep
from multiprocessing import Process
import os

# 创建进程会从新在内存中开辟空间,然后再执行进程中的线程,步骤繁琐,故比多线慢

def run():
    while True:
    # os.getppid() 获取当前进程的父进程的id号
        print('子进程1执行%s-父id号:%s'%(os.getpid(),os.getppid()))
        sleep(1)

def run2():
    while True:
        print('子进程2执行%s'%(os.getpid()))
        sleep(1.2)

if __name__ == '__main__':

    #程序本身就是一个进程,故他是主进程
    # os.getpid()  获取当前进程id号
    print('主进程启动',os.getpid())

    #创建新的进程
    p1 = Process(target=run)
    p2 = Process(target=run2)

    #启动刚创建的进程
    p1.start()
    p2.start()
