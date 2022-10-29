n = int(input())
m = int(input())

p = (lambda a, b: ((a // b) * a + (b // a) * b) // (a // b + b // a))(n, m)

q = p - (n + m - p - 1) // 2 * 2
r = 2 - (n + m - p) % 2

print(q * r)
