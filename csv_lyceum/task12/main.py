import csv
import sys


n, m = map(int, input().split())
strings = [line.strip().split() for line in sys.stdin]

with open("exam.csv", "w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=[
                            "Фамилия", "имя", "результат 1", "результат 2", "результат 3", "сумма"],
                            delimiter=';')
    writer.writeheader()

    for item in strings:
        if int(item[-1]) + int(item[-2]) + int(item[-3]) >= n \
                and m <= int(item[-1]) and m <= int(item[-2]) and m <= int(item[-3]):

            writer.writerow({
                "Фамилия": item[0],
                "имя": item[1],
                "результат 1": int(item[2]),
                "результат 2": int(item[3]),
                "результат 3": int(item[4]),
                "сумма": int(item[2]) + int(item[3]) + int(item[4])
            })
