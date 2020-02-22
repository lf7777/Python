import time

nums = 50

starttime = time.perf_counter()

for i in range(nums+1):
    star = i * '*'
    point = (50-i) * '.' 
    val = int((i / nums) * 100)
    usetime = time.perf_counter()-starttime
    print('\r{}% [{}->{}]{:.1f}s'.format(val,star,point,usetime),end='')
    time.sleep(0.5)
