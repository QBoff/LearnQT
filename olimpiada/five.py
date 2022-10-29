n = int(input())

sides = [list(input()) for _ in range(n)]

trans_side = [[sides[j][i]
               for j in range(len(sides))] for i in range(len(sides[0]))]
print(trans_side)
print(sides)

if trans_side[0] == ['.'] * len(trans_side[0]) and trans_side[-1] == ['.'] * len(trans_side[0]):
    print("I")

elif trans_side[0] == ['#'] * len(trans_side[0]) and trans_side[-1] == ['*'] * len(trans_side[0]):
    print('O')
