from sys import setrecursionlimit
setrecursionlimit(10**9)


def decomp(number):
    n = number
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans


x = int(input())
a = list(set(decomp(x)))
b = decomp(x)

y = 1
for i in range(len(a)):
    y *= a[i]
k = 1
n = k*y

if x == 1:
    print(1)
elif len(b) >= 30:
    print(y) 
else:
    while pow(n, n, x) != 0:
        n = k*y
        k += 1
    print(n)
