# n = list(map(int, input().split()))
ed = []
des = []
sot = []
tus = []
sottus = []
mil = []
desmil = []
stomil = []
milliard = []
m = 0

for i in input().split():
    # print(i)
    if len(i) == 1:
        ed.append(i)
    elif len(i) == 2:
        des.append(i)
    elif len(i) == 3:
        sot.append(i)
    elif len(i) == 4:
        tus.append(i)
    elif len(i) == 5:
        sottus.append(i)
    elif len(i) == 6:
        mil.append(i)
    elif len(i) == 7:
        desmil.append(i)
    elif len(i) == 8:
        stomil.append(i)
    elif len(i) == 9:
        milliard.append(i)

ed = sorted(ed, key=lambda x: -int(x))
des = sorted(des, key=lambda x: (-int(x[0]), -int(x[1])))
sot = sorted(sot, key=lambda x: (-int(x[0]), -int(x[1]), -int(x[2])))

tus = sorted(
    tus, key=lambda x: (-int(x[0]), -int(x[1]), -int(x[2]), -int(x[3])))

sottud = sorted(
    sottus, key=lambda x: (-int(x[0]), -int(x[1]), -int(x[2]), -int(x[3]), -int(x[4])))

mil = sorted(mil, key=lambda x: (-int(x[0]), -int(x[1]), -
             int(x[2]), -int(x[3]), -int(x[4]), -int(x[5])))

desmil = sorted(desmil, key=lambda x: (-int(x[0]), -int(x[1]), -int(
    x[2]), -int(x[3]), -int(x[4]), -int(x[5]), -int(x[6])))

stomil = sorted(stomil, key=lambda x: (-int(x[0]), -int(x[1]), -int(
    x[2]), -int(x[3]), -int(x[4]), -int(x[5]), -int(x[6]), -int(x[7])))

milliard = sorted(milliard, key=lambda x: (-int(x[0]), -int(x[1]), -int(
    x[2]), -int(x[3]), -int(x[4]), -int(x[5]), -int(x[6]), -int(x[7]), -int(x[8])))

print(f"{' '.join(milliard)} {' '.join(stomil)} {' '.join(desmil)} {' '.join(mil)} \
{' '.join(sottus)} {' '.join(tus)} {' '.join(sot)} {' '.join(des)} {' '.join(ed)}".strip())
