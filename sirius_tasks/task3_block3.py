from math import ceil, sqrt


n = int(input())
t = 2

if n == 1:
    print(1, 1)
else:
    divisors = [n, 1]

    while t < ceil(sqrt(n)):
        if n % t == 0:
            divisors.append(t)
            divisors.append(n // t)

        t += 1

    print(len(divisors), sum(divisors))
