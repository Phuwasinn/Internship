def Anagram_Grouping(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

print(Anagram_Grouping(['eat', 'tea', 'tan', 'nat',]))

