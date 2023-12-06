f = open("input.txt", "r")
x=0
y=0
dct = {}
for char in f.read().strip().replace("\n",""):
    if char == "^":
        y+=1
    elif char == "v":
        y-=1
    elif char == ">":
        x+=1
    elif char == "<":
        x-=1
    dct[str(x)+"_"+str(y)] = dct.get(str(x)+"_"+str(y),0) + 1
print(len(dct))