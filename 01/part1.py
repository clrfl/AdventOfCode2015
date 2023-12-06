f = open("input.txt", "r")
text = f.read().strip()
level = 0
for i in text:
    if i == "(":
        level += 1
    elif i == ")":
        level -= 1
print(level)