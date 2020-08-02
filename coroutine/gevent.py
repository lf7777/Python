import gevent
import time
from gevent import monkey
import requests

#作用 在send 和 receive (就是在程序执行的过程中,暂不返回值,原理是通过monkey.patch_all,向过程中添加yield)
monkey.patch_all()

def tell_me_your_name(name):
    print('start:',name)
    time.sleep(1)
    print('end:',name)
 

if __name__ == "__main__":

    #协程实现
    # g1 = gevent.spawn(tell_me_your_name,'admin')
    # g2 = gevent.spawn(tell_me_your_name,'eva')
    # g3 = gevent.spawn(tell_me_your_name,'bob')
    # g4 = gevent.spawn(tell_me_your_name,'alice')

    # gevent.joinall([g1,g2,g3,g4])

    #普通执行多个函数
    tell_me_your_name('a')
    tell_me_your_name('b')
    tell_me_your_name('c')
