from sys import setrecursionlimit
setrecursionlimit(10**9)  # увеличение максимальной глубины рекурсии


def decomp(number):
    n = number  # функция разложения числа на простые множители
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
a = list(set(decomp(x)))  # разложение числа x на простые множители в единственном экземпляре
b = decomp(x)  # разложение числа x на простые множители

y = 1
for i in range(len(a)):  # перемножение простых множителей
    y *= a[i]
k = 1
n = k*y

if x == 1:  # если x = 1, то и n = 1
    print(1)
elif len(b) >= 30:  # 29 - потому что хотя бы 2**30 уже будет более 10**9, что противоречит условию задачи
    print(y)  # тогда y**y уже будет делится на n
else:
    while pow(n, n, x) != 0:
        n = k*y
        k += 1
    print(n)
