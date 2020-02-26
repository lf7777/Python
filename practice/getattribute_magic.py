class Test:

    def __init__(self,name):

        self.name = name

    def __getattribute__(self,item):

        print()

        result = object.__getattribute__(self,item)

        result = result.replace(result[1:-1],(len(result)-2)*'*')

        return result


one = Test('雪莲花花花花胡')

print(one.name)
