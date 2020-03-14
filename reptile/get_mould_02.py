import requests

url = 'https://www.xicidaili.com/nn/'

#可以使用一个字典进行覆盖 headers 中的 User-Agent
#然后在get请求中用变量赋值给headers
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}


#可以设置 verify = False,能让验证信息不起作用.(就可以让fiddler抓到包)
response = requests.get(url,verify=False,headers=headers)

with open('XiciDaili.html','wb') as fwb:
    fwb.write(response.content)
