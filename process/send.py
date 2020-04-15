def tmp():
    yield 4

g = tmp()

print(next(g))
print(g.send(5))
print(g.send(6))
