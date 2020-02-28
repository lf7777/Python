'''
关于元类:
'''

#定义一个普通的类.
class Car:
    pass

#查看类的元类1:
#print(type(Car))

#查看类的元类2:
#print(Car.__class__)


#声明抽象类:
#导入抽象类模块 abc(abstruct的简写)
import abc

class User(metaclass = abc.ABCMeta): #制作抽象类,必须另外指定元类.

    name = '兰鹏飞'

    #抽象 对象方法
    @abc.abstractmethod
    def add_user(self):
        pass


    #抽象 类方法
    @abc.abstractclassmethod    #将classmethod 和 abstract的结合,注意.
    def set_user(cls):
        pass


    #抽象 类绑定方法
    @abc.abstractmethod
    def del_user():
        pass


    #抽象 静态方法
    @abc.abstractstaticmethod    #将 staticmethod 和 abstract的结合.注意.
    def find_user():
        pass


    #抽象类中可以有正常的方法
    def frozen_user(self):
        print('封禁用户')


#继承抽象类后,需要覆写所有抽象方法,才可以实例化.
class Myuser(User):

    def add_user(self):
        print('抽象对象方法') 

    @classmethod
    def set_user(cls):
        print('抽象类方法')


    def del_user():
        print('抽象绑定类方法')

    @staticmethod
    def find_user():
        print('抽象静态类方法')


#通过 <继承逐步覆写所有抽象类> 协同开发:

class XZ_user(User):

    def add_user(self):
        print('抽象对象方法')

class XQ_user(XZ_user):

    @classmethod
    def set_user(cls):
        print('抽象类方法')
   
class XS_user(XQ_user):

    def del_user():
        print('抽象绑定类方法')

class XL_user(XS_user):

    @staticmethod
    def find_user():
        print('抽象静态类方法')

#实例化:
one = XL_user()
#调用 抽象对象方法
one.add_user()
#调用 抽象类方法
XL_user.set_user()
#调用 绑定类方法
XL_user.del_user()
#调用 静态类方法
one.find_user()
#查看原类
print(XL_user.__class__)
