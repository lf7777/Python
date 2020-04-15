#登录bilibili 的个人主页
import requests
 
url = 'https://passport.bilibili.com/web/login/v2'

#提交给服务器的信息,data数据为字典格式.
form = {
'captchaType': 6,
'username': 15901060580,
'password': 'PbNbnkrqRkz1Z+pJ+v1xIjj6BeoW2HkLfj+ykncbtWKeXsC5nzq/cowoDdso/+CZ/49mj0dImsFIVtacR9k7+2m7Ss5VtUu+rrU13PqoRtHbSVC0uCMtB+yKKd0i7v+BJgtCX7tYYx+hi32JKmML1ikAy8JTBz6YNAUKHeBN30Q=',
'keep': 'true',
'key': '7f20a3f6c3f646b09c5721742303fdda',
'goUrl': 'https://space.bilibili.com/363990503',
'challenge': 'b5b34326995f3ed2f3f3bd6e0b349c0dlk',
'validate': '6373311f8842fa6b8baabaf2afd003a2',
'seccode': '6373311f8842fa6b8baabaf2afd003a2|jordan'
}

#实例化 session对象 (session会将post的data信息,进行登录验证并可 爬取登后的数据)
sess = requests.session()

#post(找到要登录成功马上跳转的POST请求包,data写表单的字典格式)
response = sess.post(url,data=form)

#session 对象会存取登录的信息,这时可以获取登录后的信息.
response = sess.get()

print(response)
