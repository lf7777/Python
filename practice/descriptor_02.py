class Test:

    def __init__(self):
        self.tmpvar = '兰鹏飞'

    def getusername(self):
        return self.tmpvar

    def setusername(self,value):
        self.tmpvar = value

    def deleteusername(self):
        pass

    username = property(getusername,setusername,deleteusername)

me = Test()

me.username = '鹏飞'

print(me.username)
