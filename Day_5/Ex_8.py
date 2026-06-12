import itertools

print("User ID: ")
counter = itertools.count(1000)
for _ in range(4):
    print(next(counter))

print("\nChain(): ")
combined = itertools.chain([1,2,3], [4,5,6])
for item in combined:
    print(item)
   
print("\nProduct():")
size = ["S", "M"]
colors = ["Red", "Blue"]
for pair in itertools.product(size, colors):
    print(pair)