import csv


with open("wares.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";", quotechar='"')

    for item in reader:
        if int(item["Old price"]) > int(item["New price"]):
            print(item["Name"])
