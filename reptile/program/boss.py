import requests
from lxml import  etree
import pymysql
import time
import re

def parse_detailed_page(url,headers):
    data = requests.get(url,headers=headers)
    with open('detailed.html','wb') as fw:
        fw.write(data.content)
    # with open('detailed.html','r') as fr:
    #     data = fr.read()
    html_etree = etree.HTML(data.text)
    position = html_etree.xpath('//div[@class="name"]/h1/text()')[0]
    salary = html_etree.xpath('//div[@class="name"]/span[@class="salary"]/text()')[0]
    city = html_etree.xpath('//div[@class="info-primary"]//p/text()')[0]
    experience = html_etree.xpath('//div[@class="info-primary"]//p/text()')[1]
    eduction = html_etree.xpath('//div[@class="info-primary"]//p/text()')[2]
    position_describe = html_etree.xpath('//div[@class="text"]/text()')

    position_describe_res = [i.strip() for i in position_describe]
    position_describe_res = '\n'.join(position_describe_res)

    # 建表
    # create table boss_test(id int primary key auto_increment,position varchar(10),salary varchar(20),city varchar(10),experience varchar(20),eduction varchar(20),position_describe text) default charset=utf8mb4;

    # db = pymysql.connect('localhost','root','lf','my_mysql',charset='utf8mb4')

    # cursor = db.cursor()

    # insert_sql = 'insert into boss_test  values(null,"{}","{}","{}","{}","{}","{}");'.format(position,salary,city,experience,eduction,position_describe_res);

    # cursor.execute(insert_sql)

    # db.commit()

    # db.close()

def parse_list_page(url,headers):
    rep = requests.get(url,headers=headers)

    li_strings = re.findall('<a href="(.*?)" data-jid',rep.text,re.S)

    for i in li_strings:
        print('-'*50)
        print(i)

if __name__ == "__main__":
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'cookie': '__c=1586754648; __zp_seo_uuid__=e120a81d-51bb-430b-80d6-cabadbc9017b; lastCity=101010100; sid=sem; toUrl=/; JSESSIONID=""; __g=sem; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1584637311,1586754648,1586756847,1586758599; __l=l=%2Fwww.zhipin.com%2Fbeijing%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDdiHC06L4M0KZEgs7iqFPX00000ri1T7C00000Qgs_JA.THdBULP1doZA80K85yF9pywd0ZnqrHRknjFhm1bsnjK9P1N-nsKd5HTswH7DwHDYf1bkPjm3PWb4PWckwHRsnbFanWbswbDs0ADqI1YhUyPGujY1n1m1PH6Lrj04FMKzUvwGujYkP6K-5y9YIZK1rBtEILILQMGCpgKGUB4WUvYE5LPGujd1uydxTZGxmhwsmdqbmgPEINqYpgw_ufKWThnqnH64rjn%26tpl%3Dtpl_11534_21264_17382%26l%3D1517335524%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3363587809_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D176%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26rqlang%3Dcn%26inputT%3D2196&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E6%25B5%258B%25E8%25AF%2595%26unit%3D%25E7%25BB%25BC%25E5%2590%2588-2%26keyword%3Dwww.zhipin.com%26bd_vid%3D8928505408936828252&friend_source=0&friend_source=0; __a=73053585.1584633467.1584637310.1586754648.107.3.86.62; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1586779076; __zp_stoken__=2e3crRjQ1564o0Fi7mq1kZUtCr0hkc8EZrU0bVMSLANHagzyGctRU2CAAsU5maJ%2BeEtufJA4Z8bR%2Bsf4Ku%2FmgIwoviB%2FsGYfviRKteBz0voHhq%2BCyVpqK%2BVIIqLRFbFbYeW4'
    }
    # 获取每条招聘信息的详情
    # url = 'https://www.zhipin.com/job_detail/1ab820b5825538271XZz0ty5EFE~.html?ka=search_list_jname_19_blank&lid=nlp-2xPnVXLT9K8.search.19'
    # parse_detailed_page(url,headers)

    #获取页中的信息
    url = 'https://www.zhipin.com/c101010100/?query=python&page=1&ka=page-10'
    parse_list_page(url,headers)