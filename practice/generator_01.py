import time

k = 0

def test():
    
    for i in range(2):

        print('抽烟')

        yield

    
def test2():

    for i in range(2):
        
        print('喝酒')

        yield

g1 = test()
g2 = test2()

while True:
    try:
        next(g1)
        time.sleep(0.4)

        next(g2)
        time.sleep(0.4)
    except:
        break
