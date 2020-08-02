# producer 生产者,读作泼嘟sir.consumer 消费者,读作cansumer

# import queue 是一个包,multiprocessing里也有Queue
import threading,time,queue,random

# 生产者 product
def product(id,q):
    while True:
        num = random.randint(0,10000)
        q.put(num)
        print('生产者%d生产了生产了%d放入了队列'%(id,num))
        time.sleep(3)
    # 任务完成
    q.task_done()

# 消费者
def customer(id,q):
    while True:
        item = q.get()
        if item == None:
            break
        print('消费者%d消费了%d数据'%(id,item))
        time.sleep(2)


if __name__ == "__main__":

    # 消息队列
    q = queue.Queue()

    # 启动消费者
    for i in range(4):
        threading.Thread(target=product,args=(i,q)).start()

    # 启动消费者
    for i in range(3):
        threading.Thread(target=customer,args=(i,q)).start()
