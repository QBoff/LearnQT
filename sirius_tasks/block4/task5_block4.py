def push(n):
    queue.append(n)
    print("ok")


def pop():
    if len(queue) == 0:
        print("error")
    else:
        print(queue.pop(0))


def front():
    if len(queue) == 0:
        print("error")
    else:
        print(queue[0])


def size():
    print(len(queue))


def clear():
    queue.clear()
    print("ok")


queue = []

command = input()

while command != "exit":
    if command.split()[0] == "push":
        push(int(command.split()[1]))
    elif command == "pop":
        pop()
    elif command == "front":
        front()
    elif command == "size":
        size()
    elif command == "clear":
        clear()

    command = input()
else:
    print("bye")
