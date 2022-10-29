import itertools

n = range(int(input()))
m = int(input())


def numbers_of_combination(len_):
    for s in itertools.combinations(n, len_):
        y = sum(int(i) for i in s)
        if y == m:
            return s


for L in range(0, len(n) + 1):
    ans = numbers_of_combination(L)
    if ans:
        print(ans, sep='\n')
        break
else:
    print(0)
