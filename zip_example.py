# zip 将两个可迭代对象的元素 逐一合并 (列表,元祖,集合,字典) 得到 <迭代器>

res = zip([1,2],[4,5])

res = zip((1,2),(4,5))

res1 = zip({1,2},{4,5})

res = zip({1:2},{4:5})


#通过 类型转换函数,将迭代器 转为对应的数据类型

res = list(res)

res = tuple(res)

res = set(res)

res = dict(res)

print(res1)
# 打印结果是迭代器内存地址
