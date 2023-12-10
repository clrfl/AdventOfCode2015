import json

f = open('input.txt')
data = json.load(f)


def parse(input):
    summe = 0
    if type(input) == str:
        if input == "red":
            return input
        return 0
    elif type(input) == int:
        return input
    elif type(input) == dict:
        red = False
        for element in input:
            output = parse(input[element])
            if output == "red":
                red = True
            else:
                summe += output
        summe = 0 if red else summe
    elif type(input) == list:
        for el in input:
            if el != "red":
                summe += parse(el)
    return summe


print(parse(data))
