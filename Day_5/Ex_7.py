def batch(data, size):
    for i in range(0, len(data), size):
        yield data[i: i + size]

records = list(range(1, 1001))  

batches = list(batch(records, 100))

print(f"Total batches: {len(batches)}")
for i, b in enumerate(batches, 1):
    print(f"Batch {i}: {b[0]} - {b[-1]} ({len(b)} records)")