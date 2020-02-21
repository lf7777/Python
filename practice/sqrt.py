import math

def quadratic(a,b,c):
#    if not isinstance((a,b,c),(int,float)):    为什么这两句这里不可以加
#        raise TypeError('bad operand type')   以及isinstance方法可以检查几个参数
    res_01 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    res_02 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    return res_01,res_02

print(quadratic(1,3,-1))
