import abc
#设定抽象类,定义动物规则
class Animal(metaclass = abc.ABCMeta):

    #设定抽象方法 跑
    @abc.abstractmethod
    def say(self):
        pass
    #设定抽象方法 叫
    @abc.abstractmethod
    def run(self):
        pass

#定义小狗的类
class Dog(Animal):

    def say(self):
        print('旺旺')

    def run(self):
        print('小狗四条腿跑')


#定义小鸡的类
class Chicken(Animal):

    def say(self):
        print('咯咯')

    def run(self):
        print('小鸡两条腿跑')

#定义小猫的类
class Cat(Animal):

    def say(self):
        print('喵喵')

    def run(self):
        print('小猫撒腿就跑')


money = Dog()

mimi = Cat()

jiji = Chicken()


#定义行为类:
class Action:

    def __init__(self,animal):

        self.animal = animal

    def say(self):

        self.animal.say()

    def run(self):

        self.animal.run()

action = Action(money)

action.animal = jiji

action.say()

action.run()
