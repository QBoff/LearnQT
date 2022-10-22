import csv
import sys


text = [line.strip().split("\t") for line in sys.stdin]

headers = ["nomen", "definitio", "pluma",
           "Russian nomen", "familia", "Russian nomen familia"]

with open("plantis.csv", "w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=headers,
                            delimiter=";", quotechar='"')
    writer.writeheader()
    # print(text)
    for item in text:
        res = {}
        for i in range(len(item)):
            res[headers[i]] = item[i]

        writer.writerow(res)
