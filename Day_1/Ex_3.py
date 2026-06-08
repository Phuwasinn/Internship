def Unique_preserved(list):
    seen = set()
    return [x for x in list if not (x in seen or seen.add(x))]

print(Unique_preserved([3,1,2,3,4,1]))
