class Human:

#对 象 方 法 :    

    def eat(self):
        print('这是一个对象方法')


#类 方 法 :
    @classmethod
    def drink(cls):
        print(cls)
        print('这是一个类方法')


#绑 定 类 方 法 :

    def play(val):
        print(val,'这时一个绑定类方法')


#静 态 方 法 :
    @staticmethod
    def happy():
        print('这是一个静态方法,只是暂居在类里面')


#实例化对象 调用方法
ren = Human()
#ren.eat()

#类方法
#Human.drink()

#绑定类方法
#Human.play('哈哈')

#静态方法
#Human.happy()
ren.happy()
