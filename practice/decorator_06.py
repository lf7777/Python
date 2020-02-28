class outer:

    def __init__(self,arg):

        self.arg = arg

    def __call__(self,func):
            
        self.func = func

        return self.inner

    def inner(self):

        print('抱抱')

        self.func()

        print('举高高')
   
@outer('ai')
def love():

    print('亲亲')

love()
