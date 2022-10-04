def push(n):
    stack.append(n)
    print("ok")


def pop():
    if stack:
        n = stack.pop()
        print(n)
    else:
        print("error")


def back():
    if stack:
        print(stack[-1])
    else:
        print("error")


def size():
    print(len(stack))


def clear():
    stack.clear()
    print("ok")


stack = []
command = input()

while True:
    if command == "exit":
        print("bye")
        break
    elif command == "size":
        size()
    elif "push" in command:
        push(int(command.split()[-1]))
    elif command == "pop":
        pop()
    elif command == "back":
        back()
    elif command == "clear":
        clear()
    
    command = input()
