def fun(n,count=0):
    count+=1
    if count == 8:
        return
    n=2*n+1
    print('经过第',count,'个村子,卖出了',n,'只鸭子')
    return fun(n,count)

fun(2)
