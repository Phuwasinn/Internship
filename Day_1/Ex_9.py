def Sliding_Window(list,n):
    return [list [i:i+n] for i in range(len(list) - n + 1)]

print(Sliding_Window([1, 2, 3, 4], 2))  



