# from multiprocessing import Process
from multiprocessing import Pool
import time,os,random

# pool 进程池
# 作用 : 方便管理多进程

def run(name):
    print('子进程%s启动--%s'%(name,os.getpid()))
    time.sleep(2)
    print('子进程%s结束--%s'%(name,os.getpid()))


if __name__ == "__main__":
    print('主进程启动')

    # Pool() 默认参数是 实际计算机的 CPU核心数
    pp = Pool()
    for i in range(12):
        # 创建进程,放入进程池,统一管理,子进程的启动顺序是不同的
        pp.apply_async(func=run,args=(i,))

    # 在 join 等待子进程结束之前, 调用 close()就不能再继续添加进程了
    pp.close()
    # 进程池对象调用join,会等待进程池中的所有子进程结束完毕后再去执行主进程
    pp.join()
    print('主进程结束')