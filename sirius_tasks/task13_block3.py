import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


start = 2
nums = []
repeat = []
a, b = list(map(int, input().split(' ')))

if b == 2:
    print()
    quit()

list_of_numbers = list(filter(isPrime, [i for i in range(2, b)]))

for i in range(len(list_of_numbers)):
    for j in range(i, len(list_of_numbers)):
        if list_of_numbers[i] + list_of_numbers[j] > b:
            break
        if list_of_numbers[i] + list_of_numbers[j] >= a and \
                list_of_numbers[i] + list_of_numbers[j] <= b:

            nums.append(list_of_numbers[i] + list_of_numbers[j])

print(*sorted(set(nums)), sep="\n")
