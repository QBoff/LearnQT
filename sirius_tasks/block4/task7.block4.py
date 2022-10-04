first_player = list(map(int, input().split()))  # queue 1
second_player = list(map(int, input().split()))  # queue 2
count = 0

while first_player and second_player:
    count += 1
    card1, card2 = first_player.pop(0), second_player.pop(0)

    if card1 > card2 and (card2, card1) != (0, 9) or (card1, card2) == (0, 9):
        first_player.append(card1)
        first_player.append(card2)

    else:
        second_player.append(card1)
        second_player.append(card2)

    if count == 1000000:
        print("botva")
        break

if len(first_player) == 0:
    print(f"second {count}")
else:
    print(f"first {count}")
