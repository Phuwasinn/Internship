import time, sys

N = 1_000_000

start = time.time()
list_square = [x**2 for x in range(1, N + 1)]
list_time = time.time() - start
list_memory = sys.getsizeof(list_square)

start = time.time()
gen_square = (x**2 for x in range(1, N + 1))
gen_time = time.time() - start
gen_memory = sys.getsizeof(gen_square)

print(f"List time: {list_time:.4f} s | memory: {list_memory:,} bytes")
print(f"Generator time: {gen_time:.4f} s | memory: {gen_memory:,} bytes")