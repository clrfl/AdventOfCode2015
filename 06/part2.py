f = open("input.txt", "r")
dct = {}
summe = 0

for line in f.readlines():
    line = line.strip().split(" ")
    if line[0] != "toggle":
        line = line[1:]

    start = line[1].split(",")
    end = line[3].split(",")

    if line[0] == "on":
        for i in range(int(start[0]), int(end[0]) + 1):
            for j in range(int(start[1]), int(end[1]) + 1):
                dct[str(i) + "-" + str(j)] = dct.get(str(i) + "-" + str(j), 0) + 1
    elif line[0] == "off":
        for i in range(int(start[0]), int(end[0]) + 1):
            for j in range(int(start[1]), int(end[1]) + 1):
                val = dct.get(str(i) + "-" + str(j), 0)
                val -= 1
                if val < 0:
                    val = 0
                dct[str(i) + "-" + str(j)] = val
    else:
        for i in range(int(start[0]), int(end[0]) + 1):
            for j in range(int(start[1]), int(end[1]) + 1):
                dct[str(i) + "-" + str(j)] = dct.get(str(i) + "-" + str(j), 0) + 2

for entry in dct:
    summe += dct[entry]
print(summe)
