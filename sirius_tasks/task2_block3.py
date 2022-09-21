from math import sqrt, ceil


def isPrime(a) -> bool:
    flag = True
    for i in range(2, ceil(sqrt(a))):
        if a % i == 0:
            flag = False
    if flag:
        return True
    return False


n = int(input())

t = 2
flag = False
i = ceil(sqrt(n))
while t <= ceil(sqrt(n)):
    if n % t == 0 and isPrime(t):
        flag = True
        print(t)
        break
    else:
        t += 1

if not flag:
    print(n)
