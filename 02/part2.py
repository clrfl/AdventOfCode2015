f = open("input.txt", "r")
area = 0
for line in f.readlines():
    line = line.strip().split("x")
    for i in range(3):
        line[i] = int(line[i])
    line.sort()
    area += (line[0]+line[1])*2 + line[0]*line[1]*line[2]

print(area)
