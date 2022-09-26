def reverse():
    with open("input.dat", "rb", encoding="utf-8") as file:
        b = file.read()
    
    with open("output.dat", "wb", encoding="utf-8") as file:
        file.write(b[::-1])


print()