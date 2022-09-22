from math import ceil, sqrt


n = int(input())
t = 2

if n == 1:
    print(1, 1)
else:
    count, summ = 0, 0
    
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0 and i != sqrt(n):
            count += 2
            summ += (i + n // i)
        elif n % i == 0 and i == sqrt(n):
            count += 1
            summ += i
    print(int(count), int(summ))
    print(type(ceil(sqrt(n))))
    print(ceil(sqrt(n)), int(sqrt(n)) + 1)