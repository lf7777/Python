import requests as req

from lxml import etree

url = 'http://goal.sports.163.com/'

rep = req.get(url)

#with open('../html/wangyiSports.html','wb') as fw:

#    fw.write(rep.content)

with open('../html/wangyiSports.html','r') as fr:

    fr = fr.read()

tree = etree.HTML(fr)

res = tree.xpath('/html/body//div[@class="leftList4"][1]/table/tr')

for i in range(1,len(res),3):
    roud = res[i].xpath('td[1]/text()')[0].strip()
    time = res[i].xpath('td[2]/text()')[0].strip()
    status = res[i].xpath('td[3]/text()')[0].strip()
    host_team = res[i].xpath('td[4]//a/text()')[0].strip()
    score = res[i].xpath('td[5]/text()')[0].strip()
    guest_team = res[i].xpath('td[6]//a/text()')[0].strip()
    print(roud,time,status,host_team,score,guest_team)
    print('-'*40)
