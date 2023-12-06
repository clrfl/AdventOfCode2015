f = open("input.txt", "r")
sum = 0
for line in f.readlines():
    line = line.strip()
    vowels = 0
    last = "."
    doubles = 0
    forbidden = 0
    for char in line:
        if last + char in ["ab","cd","pq","xy"]:
            forbidden += 1
        if char == last:
            doubles += 1
        last = char
        if char in "aeiou":
            vowels +=1
    if vowels >= 3 and doubles > 0 and forbidden == 0:
        sum += 1
print(sum)
