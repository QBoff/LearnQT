N = int(input())
d = {}
a = {}
 
for i in range(N-1):
    a1, a2 = input().split()
    d[a1] = a2
    a[a1] = 0
    a[a2] = 0
    
for i in d:
    s = i
    while s in d:
        s = d[s]
        a[i] += 1

# print()
for i in sorted(a):
    print(i, a[i])