import re

line = 'aaasssaaa'

# 定义模式

pattern = '.{3}'

#调用findall函数

res = re.findall(pattern,line)

print(res)


#找到所有,并返回 列表格式.
