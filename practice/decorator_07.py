def decor(cls):

    def inner():

       obj = cls()

       obj.name = '兰鹏飞'

       obj.age = 24

       return obj

    return inner


@decor
class Human:
    pass


ren = Human()

print(ren.__dict__)
