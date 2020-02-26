class Fruits:
    name = 'orange'

    def effect(self):
        print('吃')

    def __bool__(self):
        if self.name == 'orange':
            return 
        else:
            return '错了'
o = Fruits()

print(bool(o))
