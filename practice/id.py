=0
k=0
for i in range(1000):
    for k in range(1000): 
        if id(i)==id(k):
            print(i,k)

