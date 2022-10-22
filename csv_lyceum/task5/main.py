import csv


percent = float(input())

with open("vps.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=';', quotechar='"')

    for item in reader:
        if float(item["соответствует в %"]) >= percent:
            print(item["Специальность"])
