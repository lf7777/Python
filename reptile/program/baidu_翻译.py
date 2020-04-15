import requests,json

url = 'https://fanyi.baidu.com/sug'

form = {'kw':'英文'}

response = requests.post(url,data=form)

#服务器返回的数据是json格式的,并非编码问题,需要用json解析.步骤如下:
res_dict = json.loads(response.text)

print(res_dict)
