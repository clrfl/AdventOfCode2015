from itertools import permutations

f = open('input.txt')
dct = {}
for line in f.readlines():
    line = line.strip().strip(".").split()
    if line[2] == "gain":
        value = dct.get(line[0], {})
        value.update({line[-1]: int(line[3])})
        dct[line[0]] = value
    else:
        value = dct.get(line[0], {})
        value.update({line[-1]: -int(line[3])})
        dct[line[0]] = value


def evaluate(perm):
    value = 0
    for i in range(len(perm)):
        value += dct[perm[i]][perm[i - 1]]
        value += dct[perm[i]][perm[(i + 1) % len(perm)]]
    return value


all_people = list(dct.keys())
my_dict = {}
for person in all_people:
    person_dict = dct[person]
    person_dict.update({"me":0})
    dct[person] = person_dict
    my_dict.update({person:0})

dct.update({"me":my_dict})

best = [(), float("-inf")]
perms = permutations(list(dct.keys()))

for p in perms:
    val = evaluate(p)
    best = best if best[1] > evaluate(p) else [p, val]

print(best[1])
