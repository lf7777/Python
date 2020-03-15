import re

#定义 模式(pattern)

#内容
line = 'huang123'

#需要两个参数, 模式, 文本内容

#定义模式
pattern = 'uang'

#调用 match() 查找内容
res = re.match(pattern,line)

print(res)

#return <re.Match object; span=(0, 5), match='huang'> 
#span 的开始必须是 0


#总结 match() 在进行匹配时 : 

    #match() 必须 从头开始匹配

    #<1> 如果 模式 和 文本内容 自第一个字符开始 就匹配上了,并且连续相同.

             # return span=(0开始,到匹配相同部分末尾的下标),match到的内容.

    #<2> 如果不是从第一个开始 则 :

             # 全部 return None

