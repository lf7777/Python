class Test:

    def __init__(self,name):

        self.name = name

    def __getattr__(self,item):
        if 'name' in item:
            return self.name
        else:
            return '成员不存在'


one = Test('雪莲花花花花胡')

print(one.name2)
