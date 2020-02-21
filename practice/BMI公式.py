# -*- coding: utf-8 -*-

h = 1.75

w = 80.5

BMI = w/h**2

print('BMI的值为，%f'%BMI)

if BMI>32:

    print('高于32：严重肥胖')

elif BMI>=28:

    print('28-32：肥胖')

elif BMI>=25:

    print('25-28：过重')

elif BMI>=18.5:

    print('18.5-25：正常')

else:

    print('低于18.5：过轻')
