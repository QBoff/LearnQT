n = input()
set_a = set(map(int, input().split()))

n2 = input()
set_b = set(map(int, input().split()))

print(len(set_a ^ set_b))

if len(set_a ^ set_b) != 0:
    print(*sorted(list(set_a ^ set_b)))
