import re

text = 'He was carefully dislyguised but captured quickly by policely.'

#有固定 词数 的找到副词,且最后一个不能是 ly 结尾(很大的问题)

'''
pattern = '.*ly$'

res1 = text.split(' ')

l = []

for i in range(8):
    res = re.search(pattern,res1[i])
    if res != None:
        l.append(res.group())

print(l)
'''

#定义模式

pattern = '(\w*ly)[^a-zA-Z]'

res = re.findall(pattern,text)

print(res)
