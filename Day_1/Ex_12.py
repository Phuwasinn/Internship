def Sort_Dict_By_Value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

print(Sort_Dict_By_Value({'apple': 10, 'orange': 5, 'banana': 12}))
