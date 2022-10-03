def palindrome():
    a = ""
    
    with open("input.dat", "rb") as f:
        a = f.read()
    
    return a == a[::-1]


print(palindrome())