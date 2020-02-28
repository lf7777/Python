class Descriptor:

    def __init__(self):
        self.tmpvar = '匿名用户'

    def __get__(self,obj,cls):
        res = self.tmpvar.replace(self.tmpvar[1:-1],'*')
        return res

    def __set__(self,obj,value):
        if len(value) > 10 :
            print('请重新设置')
        else:
            self.tmpvar = value

    def __delete__(self,obj):
        if obj.isallowdel_username == True:
            del self.tmpvar

class Email:

    username = Descriptor()

    password = '123456'

    phone = 123456789

    isallowdel_username = False

    def login(self):
        print('登录方法')

    def logout(self):
        print('退出方法')

mail = Email()

#mail.username = 'lovemybaby'

print(mail.username)

del mail.username

print(mail.username)
