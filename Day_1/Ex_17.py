def Frequency(list):
    result = {}
    for item in list:
        result[item] = result.get(item, 0) + 1
    return result

print(Frequency(['a', 'b', 'a', 'c']))  