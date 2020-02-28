def decor(func):

    def inner(z,q):

        print('谁在干嘛')

        func(z,q)

    return inner

@decor

def ss(x,y):

    print('{}在{}'.format(x,y))

ss('我','学习')
