import requests
# from lxml import etree
#导包
from bs4 import BeautifulSoup

url = 'https://xueqiu.com/ask/square'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

# rep = requests.get(url,headers=headers)

with open('xueqiu.html','rb') as fr:
    xueqiu = fr.read()
xueqiu = xueqiu.decode('utf-8')

# 实例化 BeautifulSoup 对象,传入数据参数
soup = BeautifulSoup(xueqiu,'lxml')

# 定位某个标签
# title_tag = soup.select('title')
# print(title_tag)
# print(type(title_tag))
# print(title_tag[0].text)

# 定位 head 里 所有 meta 标签
# meta_tag_list = soup.select('head>meta')
# print(meta_tag_list)
div_tag_list = soup.select('div.square-main')

print(div_tag_list[0])