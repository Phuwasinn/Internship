def Deep_flatten(list):
    result = []
    for item in list:
        if isinstance(item, list):
            result.extend(Deep_flatten(item))
        else:
            result.append(item)
    return result

print(Deep_flatten([1, [2, [3, 4]], 5])) 
