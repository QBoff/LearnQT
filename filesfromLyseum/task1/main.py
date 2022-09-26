import random


def random_line(afile):
    line = None
    try:
        line = next(afile)
        for num, aline in enumerate(afile, 2):
            n = random.randrange(num)
            if n:
                # print(random.randrange(num))
                continue
            line = aline
        return line.strip()

    except Exception:
        pass


with open("lines.txt", encoding="utf-8") as file:
    n = random_line(file)
    if n is not None:
        print(n)
