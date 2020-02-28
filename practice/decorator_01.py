def decor(func):
    def inner():
        x = func()
        print(func() +'啊啊')
        return x
    return inner

@decor
def ss():
    s = '哈哈哈'
    return s

ss()
