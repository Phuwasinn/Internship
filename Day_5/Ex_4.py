import os

with open("large_file.txt", "w") as f:
    for i in range(1, 10_001):
        f.write(f"Line {i}\n")
    
def read_file(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()

gen = read_file("large_file.txt")

for _ in range(5):
    print(next(gen))

line_count = sum(1 for _ in read_file("large_file.txt"))
print(f"Total lines: {line_count}")

os.remove("large_file.txt")