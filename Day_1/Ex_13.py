def Max_in_list(data, key):
    return max(item[key] for item in data)

print(Max_in_list([{'val': 10}, {'val': 50}], 'val')) 
