def sort_wagons(queue_w):
    m = 1
    stack = []  # аналог тупика для вагонов

    for wag in queue_w:
        stack.append(wag)

        while stack[-1] == m:
            m += 1
            stack.pop()
            if len(stack) == 0:
                break

    for ost in stack[::-1]:
        if ost == m:
            stack.pop()
            m += 1

    return not stack


n = input()  # просто так :)

queue_w = list(map(int, input().split()))
print("YES" if sort_wagons(queue_w) else "NO")
