def solve(lst):
    st = []
    for w in lst:
        if w.isdigit():
            st.append(int(w))
            continue
        y = st.pop()
        x = st.pop()
        z = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y
        }[w](x, y)
        st.append(z)
    return st.pop()
 
 
lst = input().split()
print(solve(lst))