try:
    f = open("test.txt", "a")
    f.write("Hello")
    
except Exception as e:
    print("Error: ", e)
finally:
    f.close()
    print("File closed")