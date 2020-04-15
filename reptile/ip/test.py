import requests

url = 'http://icanhazip.com'

proxy = {
    'http':'http://222.173.10.82:8888',
    'https':'http://222.173.10.82:8888'
}

rep = requests.get(url,proxies=proxy)

if rep.status_code == 200:


with open('1.html','wb') as fw:
    fw.write(rep.content)