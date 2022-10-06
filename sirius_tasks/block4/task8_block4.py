st = []
st2 = []
mn = []  # Поддержание минимума в 1 стеке
mn2 = []  # Поддержание минимума во 2 стеке
res = []  # Результаты операций для вывода ответа


def push(a):
    global st
    global mn
    st.append(a)
    if not mn or a < mn[-1]:
        mn.append(a)
    else:
        mn.append(mn[-1])


def get_min():
    global st
    global st2
    global mn
    global mn2
    if not st2 and st:
        for i in range(len(st)):
            if not mn2 or st[-1] < mn2[-1]:
                mn2.append(st[-1])
            else:
                mn2.append(mn2[-1])
            st2.append(st.pop())
        st = []
        mn = []
    if not st2 and not st:
        res.append(-1)
    elif mn:
        st2.pop()
        res.append(min(mn[-1], mn2.pop()))
    else:
        st2.pop()
        res.append(mn2.pop())


for k in range(int(input())):
    a = int(input())
    if a != 0:
        push(a)
    else:
        get_min()
print(*res, sep='\n')
