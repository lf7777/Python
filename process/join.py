import time
from multiprocessing import Process

# 平时情况下,主进程在遇到子进程,会单开一个进程取执行,不会影响主进程的继续执行
# 需要主进程等等待子进程执行完毕,需要时候join

# join 的作用 : 让主进程等待子进程结束后,再执行主进程后续的代码

def run():
    print('子进程启动')
    time.sleep(3)
    print('子进程结束')

if __name__ =='__main__':
    print('主进程开启')
    p1 = Process(target=run)
    p1.start()
    p1.join()
    print('主进程结束')
