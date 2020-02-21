def func(x,y):
    print('初始值价格为:',x)
    count = 0;
    i = 0
    while i<100: 
        x +=x/10
        count+=1
        print('第',count,'个涨停板的价格是','%.2f'%x)
        i+=1
        if x>y:
            break

func(7.74,20)
