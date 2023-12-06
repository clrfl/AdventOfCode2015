f = open("input.txt", "r")
text = f.read().strip()
level = 0
for i in range(len(text)):
    if text[i] == "(":
        level += 1
    elif text[i] == ")":
        level -= 1
    if level == -1:
        break
print(i+1)