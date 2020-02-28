def decor(func):
    
    def inner(*parents,**child):
        print('结果是')
        func(*parents,**child)
        return 5
    
    return inner


@decor
def ss(*parents,**child):

    print(parents,child)

    return  222

result = ss('爸爸','妈妈',son='儿子',gile = '女儿')

print(result)
