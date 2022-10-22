import csv


with open("wares.csv", "r", encoding="utf-8") as file:
    cash, ind, limit = 1000, 0, 10
    res = []
    reader = csv.reader(file, delimiter=';', quotechar='"')

    costs_list = list(
        map(lambda x: [x[0], int(x[1])], sorted(reader, key=lambda x: int(x[1]))))
    # print(costs_list)
    while cash > 0:
        if costs_list[ind][1] > 1000 and ind == 0:
            res.append("error")
            break

        if limit > 0:
            if cash - costs_list[ind][1] >= 0:
                res.append(costs_list[ind][0])
                limit -= 1
                cash -= costs_list[ind][1]
            else:
                break

        if limit == 0:
            limit = 10
            ind += 1

    print(', '.join(res))
