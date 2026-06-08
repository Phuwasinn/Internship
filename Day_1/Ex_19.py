def Intersect (list1, list2):
    return [x for x in list1 if x in list2]

print(Intersect([1, 2, 3], [2, 3, 4]))