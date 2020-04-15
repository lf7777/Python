import threading
import time

def func():
    #创建事件对象
    event = threading.Event()

    def run():
        for i in range(5):
            #阻塞,等待事件的触发
            event.wait()
            #重置
            event.clear()
            print('lpf%d'%(i))
    t = threading.Thread(target=run).start()

    return event

if __name__ == "__main__":

    e = func()
    for i in range(5):
        time.sleep(2)
        e.set()