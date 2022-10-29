import csv


name_of_fo = input()
start_year, finish_year = map(str, input().split())

with open("salary.csv", "r", encoding="utf-8") as file, \
        open("out_file.csv", "w", encoding="utf-8") as out_file:

    flag = False
    reader = list(csv.DictReader(file, delimiter=';'))
    writer = csv.DictWriter(out_file, fieldnames=[
                            "Субъект", start_year, finish_year], delimiter=';')

    for item in reader:
        if item["Федеральный округ"] == name_of_fo \
                and int(item[finish_year]) - int(item[start_year]) < int(item[start_year]) * 0.04:
            
            if not flag:
                writer.writeheader()
                flag = True
            writer.writerow(
                {"Субъект": item["Субъект"], start_year: item[start_year], finish_year: item[finish_year]})
