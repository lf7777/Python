import re

text = 'He was carefully dislyguised but captured quickly by policely.'

pattern = '(\w*ly)[^a-zA-Z]'

#sub 将 findall()所有都获取到的内容 都替换成字符串.

res = re.sub(pattern,text)

print(res)
