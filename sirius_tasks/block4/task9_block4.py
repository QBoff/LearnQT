from collections import deque


def push_front(n):
    q.appendleft(n)
    print("ok")


def push_back(n):
    q.append(n)
    print("ok")


def pop_front():
    if len(q) == 0:
        print("error")
    else:
        print(q.popleft())


def pop_back():
    if len(q) == 0:
        print("error")
    else:
        print(q.pop())


def front():
    if len(q) == 0:
        print("error")
    else:
        print(q[0])


def back():
    if len(q) == 0:
        print("error")
    else:
        print(q[-1])


def size():
    print(len(q))


def clear():
    q.clear()
    print("ok")


q = deque()

while True:
    command = input()
    if command == "exit":
        print("bye")
        break
    elif command.split()[0] == "push_front":
        push_front(int(command.split()[-1]))
    elif command.split()[0] == "push_back":
        push_back(int(command.split()[-1]))
    elif command == "pop_front":
        pop_front()
    elif command == "pop_back":
        pop_back()
    elif command == "front":
        front()
    elif command == "back":
        back()
    elif command == "size":
        size()
    elif command == "clear":
        clear()
