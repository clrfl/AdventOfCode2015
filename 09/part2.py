f = open("input.txt", "r")
dct = {}
dist_nodes = []
for line in f.readlines():
    line = line.strip().split(" = ")
    dist = line[1]
    nodes = line[0].split(" to ")
    dct[nodes[0]] = dct.get(nodes[0], []) + [(nodes[1], dist)]
    dct[nodes[1]] = dct.get(nodes[1], []) + [(nodes[0], dist)]
    if nodes[0] not in dist_nodes:
        dist_nodes.append(nodes[0])
    if nodes[1] not in dist_nodes:
        dist_nodes.append(nodes[1])


def explore_node(node):
    positions = [(0, [node])]
    final_paths = []

    while positions:

        entry = positions.pop()
        path = entry[1]

        if len(path) == len(["start"] + dist_nodes):
            final_paths.append(entry)
            continue

        for element in dct[path[-1]]:

            if element[0] not in path:  # not visited yet
                positions.append((int(entry[0]) + int(element[1]), path + [element[0]]))

    return final_paths


for node in dist_nodes:
    dct["start"] = dct.get("start", []) + [(node, "0")]

finals = explore_node("start")

maxi = 0
for entry in finals:
    maxi = max(entry[0], maxi)

print(maxi)
