def Missing_Num(list):
    n = len(list) + 1
    expected = n * (n+1) // 2
    return expected - sum(list)

print (Missing_Num([1, 2, 4, 5]))