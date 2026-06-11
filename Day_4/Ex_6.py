MAX_ATTEMPTS = 3

for attempt in range(1, MAX_ATTEMPTS + 1):
    try:
        value = int (input(f"Attempt {attempt} | Enter an integer: "))
        print("Got: ", value)
        break
    except ValueError:
        print("Invalid input, try againnn")
          
else:
    print("Too many failed attempts")