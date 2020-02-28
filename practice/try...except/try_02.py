girls = ['貂蝉','杨玉环']

try:

    x = 1 + 'a'

    print(girls[2])

except IndexError:

    print('索引出现了问题,请检查索引')

except TypeError:
    
    print('type')
