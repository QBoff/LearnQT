import csv


length = 0
results = []
start_time = ""
start_date = ""
with open("alpha_oriona.csv", "r", encoding="utf-8") as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    pq = []
    start_time = reader[0]["time"]
    start_date = reader[0]["date"]
    for i in range(1, len(reader)):
        if int(reader[i - 1]["luminosity"]) >= int(reader[i]["luminosity"]):
            pq.append(int(reader[i - 1]["luminosity"]))
            if i == len(reader) - 1:
                pq.append(int(reader[i]["luminosity"]))
                results.append((pq, length, start_time, start_date))
        else:
            pq.append(int(reader[i - 1]["luminosity"]))
            results.append((pq, length, start_time, start_date))
            pq = []
            start_time = reader[i]["time"]
            start_date = reader[i]["date"]

res = max(results, key=lambda x: len(x[0]))
# print(res)
# print(max(results, key=lambda x: x[0]))
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(f"{len(res[0])}\n")
    f.write(f"{res[-1]} {res[-2]}")
