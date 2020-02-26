class Test:

    l = [1,23,4,5]

    def __init__(self,water):
        self.water = water

    def eat(self):
        print('吃')

    def drink(self):
        print('喝',self.water)

    def __call__(self,play):
        self.eat()
        self.drink()
        print(play)

t('玩')
