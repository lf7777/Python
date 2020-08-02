# key 必须是 函数

x = [1,5,3,4,2]

y = [9,7,3,11,2]

z = list(zip(x,y))

z1 = sorted(z,key=lambda t : t[1]) 

#此处 t 就是 z 中的每一个元素,t[1]就是元素中的第二个元素

print(z)

print(z1)
