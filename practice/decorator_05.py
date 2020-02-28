class Parents:

    def baobao():
        print('抱抱')

    def jugaogao():
        print('举高高')


def outer(cls):

    def decor(func):
    
        def inner():
    
            cls.baobao()

            func()

            cls.jugaogao()

        return inner
    return decor


@outer(Parents)
def love():
    print('亲亲')

love()
