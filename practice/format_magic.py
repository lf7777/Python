class Girl:
    name = '初墨'

    sex = '女'

    def shopping(self):
        print('购物')
    
    def __format__(self,arg):
        if arg[1] == '>':
            newname = self.name.rjust(int(arg[2:]),arg[0])
            return newname
        elif arg[1] == '^':
            newname = self.name.center(int(arg[2:],arg[0]))
            return newname
        elif arg[1] == '<':
            newname = self.name.ljust(int(arg[2:],arg[0]))
            return newname
        else:
            return ''


xcm = Girl()

print('我的女朋友叫{:0>10}'.format(xcm))
