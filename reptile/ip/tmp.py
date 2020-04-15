import requests
from lxml import etree
from multiprocessing import Pool

# 获取单页的 ip 和 port
def get_ip_port(url):
    rep = requests.get(url)
    tree = etree.HTML(rep.content.decode('gb2312'))
    
    #获取一行数据
    ip = tree.xpath('/html/body/div[@id="main"]/div[1]/div[1]/table//tr/td[1]/text()')
    prot = tree.xpath('/html/body/div[@id="main"]/div[1]/div[1]/table//tr/td[2]/text()')
    return list(zip(ip,prot))

# def verify_ip(item):
    proxy={
        'http':item,
        'https':item
    }
    url = 'http://httpbin.org/get'
    try:
        rep = requests.get(url,proxies=proxy,timeout=3)
        if rep.status_code == 200:
            print('代理可以使用',item)
            return item
    except:
        print('代理不可使用',item)
        return None

if __name__ == "__main__":
    res_list=[]
    good_ip_list=[]
    #获取多页
    #for i in range(2,11):
    url = 'http://www.66ip.cn/{}.html'.format(2)
    res = get_ip_port(url)
    print(res)