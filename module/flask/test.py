#小项目临时记录:

from flask import Flask,render_template
import pymongo
app = Flask(__name__)

#装饰器语法定义路由,访问路径,在后面的函数中进行业务逻辑操作
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():

    #连接到 127.0.0.1 的mongo
    client = pymongo.MongoClient('127.0.0.1',27017)

    #选择tmp库
    db = client.tmp

    #获取数据
    staff = db.staff.find()
    #使用模板 返回值为固定格式,参数 为会在当前目录下(同py文件平级)
    #到templates文件夹里寻找 文件名 是指定参数的文件.
    return render_template('template_01.html',data=staff)

if __name__ == '__main__':
    app.run(debug=True)
