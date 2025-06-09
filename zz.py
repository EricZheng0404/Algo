lst1 = [1,2,3]
lst2 = [2,1,3]
lst2.sort()
res = set()
res.add(tuple(lst1))
res.add(tuple(lst2))
print(res)