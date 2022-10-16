import math

nums = {
    0: [0],
    1: [2, 4, 8, 6],
    2: [4, 8, 6, 2],
    3: [6, 2, 4, 8],
    4: [8, 6, 2, 4],
    5: [0],
    6: [2, 4, 8, 6],
    7: [4, 8, 6, 2],
    8: [6, 2, 4, 8],
    9: [8, 6, 2, 4]
}

a, n = list(map(int, input().split()))
if n <= 0:
    print(a)
else:    
    last_t = int(str(a)[-1])
    if n >= len(nums[last_t]):
        lp = len(nums[last_t])
        s = 0
        nn = n
        for i in range(math.ceil(n / len(nums[last_t]))):
            if nn - lp >= 0:
                s += sum(nums[last_t])
            else:
                s += sum(nums[last_t][:nn - lp])
            nn -= lp
        # if a < 10:
        #     print(s)
        # else:
        #     print(10 + s)
        print(s)
    else:
        print(a + last_t + sum(nums[last_t][:n - 1]))
