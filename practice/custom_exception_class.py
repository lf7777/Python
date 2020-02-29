#定义异常类型
class UnlockError(Exception):

    #为异常类添加更多信息
    def __init__(self,errmg,errnb,errfile):

        #记录错误信息
        self.errmg = errmg

        #记录错误编号
        self.errnb = errnb

        #记录错误文件
        self.errfile = errfile

#try语法

try:
    tmplist = [1,2,3,4,5,6]

    for i in tmplist:

        #检测容器中是否包含4的数据. <有没有异常需要自己判断>
        if '4' in str(i):

            #出现不幸运的异常,手动抛出
            raise UnlockError('容器中出现了不幸运的数字4',444,'practice/custom_exception_class.py')

except UnlockError as err:

    print(err)

    print('出错')
