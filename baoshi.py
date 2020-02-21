def find(J,S):
    return sum([S.count(x) for x in J])

print(find('aA','aAAbbbb'))
