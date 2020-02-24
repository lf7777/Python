#父类
class Father:

    first_name = '刘'

    last_name = '备'

    __wife = ('甘夫人','糜夫人','孙尚香')

    age = 48 

    color = '黄色'

    def eat(self):
        print('甜甜圈')

    def run(self):
        print('拔起腿就跑')

    def make_shoes(self):
        print(self.__wife,'做草鞋')

    def m():
        print(Father.age,'aa')

#子类
class Son(Father):
    pass

Father.m()
