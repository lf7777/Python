from multiprocessing import Process
import time
'''
全局变量在多个进程中不能共享
创建子进程时,会将全局变量到子进程里做个备份
该 num 是在主进程中定义的全局变量,在主进程的堆栈里
'''
num = 100

def run():
    print('子进程开始')
    global num
    num += 1
    print('子进程结束-%d'%(num))

if __name__ == "__main__":
    print('主进程启动')
    p1 = Process(target=run)
    p1.start()
    p1.join()

    print('主进程结束--%d'%(num))