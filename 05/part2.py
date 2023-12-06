f = open("input.txt", "r")
sum = 0
for line in f.readlines():
    line = line.strip()
    pairs = []
    last = "."
    doubles = 0
    doublechars = 0

    for char in line:
        pairs.append(last+char)
        last = char

    for i in range(len(pairs)):
        indices = [j for j, x in enumerate(pairs) if x == pairs[i]]
        for index in indices:
            if index != i-1 and index != i and index != i+1:
                doubles += 1

    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            doublechars += 1

    if doubles > 0 and doublechars > 0:
        sum += 1

print(sum)
