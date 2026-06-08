def Group_By_Prefix(words):
    result = {}
    for word in words:
        Prefix = word[0]
        if Prefix not in result:
            result[Prefix] = []
        
        result[Prefix].append(word)
    return result

print(Group_By_Prefix(['apple', 'bat', 'ant']))  
