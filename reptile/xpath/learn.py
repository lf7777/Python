#import requests as req
from lxml import etree

# ./相对路径     /绝对路径
# @查找属性的值  //搜索
# 过滤:[@itemprop] 包含content属性的
# 不包含 [not(@itemprop)]

#url = 'http://lol.178.com/'
#rep = req.get(url)

# 写入文件
#with open('learn.html','wb') as fw:
#    fw.write(rep.content)

# 读取文件 !!! 将fr.read()指向fr,获得对象(读取格式默认是string)
with open("learn.html", 'r') as fr:
    fr_out = fr.read()

tree = etree.HTML(fr_out)

res = tree.xpath('//div[@class="ui-oline-drop"]/a//text()')

print(res)


#title_ele = html_ele.xpath('/html/head/title')
# print(title_ele[0].text)
#title_ele = html_ele.xpath('/html/head/title/text()')
# print(title_ele[0])
# 找head中所有的meta标签 Xpath 索引1开始,和python不同
# @获取属性的 值
#port = tree.xpath('/html/body//tr//td[3]/text()')
                　#找所有tr中的所有td,取第三个td,并取其内容
