#全局变量和局部变量:

#示例:

total = 0 #全局变量

def sum(arg1,arg2):
    total = arg1+arg2
    print('函数内部的局部变量:',total)
    return total

#调用sum函数
sum(10,20)
print('函数外是全局变量:',total)


#总结:
#sum函数内部的total和函数返回的total都是在该函数内部的,作用域仅限于该函数
#并不能修改全局作用域,如想修改,需要在函数内部添加global.
