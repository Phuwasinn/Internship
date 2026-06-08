def Flatten_2D_List(list):
    return [item for sublist in list for item in sublist]

print(Flatten_2D_List([[1,2],[3,4],[5]]))