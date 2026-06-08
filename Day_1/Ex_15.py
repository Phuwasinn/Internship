def Palindrome_Clean(string):
    cleaned = ''.join (c.lower() for c in string if c.isalnum())
    return cleaned == cleaned[::-1]

print(Palindrome_Clean('Race Car'))
