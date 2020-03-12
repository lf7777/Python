#导入 pymongo 模块
import pymongo

#连接 mongo 服务器,创建客户端对象
client = pymongo.MongoClient('127.0.0.1',27017)

#选择库
db = client.tmp

#注意 python 操作mongo时,需要将 语句中的 字符加'',比如 '$set',但数字不需要.

# 增加数据 为staff集合增加数据
#db.staff.insert({'_id':100,'name':'小明','age':25,'sex':'男'})

# 删除数据 
#db.staff.remove({'_id':101})

# 修改数据 name 小a红 的年龄为35岁
#db.staff.update({'name':'小a红'},{'$set':{'age':36}})

# 查看数据 获取数据对象
tmp = db.staff.find()

#遍历对象,查看数据
for i in tmp:
    print(i)
