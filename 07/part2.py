import numpy as np

f = open("input.txt", "r")

dct = {}
results = {}


def reduce(idx, val):

    if len(val) == 1:

        if type(val[0]) == np.uint16:
            if idx not in results:
                results[idx] = val[0]

        elif type(val[0]) == str:
            if val[0] in results and idx not in results:
                results[idx] = results[val[0]]

    if len(val) == 2:

        if type(val[1]) == np.uint16:
            results[idx] = ~val[1]

        elif type(val[1]) == str:
            if val[1] in results and idx not in results:
                results[idx] = ~results[val[1]]

    elif len(val) == 3:

        if type(val[0]) == str:
            if val[0] in results:
                val[0] = results[val[0]]

        if type(val[2]) == str:
            if val[2] in results:
                val[2] = results[val[2]]

        if type(val[0]) == type(val[2]) == np.uint16:

            if val[1] == "AND" and idx not in results:
                results[idx] = val[0] & val[2]

            elif val[1] == "OR" and idx not in results:
                results[idx] = val[0] | val[2]

            elif val[1] == "RSHIFT" and idx not in results:
                results[idx] = val[0] >> val[2]

            elif val[1] == "LSHIFT" and idx not in results:
                results[idx] = val[0] << val[2]


for line in f.readlines():
    line = line.strip().split("->")
    values = line[0].strip().split(" ")
    for i in range(len(values)):
        if values[i].isnumeric():
            values[i] = np.uint16(values[i])
    dct[line[1].strip()] = values

dct["b"] = [np.uint16("16076")]

request = "a"
while request not in results:
    for entry in dct:
        reduce(entry, dct[entry])

print(results[request])
