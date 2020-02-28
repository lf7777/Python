girls = ['貂蝉','杨玉环','嫦娥']

try:

    print(girls[10])

except IndexError as err:

#索引出现问题,自动设置为最大索引.

    print(girls[-1])

except TypeError as t :

    print(t)
