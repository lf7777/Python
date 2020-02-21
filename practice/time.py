import time

strvar = '春眠不觉晓,疑是地上霜'

l = len(strvar)

for i in range(l):
    print("\r"+strvar[:l-1-i],end=" "*i)
    time.sleep(0.5)

print('aa\tbbb')
