
dct = {input() for _ in range(int(input()))}
dct2 = {w.lower() for w in dct}
# print(dct2)
# print(dct)
text = input().split()

mist = 0

for word in text:

    if word not in dct:
        x = sum(map(str.isupper, word))

        if x != 1:
            mist += 1
            continue

        if word.lower() in dct2:
            mist += 1

print(mist)
