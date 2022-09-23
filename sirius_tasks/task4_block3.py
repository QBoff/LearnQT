n = int(input())
a = n * 17

prime = [True] * (a + 1)
prime[0] = prime[1] = False

if n == 1:
    print(2)
    quit()

for i in range(2, a + 1):
    if not prime[i]:
        continue

    for j in range(i * i, a + 1, i):
        prime[j] = False

count = 0

for item in range(a):
    if prime[item]:
        count += 1
    
    if count == n:
        print(item)
        break
