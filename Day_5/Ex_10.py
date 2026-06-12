def generate_numbers():
    yield from range(1,6)
    
def generate_squares():
    yield from (x**2 for x in range (1,6))

def combine_stream():
    yield from generate_numbers()
    yield from generate_squares()

for value in combine_stream():
    print(value)