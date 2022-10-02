def solve(n):
    d = 0
    while not (n & 1):
        d += 1
        n //= 2

    a = [2]*d
    a[-1] *= n

    if d == 1:
        print("prime")
        return

    for x in range(3, int(n**.5)+1, 2):
        if not (n % x):
            b = a[:]
            b[-1] //= x
            b[-2] *= x
            print("many")
            print(" ".join(map(str, a)))
            print(" ".join(map(str, b)))
            return

    print("single")
    print(" ".join(map(str, a)))


# for line in stdin:
#   print("=== " + line.strip() + " ===")
solve(int(input()))
