class Animal(object):
    eye = 'blue'
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    eye = 'red'
    def run(self):
        print('dog is running')
    def eat(self):
        print('dog is eating...')

class Cat(Animal):
    def run(self):
        print('cat is running')

def run_twice(animal):
    animal.run()
    animal.run()

print(type(Dog))
run_twice(Cat())
