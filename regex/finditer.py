import re

#finditer()得到的是一个生成器.



if __name__ == '__main__':

    text = 'He was carefully dislyguised but captured quickly by policely.'

    pattern = '(\w*ly)[^a-zA-Z]'

    res = re.finditer(pattern,text)

#next 调用通过 finditer()函数 实例化出来的 res

    #i = 0
    #while i<10:
    #    print(next(res))

    #for item in res:

    #    print(item)

    print(type(res))

    for item in res:

        print(item.group(1))

