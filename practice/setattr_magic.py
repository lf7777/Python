class Test:

    age = 18

    def __init__(self,name):

        self.name = name

    def __setattr__(self,attrname,value):

        if len(value) <= 3 :
            object.__setattr__(self,attrname,value)
        else:
            print('请输入不超过三个字符')

one = Test('佐助')

one.name = '鸣人哈'

print(one.__dict__)

