import json

f = open('input.txt')
data = json.load(f)


def parse(input):
    summe = 0
    if type(input) == str:
        return 0
    elif type(input) == int:
        return input
    elif type(input) == dict:
        for element in input:
            summe += parse(input[element])
    elif type(input) == list:
        for el in input:
            summe += parse(el)
    return summe


print(parse(data))
