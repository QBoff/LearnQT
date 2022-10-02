def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


input()
a = [int(i) for i in input().split()]
mx = 0
for i in range(len(a)):
    cur_g = a[i]
    p = 0
    if len(a) - i < mx:
        break
    for j in range(i, len(a)):
        p += 1
        cur_g = gcd(cur_g, a[j])
        if cur_g == 1:
            break
        a[j] //= cur_g
        if mx < p:
            mx = p
print(mx)
