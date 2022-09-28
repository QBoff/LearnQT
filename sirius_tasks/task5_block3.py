def factorization(n: int):
    p = []
    d = 2
    string = ""
    while d * d <= n:
        while n % d == 0:
            p.append(d)
            n //= d

        if d in p:
            if p.count(d) == 1:
                string += f"{d}*"
            else:
                string += f"{d}^{p.count(d)}*"

        d += 1

    if n > 1:
        p.append(n)
        string += str(n)
    if len(string) > 0:
        return string if string[-1] != '*' else string[:-1]
    return ""


n = int(input())
print(factorization(n))
