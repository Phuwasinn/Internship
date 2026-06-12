class MyRange:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for num in MyRange(1,5):
    print(num)