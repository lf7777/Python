import requests
from lxml import etree
from multiprocessing import Pool

# 获取单页的 ip 和 port
def get_ip_port(url):
    rep = requests.get(url)
    tree = etree.HTML(rep.content.decode('gb2312'))
    
    #获取一行数据
    mid = tree.xpath('/html/body/div[@id="main"]/div[1]/div[1]/table//tr')
    for i in range(1,len(mid)):
        ip = mid[i].xpath('.//td/text()')[0]
        port = mid[i].xpath('.//td/text()')[1]
        yield 'http://'+ip+':'+port

def verify_ip(item):
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
    pool = Pool(10)
    res_list=[]
    good_ip_list=[]
    #获取多页
    for i in range(2,11):
        url = 'http://www.66ip.cn/{}.html'.format(i)
        for item in get_ip_port(url):
            res = pool.apply_async(func=verify_ip,args=(item,))
            res_list.append(res)
            for res in res_list:
                good_ip = res.get() 
                good_ip_list.append(good_ip)

    print('good ip is :')
    print(good_ip_list)


