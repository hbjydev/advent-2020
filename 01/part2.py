input = []
target = 2020

with open('input.txt', 'r') as file:
    input = file.read().splitlines()

for i in range(0, len(input)):
    input[i] = int(input[i])

for i, number in enumerate(input[:-1]):
    compl_top = target - number
    for i2, number2 in enumerate(input[:-1]):
        compl_bottom = compl_top - number2
        if compl_bottom in input[i2+1:]:
            print(number * number2 * compl_bottom)
            break
