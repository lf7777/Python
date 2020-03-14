#导包
import requests

'''
返回的html信息 格式 

状态码 : response
字符串 : response.text    乱码问题解决 : response.content = 'utf-8'
二进制 : response.content 二进制格式进行 编码用 str.decode()
 
'''

#url
url = 'http://www.baidu.com'


#调用函数,返回html的信息
response = requests.get(url)


#指定编码格式
response.encoding = 'utf-8'


#打印测试数据
#print(response.content)


#保存到文件系统
with open('baidu.html','wb') as fwb :
    
    fwb.write(response.content)
