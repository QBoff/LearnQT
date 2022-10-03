def size(a):
    summ = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4}
    asum = 0
    for i in a:
        j = i.split()
        asum += int(j[0]) * 2 ** (10 * int(summ[j[1]]))
    k = 0
    while asum >= 1024:
        asum /= 1024
        k += 1
    summ1 = {v: k for k, v in summ.items()}
    st = str(round(asum)) + ' ' + summ1[k]
    return st


d = {}
dt = {}


with open("input.txt", "r", encoding="utf-8") as f:

    f = f.readlines()
    for i in f:
        a = i.split(maxsplit=1)
        t = a[0].split('.')
        if t[1] not in d:
            d[t[1]] = [a[0]]
            dt[t[1]] = [a[1]]
        else:
            d[t[1]].append(a[0])
            dt[t[1]].append(a[1])

    with open("output.txt", "w", encoding="utf-8") as f2:
        # f2 = open('output.txt', 'w')
        list_keys = sorted(list(d.keys()))
        for i in list_keys:
            for j in sorted(d[i]):
                f2.write(j + '\n')
            Summary = size(dt[i])
            f2.write('----------' + '\n' + 'Summary: ' + Summary + '\n \n')
