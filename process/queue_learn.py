from multiprocessing import Process,Queue
import os,time

'''
queue :
put()写入值
get()获取值
'''

def write(que):
    print('启动写子进程%s'%(os.getpid()))
    for chr in ['A','B','C','D']:
        que.put(chr)
        time.sleep(1)
    print('结束写子进程%s'%(os.getpid()))

def read(q):
    print('启动读子进程%s'%(os.getpid()))jieshu
    while True:
        value = que.get()
        print('value=',value)
    print('结束读子进程%s'%(os.getpid()))

if __name__ == "__main__":

    # 只能在主进程创建队列,之后把队列的引用分别给子进程
    que = Queue()
    print('主进程开始')

    pw = Process(target=write,args=(que,))
    pr = Process(target=read,args=(que,))

    pw.start()
    pr.start()

    pw.join()
    # 强行结束子进程
    pr.terminate()

    print('父进程结束')