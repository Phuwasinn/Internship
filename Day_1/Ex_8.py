def Chunking_List(list, n):
    return [list[i:i+n] for i in range(0, len(list), n)]

print(Chunking_List([1, 2, 3, 4, 5], 2)) 
