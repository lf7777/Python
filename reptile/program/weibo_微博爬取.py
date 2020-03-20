import requests,json
from w3lib.html import remove_tags
import pymysql

url ='https://m.weibo.cn/comments/hotflow?id=4481405499626858&mid=4481405499626858&max_id_type=0' 

headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
'Referer': 'https: // m.weibo.cn/u/1211441627'
}

#爬取评论中的json转为dict的数据
response = requests.get(url, headers=headers)
res_dict = json.loads(response.content)
data_list = res_dict['data']['data']

#连接mysql数据库
db = pymysql.connect('localhost','root','lf','reptile',charset='utf8mb4')

cursor = db.cursor()

sql = 'insert into comment(username,content) values'
for i in data_list:
    user = i['user']['screen_name']
    text = remove_tags(i['text'])
    # str=''
    # for k in text:
    #     if k == '<':
    #         break    global insert_sql
    #     str+=k
    if text !='':
        #执行sql添加数据语句
        insert_sql = '("{}","{}"),'.format(user,text)
        sql += insert_sql

sql = sql.rstrip(',')+';'
print(sql)
cursor.execute(sql)
# print(insert_sql)
db.commit()
db.close()

# with open('六小龄童','w') as fwb:
#     fwb.write(response.text)
