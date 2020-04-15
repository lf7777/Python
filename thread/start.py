import threading
import time

'''
线程是进程内的子任务,没有独立的堆栈,共享进程的堆栈,并发执行的多任务
线程会利用进程的资源,而不会重新开辟进程,所以多线程的运行速度较快 
'''

'''
属性:
        1. threading.current_thread().name    current:现在的
            获取当前的线程的名称 比如 MainThread,Thread-1,Thread-2
'''

def run():
    print('开启',threading.current_thread().name)
    time.sleep(2)
    print('线程结束')

if __name__ == "__main__":
    print('启动主进程')
    print('主线程(%s)启动'%(threading.current_thread().name))

    # 创建子线程 name参数,为线程起名字
    t1 = threading.Thread(target=run,name='测试1')
    t2 = threading.Thread(target=run,name='测试2')

    # 启动线程 
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('主线程(%s)结束'%(threading.current_thread().name))