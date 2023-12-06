f = open("input.txt", "r")
santa_x=0
santa_y=0
robot_x=0
robot_y=0
turn=True
dct = {}
for char in f.read().strip().replace("\n",""):
    if char == "^":
        y=1
        x=0
    elif char == "v":
        y=-1
        x=0
    elif char == ">":
        x=1
        y=0
    elif char == "<":
        x=-1
        y=0
    if turn:
        santa_x+=x
        santa_y+=y
        dct[str(santa_x) + "_" + str(santa_y)] = dct.get(str(santa_x) + "_" + str(santa_y), 0) + 1
    else:
        robot_x+=x
        robot_y+=y
        dct[str(robot_x) + "_" + str(robot_y)] = dct.get(str(robot_x) + "_" + str(robot_y), 0) + 1
    turn = not turn


print(len(dct))