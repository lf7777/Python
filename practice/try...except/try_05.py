girls = ['貂蝉','杨玉环','嫦娥']

try:

    print(girls[10])

except NameError as err:

    print(girls[-1])

except TypeError as t :

    print(t)

except :

    print('索引出现问题')
