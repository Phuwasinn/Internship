class Shelf:
    def __init__(self, item):
        self.item = item

    def __len__(self):
        return len(self.item)
    
my_shelf = Shelf(["Phone", "Cup", "Computer"])
print (len(my_shelf))