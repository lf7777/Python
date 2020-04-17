# 线程调度 : 控制线程按照自己规定的方式运行
# from threading import Condition
import threading,time

cond = threading.Condition()

def run1():
    with cond:
        for i in range(0,10,2):
            print(threading.current_thread().name,i)
            time.sleep(1)
            cond.wait()
            cond.notify()

def run2():
    with cond:
        for i in range(1,10,2):
            print(threading.current_thread().name,i)
            time.sleep(1)
            cond.notify() # notify 通知
            cond.wait()


if __name__ == "__main__":
 
    threading.Thread(target=run1).start()
    threading.Thread(target=run2).start()
