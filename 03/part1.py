input = []

with open('input.txt', 'r') as file:
    input = file.read().splitlines()

y = 0 # Vertical Position (used for progress)
x = 0 # Horizonal Position (used for scroll tracking)

finish = False

trees = 0

while finish == False:
    position = input[y][x]
    if position == '#':
        trees += 1

    if x + 3 >= 31:
        x = (x + 3) - 31
    else:
        x += 3

    if y + 1 == len(input):
        finish = True
    else:
        y += 1

print(trees)
