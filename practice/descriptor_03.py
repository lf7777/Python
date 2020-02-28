class Email:

    password = '123456'

    phone = 123456789

    isallowdel_username = False

    def __init__(self):
        self.tmpvar = '匿名用户'
    
    @property 
    def username(self):
        return self.tmpvar

    @username.setter 
    def username(self,value):
        self.tmpvar = value

    @username.deleter 
    def username(self):
        if self.isallowdel_username == True:
            del self.tmpvar

    def login(self):
        print('登录方法')

    def logout(self):
        print('退出方法')


mail = Email()

print(mail.username)

mail.username = '火云邪神'

print(mail.username)

del mail.username

print(mail.username)

