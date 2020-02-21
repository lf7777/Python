import doctest
def dijia(n,time=0):
    if n == 100:
        return time
    n=n+2
    time=time+1
    return dijia(n,time)

print(dijia(0))

print(doctest.testmod())
