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

# <伪装>
#可以使用一个字典进行覆盖 headers 中的 验证信息
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

# <抓包>
#可以设置 verify = False,能让验证信息不起作用.(就可以让fiddler抓到包)
response = requests.get(url,verify=False,headers=headers)


#保存到文件系统
with open('baidu.html','wb') as fwb :
    
    fwb.write(response.content)

# response.text是根据操作系统自动设置字符集,linxu写入和读取都是utf-8字符集

# 网站字符集如果不是和linux系统一致 not utf-8,需要用网站使用的字符集对bytes进行解码,rep.content.decode('网站'),解为纯二进制格式,linux系统再用utf-8读取
# with ope('','w')as fw:
    #fw.write(response.content.decode('网站使用码'))
