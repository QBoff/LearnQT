with open("pipes.txt", "r", encoding="utf-8") as file:
    times = []
    numbers = []
    total = 0
    for line in file.readlines():
        line = line.strip()
        times.append(line)
    
    numbers = times[-1].split(' ')
    
    del times[-1]
    del times[-1]
    
    for n in numbers:
        total += (1 / float(times[int(n) - 1]))
    
    with open("time.txt", "w") as f:
        f.write(str(1 / total * 60))