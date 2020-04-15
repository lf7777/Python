# 获取免费的代理，并验证代理的可用性
import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

def get_free_proxy():
    
    url ='https://www.xicidaili.com/nn'
    response = requests.get(url,headers=headers)

    tree = etree.HTML(response.content)

    ip = tree.xpath('/html/body//tr//td[2]/text()')
    port = tree.xpath('/html/body//tr//td[3]/text()')

    # 获取到 格式:'http://ip+端口'
    mid = ['http://'+i+':'+p for i,p in zip(ip,port)]

    return mid

def validate_proxy(item):
    url = 'http://httpbin.org/get'
    proxy = {
        'http':item,
        'https':item
    }
    try:
        rep = requests.get(url,proxies=proxy,timeout=3)
        if rep.status_code == 200:
            print('这个代理好使!!!',item)
            return item
        else:
            print('这个代理好使!!!',item)
            return item
    except:
        print('代理不可用',item)
        return None
            
if __name__ == "__main__":

    res_list = []
    good_proxy=[]
    # 使用进程池,多进程写法 (多进程)
    '''
    多进程得到返回值的方法:
    1. 先得到进程的返回值 res = pool.apply....
    2. 把返回值存到列表中 res_list.append(res)
    3. 在进程的循环中遍历这个列表,变量来接收 for i in res_list: (注:在上面的大循环中进行)
    4. 变量.get() 获取到真正的返回值 r = i.get()
    5. 判断得到的结果是否存在,存在则将其储存 if i: finaly_res_list.append(r)
    '''
    from multiprocessing import Pool
    pool = Pool(10)
    for item in get_free_proxy():
        res = pool.apply_async(func=validate_proxy,args=(item,))
        res_list.append(res)
        for res in res_list:
            proxy = res.get()
            if proxy:
                good_proxy.append(proxy)

        # 单进程单线程写法
        # for item in get_free_proxy()
        #     if validate_proxy(item)
        #         goog_proxy.append(item)
    print('good proxy is:')
    print(good_proxy)
    #结束进程池,等待所有进程执行结束
    pool.close()
    pool.join()
