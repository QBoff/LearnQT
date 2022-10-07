input()
busy_teachers = set(list(map(int, input().split())))

input()
busy_classes = set(list(map(int, input().split())))

input()
need_teachers = set(list(map(int, input().split())))

input()
free_classes = set(list(map(int, input().split())))

if len(busy_teachers & need_teachers) == 0 and \
        len(busy_classes & free_classes) < len(free_classes):

    busy_classes.add(min(list(free_classes - busy_classes)))
    busy_teachers |= need_teachers

    print(len(busy_teachers))
    print(" ".join(sorted(list(map(str, busy_teachers)))))
    print(len(busy_classes | free_classes))
    print(" ".join(sorted((list(map(str, busy_classes))))))

else:
    print(-1)
