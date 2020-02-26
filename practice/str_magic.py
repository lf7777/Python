class Fruits:

    def __init__(self,fruits):

        self.fruits = fruits

    def __str__(self):

        return self.fruits+' 对象实例化成功'

banana = Fruits('banana')

print(banana)
