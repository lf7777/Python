def findMinAndMax(L):
    max = min = None
    if len(L) == 0:
        return min,max
    for x in L:
        if min == None or min > x:
            min = x
        if max == None or max < x:
            max = x
    return min,max

print(findMinAndMax([2,2]))

