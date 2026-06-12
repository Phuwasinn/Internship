numbers = range(1,101)

even = (x for x in numbers if x % 2 == 0)
square = (x**2 for x in even)
total = sum(square)

print("Total sum = ", total)