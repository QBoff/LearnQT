import math


def mutually_prime_numbers(a, b) -> bool:
    while b > 0:
        a, b = b, a % b

    return a


def factorization(n):
    p = []
    d = 1
    while d * d <= n:

        if n % d == 0:
            p.append(d)
            if n // d != d:
                p.append(n // d)
        d += 1

    return p


n = int(input())
li = factorization(n)
size = len(li)
count = 0

for i in range(size):
    for j in range(i + 1, size):
        a = li[i]
        b = li[j]

        if mutually_prime_numbers(a, b) == 1 and a * b <= n:
            count += 1

print(count)
