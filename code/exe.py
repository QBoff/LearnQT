def gcd_ext(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = gcd_ext(b, a % b)
    x, y = y, x - (a // b) * y
    return d, x, y


a, b, c = list(map(int, input().split(' ')))

d, x0, y0 = gcd_ext(a, b)  # здесь мы получаем d и начальные x и y

if c % d != 0:
    print(-1)
else:
    cd = int(c / d)  # находим cd
    t = -(cd * x0 // int(b / d))  # находим t подробность есть в тетради

    x = cd * x0 + int(b / d) * t  # находим наши x и y
    y = cd * y0 - int(a / d) * t  # находим наши x и y

    if x < 0:  # нам нужны только положительные x
        # находим без t потомучто из-за t наш x стал меньше 0
        x = cd * x + int(b / d)  # находим наши x и y
        y = cd * y - int(a / d)  # находим наши x и y

    print(x, y)