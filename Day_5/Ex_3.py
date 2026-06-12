import sys

list = [x**2 for x in range(1, 1_000_001)]
gen = (x**2 for x in range(1, 1_000_001))

print("List type: ", type(list))
print("Generator type: ", type(gen))

print(f"List size: {sys.getsizeof(list):,} bytes")
print(f"Generator size: {sys.getsizeof(gen):,} bytes")