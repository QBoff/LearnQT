a, n = list(map(int, input().split()))
listt = []
for i in range(n):
    a = a + int(str(a)[-1])
    listt.append(int(str(a)[-1]))

print(a)
print(listt)