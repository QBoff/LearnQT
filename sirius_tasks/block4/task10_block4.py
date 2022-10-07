from collections import deque


n = int(input())

q = deque()  # очередь до середины
q2 = deque()  # очередь после середины
length_q = 0
length_q2 = 0

for i in range(n):
    com = input().split()

    if com[0] == '-':
        print(q.popleft())
        length_q -= 1
    elif com[0] == '+':
        q2.append(com[-1])
        length_q2 += 1

    else:
        q2.appendleft(com[-1])
        length_q2 += 1

    if length_q < length_q2:

        length_q += 1
        length_q2 -= 1
        q.append(q2.popleft())
