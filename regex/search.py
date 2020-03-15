import re


#文本

line = 'huang123ang'

#定义模式

pattern = 'ang'

#调用 search() 查找内容

res = re.search(pattern,line)

print(res)

#return <re.Match object; span=(2, 5), match='ang'>


#总 结 :

        #<1> search 和 match 的不同在于 不那么极端,会慢慢向后找. 

        #<2> search 只会返回找到的 和模式匹配的 第一块内容 的下标头尾 及 内容. 
