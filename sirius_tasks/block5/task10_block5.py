n = int(input())
a = list()
x = set()
y = set()

for i in range(n):
    xx, yy = map(int, input().split())
    a.append([xx, yy])

a.sort()

for i in range(n - 1):
    if a[i + 1][0] == a[i][0] and a[i + 1][1] > a[i][1]:
        y.add(a[i][1] + 1)
    else:
        x.add(a[i][0] + 1)

print(len(x) + len(y))

for i in y:
    print("y " + str(i))
for i in x:
    print("x " + str(i))
