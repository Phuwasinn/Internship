def Dict_Merge_Sum(d1, d2):
    result = dict(d1)
    for key, value in d2.items():
        result[key] = result.get(key, 0) + value
    return result

print(Dict_Merge_Sum({'a': 10, 'b': 5}, {'a': 5, 'c': 1}))  

