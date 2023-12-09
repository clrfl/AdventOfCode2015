input = "1113122113"

for i in range(50):

    new = ""
    j = 0

    while j < len(input):

        count = 1
        while j + 1 < len(input) and input[j] == input[j + 1]:
            j += 1
            count += 1
        new += str(count) + input[j]
        j += 1

    input = new
    print(len(input))

print(len(input))
