class person:
    ooo = 50
    source = 100
    __weight = 10
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def fun(self):
        return self.name+'我最帅了'

x = person('bob',10)

print(x.fun())

class student(person):
    #只有子类构造函数才可以接收父类构造函数:
    def __init__(self,name,age):
        #调用父类的构造函数 
        person.__init__(self,name,age)
    def fun(self):
        return self.name+'我最帅了'+'哈哈'

z = student('mike',10)
print(z.name)
print(z.fun())
