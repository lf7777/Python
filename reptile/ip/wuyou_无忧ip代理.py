import requests
from lxml import etree
from multiprocessing import Pool


def get_all_ip(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    rep = requests.get(url,headers=headers)
    with open('tmp.html', 'wb') as fw:
        fw.write(rep.content)

    tree = etree.HTML(rep.text)
    ip_and_port = tree.xpath('//ul[@class="l2"]')
    for i in ip_and_port:
        ip = i.xpath('./span[1]/li/text()')[0]
        port = i.xpath('./span[2]/li/text()')[0]
        yield 'http://'+ip+':'+port


def verify_ip(item):
    print('检测',item)
    url = 'http://httpbin.org/get'
    proxy = {
        'http': item,
        'https': item
    }
    try:
        rep = requests.get(url, proxies=proxy, timeout=3)
        if rep.status_code == 200:
            print('代理可用')
            return item
        else:
            print('代理可用')
            return item
    except:
        print('代理不可用')
        return None


if __name__ == "__main__":
    data5u_url = 'http://www.data5u.com/'
    # 多进程验证是否可用ip
    ip_list = []
    good_ip_list = []
    pool = Pool(processes=20)
    for item in get_all_ip(data5u_url):
        res = pool.apply_async(func=verify_ip, args=(item,))
        ip_list.append(res)
        for i in ip_list:
            proxy = i.get()
            if proxy:
                good_ip_list.append(proxy)

    print('good ip is:')
    print(good_ip_list)

    pool.close()
    pool.join()
