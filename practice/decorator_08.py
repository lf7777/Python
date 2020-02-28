def decor1(func):

    def inner():

        print('亲亲')

        func()

        print('举高高')

    return inner


def decor2(func):

    def inner():

        print('转转')

        func()

        print('笑一笑')

    return inner


@decor2
@decor1    #装饰顺序:先被装饰器1装饰,然后再外层套上装饰器2.
def love():

    print('抱抱')

love()
