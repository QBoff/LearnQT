import csv

s = {}

with open('input.csv', encoding='utf-8') as csvfile:

    reader = list(csv.reader(csvfile, delimiter=';'))
    S = reader[-1]
    reader = sorted(reader[:-1], key=lambda x: int(x[-1]))

    for i in reader[:-1]:
        if i[0] == S[0] and i[1] == S[1]:
            s[f'{i[0]} {i[1]}'] = int(i[2])
            continue

        for j in reader[:-1]:

            if i[1] == j[0] and i[0] == S[0] and j[1] == S[1]:
                s[f'{i[0]} {i[1]} {j[1]}'] = int(i[2]) + int(j[2])

    f = min(list(s.values()))
    for i in s.keys():
        if s[i] == f:
            print(i)
