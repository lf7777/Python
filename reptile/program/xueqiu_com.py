import requests,json

import pymysql


#url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20368889&count=15&category=-1'

#url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20368874&count=15&category=-1'


headers = {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive', 'Cookie': 'aliyungf_tc=AQAAAHtUiUOr+AoArSaIdaeRj2cy41G4; acw_tc=2760822715842685557376402edc11bb9ace3d6cfd97413ef8828dffc3efaa; xq_a_token=a664afb60c7036c7947578ac1a5860c4cfb6b3b5; xqat=a664afb60c7036c7947578ac1a5860c4cfb6b3b5; xq_r_token=01d9e7361ed17caf0fa5eff6465d1c90dbde9ae2; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU4NTM2MjYwNywiY3RtIjoxNTg0MjY4NTAzNDExLCJjaWQiOiJkOWQwbjRBWnVwIn0.k7JLo_TNAJr_ynkDcM9DdZODrzeUUCX92uDmDgxnwWzLy99_DXq6NrFQwSru8tMVmVm9NDNg1MU4_sjjZDCJOaoNJWvhckojNgzD-M_kSj6FVWRmOCLwWiTwA9pz_sj_2vzbAbUcmNCvb73JFdS43O9OYb9SG-Zx4--pyUFwQyKQwfOJa6v1CZgjK-dOCLxr-wKADlDhJ8xbFs8ue4mQrQKZwuu-xdB9veTjdcrO7_37_VqHOFBYnSZyyVnmphKYStOfpzvjugEMFTrH9Y8K6ZbkGJQCTswecj33z1xjq1bytpfYHQ5gyadJ0u29wGOvGDvpqpEhX-x-rAk0cZ_ejw; u=831584268555745; Hm_lvt_1db88642e346389874251b5a1eded6e3=1584268558; device_id=24700f9f1986800ab4fcc880530dd0ed; cookiesu=661584268926513; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1584268927', 'elastic-apm-traceparent': '00-2082e0f193fc28858cea747f1eeb85f8-7f01cca1d2e18578-01', 'Host': 'xueqiu.com', 'Referer': 'https://xueqiu.com/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}



#连接数据库

db = pymysql.connect('localhost','root','lf','reptile',charset='utf8mb4')

cursor = db.cursor()


for k in range(0,400,15):

    url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id={}&count=15&category=-1'.format(20368904-k)
    
    response = requests.get(url,headers=headers)

    res_dict = json.loads(response.text)

    data_list = res_dict['list']
    

    for i in data_list:

        res = json.loads(i['data'])

        title = res['title']

        if title == '':
            continue

        sql = 'insert into xueqiu values(null,"{}")'.format(title)

        cursor.execute(sql)

        print(1)

db.commit()

db.close()
