i = k = 1

while i < 10 :
    while k < 10 :
        print(i,'*',k,'=',i*k,'  ',end='')
        k += 1
    print()
    i += 1
    k = i
