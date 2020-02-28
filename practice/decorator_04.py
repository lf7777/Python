def outer(par):
    def decor(func):
        def inner():
            if par =='笑':
                print('哈哈')
                func()
            elif par == '哭':
                print('哇哇')
                func()
        return inner
    return decor


@outer('笑')
def langh():
    print('笑')

@outer('哭')
def cry():
    print('哭')

langh()

cry()
