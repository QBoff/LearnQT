chars = list(input())
set_chars = set()
new_string = ""

for i in chars:
    if i in set_chars:
        continue
    else:
        new_string += i
        set_chars.add(i)

print(new_string)
