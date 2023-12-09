totallength = 0
f = open("input.txt", "r")
strbuilder = ""

for line in f.readlines():
    totallength += len(line.strip())
    line = '"' + line.strip().replace('\\', '\\\\').replace('"', '\\"') + '"'
    #line = re.sub("\\\\x[a-fA-F0-9]{2}", "X", line)
    strbuilder += line

print(len(strbuilder) - totallength)
